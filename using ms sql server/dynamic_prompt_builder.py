from schema_retriever import SchemaRetriever
from relationship_path_finder import RelationshipPathFinder
from prompt_builder import PromptBuilder
from archive.business_definition_loader import BusinessDefinitionLoader


class DynamicPromptBuilder:

    @staticmethod
    def build_prompt_for_question(
        question,
        schema_loader
    ):

        schema_df = schema_loader.get_schema_dataframe()

        relationship_df = (
            schema_loader.get_relationship_dataframe()
        )

        detected_tables = (
            SchemaRetriever.retrieve_tables(
                question,
                schema_df
            )
        )

        expanded_tables = (
            RelationshipPathFinder.expand_tables(
                detected_tables,
                relationship_df
            )
        )

        schema_text = (
            schema_loader.get_schema_context(
                expanded_tables
            )
        )

        relationship_text = (
            schema_loader.get_relationships()
        )

        business_text = (
            BusinessDefinitionLoader.get_definitions()
        )

        prompt = PromptBuilder.build(
            schema_text=schema_text,
            relationship_text=relationship_text,
            business_text=business_text
        )

        return prompt