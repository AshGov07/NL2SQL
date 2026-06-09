# vanna_ollama

An advanced Text-to-SQL framework execution, validation, and benchmarking pipeline leveraging the Vanna.AI framework, locally hosted Ollama LLMs, and a MySQL database backend.

---

## 🛠️ Core Pipeline Architecture
The system processes natural language queries through a four-stage execution, safety, and self-healing pipeline:
1. **Context Discovery & Context Assembling:** Extracts database metadata, maps keywords to physical tables, and embeds documentation definitions into the context.
2. **Generation & Extraction:** Routes contextual prompts to local Ollama endpoints and parses clean raw SQL code blocks out of the responses using regular expressions.
3. **Multi-Layer Guard & Validation:** Enforces strict Abstract Syntax Tree (AST) constraints, checks column/table mappings, and acts as a read-only whitelist guard (allowing SELECT queries only).
4. **Heuristic Self-Healing & Repair:** Automatically repairs minor identifier typos and missing or broken table relationships using string-distance metrics and a directed network graph.

---

## 📂 File Repository Directory

### 🚀 Pipeline Core & Orchestration Engine
* **`setup.py`**: Configures and initializes the Vanna framework, registers local tools, configures prompts, connects to the database, and boots a user-facing FastAPI web server.
* **`evaluate_engine.py`**: The main benchmark evaluation harness. Reads test questions, queries Ollama, tracks execution timing statistics, coordinates validation/repair flows, and calculates final system accuracy.
* **`benchmark_profiler.py`**: Captures step-by-step execution logs, query success statuses, and fine-grained timing metrics. Provides utilities to export summary data into JSON or print CLI summary tables.
* **`profile_ollama.py`**: A dedicated utility script that directly queries local Ollama API endpoints to verify connectivity and measure baseline inference latency independent of the framework.

### 📊 Schema Introspection & Semantic Context Builders
* **`schema_loader.py`**: Connects to the target MySQL database to extract metadata for active tables, columns, and foreign key constraints into structured Pandas dataframes.
* **`schema_retriever.py`**: Identifies database tables matching keywords in user questions and expands references to include required intermediate bridging tables.
* **`business_definitions.py`**: Defines central text-based documentation context specifying calculations for key business metrics (such as revenue, customer count, and rental count) to align the LLM.
* **`metric_discovery.py`**: Uses heuristics and regular expressions to auto-discover financial or volumetric dimensions (like price, quantity, and revenue columns) directly from database files.
* **`prompt_builder.py`**: Assembles comprehensive system instructions combining table relationships, schemas, metrics, and business rules to guide valid SQL generation.

### 🔒 Query Validation & Security Enforcement Layer
* **`query_validator.py`**: The core system gatekeeper. Performs structural schema mapping assertions, checks physical column existence, and verifies JOIN syntax correctness.
* **`sql_guard.py`**: Implements strict security whitelists to inspect SQL syntax. Explicitly blocks hazardous modifying operations like INSERT, ALTER, DROP, or UPDATE.
* **`safe_mysql_runner.py`**: Extends the default database execution class to run queries safely, ensuring only read-only statements are dispatched to the database.
* **`sql_extractor.py`**: Employs targeted regex logic to extract raw executable SQL query blocks from unstructured markdown strings returned by the LLMs.
* **`cte_helper.py`**: Contains utility logic to extract Common Table Expression (CTE) names from generated SQL statements to evaluate virtual tables during validation.

### 🩹 Automated Query Healing & Repair Modules
* **`sql_repair.py`**: Features text-matching algorithms to automatically identify and fix typo-ridden table or column names in generated SQL based on valid database identifiers.
* **`relationship_path_finder.py`**: Builds a directed graph representing foreign key relationships to compute valid join paths across disconnected components.
* **`join_repair_suggester.py`**: Analyzes broken join operations and utilizes the pathfinding graph to suggest missing table references or introduce intermediate junction tables.

### 🧪 Comprehensive Unit & Integration Test Architecture
* **`test_validator.py`**: Tests the validation module with sound and broken SQL to ensure unmatched components accurately throw errors.
* **`test_auto_repair.py`**: Evaluates end-to-end orchestration of the query validator hooks coupled to healing pathways on sample broken JOIN statements.
* **`test_join_repair.py`**: A unit test verifying that the JoinRepairSuggester successfully maps bridging links when table dependencies are severed.
* **`test_relationship_path.py`**: Targets the RelationshipPathFinder to check neighbor lookup, graph construction, and multi-hop path accuracy.
* **`test_relationship_expansion.py`**: Verifies context expansion layers and how table boundaries scale dynamically when foreign key structures are evaluated.
* **`test_schema_retriever.py`**: Validates table detection logic and entity-matching components based on a set of natural language test questions.
* **`test_aliases.py`**: Ensures the query validator correctly tracks, parses, and maps internal query table aliases (AS identifiers) to original targets.
* **`test_relationship.py`**: Verifies that the SchemaLoader correctly retrieves database foreign keys and maps relationship dataframes reliably.
* **`debug_validator.py`**: A lightweight development script used to quickly introspect active methods, attributes, and import pathways of the QueryValidator class.

### 📈 Benchmark Datasets & Performance Tracking Data
* **`evaluation_queries.json`**: The ground-truth test collection containing a suite of natural language questions paired with their expected database tables.
* **`failed_questions.json`**: A dynamic operational log written automatically by the evaluation script to capture errors, generated SQL, and repair trajectories for tuning.
* **`performance_gemma3_12b.json`**: Telemetry log detailing latency, validation checkpoints, and query-by-query results for the Gemma-3 12B model benchmark.
* **`performance_qwen2.5-coder_7b.json`**: Stores performance metrics and query validation tracking logs for the Qwen 2.5 Coder 7B engine.
* **`performance_qwen3.5_4b.json`**: Performance metrics documenting execution outcomes and inference durations for the Qwen 3.5 4B model.
* **`performance_qwen3_4b.json`**: Contains structured telemetry recording extraction, validation, and repair time spent on the baseline Qwen 3 4B variant.
* **`performance_qwen3_latest.json`**: Saves benchmark timing results and output success profiles tracking the latest version of the Qwen 3 model series.

---

## ⚡ Quick Start & Execution

Run the following workflow commands in your terminal workspace to initialize the pipeline components, start the FastAPI interface, or kick off benchmarking passes:

```powershell
# 1. Activate your local virtual environment
.\venv\Scripts\Activate.ps1

# 2. Configure framework bindings and spin up the FastAPI user interface
python setup.py

# 3. Launch the automated evaluation harness against your test suite
python evaluate_engine.py
