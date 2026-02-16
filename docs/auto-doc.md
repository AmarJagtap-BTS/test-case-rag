# Auto Generated Documentation

*Last updated: Mon Feb 16 11:36:13 UTC 2026*

## File: generate_diagrams.py
# Project Architecture Diagram Generator

This Python script analyzes a Python project's structure, extracts modules, their dependencies, classes, and functions, and generates comprehensive Mermaid diagrams representing the system architecture, class diagram, sequence flows, and process flowcharts. It further integrates with Azure OpenAI to create AI-generated architecture diagrams based on the discovered project structure.

---

## Overview

The tool performs the following key tasks:

1. **Analyze Project Structure**: Walks through the project directory, parses Python files using the `ast` module to extract imports, classes, and functions.
2. **Generate Mermaid Diagrams**:
   - System architecture flowchart
   - Module dependency graph
   - Class diagrams with methods
   - Sequence diagrams depicting typical workflows
   - Process flowcharts of main operations
3. **AI-Generated Diagrams**: Sends project metadata to Azure OpenAI's GPT model to produce a comprehensive architecture Mermaid diagram.
4. **Output**: Generates a markdown file aggregating all generated diagrams and a module summary for easy documentation.

---

## Dependencies

- Python 3.7+
- `openai` package with AzureOpenAI client support
- Environment variables for Azure OpenAI credentials:
  - `AZURE_OPENAI_API_KEY` — API key for Azure OpenAI service
  - `AZURE_OPENAI_API_VERSION` — (optional) API version (default: `2025-01-01-preview`)
  - `AZURE_OPENAI_ENDPOINT` — Azure OpenAI service endpoint
  - `AZURE_OPENAI_DEPLOYMENT` — Deployment/model name (default: `gpt-4.1-mini`)

---

## Module-Level Documentation

### Initialization

```python
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY", ""),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2025-01-01-preview"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", "")
)
```

- Creates an AzureOpenAI client instance using environment variables.

---

### `analyze_project_structure() -> Dict`

Analyzes Python project files to extract module structure and relationships.

- Walks recursively starting at current directory (`.`).
- Skips hidden directories and common virtual environment or cache folders.
- Parses `.py` files using `ast`.
- Extracts:
  - Imported modules (both `import` and `from ... import ...`)
  - Classes
  - Functions

Returns a dictionary with keys:

```python
{
  'modules': {module_path: {'imports': [...], 'classes': [...], 'functions': [...]}},
  'dependencies': {},  # unused/empty
  'classes': {},       # unused/empty
  'functions': {}      # unused/empty
}
```

---

### `generate_mermaid_architecture_diagram(structure: Dict) -> str`

Generates a Mermaid graph (`graph TB`) depicting module dependencies:

- Groups modules by their directory (creates subgraphs for non-root folders).
- Creates nodes for each Python module.
- Adds directional edges for imports between modules detected as internal dependencies.
- Returns the Mermaid diagram as a markdown code block string.

---

### `generate_mermaid_class_diagram(structure: Dict) -> str`

Creates a Mermaid class diagram showing up to 15 classes and their methods:

- Classes are labeled with their module names.
- Shows up to 5 functions per class.
- Diagram returned as a markdown code block string.

---

### `generate_mermaid_sequence_diagram() -> str`

Returns a Mermaid sequence diagram (hardcoded) illustrating a typical workflow:

- Participants: User, API, RAGEngine, KnowledgeBase, TestGenerator, VectorDB.
- Shows messaging flows for test case generation and storage.

---

### `generate_mermaid_flowchart() -> str`

Returns a Mermaid flowchart that models the main process steps:

- Starts from user input.
- Parses, searches knowledge base, decision branches based on similarity scores.
- Includes processes like augmenting tests, generating new ones, storing, and formatting.
- Applies visual styling for key decision nodes.
- Diagram returned as a markdown code block string.

---

### `generate_ai_diagrams(structure: Dict) -> str`

Uses the Azure OpenAI client to prompt GPT for a comprehensive Mermaid diagram based on the analyzed structure:

- Summarizes number of modules and a brief listing of their contents.
- Sends a prompt asking for a system architecture, data flow, and component interaction diagram.
- Returns the AI-generated Mermaid diagram as a string.
- Handles exceptions by printing errors and returning an empty string.

---

### `main()`

The main execution function:

1. Calls `analyze_project_structure()` and prints found modules count.
2. Generates all Mermaid diagrams and collates them with explanatory markdown sections:
   - System Architecture
   - Module Dependencies
   - Class Diagram
   - Sequence Diagram
   - Process Flowchart
   - AI-Generated Architecture
3. Adds a module summary table.
4. Writes the complete markdown content to `docs/architecture-diagrams.md`.
5. Prints completion message including output location and analyzed module count.

When executed as a script, `main()` runs automatically.

---

## Usage

Set the required environment variables (or configure defaults), then run:

```bash
python path/to/this_script.py
```

Output is saved to `docs/architecture-diagrams.md` with markdown-formatted Mermaid diagrams documenting the project structure and flow.

---

## Summary

This tool automates the generation of architectural and flow diagrams for Python projects, combining static code analysis and AI-powered diagram synthesis — useful for documentation, onboarding, and architectural reviews.

