# from vanna.core.enhancer import LlmContextEnhancer

# from schema_retriever import SchemaRetriever
# from relationship_path_finder import RelationshipPathFinder
# from prompt_builder import PromptBuilder
# from archive.business_definition_loader import BusinessDefinitionLoader


# class AdventureWorksContextEnhancer(LlmContextEnhancer):
#     """
#     Builds a question-aware system prompt using the same retrieval pipeline
#     as the benchmark engine.
#     """

#     def __init__(self, schema_loader):
#         self.schema_loader = schema_loader

#         # Cache metadata once at startup
#         self.schema_df = self.schema_loader.get_schema_dataframe()
#         self.relationship_df = self.schema_loader.get_relationship_dataframe()
#         self.relationship_text = self.schema_loader.get_relationships()
#         self.business_text = BusinessDefinitionLoader.get_definitions()

#     async def enhance_system_prompt(self, system_prompt, message, user):
#         question = (message or "").strip()

#         if not question:
#             return system_prompt or ""

#         detected_tables = SchemaRetriever.retrieve_tables(
#             question,
#             self.schema_df
#         )

#         expanded_tables = RelationshipPathFinder.expand_tables(
#             detected_tables,
#             self.relationship_df
#         )

#         schema_text = self.schema_loader.get_schema_context(expanded_tables)

#         dynamic_prompt = PromptBuilder.build(
#             schema_text=schema_text,
#             relationship_text=self.relationship_text,
#             business_text=self.business_text
#         )

#         if system_prompt:
#             return f"{system_prompt}\n\n{dynamic_prompt}"

#         return dynamic_prompt

#     async def enhance_user_messages(self, messages, user):
#         return messages



from vanna.core.enhancer.base import LlmContextEnhancer

from schema_retriever import SchemaRetriever
from relationship_path_finder import RelationshipPathFinder
from prompt_builder import PromptBuilder
from archive.business_definition_loader import BusinessDefinitionLoader


class AdventureWorksContextEnhancer(
    LlmContextEnhancer
):

    def __init__(
        self,
        schema_loader
    ):

        self.schema_loader = schema_loader

        self.schema_df = (
            schema_loader.get_schema_dataframe()
        )

        self.relationship_df = (
            schema_loader.get_relationship_dataframe()
        )

        self.relationship_text = (
            schema_loader.get_relationships()
        )

        self.business_text = (
            BusinessDefinitionLoader
            .get_definitions()
        )

    async def enhance_system_prompt(
        self,
        system_prompt,
        message,
        user
    ):

        question = message.strip()

        detected_tables = (
            SchemaRetriever.retrieve_tables(
                question,
                self.schema_df
            )
        )

        print(
            "\nDetected Tables:",
            detected_tables
        )

        expanded_tables = (
            RelationshipPathFinder.expand_tables(
                detected_tables,
                self.relationship_df
            )
        )

        print(
            "\nExpanded Tables:",
            expanded_tables
        )

        schema_text = (
            self.schema_loader
            .get_schema_context(
                expanded_tables
            )
        )

        dynamic_prompt = (
            PromptBuilder.build(
                schema_text=schema_text,
                relationship_text=self.relationship_text,
                business_text=self.business_text
            )
        )

        return dynamic_prompt

    async def enhance_user_messages(
        self,
        messages,
        user
    ):
        return messages