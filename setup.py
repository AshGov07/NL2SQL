# # All imports at the top
# from vanna import Agent
# from vanna.core.registry import ToolRegistry
# from vanna.core.user import UserResolver, User, RequestContext
# from vanna.tools import RunSqlTool, VisualizeDataTool
# from vanna.tools.agent_memory import SaveQuestionToolArgsTool, SearchSavedCorrectToolUsesTool, SaveTextMemoryTool
# from vanna.servers.fastapi import VannaFastAPIServer
# from vanna.integrations.ollama import OllamaLlmService
# from vanna.integrations.mysql import MySQLRunner
# from vanna.integrations.local.agent_memory import DemoAgentMemory

# #for production use SQL Alchemy
# # from sqlalchemy import create_engine

# #newley added
# from vanna.core.system_prompt.default import DefaultSystemPromptBuilder
# #temporary commenting out  for the database's schema context
# # from schema_context import SCHEMA_CONTEXT
# # system_prompt_builder = DefaultSystemPromptBuilder(
# #     base_prompt=SCHEMA_CONTEXT
# # )
# from vanna.core.agent.config import AgentConfig

# config = AgentConfig(
#     max_tool_iterations=20
# )

# # Configure your LLM
# llm = OllamaLlmService(
#     # model="gpt-oss:20b",
#     model = "qwen3:latest",
#     host="http://localhost:11434"
# )

# # Configure your database (old)
# # db_tool = RunSqlTool(
# #     sql_runner=MySQLRunner(
# #         host="localhost",
# #         database="classicmodels",
# #         user="root",
# #         password="Root",
# #         port=3306
# #     )
# # )

# # Configure your database (newly added)
# from safe_mysql_runner import SafeMySQLRunner

# db_tool = RunSqlTool(
#     sql_runner=SafeMySQLRunner(
#         host="localhost",
#         database="classicmodels",
#         user="root",
#         password="Root",
#         port=3306
#     )
# )

# #temporary test
# from schema_loader import SchemaLoader

# schema_loader = SchemaLoader(
#     host="localhost",
#     user="root",
#     password="Root",
#     database="classicmodels",
#     port=3306
# )

# schema_text = schema_loader.get_schema_context()


# #phase 3 - Fk discovery
# relationship_text = schema_loader.get_relationships()

# print("\n")
# print("=" * 50)
# print("AUTO GENERATED RELATIONSHIPS")
# print("=" * 50)
# print(relationship_text)
# print("=" * 50)




# system_prompt_builder = DefaultSystemPromptBuilder(
#     base_prompt=f"""
# You are a SQL analyst working with a MySQL database.

# DATABASE SCHEMA

# {schema_text}

# RELATIONSHIPS

# The following relationships should be used when generating JOIN queries:

# {relationship_text}

# IMPORTANT RULES

# - Database engine is MySQL.
# - Use only tables listed above.
# - Use only columns listed above.
# - Never invent tables.
# - Never invent columns.
# - If asked about revenue, derive it from available tables.
# - If unsure, inspect schema before generating SQL.

# SECURITY RULES

# - Generate only read-only SQL.
# - Allowed SQL commands:
#   SELECT
#   SHOW
#   DESCRIBE
#   EXPLAIN
#   WITH

# - Never generate:
#   INSERT
#   UPDATE
#   DELETE
#   DROP
#   ALTER
#   CREATE
#   TRUNCATE
#   REPLACE
#   GRANT
#   REVOKE

# - If a user requests data modification or schema modification, explain why the action is not permitted and suggest a read-only alternative.
# """
# )
# print("\n")
# print("=" * 50)
# print("AUTO GENERATED SCHEMA")
# print("=" * 50)
# print(schema_text)
# print("=" * 50)


# # Configure your agent memory
# agent_memory = DemoAgentMemory(max_items=1000)

# # Configure user authentication
# class SimpleUserResolver(UserResolver):
#     async def resolve_user(self, request_context: RequestContext) -> User:
#         user_email = request_context.get_cookie('vanna_email') or 'guest@example.com'
#         group = 'admin' if user_email == 'admin@example.com' else 'user'
#         return User(id=user_email, email=user_email, group_memberships=[group])

# user_resolver = SimpleUserResolver()

# # Create your agent
# tools = ToolRegistry()
# tools.register_local_tool(db_tool, access_groups=['admin', 'user'])
# tools.register_local_tool(SaveQuestionToolArgsTool(), access_groups=['admin'])
# tools.register_local_tool(SearchSavedCorrectToolUsesTool(), access_groups=['admin', 'user'])
# tools.register_local_tool(SaveTextMemoryTool(), access_groups=['admin', 'user'])
# tools.register_local_tool(VisualizeDataTool(), access_groups=['admin', 'user'])

# # agent = Agent(
# #     llm_service=llm,
# #     tool_registry=tools,
# #     user_resolver=user_resolver,
# #     agent_memory=agent_memory
# # )

# #newly added
# agent = Agent(
#     llm_service=llm,
#     tool_registry=tools,
#     user_resolver=user_resolver,
#     agent_memory=agent_memory,
#     config=config,
#     system_prompt_builder=system_prompt_builder
#     # system_prompt_builder = DefaultSystemPromptBuilder()
# )

# # Run the server
# server = VannaFastAPIServer(agent)
# server.run()  # Access at http://localhost:8000

# # print(dir(agent))




# setup.py

