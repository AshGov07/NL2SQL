import json
import asyncio
import re
import time
from schema_loader import SchemaLoader
from prompt_builder import PromptBuilder
from archive.business_definition_loader import (
    BusinessDefinitionLoader
)

from query_validator import QueryValidator
from sql_repair import SQLRepair

from vanna.integrations.ollama import OllamaLlmService

from vanna.core.llm import (
    LlmRequest,
    LlmMessage
)

from vanna.core.user import User
from benchmark_profiler import (
    BenchmarkProfiler
)


from schema_retriever import (
    SchemaRetriever
)

from relationship_path_finder import (
    RelationshipPathFinder
)

# --------------------------------------------------
# CONFIG
# --------------------------------------------------

DB_CONFIG = {
   "server": "MLS-AI-PC",
    "database": "AdventureWorksDW2025",
    "trusted_connection": "yes",
    "driver": "ODBC Driver 17 for SQL Server"
}

OLLAMA_CONFIG = {
    "model": "qwen3:latest",
    # "model":"qwen2.5-coder:7b",
    # "model":"qwen3.5:4b",
    # "model":"qwen3:4b",
    "host": "http://localhost:11434"
}
profiler = BenchmarkProfiler(
    OLLAMA_CONFIG["model"]
)

# --------------------------------------------------
# HELPERS
# --------------------------------------------------

def extract_tables(sql):

    tables = re.findall(
        r'(?:from|join)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
        sql,
        re.IGNORECASE
    )

    return sorted(
        list(
            set(
                table.lower()
                for table in tables
            )
        )
    )


# --------------------------------------------------
# LOAD SCHEMA
# --------------------------------------------------

schema_loader = SchemaLoader(
    server="MLS-AI-PC",
    database="AdventureWorksDW2025"
)

# schema_text = schema_loader.get_schema_context()

# relationship_text = (
#     schema_loader.get_relationships()
# )

schema_df = (
    schema_loader.get_schema_dataframe()
)

relationship_df = (
    schema_loader.get_relationship_dataframe()
)

business_text = (
    BusinessDefinitionLoader.get_definitions()
)

# prompt_text = PromptBuilder.build(
#     schema_text=schema_text,
#     relationship_text=relationship_text,
#     business_text=business_text
# )


# --------------------------------------------------
# LLM
# --------------------------------------------------

llm = OllamaLlmService(
    model=OLLAMA_CONFIG["model"],
    host=OLLAMA_CONFIG["host"]
)

profiler = BenchmarkProfiler(
    OLLAMA_CONFIG["model"]
)
# --------------------------------------------------
# USER
# --------------------------------------------------

benchmark_user = User(
    id="benchmark",
    email="benchmark@test.com",
    group_memberships=["admin"]
)


# --------------------------------------------------
# SQL GENERATION
# --------------------------------------------------
def build_prompt_for_question(
    question
):

    detected_tables = (
        SchemaRetriever
        .retrieve_tables(
            question,
            schema_df
        )
    )

    # expanded_tables = (
    #     RelationshipPathFinder
    #     .expand_two_hops(
    #         detected_tables,
    #         relationship_df
    #     )
    # )

    # expanded_tables = (
    #     RelationshipPathFinder
    #     .expand_one_hop(
    #         detected_tables,
    #         relationship_df
    #     )
    # )



    if len(detected_tables) >= 2:

        expanded_tables = detected_tables

    else:

        expanded_tables = (
            RelationshipPathFinder
        .expand_one_hop(
            detected_tables,
            relationship_df
        )
    )
    print("\nDetected Tables:")
    print(detected_tables)

    print("\nExpanded Tables:")
    print(expanded_tables)

   

    schema_text = (
        schema_loader
        .get_schema_context(
            expanded_tables
        )
    )
    print("\n")
    print("=" * 60)
    print("SCHEMA STATS")
    print("=" * 60)

    print(
        f"Schema Length = "
        f"{len(schema_text)}"
    )
    metrics = {
        "question": question,
        "detected_tables_count": len(detected_tables),
        "expanded_tables_count": len(expanded_tables),
        "schema_length": len(schema_text)
    }

    print("\nMETRICS")
    print(metrics)
    print(
        schema_text[:1500]
    )

    relationship_text = (
        schema_loader
        .get_relationships()
    )
    print(
    f"Relationships: "
    f"{len(relationship_df)}"
)
    prompt_text = (
        PromptBuilder.build(
            schema_text=schema_text,
            relationship_text=relationship_text,
            business_text=business_text
        )
    )

    return prompt_text


async def generate_sql(question):
    prompt_text = (
        build_prompt_for_question(
            question
        )
    )
    llm_start = time.perf_counter()
    
    # request = LlmRequest(
    #     messages=[
    #         LlmMessage(
    #             role="user",
    #             content=(
    #                 "Generate only SQL.\n\n"
    #                 f"Question: {question}"
    #             )
    #         )
    #     ],
    #     user=benchmark_user,
    #     stream=False,
    #     temperature=0,
    #     system_prompt=prompt_text
    # )
    request = LlmRequest(
        messages=[
            LlmMessage(
                role="user",
                content=(
                    "Generate only SQL.\n\n"
                    f"Question: {question}"
                )
            )
        ],
        user=benchmark_user,
        stream=False,
        temperature=0,
        system_prompt=prompt_text
    )
    response = await llm.send_request(
        request
    )
    llm_end = time.perf_counter()
    return (response.content.strip() ,llm_end - llm_start)


# --------------------------------------------------
# EVALUATION
# --------------------------------------------------