from vanna import Agent
from vanna.core.registry import ToolRegistry
from vanna.core.user import UserResolver, User, RequestContext
from vanna.tools import RunSqlTool, VisualizeDataTool
from vanna.tools.agent_memory import (
    SaveQuestionToolArgsTool,
    SearchSavedCorrectToolUsesTool,
    SaveTextMemoryTool
)
from vanna.servers.fastapi import VannaFastAPIServer
from vanna.integrations.ollama import OllamaLlmService
from vanna.integrations.local.agent_memory import DemoAgentMemory
from vanna.core.system_prompt.default import DefaultSystemPromptBuilder
from vanna.core.agent.config import AgentConfig

from safe_mysql_runner import SafeMySQLRunner
from schema_loader import SchemaLoader
from prompt_builder import PromptBuilder
from archive.business_definition_loader import BusinessDefinitionLoader

# --------------------------------------------------
# CONFIG
# --------------------------------------------------

MYSQL_CONFIG = {
    "host": "localhost",
    # "database": "classicmodels",
    "database": "sakila",
    "user": "root",
    "password": "Root",
    "port": 3306
}

OLLAMA_CONFIG = {
    "model": "qwen3:latest",
    # "model": "qwen3.5:4b",
    "host": "http://localhost:11434"
}


# --------------------------------------------------
# AGENT CONFIG
# --------------------------------------------------

config = AgentConfig(
    max_tool_iterations=20
)


# --------------------------------------------------
# LLM
# --------------------------------------------------

llm = OllamaLlmService(
    model=OLLAMA_CONFIG["model"],
    host=OLLAMA_CONFIG["host"]
)


# --------------------------------------------------
# DATABASE
# --------------------------------------------------

db_tool = RunSqlTool(
    sql_runner=SafeMySQLRunner(
        host=MYSQL_CONFIG["host"],
        database=MYSQL_CONFIG["database"],
        user=MYSQL_CONFIG["user"],
        password=MYSQL_CONFIG["password"],
        port=MYSQL_CONFIG["port"]
    )
)


# --------------------------------------------------
# SCHEMA DISCOVERY
# --------------------------------------------------

schema_loader = SchemaLoader(
    host=MYSQL_CONFIG["host"],
    user=MYSQL_CONFIG["user"],
    password=MYSQL_CONFIG["password"],
    database=MYSQL_CONFIG["database"],
    port=MYSQL_CONFIG["port"]
)

schema_text = schema_loader.get_schema_context()

relationship_text = schema_loader.get_relationships()


# --------------------------------------------------
# BUSINESS DEFINITIONS
# Phase 4 will generate this automatically ( for now it is in stop)
# --------------------------------------------------
# from metric_discovery import MetricDiscovery
# schema_df = schema_loader.get_schema_dataframe()

# business_text = MetricDiscovery.generate(schema_df)

# print("\n")
# print("=" * 50)
# print("AUTO GENERATED BUSINESS DEFINITIONS")
# print("=" * 50)
# print(business_text)
# print("=" * 50)

business_text = (
    BusinessDefinitionLoader.get_definitions()
)
# --------------------------------------------------
# PROMPT BUILDER
# --------------------------------------------------

prompt_text = PromptBuilder.build(
    schema_text=schema_text,
    relationship_text=relationship_text,
    business_text=business_text
)

system_prompt_builder = DefaultSystemPromptBuilder(
    base_prompt=prompt_text
)


# --------------------------------------------------
# DEBUG OUTPUT
# --------------------------------------------------

print("\n")
print("=" * 60)
print("AUTO GENERATED RELATIONSHIPS")
print("=" * 60)
print(relationship_text)

print("\n")
print("=" * 60)
print("AUTO GENERATED SCHEMA")
print("=" * 60)
print(schema_text)

print("\n")
print("=" * 60)
print("BUSINESS DEFINITIONS")
print("=" * 60)
print(business_text)


# --------------------------------------------------
# MEMORY
# --------------------------------------------------

agent_memory = DemoAgentMemory(max_items=1000)


# --------------------------------------------------
# USER RESOLVER
# --------------------------------------------------

class SimpleUserResolver(UserResolver):

    async def resolve_user(
        self,
        request_context: RequestContext
    ) -> User:

        user_email = (
            request_context.get_cookie("vanna_email")
            or "guest@example.com"
        )

        group = (
            "admin"
            if user_email == "admin@example.com"
            else "user"
        )

        return User(
            id=user_email,
            email=user_email,
            group_memberships=[group]
        )


user_resolver = SimpleUserResolver()


# --------------------------------------------------
# TOOLS
# --------------------------------------------------

tools = ToolRegistry()

tools.register_local_tool(
    db_tool,
    access_groups=["admin", "user"]
)

tools.register_local_tool(
    SaveQuestionToolArgsTool(),
    access_groups=["admin"]
)

tools.register_local_tool(
    SearchSavedCorrectToolUsesTool(),
    access_groups=["admin", "user"]
)

tools.register_local_tool(
    SaveTextMemoryTool(),
    access_groups=["admin", "user"]
)

tools.register_local_tool(
    VisualizeDataTool(),
    access_groups=["admin", "user"]
)


# --------------------------------------------------
# AGENT
# --------------------------------------------------

agent = Agent(
    llm_service=llm,
    tool_registry=tools,
    user_resolver=user_resolver,
    agent_memory=agent_memory,
    config=config,
    system_prompt_builder=system_prompt_builder
)


# --------------------------------------------------
# SERVER
# --------------------------------------------------

server = VannaFastAPIServer(agent)

server.run()