async def evaluate():
    benchmark_start = time.perf_counter()
    with open(
        "test_engine_query copy 2.json",
        "r",
        encoding="utf-8"
    ) as f:

        questions = json.load(f)

    total = len(questions)

    passed = 0
    repaired = 0
    failed = 0
    failed_questions = []

    for index, item in enumerate(
        questions,
        start=1
    ):
        question_start = time.perf_counter()
        llm_time = 0
        extract_time = 0
        validation_time = 0
        repair_time = 0

        question = item["question"]

        expected_tables = sorted(
            [
                table.lower()
                for table in item[
                    "expected_tables"
                ]
            ]
        )

        print("\n")
        print("=" * 80)
        print(
            f"QUESTION {index}/{total}"
        )
        print("=" * 80)

        print(
            f"\nQuestion:\n{question}"
        )

        try:

            sql_raw,llm_time= await generate_sql(
                question
            )
            from sql_extractor import SQLExtractor
            extract_start = time.perf_counter()
            sql = SQLExtractor.extract(
                sql_raw
            )
            extract_time = time.perf_counter() - extract_start
            print("\nRAW RESPONSE:")
            print(sql_raw)

            print("\nEXTRACTED SQL:")
            print(sql)

            print(
                f"\nGenerated SQL:\n{sql}"
            )

            actual_tables = extract_tables(
                sql
            )

            print(
                f"\nExpected Tables:\n{expected_tables}"
            )

            print(
                f"\nActual Tables:\n{actual_tables}"
            )
            validate_start = time.perf_counter()
            QueryValidator.validate(
                sql,
                schema_df,
                relationship_df
            )
            validate_time = time.perf_counter() - validate_start

            print(
                "\nValidation: PASS"
            )

            passed += 1

            profiler.add_record(
                question=question,
                llm_time=llm_time,
                extract_time=extract_time,
                validation_time=validate_time,
                repair_time=0,
                total_time=(
                    time.perf_counter()
                    - question_start
                ),
                status="PASS"
            )
            question_end = time.perf_counter()

            print(
                f"\nExecution Time: "
                f"{question_end - question_start:.2f} seconds"
            )

        except Exception as e:

            print(
                f"\nValidation Failed:\n{e}"
            )

            valid_tables = (
                schema_df[
                    "TABLE_NAME"
                ]
                .unique()
                .tolist()
            )

            valid_columns = (
                schema_df[
                    "COLUMN_NAME"
                ]
                .unique()
                .tolist()
            )
            repair_start = time.perf_counter()
            repaired_sql = (
                SQLRepair.repair_sql(
                    sql,
                    valid_tables,
                    valid_columns
                )
            )
            repair_time = time.perf_counter() - repair_start
            print(
                "\nRepaired SQL:"
            )

            print(
                repaired_sql
            )

            try:

                QueryValidator.validate(
                    repaired_sql,
                    schema_df,
                    relationship_df
                )

                print(
                    "\nValidation: REPAIRED"
                )

                repaired += 1
                profiler.add_record(
                    question=question,
                    llm_time=llm_time,
                    extract_time=extract_time,
                    validation_time=0,
                    repair_time=repair_time,
                    total_time=(
                        time.perf_counter()
                        - question_start
                    ),
                    status="REPAIRED"
                )
                question_end = time.perf_counter()

                print(
                    f"\nExecution Time: "
                    f"{question_end - question_start:.2f} seconds"
                )

            except Exception as e2:

                print(
                    f"\nFAILED:\n{e2}"
                )

                failed += 1
                question_end = time.perf_counter()

                print(
                    f"\nExecution Time: "
                    f"{question_end - question_start:.2f} seconds"
                )
                profiler.add_record(
                    question=question,
                    llm_time=llm_time,
                    extract_time=extract_time,
                    validation_time=0,
                    repair_time=repair_time,
                    total_time=(
                        time.perf_counter()
                        - question_start
                    ),
                    status="FAILED"
                )

                failed_questions.append(
                    {
                        "question": question,
                        "generated_sql": sql,
                        "repaired_sql": repaired_sql,
                        "error": str(e2),
                        "execution_time_seconds":
                            round(
                                question_end -
                                question_start,
                                2
                            )
                    }
                )
                
    benchmark_end = time.perf_counter()

    total_time = (
        benchmark_end -
        benchmark_start
    )
    print("\n")
    print("=" * 80)
    print("FINAL REPORT")
    print("=" * 80)

    print(
        f"Total Questions : {total}"
    )

    print(
        f"Passed          : {passed}"
    )

    print(
        f"Repaired        : {repaired}"
    )

    print(
        f"Failed          : {failed}"
    )
    print(
        f"Total Time      : {total_time:.2f} seconds"
    )

    print(
        f"Avg Time        : {total_time / total:.2f} seconds/query"
    )

    score = (
        (
            passed + repaired
        )
        / total
    ) * 100

    print(
        f"\nAccuracy : {score:.2f}%"
    )
    profiler.print_summary()
    profiler.save()
    print("\n")
    print("=" * 80)
    print("FAILED QUESTIONS")
    print("=" * 80)

    for index, item in enumerate(
        failed_questions,
        start=1
    ):

        print("\n")
        print("-" * 80)

        print(
            f"Failure #{index}"
        )

        print(
            f"\nQuestion:\n{item['question']}"
        )

        print(
            f"\nGenerated SQL:\n{item['generated_sql']}"
        )

        print(
            f"\nRepaired SQL:\n{item['repaired_sql']}"
        )

        print(
            f"\nError:\n{item['error']}"
        )

        print("-" * 80)


        with open(
            "failed_questions.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                failed_questions,
                f,
                indent=4
            )

        print("\nSaved failures to failed_questions.json")


# --------------------------------------------------
# MAIN
# --------------------------------------------------

if __name__ == "__main__":

    asyncio.run(
        evaluate()
    )