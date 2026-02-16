# Auto Generated Documentation

*Complete project documentation - Generated on: Mon Feb 16 11:17:47 UTC 2026*

## File: config/__init__.py
# Configuration Management Module

This module provides functionality related to configuration management.

## Overview

The module exports the `Config` class from the internal `config` submodule, making it available for external use.

## Contents

- `Config`: The primary class responsible for managing configuration settings.

## Usage

```python
from your_package_name import Config

config = Config()
# Use config instance as needed
```

## Notes

- The internal implementation of `Config` is located in the `config` submodule.
- This module acts as a facade to simplify imports for users of the package.

## File: config/config.py
# Configuration Module Documentation

This module provides centralized configuration management for a Retrieval-Augmented Generation (RAG)-based test case generation system. It loads environment variables, sets default values, and exposes all configuration parameters through a single `Config` class. This design facilitates easy customization and tuning of the system by changing environment variables or default values in one place.

---

## Module Overview

```python
import os
from dotenv import load_dotenv
from typing import Optional
```

- **Environment Variable Loading:** Utilizes `python-dotenv`'s `load_dotenv()` to load environment variables from a `.env` file (if present), enabling configuration outside the codebase.
- **Config Class:** Contains all configuration parameters as class variables with appropriate type conversions.
- **Directory Initialization:** Ensures all necessary filesystem paths exist by creating directories on module import.

---

## Class: `Config`

Centralized container for all configurable parameters, grouped by functionality.

### Attributes

#### Azure OpenAI Configuration

- `AZURE_OPENAI_API_KEY: str`  
  API key for Azure OpenAI access.  
  **Default:** `""` (empty string)

- `AZURE_OPENAI_ENDPOINT: str`  
  Base endpoint URL for Azure OpenAI service.  
  **Default:** `""` (empty string)

- `AZURE_OPENAI_DEPLOYMENT_NAME: str`  
  Name of the deployed OpenAI model to use.  
  **Default:** `"gpt-4.1-mini"`

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT: str`  
  Deployment name for the embedding model.  
  **Default:** `"text-embedding-ada-002"`

- `AZURE_OPENAI_API_VERSION: str`  
  API version string for Azure OpenAI.  
  **Default:** `"2024-08-01-preview"`

#### Vector Database Configuration

- `CHROMA_PERSIST_DIRECTORY: str`  
  Filesystem path where the vector database (Chroma) persists its data.  
  **Default:** `"./chroma_db"`

#### Similarity Thresholds

- `THRESHOLD_SAME: float`  
  Similarity score threshold above which vectors are considered effectively identical.  
  **Default:** `0.99`

- `THRESHOLD_ADDON_MIN: float`  
  Lower bound similarity threshold for considering additional test cases.  
  **Default:** `0.60`

- `THRESHOLD_ADDON_MAX: float`  
  Upper bound similarity threshold for considering additional test cases.  
  **Default:** `0.85`

#### Hybrid Scoring Weights (Semantic + LLM)

- `SEMANTIC_WEIGHT: float`  
  Weight assigned to embedding-based similarity in hybrid scoring. Prioritized for speed and exact matches.  
  **Default:** `0.60` (60%)

- `LLM_WEIGHT: float`  
  Weight assigned to language model-based contextual similarity in hybrid scoring. Used to catch semantic equivalence.  
  **Default:** `0.40` (40%)

#### RAG Configuration

- `RAG_TOP_K: int`  
  Number of top relevant documents retrieved in RAG pipeline.  
  **Default:** `10`

#### Test Case Generation Configuration

- `USE_PARALLEL_GENERATION: bool`  
  Flag to enable parallel generation of test cases to improve throughput.  
  **Default:** `True`

- `PARALLEL_BATCH_SIZE: int`  
  Number of test cases generated in one parallel batch.  
  **Default:** `10`

- `BATCH_TIMEOUT_SECONDS: int`  
  Timeout limit (in seconds) for processing a batch of test case generations.  
  **Default:** `45`

#### Test Case Generation Limits

- `MIN_TEST_CASES: int`  
  Minimum number of test cases to generate.  
  **Default:** `8`

- `MAX_TEST_CASES: int`  
  Maximum number of test cases to generate.  
  **Default:** `25`

- `DEFAULT_TEST_CASES: int`  
  Default number of test cases to generate when no user input is provided.  
  **Default:** `12`

#### Test Case Type Distribution (Proportion as float 0.0-1.0)

- `POSITIVE_MIN_PERCENT: float` — Minimum ratio of positive test cases. Default `0.50`  
- `POSITIVE_MAX_PERCENT: float` — Maximum ratio of positive test cases. Default `0.50`

- `NEGATIVE_MIN_PERCENT: float` — Minimum ratio of negative test cases. Default `0.30`  
- `NEGATIVE_MAX_PERCENT: float` — Maximum ratio of negative test cases. Default `0.30`

- `UI_MIN_PERCENT: float` — Minimum ratio of UI test cases. Default `0.20`  
- `UI_MAX_PERCENT: float` — Maximum ratio of UI test cases. Default `0.20`

- `SECURITY_MIN_PERCENT: float` — Minimum ratio of security test cases. Default `0.00`  
- `SECURITY_MAX_PERCENT: float` — Maximum ratio of security test cases. Default `0.00`

- `EDGE_CASE_MIN_PERCENT: float` — Minimum ratio of edge case test cases. Default `0.00`  
- `EDGE_CASE_MAX_PERCENT: float` — Maximum ratio of edge case test cases. Default `0.00`

#### Storage Paths

- `KNOWLEDGE_BASE_PATH: str`  
  Directory path where knowledge base files are located or stored.  
  **Default:** `"./knowledge_base"`

- `TEST_SUITE_OUTPUT: str`  
  Directory path where generated test suite output files are saved.  
  **Default:** `"./output"`

#### Collection Names

- `CHROMA_COLLECTION_NAME: str`  
  Name identifier for the Chroma vector store collection to use for test cases.  
  **Default:** `"test_cases"`

---

### Methods

- `@classmethod validate() -> bool`  
  Validates presence of critical configuration items necessary for correct operation.  
  Currently validates that both `AZURE_OPENAI_API_KEY` and `AZURE_OPENAI_ENDPOINT` are set and non-empty.  
  **Returns:** `True` if all required configurations are present, else `False`.

- `@classmethod create_directories()`  
  Creates all directories specified by the configuration (for vector DB persistence, knowledge base path, and output path) if they do not already exist. Ensures the system has necessary file storage infrastructure.

---

## Initialization Behavior

Upon importing the module, the following occurs automatically:

- Environment variables are loaded from `.env`.
- The `Config.create_directories()` method is called to create necessary directories as per configuration.

This ensures the environment is prepared before the rest of the application starts.

---

## Usage Example

```python
from config_module import Config

# Check if critical configurations are valid
if not Config.validate():
    raise RuntimeError("Critical configuration missing. Please set AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT.")

# Access API key
api_key = Config.AZURE_OPENAI_API_KEY

# Use paths
output_dir = Config.TEST_SUITE_OUTPUT
```

---

## Notes

- Configuration values default to environment variables if present; otherwise, fall back to defaults defined in the class.
- Boolean configurations are case-insensitive and expect "true" or "false" strings.
- Thresholds and weighting parameters can be tuned according to system performance and accuracy requirements.
- Directory paths and deployment names can be customized to fit user environments without code modifications.
- The modular design allows easy extension for additional configuration parameters.

---

This documentation ensures maintainers and users can understand, configure, and extend the system effectively.

## File: core/__init__.py
# Module Documentation: Core Business Logic and Data Models

This module serves as the central interface for accessing the core business logic components and data models used throughout the application. It aggregates key classes, functions, and utilities that support the handling, processing, and exporting of test cases, user stories, and related decision data.

## Import Summary

- **Data Models**
  - `TestCase` — Represents a test case entity with its associated properties and behaviors.
  - `UserStory` — Encapsulates a user story for managing feature requirements and descriptions.
  - `ComparisonResult` — Contains results of test case or user story comparisons.
  - `DecisionType` — Enumerates the types of decisions or statuses used in comparisons or workflows.

- **Utility Functions**
  - `generate_id` — Generates unique identifiers for objects or transactions.
  - `load_json` — Loads JSON data from a file or string input.
  - `save_json` — Saves data structures to JSON format in persistent storage.
  - `parse_test_case_json` — Parses and validates JSON data into `TestCase` objects.
  - `export_to_excel` — Exports data collections into Excel spreadsheet format.
  - `export_to_csv` — Exports data collections into CSV text format.

- **Knowledge Base**
  - `KnowledgeBase` — Provides structured storage and retrieval of domain-specific knowledge, aiding decision-making and test case validation.

## Exports (`__all__`)

This module explicitly exports the following components for external usage:

```python
[
    'TestCase',
    'UserStory',
    'ComparisonResult',
    'DecisionType',
    'generate_id',
    'load_json',
    'save_json',
    'parse_test_case_json',
    'export_to_excel',
    'export_to_csv',
    'KnowledgeBase'
]
```

## Usage Overview

The module acts as a facade, allowing importing components from a single entry point.

Example usage:

```python
from core import TestCase, generate_id, KnowledgeBase

# Create a new test case with a unique ID
test_case = TestCase(id=generate_id(), name="Login feature test")

# Load additional information from JSON
test_cases_data = load_json("test_cases.json")

# Parse raw JSON data into TestCase objects
test_cases = [parse_test_case_json(data) for data in test_cases_data]

# Export test cases to Excel format for reporting
export_to_excel(test_cases, "test_cases_report.xlsx")

# Access knowledge base for decision support
kb = KnowledgeBase()
decision = kb.evaluate(test_case)
```

---

This module consolidates all core functionalities relevant to test case management, user story tracking, comparison evaluation, and data exportation, making it a cornerstone for the application’s backend logic.

## File: core/knowledge_base.py
# KnowledgeBase Module

Provides management for test case storage and retrieval within test suites, including loading from disk, creation, update, export, and querying capabilities.

---

## Class: `KnowledgeBase`

Manages test case knowledge base including multiple test suites and their test cases.

### Initialization

```python
KnowledgeBase()
```

- Initializes the knowledge base storage path using the configured `KNOWLEDGE_BASE_PATH`.
- Loads existing test suites from disk into memory.

---

### Methods

#### `_load_existing_suites()`

Loads test suites stored as JSON files from the knowledge base directory into memory.

- Creates the directory if it does not exist.
- For each `.json` file, attempts to deserialize it into a `TestSuite` object.
- Errors during loading are caught and printed.

---

#### `create_test_suite(name: str, description: str = "") -> TestSuite`

Creates a new test suite with a given name and optional description.

- Stores the suite in memory.
- Saves it to disk as a JSON file.

**Parameters:**

- `name` (str): The name of the test suite.
- `description` (str, optional): Description of the suite (default empty string).

**Returns:**

- `TestSuite`: The newly created test suite object.

---

#### `get_test_suite(name: str) -> Optional[TestSuite]`

Retrieves the test suite with the specified name.

**Parameters:**

- `name` (str): The test suite name.

**Returns:**

- `TestSuite` if found, else `None`.

---

#### `add_test_case_to_suite(suite_name: str, test_case: TestCase)`

Adds a test case to an existing suite.

- If the suite does not exist, it will be created automatically.
- Saves the updated suite to disk.

**Parameters:**

- `suite_name` (str): The name of the test suite.
- `test_case` (TestCase): The test case to be added.

---

#### `update_test_case_in_suite(suite_name: str, test_case: TestCase)`

Updates an existing test case in the specified suite.

- If the suite or test case does not exist, no action is taken.
- Saves the updated suite to disk.

**Parameters:**

- `suite_name` (str): The name of the test suite.
- `test_case` (TestCase): The updated test case.

---

#### `get_test_case_from_suite(suite_name: str, test_case_id: str) -> Optional[TestCase]`

Retrieves a test case by ID from the specified test suite.

**Parameters:**

- `suite_name` (str): The test suite name.
- `test_case_id` (str): The ID of the test case.

**Returns:**

- `TestCase` if found, else `None`.

---

#### `get_all_test_cases(suite_name: Optional[str] = None) -> List[TestCase]`

Retrieves all test cases from a single suite or from all suites if no suite name is specified.

**Parameters:**

- `suite_name` (str, optional): Name of test suite to filter by; retrieves from all suites if omitted.

**Returns:**

- List of `TestCase` objects.

---

#### `list_suites() -> List[str]`

Returns the list of all test suite names currently loaded.

**Returns:**

- List of suite names (`str`).

---

#### `_save_suite(suite: TestSuite)`

Serializes and saves a test suite to a JSON file on disk using a filename based on the suite name.

**Parameters:**

- `suite` (TestSuite): The test suite to save.

---

#### `export_suite(suite_name: str, output_path: str, format: str = "json")`

Exports a test suite to a specified file in one of the supported formats: JSON, Excel, or CSV.

- Raises `ValueError` if the suite is not found or if the format is unsupported.

**Parameters:**

- `suite_name` (str): Name of the suite to export.
- `output_path` (str): Path to the output file.
- `format` (str): Export format: `"json"`, `"excel"`, or `"csv"` (default `"json"`).

---

# Notes

- The module depends on external components:
  - `core.models` for `TestCase` and `TestSuite` classes.
  - `core.utils` for JSON operations (`save_json`, `load_json`) and export utilities (`export_to_excel`, `export_to_csv`).
  - `config.config.Config` for configuration including the knowledge base path.
- Exception handling during loading of test suites prevents a crash on corrupted files but only prints the error.
- Supports test case addition, update, querying, and suite export to facilitate integration with other tools.

## File: core/models.py
# Pydantic Models for Test Case Management System

This module defines Pydantic data models used for managing test cases, test suites, user stories, and results of test case comparisons. These models provide structured representations useful for serialization, validation, and manipulation of test artifacts in a test management system.

---

## Enumerations

### `DecisionType`
```python
class DecisionType(str, Enum)
```
Enumeration of decision types used in test case comparison results.

- `SAME`: Indicates the compared test cases are the same.
- `ADDON`: Indicates one test case is an add-on to the other.
- `NEW`: Indicates a new test case with no equivalent existing case.

---

## Models

### `TestStep`
```python
class TestStep(BaseModel)
```
Represents an individual step in a test case.

**Fields:**
- `step_number: int`  
  The sequence number of the step within the test case.
- `action: str`  
  The action to perform in this step.
- `expected_result: str`  
  The expected outcome after performing the action.

---

### `TestCase`
```python
class TestCase(BaseModel)
```
Structured model describing a detailed test case.

**Fields:**
- `id: str` (default: `""`)  
  Unique identifier for the test case.
- `title: str`  
  Title of the test case.
- `description: str`  
  Detailed description outlining the test case purpose.
- `business_rule: str` (default: `"Functional requirement validation"`)  
  Business rule or requirement this test case validates.
- `preconditions: List[str]` (default: empty list)  
  List of conditions that must hold before test execution.
- `test_steps: List[TestStep]`  
  Ordered list of test steps to execute.
- `expected_outcome: str`  
  Description of the expected final result after execution.
- `postconditions: List[str]` (default: empty list)  
  Conditions that must hold after test execution.
- `tags: List[str]` (default: empty list)  
  Tags or keywords associated with the test case.
- `priority: str` (default: `"Medium"`)  
  Priority level (e.g., Low, Medium, High).
- `test_type: str` (default: `"Functional"`)  
  Type of test (e.g., Functional, Integration, E2E, API, Security, Performance, UI, Regression, Smoke).
- `is_regression: bool` (default: `False`)  
  Flag indicating if this test case is part of regression testing.
- `boundary_conditions: List[str]` (default: empty list)  
  Boundary conditions to verify.
- `side_effects: List[str]` (default: empty list)  
  Possible side effects occurring after test execution.
- `created_at: datetime` (default: current datetime)  
  Timestamp when the test case was created.
- `updated_at: datetime` (default: current datetime)  
  Timestamp when the test case was last updated.
- `version: int` (default: `1`)  
  Version number of the test case to track revisions.
- `source_document: Optional[str]`  
  Reference or link to the source document for the test case.

**Methods:**

- `to_text() -> str`  
  Converts the test case into a human-readable textual format suitable for search or reporting.  
  Outputs key fields including title, description, business rule, preconditions, detailed test steps, expected outcome, postconditions, boundary conditions, side effects, and tags.

---

### `ComparisonResult`
```python
class ComparisonResult(BaseModel)
```
Model to represent the outcome of comparing two test cases for similarity and coverage.

**Fields:**
- `new_test_case_id: str`  
  Identifier of the newly created or incoming test case.
- `existing_test_case_id: Optional[str]`  
  Identifier of the existing test case compared against, if any.
- `similarity_score: float`  
  Numeric score indicating how similar the two test cases are.
- `decision: DecisionType`  
  Decision made based on the comparison (`SAME`, `ADDON`, `NEW`).
- `reasoning: str`  
  Textual explanation supporting the comparison decision.
- `business_rule_match: bool`  
  Whether the compared test cases share the same business rules.
- `behavior_match: bool`  
  Whether the test cases exhibit the same behavior.
- `coverage_expansion: List[str]` (default: empty list)  
  List of new coverage areas introduced by the new test case.
- `confidence_score: float`  
  Confidence level of the decision.
- `timestamp: datetime` (default: current datetime)  
  Date and time when the comparison result was generated.

---

### `TestSuite`
```python
class TestSuite(BaseModel)
```
Represents a collection of test cases grouped as a suite.

**Fields:**
- `name: str`  
  Name of the test suite.
- `description: str`  
  Description of the test suite purpose.
- `test_cases: List[TestCase]` (default: empty list)  
  List of test cases included in the suite.
- `created_at: datetime` (default: current datetime)  
  Timestamp when the suite was created.
- `updated_at: datetime` (default: current datetime)  
  Timestamp when the suite was last updated.
- `version: int` (default: `1`)  
  Version number of the test suite.

**Methods:**

- `add_test_case(test_case: TestCase) -> None`  
  Adds a `TestCase` instance to the suite and updates the `updated_at` timestamp.

- `get_test_case_by_id(test_case_id: str) -> Optional[TestCase]`  
  Retrieves a `TestCase` from the suite by its `id`. Returns `None` if not found.

- `update_test_case(test_case: TestCase) -> None`  
  Updates an existing test case within the suite matching by `id`.  
  Increments the test case version, updates its timestamp, replaces it in the suite, and updates the suite's `updated_at` timestamp.

---

### `UserStory`
```python
class UserStory(BaseModel)
```
Model representing a user story or requirements document that test cases may be derived from.

**Fields:**
- `id: str`  
  Unique identifier for the user story/requirement.
- `title: str`  
  Title describing the user story.
- `description: str`  
  Detailed description of the user story.
- `acceptance_criteria: List[str]` (default: empty list)  
  List of criteria that must be met for acceptance.
- `business_rules: List[str]` (default: empty list)  
  Business rules related to this user story.
- `context: Optional[str]`  
  Additional contextual information, if any.
- `created_at: datetime` (default: current datetime)  
  Timestamp when this user story was created.

---

# Summary

These Pydantic models form a structured backbone for a test case management system, supporting features like test case creation, grouping into suites, versioning, conversion to text for searchability, tracking comparison and decision-making on test case similarity, and linking test cases to business requirements or user stories.

## File: core/utils.py
# Utility Functions for Test Case Management System

This module provides a collection of utility functions to assist in handling test cases and their associated data within the test case management system. It includes functions for generating IDs, validating test types, formatting test steps, importing/exporting data in various formats, and more.

---

## Functions

### `generate_id(text: str) -> str`

Generate a unique identifier based on the input text.

- **Args:**
  - `text` (str): The input string to generate the ID from.

- **Returns:**
  - `str`: A 12-character hexadecimal string generated by MD5 hashing the input text.

---

### `calculate_test_distribution(num_test_cases: int) -> Dict[str, Any]`

Calculate the distribution of test cases by type according to configured minimum percentages.

- **Args:**
  - `num_test_cases` (int): Total number of test cases.

- **Returns:**
  - Dict containing counts for each test type (`positive`, `negative`, `ui`, `security`, `edge_case`), total number of test cases (`total`), and a formatted distribution string (`distribution_string`).

- **Details:**
  - Enforces at least one test case per category.
  - Adjusts positive test case count to ensure the total matches the input number.
  - Provides a multi-line distribution string suitable for inclusion in prompts or reports.

---

### `validate_test_type(test_type: str) -> str`

Validate and normalize the test type string.

- **Args:**
  - `test_type` (str): Provided test type string.

- **Returns:**
  - Normalized test type string, defaulting to `"Functional"` if the input is empty or only whitespace.

- **Notes:**
  - Preserves case and formatting but trims whitespace.
  - Accepts various common test types such as Functional, Integration, E2E, API, Security, Performance, UI, Regression, Smoke, Unit, System, Acceptance, etc.

---

### `has_existing_numbering(text: str) -> bool`

Check if a given text string starts with numbering-like patterns.

- **Args:**
  - `text` (str): Input text to analyze.

- **Returns:**
  - `True` if the text starts with numbering patterns such as `"1."`, `"2)"`, `"Step 1:"`, `"1 -"`; otherwise, `False`.

- **Patterns detected:**
  - Numeric followed by punctuation (`.`, `)`, `:` or `-`)
  - The word "Step" followed by a number and optional punctuation

---

### `remove_existing_numbering(text: str) -> str`

Remove all leading numbering patterns from the input text, including multiple levels like `"1. 2. Open page"`.

- **Args:**
  - `text` (str): Text possibly containing numbering.

- **Returns:**
  - The input text with all numbering prefixes removed.

- **Safety:**
  - Iteratively removes numbering up to 5 times to handle nested numbering and avoid infinite loops.

---

### `format_step_with_number(number: int, text: str, preserve_existing: bool = True) -> str`

Format a test step with a step number.

- **Args:**
  - `number` (int): Step number to prepend.
  - `text` (str): Step description text.
  - `preserve_existing` (bool): If `True`, retains existing numbering if present. Otherwise, normalizes to `"N. Text"` format with numbering replaced.

- **Returns:**
  - Formatted step string.

---

### `load_json(file_path: str) -> Dict[str, Any]`

Load JSON data from a file.

- **Args:**
  - `file_path` (str): Path to JSON file. Can be absolute or a filename relative to the `config` directory.

- **Returns:**
  - Parsed JSON data as a Python dictionary or list.

---

### `save_json(data: Any, file_path: str)`

Save data to a JSON file.

- **Args:**
  - `data` (Any): Data to serialize to JSON.
  - `file_path` (str): Destination file path.

- **Notes:**
  - Supports indentation and serialization of non-standard types by converting them to strings.

---

### `export_to_excel(test_cases: List[TestCase], output_path: str)`

Export a list of test cases to an Excel (.xlsx) file.

- **Args:**
  - `test_cases` (List[TestCase]): List of `TestCase` objects to export.
  - `output_path` (str): Path where the Excel file will be saved.

- **Details:**
  - Includes comprehensive test case details and concatenates associated test steps and expected results.
  - Uses pandas with `openpyxl` engine for Excel operations.

---

### `export_results_to_excel_with_sheets(results: Dict[str, Any], output_path: str)`

Export test case comparison results into an Excel file with multiple sheets.

- **Args:**
  - `results` (Dict[str, Any]): Dictionary containing test case results with decision types.
  - `output_path` (str): Path to save the Excel file.

- **Sheets created:**
  1. **All Test Cases:** All processed test cases.
  2. **Modified:** Test cases with decision type `ADDON`.
  3. **New:** Test cases with decision type `NEW`.

- **Additional details:**
  - Includes comparison data such as decision, similarity, confidence, reasoning, and coverage expansion.
  - Automatically adjusts column widths for readability.
  - Creates empty sheets with headers if no modified or new test cases are present.

---

### `export_test_cases_user_format(test_cases: List[TestCase], output_path: str)`

Export test cases using a user-preferred Excel format with specific columns and formatting.

- **Args:**
  - `test_cases` (List[TestCase]): List of `TestCase` objects.
  - `output_path` (str): Output Excel file path.

- **Columns included:**
  - Test Case ID, Layer, Test Case Scenario, Test Case, Pre-Condition, Test Case Type, Test Steps, Expected Result, Priority.

- **Formatting:**
  - Test steps and expected results are concatenated with numbering and line breaks.
  - Applies specific column widths and enables text wrapping for readability.

---

### `export_to_csv(test_cases: List[TestCase], output_path: str)`

Export test cases to a CSV file.

- **Args:**
  - `test_cases` (List[TestCase]): List of test cases.
  - `output_path` (str): CSV file path.

- **Details:**
  - Fields are separated and test steps concatenated with `" | "` separator between each step.

---

### `parse_test_case_json(json_data: Dict[str, Any]) -> TestCase`

Parse a dictionary derived from JSON into a `TestCase` model instance.

- **Args:**
  - `json_data` (Dict[str, Any]): JSON data representing a test case.

- **Returns:**
  - A `TestCase` object populated with parsed fields.

- **Features:**
  - Converts test steps from various formats (list of dicts or strings).
  - Cleans up numbering in step action texts.
  - Generates unique IDs if not provided.
  - Sets default values for missing fields.
  - Validates test type, coerces `expected_outcome` to string.
  - Determines regression flag automatically based on priority if not explicitly set.

---

### `calculate_text_similarity(text1: str, text2: str) -> float`

Calculate simple Jaccard similarity between two text strings.

- **Args:**
  - `text1` (str): First text string.
  - `text2` (str): Second text string.

- **Returns:**
  - Similarity score (float) between 0 and 1.

- **Details:**
  - Splits texts into word sets, computes intersection over union.

---

### `format_timestamp(dt: datetime) -> str`

Format a datetime object into a standardized string representation.

- **Args:**
  - `dt` (datetime): Datetime object.

- **Returns:**
  - String formatted as `YYYY-MM-DD HH:MM:SS`.

---

### `import_from_excel(file_path: str) -> List[TestCase]`

Import test cases from an Excel file supporting multiple column naming conventions.

- **Args:**
  - `file_path` (str): Path to the Excel file.

- **Returns:**
  - List of `TestCase` objects parsed from the spreadsheet.

- **Capabilities:**
  - Maps multiple possible column names for each data field.
  - Parses test steps from strings with numbering and "action -> expected result" patterns.
  - Automatically generates IDs if missing.
  - Handles missing data and fills in default values.
  - Parses boolean and string representations for regression flag.
  - Resilient to parsing errors, logs warnings, and skips invalid rows.

---

### `import_from_json(file_path: str) -> List[TestCase]`

Import test cases from a JSON file.

- **Args:**
  - `file_path` (str): Path to JSON file.

- **Returns:**
  - List of `TestCase` objects.

- **Supported JSON formats:**
  - Array of test case objects.
  - Object containing `"test_cases"` or `"testCases"` arrays.
  - Single test case object.

- **Error Handling:**
  - Skips invalid test case data with warnings.
  - Attempts to parse each test case independently.

---

# Data Models (Imported Types)

- `TestCase`  
  Represents a full test case with fields like ID, title, description, business rules, preconditions, test steps, expected outcomes, tags, priority, test type, and other metadata.

- `TestStep`  
  Represents a single step in a test case including step number, action text, and expected result.

- `DecisionType`  
  Enumerated type used in comparison results (e.g., `ADDON` for modified, `NEW` for new test cases).

---

# External Dependencies

- `pandas` (for Excel and CSV processing)
- `openpyxl` (Excel writer engine)
- `json`, `hashlib`, `re`, `datetime`
- Models and configuration imported from:
  - `core.models`: Contains `TestCase`, `TestStep`, `DecisionType`
  - `config.config`: Contains configuration values for minimum test case percentages

---

# Usage Summary

This module provides essential building blocks to manage test case lifecycle and data interchange, including:

- Calculating the distribution of test cases by type for test generation.
- Importing and exporting test cases in JSON, Excel, and CSV formats with flexible schema handling.
- Formatting and cleaning test step descriptions.
- Generating unique consistent test case IDs.
- Handling test case comparison results with detailed Excel reporting.
- Utility functions for timestamp formatting and simple text similarity estimation.

---

# Notes

- Functions are designed with robustness in mind, handling missing data and common formatting variations.
- Some functions rely on configuration values defined externally (`Config` class).
- Text extraction and cleaning utilities use regular expressions to handle common numbering styles.
- Exported files include Excel styling for readability and user-preferred formats.
- Import functions try to support a variety of column headers and input styles to ease integration with different input sources.

## File: create_regression_suite.py
# Documentation for `create_regression_suite.py`

---

## Overview

This Python script automates the creation and export of a regression test suite from an API-based test case management system. It is designed to be run **after** the API server is started locally.

The script performs the following key operations:

- Waits until the API server is ready.
- Checks existing test cases and reports regression-marked ones.
- Exports high-priority regression tests to an Excel file.
- Exports all regression tests regardless of priority to a separate Excel file.
- Provides a summary report of regression test cases by priority and test type.

---

## Usage

Run the script in a terminal:

```bash
python create_regression_suite.py
```

Ensure the API server is running locally at `http://localhost:8000` before executing the script.

---

## Requirements

- Python 3.x
- `requests` library (for HTTP calls)
- API server running locally and exposing endpoints as per documented paths below.

---

## Constants

- `API_BASE`: Base URL of the API. Defaults to `http://localhost:8000`.

---

## Functions

### `wait_for_api() -> bool`

Waits for the API server readiness by pinging the `/health` endpoint.

**Behavior:**
- Tries up to 30 times (waiting 1 second between attempts).
- Considers API ready if `/health` returns HTTP 200.
- Prints progress and final status.
- Returns `True` if API is ready, else `False`.

---

### `create_regression_suite()`

Main function that orchestrates the regression test suite creation process.

**Steps Performed:**

1. **API Health Check**
   - Calls `wait_for_api()` to ensure the API is reachable before proceeding.

2. **Check Existing Test Cases**
   - GET `/test-cases?suite_name=default`
   - Lists total test cases and counts how many are marked with `"is_regression": True`.
   - Provides tips if no regression tests are found.

3. **Export High-Priority Regression Tests**
   - POST `/export/filtered-test-suite`
   - Filtering criteria: 
     - `"suite_name": "default"`
     - `"format": "excel"`
     - `"priorities": ["High", "Critical"]`
     - `"is_regression": True`
   - Saves response content as `regression_suite_high_critical.xlsx`.
   - Handles cases where no tests match the filter.

4. **Export All Regression Tests**
   - POST `/export/filtered-test-suite`
   - Filtering criteria:
     - `"suite_name": "default"`
     - `"format": "excel"`
     - `"is_regression": True`
   - Saves response content as `regression_suite_all.xlsx`.

5. **Summary**
   - GET `/test-cases/filtered?is_regression=True`
   - Displays count of regression tests.
   - Breaks down counts by priority (`Critical`, `High`, `Medium`, `Low`).
   - Breaks down counts by test type.
   - Provides guidance if no regression tests are found.

6. **Next Steps**
   - Informs user to review exported Excel files.
   - Suggests importing files to a test management tool.
   - Mentions continuous integration/continuous delivery integration.
   - References a markdown guide `HOW_TO_CREATE_REGRESSION_SUITE.md` for detailed instructions.

---

## API Endpoints Used

| HTTP Method | Endpoint                       | Description                                                          |
|-------------|--------------------------------|----------------------------------------------------------------------|
| GET         | `/health`                     | Health-check endpoint; returns 200 if API is healthy.                |
| GET         | `/test-cases`                 | Retrieves list of test cases; supports query parameter `suite_name`.|
| POST        | `/export/filtered-test-suite`| Exports a filtered test suite to specified format (Excel).           |
| GET         | `/test-cases/filtered`        | Retrieves filtered test cases; supports query parameters such as `is_regression`. |

---

## Output Files

- `regression_suite_high_critical.xlsx`: Excel file containing only regression test cases with priority High or Critical.
- `regression_suite_all.xlsx`: Excel file containing all regression test cases regardless of priority.

---

## Error Handling

- Network and server errors during API calls are caught and printed with a description.
- Timeout handling to avoid indefinite waiting.
- Status codes other than 200 during export or fetch operations print warnings accordingly.

---

## Notes

- The script assumes that test cases API responses are JSON objects with fields such as `is_regression`, `priority`, and `test_type`.
- The script uses UTF-8 console output including emojis for user-friendly logs.
- Excel export files can be imported into other test management or automation tools.
- Ensure the API server implementation matches the expected API contract for smooth operation.

---

## Contact / References

- For detailed instructions, refer to the `HOW_TO_CREATE_REGRESSION_SUITE.md` document.
- Script author / maintainer contact is not provided (assumed internal or open-source project).

---

# End of Documentation

## File: engines/__init__.py
"""
AI Engines Package
==================

This package provides a suite of AI engines and utilities designed for retrieval-augmented generation (RAG),
embedding generation, comparison tasks, test case generation and management, and contextual engineering.

Modules and Classes
-------------------

- `rag_engine.RAGEngine`  
  Implements retrieval-augmented generation capabilities, combining retrieval techniques with generative models
  to enhance response relevance and accuracy.

- `embeddings.EmbeddingGenerator`  
  Provides functionality to generate vector embeddings from various data inputs, facilitating semantic search,
  similarity comparisons, and other embedding-based operations.

- `comparison_engine.ComparisonEngine`  
  Offers tools for comparing embeddings, documents, or other data structures to evaluate similarity, differences,
  or other relational metrics.

- `test_case_generator.TestCaseGenerator`  
  Automates the creation of test cases to support validation and testing of AI models or software components.

- `test_case_manager.TestCaseManager`  
  Manages test cases, including storage, retrieval, execution status tracking, and result management.

- `context_engineering.ContextEngineer`  
  Supports advanced context manipulation and engineering to enhance AI model interactions by optimizing prompt
  or context structures.

Package Contents
----------------

The main package exports the following classes for direct import:

```python
from ai_engines import (
    RAGEngine,
    EmbeddingGenerator,
    ComparisonEngine,
    TestCaseGenerator,
    TestCaseManager,
    ContextEngineer
)
```

Usage
-----

Import the required classes from this package to build applications involving retrieval-augmented generation,
embedding generation, comparison analysis, and automated test case workflows.

Example:

```python
from ai_engines import RAGEngine, EmbeddingGenerator

rag = RAGEngine(...)
embedder = EmbeddingGenerator(...)
```

This package serves as a foundational toolkit for building complex AI-driven systems with modular components focused
on knowledge retrieval, embedding operations, comparison logic, and test automation.

"""

## File: engines/comparison_engine.py
# ComparisonEngine Class Documentation

## Overview

The `ComparisonEngine` class performs advanced similarity analysis and comparison between software test cases. It leverages both semantic embeddings and large language model (LLM) contextual analysis, combined into a hybrid scoring system, to assess relationships such as identical, additive (add-on), or new test cases. An optional context engineering component improves prompt construction and LLM analysis.

---

## Module Description

```python
"""
Comparison engine for analyzing test case similarities with Context Engineering
"""
```

This module provides an engine for comparing two test cases through a hybrid approach of embedding-based semantic similarity and deep LLM-based context analysis. It helps identify relationships like identical test cases, add-ons (test coverage expansions), or new test cases, assisting in managing and evolving test suites systematically.

---

## Class: ComparisonEngine

### Purpose

The `ComparisonEngine` is responsible for:

- Generating semantic embeddings of test cases.
- Utilizing an LLM (via AzureOpenAI) for detailed relationship analysis.
- Combining semantic and LLM similarity into a hybrid score.
- Making informed decisions about test case relationships.
- Explaining decisions with human-readable reasoning.
- Computing confidence scores to express certainty.

### Initialization

```python
def __init__(self, use_context_engineering: bool = True):
```

- **use_context_engineering** (`bool`): Flag to enable advanced context engineering for prompt enhancement and analysis improvement (default: `True`).

Initializes:

- AzureOpenAI client with API keys and deployment info from configuration.
- Embedding generator for semantic similarity.
- Loads static prompt templates from `prompts.json`.
- Initializes the `ContextEngineer` when context engineering is enabled.

---

### Public Methods

#### `compare_test_cases`

```python
def compare_test_cases(
    self, 
    new_test_case: TestCase, 
    existing_test_case: TestCase,
    historical_decisions: Optional[List[Dict]] = None
) -> ComparisonResult:
```

**Purpose:**  
Compare two test cases to evaluate their relationship through hybrid semantic and contextual similarity.

**Arguments:**  
- `new_test_case` (`TestCase`): The new test case that needs to be compared.  
- `existing_test_case` (`TestCase`): An existing reference test case from the knowledge base.  
- `historical_decisions` (`Optional[List[Dict]]`): Optional list of past decision data to inform context.

**Returns:**  
- `ComparisonResult`: An object containing similarity score, decision type, reasoning explanation, behavioral and business rule matches, coverage expansions, and confidence metrics.

**Workflow:**  
1. Generates embeddings and calculates semantic similarity.  
2. Conducts in-depth context analysis using an LLM.  
3. Converts LLM output into a similarity score.  
4. Calculates a hybrid similarity score combining semantic and LLM scores.  
5. Makes a decision enumerating if the test case is the same, an add-on, or new.  
6. Generates human-readable reasoning for the decision.  
7. Computes an overall confidence score.

---

### Internal Methods

These helper methods are used internally within the `compare_test_cases` method.

#### `_analyze_with_llm`

```python
def _analyze_with_llm(
    self, 
    new_test_case: TestCase, 
    existing_test_case: TestCase,
    historical_decisions: Optional[List[Dict]] = None
) -> Dict[str, Any]:
```

**Purpose:**  
Invoke the large language model to assess the relationship between two test cases with support for context engineering-enhanced prompts.

**Arguments:**  
- `new_test_case` (`TestCase`): The new test case to analyze.  
- `existing_test_case` (`TestCase`): Existing test case for comparison.  
- `historical_decisions` (`Optional[List[Dict]]`): Past decisions to provide context.

**Returns:**  
- Dictionary with keys such as `"business_rule_match"`, `"behavior_match"`, `"coverage_expansion"`, `"relationship"`, and `"reasoning"` as the analysis output.

**Details:**  
- Builds prompts either with or without context engineering.  
- Handles JSON extraction and cleaning from the LLM response.  
- Provides fallback parsing strategies for malformed responses.  
- Supplies default values for missing fields in output.

---

#### `_calculate_llm_similarity`

```python
def _calculate_llm_similarity(self, analysis: Dict[str, Any]) -> float:
```

**Purpose:**  
Convert the descriptive LLM analysis into a normalized numerical similarity score (0.0 - 1.0).

**Arguments:**  
- `analysis` (`Dict[str, Any]`): The result dictionary from LLM analysis.

**Returns:**  
- Float similarity score reflecting semantic and behavioral closeness.

**Scoring logic:**  
- Base score from `relationship` category (e.g., "identical" = 1.0, "different" = 0.2).  
- Additive boosts for `business_rule_match` (+0.15) and `behavior_match` (+0.10).

---

#### `_make_decision`

```python
def _make_decision(
    self, 
    hybrid_similarity: float,
    semantic_similarity: float,
    analysis: Dict[str, Any]
) -> DecisionType:
```

**Purpose:**  
Make a final categorical decision based on similarity scores and LLM analysis.

**Arguments:**  
- `hybrid_similarity` (`float`): Combined LLM and embedding similarity score.  
- `semantic_similarity` (`float`): Embedding-based similarity only.  
- `analysis` (`Dict[str, Any]`): Contextual information from the LLM.

**Returns:**  
- One of `DecisionType` enum values: `SAME`, `ADDON`, or `NEW`.

**Decision Rules:**  
- **SAME:** High hybrid + semantic similarity, matched business rules & behavior, and identified as identical.  
- **ADDON:** Medium-high similarity, business matches, and coverage expansions or expanded relationship.  
- **NEW:** Otherwise, considered a new test case.

---

#### `_generate_reasoning`

```python
def _generate_reasoning(
    self, 
    decision: DecisionType, 
    hybrid_similarity: float,
    semantic_similarity: float,
    llm_similarity: float,
    analysis: Dict[str, Any]
) -> str:
```

**Purpose:**  
Generate a natural language explanation for the chosen decision.

**Arguments:**  
- `decision` (`DecisionType`): The classification decision.  
- `hybrid_similarity` (`float`): The combined similarity score.  
- `semantic_similarity` (`float`): Embedding similarity component.  
- `llm_similarity` (`float`): LLM similarity component.  
- `analysis` (`Dict[str, Any]`): Detailed LLM-derived analysis.

**Returns:**  
- Reasoning text string explaining the decision.

**Details:**  
- Uses an LLM prompt and static templates to produce explanation text.  
- Falls back to a concise string with scores if LLM fails.

---

#### `_calculate_confidence`

```python
def _calculate_confidence(
    self, 
    hybrid_similarity: float,
    semantic_similarity: float,
    llm_similarity: float,
    analysis: Dict[str, Any]
) -> float:
```

**Purpose:**  
Compute a confidence score (0 to 1) based on how well the semantic and LLM components agree and quality of matches.

**Arguments:**  
- `hybrid_similarity` (`float`): Combined score.  
- `semantic_similarity` (`float`): Embedding-based score.  
- `llm_similarity` (`float`): LLM-based score.  
- `analysis` (`Dict[str, Any]`): Detailed LLM analysis.

**Returns:**  
- Confidence as a float in `[0, 1]`.

**Computation details:**  
- Starts from hybrid similarity.  
- Adds a small bonus for semantic and LLM score agreement.  
- Adds boosts if business rules and behavior matches exist.  
- Caps confidence at 1.0.

---

## Configuration Dependencies

The engine relies on several configuration constants and settings typically defined in the `Config` object:

- `AZURE_OPENAI_API_KEY`  
- `AZURE_OPENAI_API_VERSION`  
- `AZURE_OPENAI_ENDPOINT`  
- `AZURE_OPENAI_DEPLOYMENT_NAME`  
- `SEMANTIC_WEIGHT` (default 0.6)  
- `LLM_WEIGHT` (default 0.4)  
- `THRESHOLD_SAME` (similarity cutoff for "same" decision)  
- `THRESHOLD_ADDON_MIN` (lower bound for "add-on" decision)

---

## Dependencies

- **AzureOpenAI Client**: For interfacing with Azure-hosted LLMs.  
- **EmbeddingGenerator**: Module generating embeddings and computing similarity.  
- **ContextEngineer**: (optional) Enhances LLM prompts with test case context.  
- **TestCase, ComparisonResult, DecisionType**: Data models representing test cases, output, and decision categories.  
- **prompts.json**: JSON file containing prompt templates for LLM queries and explanations.

---

## Usage Example (pseudo-code)

```python
engine = ComparisonEngine(use_context_engineering=True)

comparison_result = engine.compare_test_cases(
    new_test_case=test_case_1,
    existing_test_case=test_case_2,
    historical_decisions=past_decisions_list
)

print(f"Decision: {comparison_result.decision}")
print(f"Similarity Score: {comparison_result.similarity_score:.2%}")
print(f"Confidence: {comparison_result.confidence_score:.2%}")
print(f"Reasoning: {comparison_result.reasoning}")
```

---

## Summary

`ComparisonEngine` is a robust tool to semantically and contextually compare software test cases, facilitating smarter test management by understanding when tests are equivalent, expansions, or entirely new—backed by explainable AI-powered decision support.

## File: engines/context_engineering.py
# Context Engineer Module Documentation

## Overview

The **Context Engineer** module provides advanced context engineering capabilities specifically designed to enhance the performance of Retrieval-Augmented Generation (RAG) workflows for test case generation and analysis. It implements state-of-the-art prompting techniques such as few-shot learning, chain-of-thought prompting, context augmentation, dynamic example selection, and role-based prompting to improve the quality, relevance, and coverage of generated test cases.

This module is intended for use in automated test case generation and analysis systems, assisting QA engineers and software architects in deriving comprehensive and precise test cases from raw requirements and existing knowledge bases.

---

## Module Components

### Imports

- Standard libraries: `os`, `sys`, `json`
- Type hints: `List`, `Dict`, `Any`, `Optional`
- Project-specific imports:
  - `TestCase`, `UserStory` models from `core.models`
  - Configuration class from `config.config`

---

## Class: `ContextEngineer`

Primary class implementing context engineering for RAG-based test case workflows.

### Description

Encapsulates methods to produce enhanced prompts for test case generation, comparison, and merging by leveraging domain knowledge, contextual examples, and advanced prompting patterns.

It supports:

- Few-shot learning by incorporating exemplary test cases
- Chain-of-thought prompting to encourage step-wise reasoning
- Context augmentation with domain and technical information
- Dynamic selection of examples keyed to requirement analysis
- Role-based prompting to simulate expert QA engineer behavior

---

### Initialization

```python
def __init__(self)
```

- Loads few-shot examples and context templates internally upon instantiation.

---

### Private Methods

#### `_load_examples() -> Dict[str, Dict[str, Any]]`

Loads example test cases mapped by scenario types for use in few-shot prompting.

- **Example types include**:
  - `simple_crud`: Basic CRUD user account creation
  - `api_integration`: API endpoint testing scenarios
  - `complex_workflow`: End-to-end checkout and payment flow

Each example contains detailed fields such as:

- Requirement description
- A set of fully structured test cases covering preconditions, steps, postconditions, tags, priorities, test type, boundary conditions, and side effects.

---

#### `_load_context_templates() -> Dict[str, str]`

Provides templates for structured domain, technical, and quality context to insert into prompts.

- Templates contain placeholders such as `{industry}`, `{app_type}`, `{tech_stack}`, `{coverage_goal}`, etc., intended for dynamic context expansion.

---

#### `_match_requirement_to_example(requirement: str) -> str`

Analyzes the requirement text to heuristically assign it to one of the predefined example types:

- Returns `"api_integration"` if API-related keywords are detected
- Returns `"complex_workflow"` if workflow or payment-related keywords found
- Defaults to `"simple_crud"`

---

### Public Methods

#### `enhance_generation_prompt(...) -> Dict[str, str]`

Constructs an enhanced prompt for generating test cases from a given requirement.

**Parameters**:

- `requirement` (str): Requirement textual description.
- `requirement_type` (str, default `"user_story"`): Type of requirement.
- `domain_context` (Optional[Dict[str, Any]]): Optional domain-specific context data to include.
- `similar_examples` (Optional[List[TestCase]]): Few-shot examples selected dynamically from knowledge base.
- `focus_areas` (Optional[List[str]]): Topics or concerns to emphasize (e.g., security, performance).
- `num_test_cases` (int, default 12): Number of test cases to generate.
- `test_distribution` (str): Guidelines on how to distribute test case types among the output.

**Returns**: 

A dictionary with keys:

- `"system"`: The system prompt instructing the LLM on persona, expertise, and task.
- `"user"`: The detailed user prompt containing stepwise chain-of-thought instructions, examples, and strict output formatting rules.

**Notable Features**:

- Incorporates domain context when provided.
- Integrates top similar test cases for few-shot learning.
- Provides detailed instructions to enforce a standardized test case JSON schema.
- Defines critical rules to ensure quality such as title suffix conventions, precondition detail level, and step ordering.
- Emphasizes role-based prompting reflecting a senior QA engineer with 15+ years of experience.

---

#### `enhance_comparison_prompt(...) -> Dict[str, str]`

Generates an enhanced prompt to compare two test cases for equivalence or scope overlap.

**Parameters**:

- `new_test_case` (TestCase): The new candidate test case.
- `existing_test_case` (TestCase): An existing test case to compare against.
- `similarity_score` (float): Semantic similarity score (0.0 - 1.0) between the two.
- `historical_decisions` (Optional[List[Dict]]): Optional list of past similar comparison decisions for context.

**Returns**: 

Dictionary with:

- `"system"`: Instructions defining an expert test case analyst persona.
- `"user"`: Stepwise chain-of-thought prompt guiding semantic similarity interpretation, business rule comparison, coverage analysis, and final relationship classification.

**Output enforces**:

- Return of a JSON object indicating: 
  - Whether the business rule and behavior match,
  - What coverage expansions exist,
  - The high-level relationship (`identical`, `expanded`, `different`),
  - Detailed reasoning.

---

#### `enhance_merge_prompt(...) -> Dict[str, str]`

Creates a prompt for intelligently merging two similar test cases into a single optimized test case.

**Parameters**:

- `existing_test_case` (TestCase): The base test case.
- `new_test_case` (TestCase): The test case to be merged.
- `coverage_expansion` (List[str]): List of additional coverage areas contributed by the new test case.

**Returns**:

Dictionary with:

- `"system"`: Persona of an expert test case architect.
- `"user"`: Structured instructions detailing stepwise merge considerations such as business rule union, precondition consolidation, test step parameterization, metadata updating, and final JSON output requirements.

**Merging guidelines include**:

- Eliminate duplicate preconditions.
- Parameterize common steps when possible.
- Maintain array types strictly.
- Preserve or increase coverage without loss of clarity.

---

#### `extract_domain_context(existing_test_cases: List[TestCase]) -> Dict[str, Any]`

Analyzes a list of existing test cases to extract project-specific domain context for prompt augmentation.

**Parameters**:

- `existing_test_cases`: List of `TestCase` objects from the knowledge base.

**Returns**: Dictionary including:

- `common_tags`: Top 5 most frequent tags across test cases.
- `primary_test_types`: Top 3 test types by frequency.
- `total_test_cases`: Count of analyzed test cases.
- `average_steps`: Average number of test steps per test case.
- `high_priority_count`: Count of test cases marked as High priority.

Useful for enhancing prompt contextual relevance using RAG techniques.

---

#### `get_focus_areas(requirement: str) -> List[str]`

Identifies relevant focus areas for testing based on keyword analysis of the requirement text.

**Parameters**:

- `requirement`: The text of the requirement.

**Returns**: A list of testing focus areas such as:

- Security testing (authentication, authorization)
- Performance testing (load, timeouts)
- Data integrity (CRUD, consistency)
- Integration testing (APIs, error handling)
- UI/UX testing (accessibility, responsive design)
- Error handling (validation, recovery)

Defaults to `["Comprehensive functional testing"]` if none matched.

---

## Data Models (Imported)

- **TestCase**: Represents a detailed test case entity with fields such as title, description, test steps, pre/postconditions, tags, priorities, business rule, etc.
- **UserStory**: Represents requirement or user story details.

---

## Usage Summary

An external integration typically proceeds as follows:

1. **Instantiate**: Create a `ContextEngineer` object.

2. **Context Extraction**: Call `extract_domain_context` with existing test cases to gather contextual metadata.

3. **Determine Focus Areas**: Use `get_focus_areas` to identify testing emphasis based on the requirement.

4. **Prompt Generation**: Generate a comprehensive prompt for test case generation by invoking `enhance_generation_prompt` with the requirement, domain context, similar examples from KB, and focus areas.

5. **LLM Execution**: Use the generated prompts to query a language model (LLM).

6. **Test Case Comparison & Deduplication**: Use `enhance_comparison_prompt` to analyze whether new test cases are redundant compared to existing ones.

7. **Test Case Merging**: When applicable, generate merged test cases via `enhance_merge_prompt`.

This pipeline ensures automated test case suggestions are relevant, thorough, and maintainable.

---

## Notes

- The model heavily follows a **strict JSON schema** for generated test cases to ensure downstream tooling compatibility.
- Supports **chain-of-thought prompting** to improve LLM reasoning visibility and output quality.
- Implements **role-based prompting** simulating expert QA engineers and test architects.
- Leverages **few-shot learning** with curated high-quality examples for test case generation guidance.
- Designed to support **dynamic example selection** for contextual relevance.

---

## Example: Generation Prompt Structure

1. System prompt instructing on expertise and task.
2. Optional domain context added.
3. User prompt with multi-step chain-of-thought for analysis and generation.
4. Few-shot examples injected based on requirement matching.
5. Clear rules on output formatting and test case schema.
6. Focus areas emphasized in prompt for targeted coverage.
7. Request for exact number and distribution of test cases required.

---

This detailed documentation should assist developers and architects in understanding, using, extending, and integrating the `ContextEngineer` module within automated test case generation and test management systems.

## File: engines/embeddings.py
# EmbeddingGenerator

The `EmbeddingGenerator` class provides functionality to generate vector embeddings for text data using the Azure OpenAI API. This is primarily intended for embedding test cases or similar textual content and supports caching, batch processing, and similarity calculations.

---

## Class: `EmbeddingGenerator`

### Description
Handles generation of text embeddings by interacting with Azure OpenAI's embedding API. Offers methods for individual and batch embedding generation, similarity measurement between embeddings, and cache management for performance optimization.

### Initialization
```python
def __init__(self):
```
- Initializes an Azure OpenAI client using API key, version, and endpoint information from a configuration module.
- Retrieves the embedding model deployment identifier.
- Initializes an in-memory cache (`dict`) to store computed embeddings keyed by a hash or the original text.

---

### Methods

#### `generate_embedding(text: str) -> List[float]`
Generate the embedding vector for a single input text.

- **Parameters:**
  - `text` (`str`): The input text string to generate an embedding for.
  
- **Returns:**
  - `List[float]`: A list of floating-point numbers representing the embedding vector of the input text.
  
- **Details:**
  - Uses MD5 hash of the input text as a cache key to optimize repeated embedding requests.
  - Truncates input text to the first 8000 characters to respect token limits.
  - Queries the Azure OpenAI embeddings API to compute the embedding if it's not found in the cache.
  - Caches the embedding result for future reuse.
  - Raises exceptions on API errors, printing a descriptive error message before propagating.

---

#### `generate_embeddings_batch(texts: List[str]) -> List[List[float]]`
Generate embedding vectors for a list of texts in batches.

- **Parameters:**
  - `texts` (`List[str]`): A list of text strings to generate embeddings for.
  
- **Returns:**
  - `List[List[float]]`: A list where each element corresponds to the embedding vector of the input text at the same index in the input list.
  
- **Details:**
  - Processes texts in batches of size 16 to mitigate rate limits.
  - Checks cache for each text embedding. Only sends uncached texts to API.
  - Cache keys here are the raw texts rather than hashes.
  - Aggregates embedding results from the cache and API.
  - Raises exceptions on API errors, printing a descriptive error message before propagating.

---

#### `calculate_similarity(embedding1: List[float], embedding2: List[float]) -> float`
Calculate the cosine similarity between two embeddings.

- **Parameters:**
  - `embedding1` (`List[float]`): First embedding vector.
  - `embedding2` (`List[float]`): Second embedding vector.
  
- **Returns:**
  - `float`: Normalized similarity score between 0 and 1, where 1 indicates identical vectors and 0 indicates opposites or lack of similarity.
  
- **Details:**
  - Converts embedding lists to numpy arrays.
  - Calculates cosine similarity and normalizes from range [-1, 1] to [0, 1].
  - Returns 0.0 if either vector is zero-length to avoid division errors.

---

#### `clear_cache()`
Clears all cached embeddings.

- **Parameters:** None
- **Returns:** None
- **Details:** Empties the in-memory cache storing embeddings, useful for freeing up memory or resetting state.

---

## Dependencies
- `os`, `sys` for path management.
- `hashlib` for generating cache keys.
- `numpy` for vector operations.
- `AzureOpenAI` client for embedding API calls.
- Configuration (`Config`) providing API keys, version, endpoint, and model deployment.

---

## Usage Example

```python
generator = EmbeddingGenerator()

# Generate embedding for a single text
embedding = generator.generate_embedding("Example test case")

# Generate embeddings for multiple texts
batch_embeddings = generator.generate_embeddings_batch(["test case 1", "test case 2"])

# Calculate similarity between two embeddings
similarity = generator.calculate_similarity(batch_embeddings[0], batch_embeddings[1])

# Clear cached embeddings
generator.clear_cache()
```

---

## Notes
- The batch method uses raw text strings as cache keys, while single text method uses hashed keys. This discrepancy should be considered if cache sharing is intended.
- Error handling prints exceptions and re-raises them, allowing consumers to handle failures as needed.
- Text truncation ensures compliance with API input limits but may affect embedding completeness for very long texts.

## File: engines/rag_engine.py
# RAGEngine Documentation

## Overview

`RAGEngine` is a Retrieval-Augmented Generation (RAG) engine designed for managing a knowledge base of test cases. It uses **ChromaDB** for vector storage and similarity search, and integrates an embedding generator to convert test cases into vector embeddings.

This engine supports storing, searching, updating, and deleting test cases in an efficient, persistent vector database.

---

## Dependencies

- `chromadb` - Chroma vector database client
- `core.models.TestCase` - Data model for individual test cases
- `engines.embeddings.EmbeddingGenerator` - Module generating vector embeddings for texts
- `config.config.Config` - Configuration module with persistence and retrieval parameters

---

## Class: `RAGEngine`

### Initialization

```python
def __init__(self)
```

Creates a persistent ChromaDB client and initializes the collection used as the test case knowledge base.

- Initializes an `EmbeddingGenerator` instance.
- Creates or fetches a ChromaDB collection named as per `Config.CHROMA_COLLECTION_NAME`.
- Persistence directory and telemetry settings are configured via `Config`.

---

### Methods

#### `add_test_case(test_case: TestCase) -> None`

Add a single test case to the knowledge base.

- Converts the `TestCase` instance to text.
- Generates an embedding using the embedding generator.
- Prepares metadata from the `TestCase` attributes.
- Adds the embedding, original text, and metadata to the ChromaDB collection.

---

#### `add_test_cases_batch(test_cases: List[TestCase]) -> None`

Add multiple test cases in batch mode.

- Processes empty input silently.
- Converts all test cases to texts.
- Generates embeddings for all texts in batch for efficiency.
- Extracts metadata for each test case.
- Adds all embeddings, documents, and metadata to the collection in a single operation.

---

#### `search_similar_test_cases(test_case: TestCase, top_k: Optional[int] = None) -> List[Dict[str, Any]]`

Retrieve a list of test cases similar to the provided `test_case`.

- Default `top_k` (number of results) is taken from `Config.RAG_TOP_K` if not provided.
- Returns an empty list if the collection is empty.
- Embeds the query `test_case` and performs a vector similarity search.
- Returns results as a list of dictionaries with:
  - `id` - test case identifier
  - `document` - original text representation
  - `metadata` - associated metadata dictionary
  - `similarity` - similarity score (1 - distance)

---

#### `get_test_case_by_id(test_case_id: str) -> Optional[Dict[str, Any]]`

Fetch a test case from the knowledge base by its unique identifier.

- Returns a dictionary with `id`, `document`, `metadata` if found.
- Returns `None` if the test case is not found or an error occurs.

---

#### `update_test_case(test_case: TestCase) -> None`

Update an existing test case in the knowledge base.

- Attempts to delete the existing entry with the same `test_case.id`.
- Adds the updated test case as a new entry.

---

#### `delete_test_case(test_case_id: str) -> None`

Remove a test case from the knowledge base by ID.

- Deletes the vector and metadata associated with `test_case_id` from the collection.

---

#### `get_all_test_cases() -> List[Dict[str, Any]]`

Retrieve all test cases currently stored in the knowledge base.

- Returns a list of dictionaries, each containing `id`, `document`, and `metadata`.

---

#### `count() -> int`

Return the current number of test cases in the knowledge base.

---

#### `reset() -> None`

Clear the entire test case knowledge base.

- Deletes the existing ChromaDB collection.
- Recreates it fresh with the original name and metadata.

---

## Usage Notes

- The engine relies on the `TestCase.to_text()` method to generate a text representation suited for embedding.
- Embedding generation may involve external models or APIs configured in `EmbeddingGenerator`.
- Persistence is enabled by default using paths from the global `Config`.
- Similarity scores are computed as `1 - distance`, assuming distance is normalized between 0 and 1.
- Batch additions improve efficiency and are preferred over multiple single insertions for large datasets.
- Exception handling in some methods silently catches errors; additional logging may be advisable in production.

---

## Example

```python
from core.models import TestCase

rag_engine = RAGEngine()

# Add a single test case
test_case = TestCase(...)
rag_engine.add_test_case(test_case)

# Search similar cases
similar_cases = rag_engine.search_similar_test_cases(test_case, top_k=5)

# Update a test case
test_case.title = "Updated title"
rag_engine.update_test_case(test_case)

# Delete a test case
rag_engine.delete_test_case(test_case.id)

# Get all test cases
all_cases = rag_engine.get_all_test_cases()

# Count test cases
count = rag_engine.count()

# Reset knowledge base
rag_engine.reset()
```

---

This documentation should assist developers in integrating and extending the `RAGEngine` for effective test case retrieval and management.

## File: engines/test_case_generator.py
# TestCaseGenerator Module Documentation

## Overview

The `TestCaseGenerator` class provides functionality to generate software test cases automatically from user stories or requirement texts using Azure OpenAI Large Language Models (LLMs) enhanced with advanced **context engineering** techniques. The generator supports both single-request and parallel batch generation strategies and offers utilities to clean and parse LLM outputs, extract business rules, and merge test cases.

---

## Module: `test_case_generator`

### Imports & Dependencies

- Standard libraries: `os`, `sys`, `json`, `re`, `typing`
- Azure OpenAI SDK: `AzureOpenAI`
- Project-specific modules:
  - `Config` — configuration parameters
  - `TestCase`, `UserStory` — data models
  - Utility functions: `load_json`, `parse_test_case_json`, `generate_id`, `calculate_test_distribution`
  - `ContextEngineer` — class providing context engineering enhancements for prompt generation

---

## Class: `TestCaseGenerator`

### Purpose

Generate high-quality, structured test case data from:

- User stories (with detailed descriptions, acceptance criteria, business rules, and optional context)
- Arbitrary requirement text

Utilizes Azure OpenAI GPT models with optional context engineering to improve prompt relevance and output quality.

---

### Initialization

```python
TestCaseGenerator(use_context_engineering: bool = True)
```

- **Arguments:**
  - `use_context_engineering` (bool): Whether to enable advanced context engineering techniques for prompt shaping.

- **Behavior:**
  - Instantiates Azure OpenAI client with Azure-specific keys and endpoint.
  - Loads prompt templates from `prompts.json`.
  - Initializes `ContextEngineer` if context engineering is enabled.

---

### Methods

---

#### `generate_from_user_story`

```python
generate_from_user_story(user_story: UserStory, num_test_cases: Optional[int] = None) -> List[TestCase]
```

- **Purpose:**
  Generate test cases from a structured `UserStory` input.

- **Arguments:**
  - `user_story` (UserStory): Object encapsulating a user story including title, description, acceptance criteria, business rules, and optionally context.
  - `num_test_cases` (Optional[int]): Desired number of test cases to generate. Uses configured defaults if omitted.

- **Returns:**
  - List of generated `TestCase` objects.

- **Description:**
  - Formats the user story fields into a comprehensive requirement text.
  - Delegates generation to `generate_from_text` method using the generated requirement string.

---

#### `generate_from_text`

```python
generate_from_text(
    requirement_text: str,
    source_document: Optional[str] = None,
    similar_examples: Optional[List[TestCase]] = None,
    domain_context: Optional[Dict[str, Any]] = None,
    num_test_cases: Optional[int] = None
) -> List[TestCase]
```

- **Purpose:**
  Generate test cases from freeform requirement text, optionally considering context, examples, and domain knowledge.

- **Arguments:**
  - `requirement_text` (str): Detailed natural language description of the requirement.
  - `source_document` (Optional[str]): Identifier of source document to tag generated test cases.
  - `similar_examples` (Optional[List[TestCase]]): Similar test cases retrieved via retrieval-augmented generation (RAG).
  - `domain_context` (Optional[Dict[str, Any]]): Domain-specific contextual information.
  - `num_test_cases` (Optional[int]): Number of test cases requested.

- **Returns:**
  - List of generated `TestCase` objects.

- **Behavior:**
  - Validates and constrains the number of test cases to configured min/max.
  - If parallel generation is enabled (via configuration), attempts to generate in parallel batches.
  - On failure or if parallel generation disabled, falls back to single-request generation.
  - Utilizes context engineering-enhanced prompts if enabled.

---

#### `_generate_single_request`

```python
_generate_single_request(
    requirement_text: str,
    source_document: Optional[str] = None,
    similar_examples: Optional[List[TestCase]] = None,
    domain_context: Optional[Dict[str, Any]] = None,
    num_test_cases: Optional[int] = None
) -> List[TestCase]
```

- **Purpose:**
  Internal method to generate test cases in a single Azure OpenAI API call.

- **Behavior:**
  - Calculates a distribution across various test case categories (positive, negative, UI, security, edge cases).
  - Uses context engineering prompts if enabled to generate focused test cases.
  - Processes LLM response, extracting and cleaning JSON output.
  - Implements robust multi-step JSON parsing with error handling and corrective attempts.
  - Converts parsed JSON objects into `TestCase` instances.
  - Annotates test cases with source document identifier if provided.

- **Raises:**
  - Exception on JSON parse failure, connection errors, timeout errors, or other unexpected issues.

---

#### `_clean_json_content`

```python
_clean_json_content(content: str) -> str
```

- **Purpose:**
  Apply heuristic-based cleaning and repair to JSON content generated by LLM to mitigate:
  - Extra markdown or non-JSON text
  - Trailing commas
  - Missing commas
  - Incorrect quotes
  - Python-style booleans/nulls
  - Unbalanced brackets and braces due to truncation
  - Other common formatting issues caused by LLM output variability

- **Returns:**
  Cleaned JSON string safe for parsing.

---

#### `extract_business_rule`

```python
extract_business_rule(test_case: TestCase) -> str
```

- **Purpose:**
  Extract or summarize the business rule underpinning a given test case by querying the LLM.

- **Arguments:**
  - `test_case` (TestCase): Target test case object for which to extract business rules.

- **Returns:**
  - Extracted business rule string or empty string on failure.

- **Behavior:**
  - Uses a dedicated business rule extraction prompt template.
  - Calls Azure OpenAI chat completions with low temperature for consistency.

---

#### `merge_test_cases`

```python
merge_test_cases(existing_test_case: TestCase, new_test_case: TestCase) -> TestCase
```

- **Purpose:**
  Combine two test cases into a single parameterized test case leveraging LLM capabilities.

- **Arguments:**
  - `existing_test_case` (TestCase): Original test case to merge into.
  - `new_test_case` (TestCase): Additional test case providing new parameters.

- **Returns:**
  - Merged `TestCase` object with an incremented version number.

- **Behavior:**
  - Sends serialized JSON representations of both test cases as prompt.
  - Invokes LLM to perform merge and returns parsed merged JSON.
  - On failure, returns the existing test case unmodified.

---

#### `_generate_with_parallel_batches`

```python
_generate_with_parallel_batches(
    requirement_text: str,
    source_document: Optional[str] = None,
    similar_examples: Optional[List[TestCase]] = None,
    domain_context: Optional[Dict[str, Any]] = None,
    num_test_cases: Optional[int] = None
) -> List[TestCase]
```

- **Purpose:**
  Generate test cases by splitting the workload into multiple focused batches processed in parallel threads.

- **Behavior:**
  - Splits generation workload into fixed categories (positive, negative, UI, security, edge).
  - For each category, defines a batch with its own focus, count, and descriptive instructions.
  - Uses a ThreadPoolExecutor to run batch generation concurrently.
  - Aggregates results from all batches.
  - Reports batch success/failure statistics.
  - Raises exception if all batches fail to generate test cases (triggers fallback).

---

#### `_generate_single_batch`

```python
_generate_single_batch(
    requirement_text: str,
    focus: str,
    count: str,
    description: str,
    source_document: Optional[str] = None,
    similar_examples: Optional[List[TestCase]] = None,
    domain_context: Optional[Dict[str, Any]] = None
) -> List[TestCase]
```

- **Purpose:**
  Generate a specific batch of test cases focusing on a given category with explicit instructions.

- **Arguments:**
  - `focus` (str): The focus area of the batch, e.g., "positive scenarios", "security scenarios".
  - `count` (str): Number or range of test cases expected (e.g., "3-4").
  - `description` (str): Explanation of what scenarios to cover.

- **Behavior:**
  - Constructs a batch-specific prompt emphasizing required fields (e.g., title).
  - Calls Azure OpenAI API with controlled token limits.
  - Cleans, parses, and converts the response to `TestCase` objects.
  - Fixes missing or untitled test case titles automatically.
  - Handles parse errors gracefully, returning an empty list on failure.

---

## Configuration Parameters (`Config`)

- `AZURE_OPENAI_API_KEY`: Azure OpenAI API key.
- `AZURE_OPENAI_API_VERSION`: API version string.
- `AZURE_OPENAI_ENDPOINT`: Azure OpenAI endpoint URL.
- `AZURE_OPENAI_DEPLOYMENT_NAME`: Deployment/model name to use.
- `DEFAULT_TEST_CASES`: Default number of test cases to generate.
- `MIN_TEST_CASES`: Minimum allowed number of test cases.
- `MAX_TEST_CASES`: Maximum allowed number of test cases.
- `USE_PARALLEL_GENERATION`: Whether to enable parallel batch generation.
- `PARALLEL_BATCH_SIZE`: Maximum threads to use for parallel batch generation.
- `BATCH_TIMEOUT_SECONDS`: Timeout for each parallel batch request.

---

## Usage Example

```python
from core.models import UserStory
from test_case_generator import TestCaseGenerator

user_story = UserStory(
    id="US123",
    title="User logs in",
    description="As a user, I want to log in to the system using my credentials.",
    acceptance_criteria=[
        "Login form is displayed",
        "User is authenticated with valid credentials",
        "Error shown for invalid credentials"
    ],
    business_rules=[
        "Password must be at least 8 characters",
        "Account locks after 3 failed attempts"
    ],
    context="The system uses OAuth2 for authentication."
)

generator = TestCaseGenerator(use_context_engineering=True)
test_cases = generator.generate_from_user_story(user_story, num_test_cases=10)

for tc in test_cases:
    print(tc.to_text())
```

---

## Notes

- The class robustly handles common LLM response formatting issues, making the test case generation resilient.
- Context engineering can significantly improve prompt efficacy by focusing the LLM on relevant test aspects.
- Parallel batch generation increases reliability and speeds generation for large test case volumes.
- Detailed debug output assists in troubleshooting and prompt tuning.
- Error handling gracefully falls back from parallel to standard generation methods.

---

This documentation captures the purpose, configuration, design, and usage of the `TestCaseGenerator` as implemented in the provided code.

## File: engines/test_case_manager.py
# TestCaseManager Module Documentation

## Overview

The `TestCaseManager` class is the main orchestrator for managing the lifecycle of software test cases based on user stories or requirements. It integrates various components such as a Retrieval-Augmented Generation engine (`RAGEngine`), test case generator, comparison engine, and a knowledge base to handle:

- Test case generation from user stories or textual requirements
- Semantic search and similarity analysis against existing test cases
- Decision-making to classify test cases as new, identical, or supplementary (addon)
- Applying decisions by updating the knowledge base and semantic search index
- Filtering, exporting, importing, and reporting on test suites

The module supports parallel processing for scalability and includes features to merge test cases and generate actionable recommendations.

---

## Class: `TestCaseManager`

### Initialization

```python
TestCaseManager()
```

Initializes all underlying components:

- `RAGEngine()` - for semantic search of test cases
- `TestCaseGenerator()` - for generation of test cases from text or user stories
- `ComparisonEngine()` - to compare and decide on similarity between test cases
- `KnowledgeBase()` - stores test cases organized by suites

---

### Methods

#### `_analyze_new_test_case(new_test_case: TestCase, top_k: Optional[int] = None) -> ComparisonResult`

- **Description:**  
  Analyzes a new test case by searching for similar test cases in the knowledge base and performing a detailed comparison to decide if it is a *new*, *same*, or *addon* test case.

- **Arguments:**  
  - `new_test_case`: The newly generated test case object to analyze.  
  - `top_k`: Optional limit on the number of similar cases retrieved (defaults to `Config.RAG_TOP_K`).

- **Returns:**  
  A `ComparisonResult` object summarizing similarity metrics, decision type (`NEW`, `SAME`, `ADDON`), reasoning, and other comparison details.

---

#### `_get_recommendation(comparison_result: ComparisonResult) -> str`

- **Description:**  
  Provides a textual recommendation/action based on the decision in a `ComparisonResult`.

- **Arguments:**  
  - `comparison_result`: The result of comparing a new test case against existing test cases.

- **Returns:**  
  A user-friendly recommendation string indicating whether to keep, merge, or create test cases.

---

#### `_reconstruct_test_case(similar_case_data: dict) -> TestCase`

- **Description:**  
  Rebuilds a `TestCase` object from metadata and stored document text retrieved from the semantic search database (`ChromaDB`).

- **Arguments:**  
  - `similar_case_data`: Dictionary data representing an existing test case from the semantic search index.

- **Returns:**  
  A reconstructed `TestCase` object for detailed comparison.

---

#### `process_user_story(user_story: UserStory, suite_name: str = "default", auto_apply: bool = False, num_test_cases: Optional[int] = None) -> Dict[str, Any]`

- **Description:**  
  Processes a given user story to generate test cases, analyze similarity with existing tests, optionally apply recommended decisions, and summarize results.

- **Arguments:**  
  - `user_story`: The `UserStory` object to process.  
  - `suite_name`: The test suite to assign test cases to (default `"default"`).  
  - `auto_apply`: If `True`, apply decisions automatically without user review.  
  - `num_test_cases`: Optional number of test cases to generate.

- **Returns:**  
  A dictionary containing:  
  - `user_story`: Input user story.  
  - `generated_test_cases`: List of generated `TestCase` objects.  
  - `results`: List of dictionaries with individual test case, comparison, and recommendation.  
  - `actions_taken`: Applied actions if `auto_apply` is enabled.  
  - `summary`: Aggregated statistics on decisions taken.

---

#### `process_requirement_text(requirement_text: str, suite_name: str = "default", auto_apply: bool = False, num_test_cases: Optional[int] = None) -> Dict[str, Any]`

- **Description:**  
  Similar to `process_user_story` but generates and analyzes test cases from free-form requirement text.

- **Arguments:**  
  Same as `process_user_story`, but with `requirement_text` as input instead of `UserStory`.

- **Returns:**  
  Dictionary structured similarly to `process_user_story`.

---

#### `apply_decision(test_case: TestCase, comparison: ComparisonResult, suite_name: str = "default", user_approved: bool = True) -> str`

- **Description:**  
  Applies the decision (keep, merge, create) for a single test case based on a comparison result to the specified test suite.

- **Arguments:**  
  - `test_case`: The test case to act on.  
  - `comparison`: Comparison result influencing the decision.  
  - `suite_name`: Target test suite name.  
  - `user_approved`: User approval flag (currently not used internally).

- **Returns:**  
  A string describing the action taken.

---

#### `_apply_decision(test_case: TestCase, comparison: ComparisonResult, suite_name: str) -> str`

- **Description:**  
  Internal method that executes the logic to keep existing, merge, or create new test cases in the knowledge base and update the RAG engine.

- **Returns:**  
  Action description string.

---

#### `_generate_summary(results: List[Dict[str, Any]]) -> Dict[str, Any]`

- **Description:**  
  Aggregates summary statistics about classification decisions for a batch of test case analysis results.

- **Returns:**  
  Dictionary with counts and percentages for: total test cases, same, addon, and new.

---

#### `get_test_suite(suite_name: str = "default") -> List[TestCase]`

- **Description:**  
  Retrieves all test cases from a named suite.

- **Returns:**  
  List of `TestCase` objects in the specified suite.

---

#### `get_filtered_test_cases(suite_name: str = "default", priorities: Optional[List[str]] = None, test_types: Optional[List[str]] = None, tags: Optional[List[str]] = None, is_regression: Optional[bool] = None) -> List[TestCase]`

- **Description:**  
  Fetches test cases from a suite filtered by priority, test type, tags, and regression status.

- **Arguments:**  
  - `priorities`: List of allowed priorities (e.g., `["High", "Critical"]`).  
  - `test_types`: List of allowed test types (e.g., `["Functional"]`).  
  - `tags`: List of tags to match (test case must have at least one).  
  - `is_regression`: Filter by regression flag (`True`, `False`, or `None` to ignore).

- **Returns:**  
  List of filtered `TestCase` objects.

---

#### `export_test_suite(suite_name: str, output_path: str, format: str = "excel", priorities: Optional[List[str]] = None, test_types: Optional[List[str]] = None, tags: Optional[List[str]] = None, is_regression: Optional[bool] = None)`

- **Description:**  
  Exports the test suite (optionally filtered) to a specified file in Excel, CSV, or JSON format.

- **Arguments:**  
  - `suite_name`: Suite to export.  
  - `output_path`: Destination file path.  
  - `format`: Export format (`"excel"`, `"csv"`, `"json"`).  
  - Filtering parameters, same as in `get_filtered_test_cases`.

- **Raises:**  
  `ValueError` if an unsupported export format is specified.

---

#### `get_statistics() -> Dict[str, Any]`

- **Description:**  
  Provides summary statistics about the knowledge base and test suites.

- **Returns:**  
  Dictionary with total test case count and list of available test suites.

---

#### `import_existing_test_cases(file_path: str, suite_name: str = "imported", file_format: str = "auto") -> Dict[str, Any]`

- **Description:**  
  Imports existing test cases from a file (Excel or JSON) into a named test suite and updates the semantic search index.

- **Arguments:**  
  - `file_path`: File system path of the input file.  
  - `suite_name`: Target suite to import records into (default `"imported"`).  
  - `file_format`: Format to import (`"excel"`, `"json"`, or `"auto"` for auto-detection based on file extension).

- **Returns:**  
  Dictionary containing:  
  - `success`: Import success flag.  
  - `imported_count`: Number of successfully imported test cases.  
  - `failed_count`: Number of failed imports.  
  - `errors`: List of error message strings encountered during import.  
  - `test_cases`: List of `TestCase` objects imported.

- **Behavior:**  
  - Performs format auto-detection if requested.  
  - On success, adds test cases to both the knowledge base and RAG engine for semantic retrieval.  
  - Handles exceptions gracefully, reporting failures without crashing.

---

## Usage Summary

This class serves as the central manager for generating, analyzing, managing, and reporting on test cases in a modular and semantically aware test automation system. It abstracts complexities of retrieval, comparison, and storage behind simple method calls which incorporate concurrency for efficient batch processing.

Typical usage flow:

1. Initialize `TestCaseManager`.
2. Generate test cases from user stories or requirement text.
3. Analyze test cases against the knowledge base.
4. Obtain recommendations and optionally apply actions automatically.
5. Filter, export, import, or report on test suites as needed.

---

## Dependencies

- Python standard libs: `os`, `sys`, `concurrent.futures`, `typing`
- Internal modules and classes (assumed to be part of the system):  
  - `core.models`: `TestCase`, `UserStory`, `ComparisonResult`, `DecisionType`  
  - `engines.rag_engine`: `RAGEngine`  
  - `engines.test_case_generator`: `TestCaseGenerator`  
  - `engines.comparison_engine`: `ComparisonEngine`  
  - `core.knowledge_base`: `KnowledgeBase`  
  - `config.config`: `Config`  
  - `core.utils`: utility functions for parsing and exporting/importing test cases.

---

## Notes

- The class uses in-code print statements for logging; production code may want to replace them with configurable logging.
- Parallel concurrency limits are capped to avoid rate limiting with external APIs/services.
- Decision-making uses configurable thresholds via `Config` constants.
- Import and export operations support Excel and JSON; CSV export supported but CSV import not implemented.
- Test cases are versioned and metadata-rich objects for effective management.

---

This documentation provides a comprehensive overview of the `TestCaseManager` functionality, usage, and API, enabling efficient integration and extension as part of a sophisticated testing automation platform.

## File: engines/test_case_updater.py
Sure! Please provide the code you'd like me to generate documentation for.

## File: examples/__init__.py
```python
"""
Example scripts demonstrating system usage

This module provides example scripts that showcase how to use the system's functionality.
It serves as a reference and guide for users to understand the typical usage patterns 
and integrations of the available components.

Contents:
- Sample executions illustrating core features
- Usage patterns for key classes and functions
- Guidance on system setup and initialization

Note:
These scripts are intended for demonstration purposes and may require adaptation for 
production use.

"""
```

## File: examples/example.py
# RAG Test Case Management System — Example Usage Documentation

This module provides example usage of the RAG Test Case Management System. It demonstrates how to create user stories, process requirement texts, generate and manage test cases, apply decisions, and export test suites using the provided interfaces.

---

## Overview

The examples show typical workflows for two kinds of inputs:

1. **User Story Processing**  
   Create and process a user story with acceptance criteria and business rules, generate test cases, review and apply decisions manually, export the test suite, and finally display knowledge base statistics.

2. **Requirement Text Processing**  
   Input free-form requirement text, automatically generate and apply test cases and decisions, and show summary of generated test cases and actions taken.

---

## Dependencies

- `core.models.UserStory` — Data model representing a user story.
- `core.utils.generate_id` — Utility for generating unique IDs.
- `engines.test_case_manager.TestCaseManager` — Main engine for managing test cases.
- Python standard libraries: `os`, `sys` (for path management).

---

## Functions

### example_user_story()

Processes a user story through the test case management system with the following steps:

1. **User Story Creation**  
   Defines a user story representing a "User Login Feature" with:
   - Unique ID generated from a key string.
   - Title and detailed description.
   - List of acceptance criteria.
   - List of business rules.
   - Context description.

2. **Test Case Manager Initialization**  
   Instantiates `TestCaseManager`.

3. **User Story Processing**  
   Calls `manager.process_user_story()` supplying the user story, a suite name `"authentication"`, and sets `auto_apply=False` to allow manual review.

4. **Results Display**  
   Prints a summary of generated test cases categorized as:
   - Same (test cases matching existing ones)
   - Add-on (extensions or variations)
   - New (completely new test cases)

5. **Detailed Results**  
   Iterates through each generated test case and displays:
   - Title
   - Decision (same/add-on/new)
   - Similarity and confidence scores
   - Reasoning behind the decision
   - System recommendation

6. **Decision Application**  
   Applies decisions manually for each test case with user approval.

7. **Export**  
   Exports the test suite to an Excel file in the specified output directory.

8. **Statistics**  
   Prints overall knowledge base statistics, including total test cases and current test suites.

---

### example_requirement_text()

Processes requirement text in a free-text format:

1. **Requirement Text Definition**  
   Multiline string describing a "Shopping Cart Checkout" feature, including functional requirements and business rules.

2. **Test Case Manager Initialization**

3. **Requirement Processing**  
   Calls `manager.process_requirement_text()` with the requirement, suite name `"checkout"`, and `auto_apply=True` enabling automatic decision application.

4. **Summary Display**  
   Shows counts of generated test cases by category and lists actions performed.

---

## Main Program Flow

When run as a script, the program prompts the user to select which example to run:

- `1`: Run the user story example (`example_user_story`)
- `2`: Run the requirement text example (`example_requirement_text`)
- Any other input defaults to running the user story example.

---

## Usage Example

```bash
$ python example_usage.py
================================================================================
RAG TEST CASE MANAGEMENT SYSTEM - EXAMPLE USAGE
================================================================================

Select example:
1. User Story Example
2. Requirement Text Example

Enter choice (1 or 2): 1

Initializing Test Case Manager...

Processing user story: User Login Feature

[summary and detailed output]

Applying decisions...

Exporting...

Statistics...
```

---

## Code Structure Summary

| **Component**            | **Purpose**                                            |
|--------------------------|--------------------------------------------------------|
| `example_user_story()`    | Demonstrates creating & processing a `UserStory`      |
| `example_requirement_text()` | Shows processing freeform requirement text and auto-apply |
| `__main__` block         | Script entry point to choose example to run            |

---

## Notes

- The examples assume an existing working implementation of `UserStory`, `TestCaseManager`, and `generate_id`.
- Output files are written relative to the current working directory.
- Manual decision application allows human oversight before changes are saved.
- Auto-apply mode is useful for batch processing and automation.
- The test suite name separates different feature areas for organization.

---

This documentation should assist users and developers in understanding how to use the RAG Test Case Management System APIs effectively by following practical example workflows.

## File: examples/example_context_engineering.py
# Module Documentation: Context Engineering in Test Case Generation Examples

This module provides example scripts that demonstrate the application and benefits of context engineering in automated test case generation. It contrasts basic test case generation approaches with advanced context-aware techniques, showcases automatic detection of focus areas from requirements, and presents usage of context templates to enrich test case generation.

---

## Overview

- **Purpose**: Demonstrate how incorporating contextual information enhances the quality, coverage, and relevance of generated test cases.
- **Components Covered**:
  - Basic vs Advanced Test Case Generation with Context Engineering
  - Automatic Focus Area Detection from requirements text
  - Usage of Domain and Technical Context Templates to guide generation

The examples utilize the following main classes (imported from local modules):
- `TestCaseGenerator`: Generates test cases from textual requirements.
- `RAGEngine` (not used directly here, but mentioned): Responsible for retrieval-augmented generation (retrieving similar examples).
- `ContextEngineer`: Extracts and manages contextual data to improve generation quality.

---

## Functions

### example_basic_vs_advanced()

Demonstrates the difference between **basic** (context engineering off) and **advanced** (context engineering on) test case generation for the same user requirement.

**Flow and Features:**

- Defines a simple login-related user requirement.
- **Basic Generation**:
  - Instantiates `TestCaseGenerator` without context engineering.
  - Generates test cases.
  - Prints key details of first 3 test cases (title, business rules snippet, steps count, boundary conditions count, tags).
  - Calculates and prints summarized statistics, including average steps and boundary conditions per test case.
- **Advanced Generation**:
  - Instantiates `TestCaseGenerator` with context engineering enabled.
  - Provides additional simulated domain context (e.g., industry, app type, user roles).
  - Invokes test case generation with domain context and empty similar examples list.
  - Prints details and statistics similarly to basic generation.
- **Comparison**:
  - Summarizes metrics side-by-side.
  - Shows percentage improvements in total cases, average steps, and boundary conditions due to context engineering.
- **Key Insights**:
  - Context engineering leads to more comprehensive, domain-aware, professional test cases.
  
**Usage Notes**:
- Domain context and similar examples influence advanced generation to tailor test cases better.
- Useful for understanding the impact of advanced contextual information on test case output quality.

---

### example_auto_focus_detection()

Demonstrates the capability of automatically detecting important focus areas within test requirements text using the `ContextEngineer`.

**Flow and Features:**

- Creates an instance of `ContextEngineer`.
- Defines a list of diverse sample requirements.
- For each requirement:
  - Calls `get_focus_areas()` to extract focus/key areas (e.g., security, API, concurrency).
  - Prints the detected focus areas clearly, aiding understanding of requirement emphasis.

**Use Case**:
- Helps testers quickly identify critical aspects of requirements for targeted test case design.
- Can be integrated within test case generators to highlight priority or complex areas automatically.

---

### example_context_templates()

Shows how domain and technical context templates can be formatted and used to provide structured background for test case generation.

**Flow and Features:**

- Instantiates a `ContextEngineer`.
- Defines sample domain context data (industry, app type, user roles, compliance, integrations).
- Prints formatted domain context using the `domain_context` template.
- Defines sample technical context data (tech stack, architecture, database, APIs, security).
- Prints formatted technical context using the `technical_context` template.

**Purpose**:
- Illustrates how contextual metadata is standardized and infused into generation prompts.
- Facilitates reuse of rich context snippets across projects.

---

## Main Execution

If the script is executed as the main module, it:

- Prints an introduction banner.
- Runs the three example functions in sequence:
  1. Basic vs Advanced test case generation
  2. Automatic focus area detection
  3. Context templates display
- Catches and reports exceptions, reminding users about Azure OpenAI credentials configuration (suggesting dependency of underlying engines on Azure OpenAI).

---

## Dependencies and Environment

- Requires modules from a `./engines` package:
  - `TestCaseGenerator`
  - `RAGEngine`
  - `ContextEngineer`
- Expects Azure OpenAI credentials configured (e.g., in `.env`), necessary for underlying language model calls.
- Standard Python libraries:
  - `os`, `sys`, `json`

---

## Summary

This example module provides a comprehensive demonstration of how context engineering can significantly enhance automated test case generation by:

- Incorporating domain and technical knowledge.
- Leveraging similar past examples.
- Automatically identifying key focus areas.
- Using structured context templates.

It is intended for software testers, QA engineers, and AI tool developers exploring retrieval-augmented generation (RAG) and context-driven enhancement of test automation workflows.

## File: examples/import_example.py
# Module Documentation: Import Existing Test Cases into the Knowledge Base

This module provides example scripts demonstrating how to import existing test cases into a test case management system's Knowledge Base using the `TestCaseManager` class. It supports importing test cases from Excel and JSON files, and also illustrates processing a new user story against imported test cases.

---

## Overview

- **import_from_excel_example()**  
  Imports test cases from an Excel file, handling file existence checks, import feedback, and displaying Knowledge Base statistics and sample test cases.

- **import_from_json_example()**  
  Imports test cases from a JSON file and reports success or failure with sample imported cases.

- **test_with_imported_cases()**  
  Demonstrates importing test cases from an Excel file and then processing a new user story with those test cases to generate comparison results.

- **Interactive CLI**  
  When run as the main script, allows the user to select which example to execute or run them all sequentially.

---

## Usage

```bash
python import_examples.py
```

Then select an option (1-4) from the menu to run the corresponding example(s).

---

## Detailed API Documentation

### import_from_excel_example()

```python
def import_from_excel_example():
    """
    Example: Import test cases from Excel file

    Steps:
    1. Initialize TestCaseManager.
    2. Check for presence of an example Excel file containing existing test cases.
    3. If file is missing, instruct the user on required and optional columns.
    4. Import test cases from the Excel file into the suite named "existing_tests".
    5. Display import success/failure summary with detailed errors if any.
    6. Show Knowledge Base statistics including total test cases and test suites.
    7. Display the first 3 imported test cases with key details.
    """
```

**Important Notes:**  
- The Excel file should contain at minimum these columns:  
  `Title`, `Description`, `Test Steps`, `Expected Outcome`  
- Optional columns can include:  
  `Business Rule`, `Preconditions`, `Postconditions`, `Tags`, `Priority`, `Test Type`, `Boundary Conditions`, `Side Effects`, `ID`

---

### import_from_json_example()

```python
def import_from_json_example():
    """
    Example: Import test cases from JSON file

    Steps:
    1. Initialize TestCaseManager.
    2. Check for presence of an example JSON file containing existing test cases.
    3. If file is missing, notify the user.
    4. Import test cases from the JSON file into the suite named "json_imported_tests".
    5. Display import result summary and list up to 3 imported test case titles.
    """
```

---

### test_with_imported_cases()

```python
def test_with_imported_cases():
    """
    Example: Process new user story with imported test cases

    Steps:
    1. Initialize TestCaseManager.
    2. Import existing test cases from Excel file into the suite "authentication".
    3. If import fails, skip the example.
    4. Create a new UserStory object with a unique ID, descriptive title, and acceptance criteria.
    5. Process the UserStory against the imported test cases with `auto_apply=False`.
    6. Display a summary of generated test cases classified as SAME, ADD-ON, or NEW.
    7. Show detailed comparison results for the first 3 test cases including decision, similarity, and confidence scores.

    Dependencies:
    - `UserStory` model for representing user stories.
    - `generate_id` utility to generate consistent IDs.
    """
```

---

## Command-Line Interface

When executed directly, the script presents a simple menu to the user:

```text
RAG TEST CASE MANAGEMENT - IMPORT EXAMPLES

Select example:
1. Import from Excel
2. Import from JSON
3. Test with imported cases
4. Run all examples

Enter choice (1-4):
```

Depending on the user choice, the corresponding function(s) are executed. Invalid inputs default to running the Excel import example.

---

## Module Dependencies

- `TestCaseManager` from `engines.test_case_manager` — primary class for managing test cases.
- `Path` from `pathlib` — for filesystem path checks.
- `UserStory` model and `generate_id` utility (used in `test_with_imported_cases`).

---

## Example File Formats

### Excel File

- Must be an `.xlsx` file.
- Required columns: `Title`, `Description`, `Test Steps`, `Expected Outcome`.
- Optional columns for richer metadata.

### JSON File

- Must be a JSON-formatted file with appropriate representation of test cases compatible with `TestCaseManager`.

---

## Summary

This collection of examples helps developers:

- Quickly import legacy or externally created test cases into their RAG Test Case Management system.
- Understand how to verify import success and diagnose failures.
- See how to integrate imported cases with agile artifacts such as user stories.
- Explore CLI-driven demonstration for ease of experimentation.

---

**End of Documentation**

## File: generate_docs.py
# Auto Documentation Generator

This Python script automates the generation of software documentation by invoking the Azure OpenAI API to analyze source code files and produce corresponding documentation. It supports both full project documentation generation and incremental updates for changed files.

---

## Overview

- **Reads a list of changed files** from a `changed_files.txt` file.
- **Determines whether to generate full or incremental documentation** based on the presence of an existing documentation file.
- **Processes supported source code files** (`.java`, `.py`, `.js`) by sending their contents to the Azure OpenAI API.
- **Collects generated documentation** and writes it to `docs/auto-doc.md`.
- Uses environment variables to configure Azure OpenAI API keys, endpoint, and deployment details.

---

## Prerequisites

- Python 3.x
- Azure OpenAI SDK (`openai` package with Azure support) installed
- Environment variables properly set:
  - `AZURE_OPENAI_API_KEY`: Your Azure OpenAI API key
  - `AZURE_OPENAI_ENDPOINT`: Azure OpenAI endpoint URL
  - `AZURE_OPENAI_API_VERSION`: Azure OpenAI API version (default: `2025-01-01-preview`)
  - `AZURE_OPENAI_DEPLOYMENT`: Deployment/model name for the OpenAI API (default: `gpt-4.1-mini`)
- `changed_files.txt`: A text file listing filenames to process, one per line

---

## Script Workflow

### 1. Initialization

- Reads API configuration from environment variables.
- Initializes the OpenAI client for Azure.

### 2. Read Changed Files

- Opens `changed_files.txt` and loads the list of files whose documentation needs to be generated or updated.

### 3. Determine Documentation Type

- Checks if `docs/auto-doc.md` exists.
- If **not found**: treats this as a full project documentation generation.
- If **found**: treats as incremental documentation update for changed files.

### 4. Documentation Generation Loop

- Iterates over each file in the changed files list.
- Checks if the file has a supported extension (`.java`, `.py`, `.js`).
- Reads the file content.
- Sends a prompt to the Azure OpenAI API with the role of a senior software architect asking to generate documentation for the given code.
- Appends the generated documentation or an error message into the documentation content string.

### 5. Output

- Ensures the `docs` directory exists.
- Writes the collected documentation content to `docs/auto-doc.md`.

---

## Detailed Code Description

```python
import os
from openai import AzureOpenAI

# Initialize Azure OpenAI client with API key, endpoint, and version read from environment
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY", ""),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2025-01-01-preview"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", "")
)

# Load the list of changed files from changed_files.txt
with open("changed_files.txt", "r") as f:
    files = f.read().splitlines()

# Check if the documentation file already exists to determine full or incremental update
doc_file_path = "docs/auto-doc.md"
is_full_documentation = not os.path.exists(doc_file_path)

# Prepare the initial documentation header
if is_full_documentation:
    doc_content = "# Auto Generated Documentation\n\n"
    doc_content += f"*Complete project documentation - Generated on: {os.popen('date').read().strip()}*\n\n"
    print(f"Generating complete documentation for {len(files)} files...")
else:
    doc_content = "# Auto Generated Documentation\n\n"
    doc_content += f"*Last updated: {os.popen('date').read().strip()}*\n\n"
    print(f"Generating documentation for {len(files)} changed files...")

# Process each file for documentation generation
for file in files:
    if file.endswith(".java") or file.endswith(".py") or file.endswith(".js"):
        print(f"Processing: {file}")
        try:
            with open(file, "r", encoding="utf-8") as code_file:
                code = code_file.read()

            # Send request to Azure OpenAI to generate documentation
            response = client.chat.completions.create(
                model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4.1-mini"),
                messages=[
                    {"role": "system", "content": "You are a senior software architect."},
                    {"role": "user", "content": f"Generate documentation for this code:\n{code}"}
                ],
            )

            doc_content += f"## File: {file}\n"
            doc_content += response.choices[0].message.content or ""
            doc_content += "\n\n"
        except Exception as e:
            print(f"Error processing {file}: {str(e)}")
            doc_content += f"## File: {file}\n"
            doc_content += f"*Error generating documentation: {str(e)}*\n\n"

# Ensure output folder exists, then save the documentation file
os.makedirs("docs", exist_ok=True)

with open("docs/auto-doc.md", "w", encoding="utf-8") as f:
    f.write(doc_content)
```

---

## Notes & Recommendations

- The script assumes all files listed in `changed_files.txt` exist and are readable; error handling is in place to log and annotate failures.
- The OpenAI prompt sets the system role explicitly as "senior software architect" to guide the model's style and depth.
- The documentation output is in Markdown format and grouped by filename.
- Consider adding rate limiting or batching if processing a very large number of files.
- For better date handling and cross-platform compatibility, consider replacing `os.popen('date')` with Python’s `datetime` module.
- Ensure sensitive environment variables (API keys) are securely managed and not hard-coded.

---

## Summary

This script provides an automated way to generate or update project documentation by leveraging Azure's OpenAI capabilities to interpret and describe code. It supports incremental updates by focusing on changed files, improving efficiency and enabling continuous documentation maintenance.

## File: scripts/__init__.py
# Utility Scripts for Setup, Diagnosis, and Maintenance

This module provides a collection of utility scripts designed to facilitate the setup, diagnosis, and ongoing maintenance of the system. These scripts can be used to automate common tasks, troubleshoot issues, and ensure the system remains operational and efficient.

## Overview

- **Setup:** Scripts to initialize configurations, install dependencies, and prepare the environment for deployment.
- **Diagnosis:** Tools for monitoring system health, logging, and identifying faults or performance bottlenecks.
- **Maintenance:** Utilities for routine updates, cleanup, backup, and recovery processes.

## Usage

Each utility script is intended to be run independently or as part of scheduled tasks (cron jobs, CI pipelines, etc.). Refer to individual script documentation for specific usage instructions, parameters, and output details.

## Contributing

To add new utility scripts or enhance existing ones, follow the project's coding standards and update the documentation accordingly. Include meaningful comments and error handling to maintain script robustness.

## Support

For issues and troubleshooting help, please contact the support team or consult the system administrator.

---

*Note: This is a general description based on the provided module docstring. For detailed documentation, provide the actual script code or list of utility functions.*

## File: scripts/add_diverse_test_cases.py
"""
Module: add_diverse_test_cases.py
---------------------------------

This script enhances the existing knowledge base of test cases by adding a comprehensive set of diverse test case examples. These examples cover a wide range of test case types such as Negative, UI, Security, Edge Case, and Positive scenarios, specifically focused on login functionality.

Purpose:
--------
To improve the Retrieval-Augmented Generation (RAG) system’s effectiveness by providing it richer, varied test case examples sourced from real-world scenarios, thus enabling better contextual retrieval and generation outcomes.

Key Components:
---------------
- diverse_test_cases: A list of dictionaries, each representing a detailed test case example. Each test case contains metadata and structured fields describing the testing conditions, steps, expected outcomes, priorities, tags, and side effects.

Test Case Fields Include:
    - id: Unique identifier generated from test case title using `generate_id`.
    - title: Brief descriptive title of the test case.
    - description: Explanation of what the test covers.
    - business_rule: Underlying business requirement the test validates.
    - preconditions: Conditions that must hold true before test execution.
    - test_steps: Ordered sequence of steps with corresponding expected results.
    - expected_outcome: Summary of expected behavior after test execution.
    - postconditions: System state or side effects after test completion.
    - tags: Keywords for categorizing and retrieval.
    - priority: Importance level (e.g. High, Medium, Critical).
    - test_type: Category of the test (Negative, UI, Security, Edge_Case, Positive).
    - is_regression: Boolean flag indicating if test is suited for regression.
    - boundary_conditions: Edge or boundary conditions tested.
    - side_effects: Any effects on system state or logs.
    - created_at / updated_at: Timestamps.
    - version: Version number for the test case.
    - source_document: Origin identifier for the test case examples.

Main Function:
--------------
add_diverse_test_cases()
    Reads the existing knowledge base file at 'knowledge_base/default.json', validates its structure, and appends the diverse_test_cases to it. Then writes back the updated knowledge base.

    Function Workflow:
    1. Check if the knowledge base file exists; if not, abort with a message.
    2. Load existing knowledge base data (expects a dict with a "test_cases" list or a list).
    3. Append the diverse_test_cases to the current list.
    4. Save the updated data back to the file in JSON format with indentation.
    5. Print a detailed summary of the operation including counts by test case type.

Usage:
------
Run this script directly to integrate new diverse test case examples into your knowledge base.

```bash
python add_diverse_test_cases.py
```

Dependencies:
-------------
- core.utils.generate_id: Function to create unique IDs based on titles.
- Python standard libraries: sys, os, json, datetime, pathlib.

File Structure Expectations:
----------------------------
- Expects knowledge base JSON at "knowledge_base/default.json".
- Knowledge base JSON either:
  - A dictionary with a "test_cases" key containing a list of test cases, or
  - A list (treated as the list of test cases directly).

Error Handling:
---------------
- Notifies and stops if the knowledge base file is missing or has unexpected format.

Logging:
--------
- Console print statements provide step-by-step feedback on loading, adding, saving, and summary details.

Extensibility:
--------------
- Easily add new test case examples by extending the diverse_test_cases list.
- Can adapt knowledge base path or data structure as needed.

---

End of documentation.
"""

## File: scripts/create_excel_template.py
# Script: Create Sample Excel Template for Importing Test Cases

## Overview
This script generates a sample Excel file containing predefined test cases to serve as a template for importing test cases into a test management system or for use as a reference. The Excel file includes detailed fields for each test case, such as ID, title, description, test steps, expected outcomes, priority, and other relevant information.

## Requirements
- Python 3.x
- pandas library
- openpyxl library (used as the Excel engine)
- pathlib library (standard in Python 3.4+)

## Functionality
- Defines a list of dictionaries representing test cases with comprehensive information.
- Converts the list of test cases into a pandas DataFrame.
- Creates an `examples` directory if it does not exist.
- Saves the DataFrame to an Excel file named `existing_test_cases.xlsx` inside the `examples` directory, using the `openpyxl` engine.
- Outputs a confirmation message summarizing the generated file and contents.

## Test Case Data Fields
Each test case dictionary includes the following fields:
- **ID**: Unique identifier for the test case (e.g., TC001).
- **Title**: Concise test case title.
- **Description**: Detailed purpose of the test case.
- **Business Rule**: The business logic or rules the test case verifies.
- **Preconditions**: Required conditions before test execution.
- **Test Steps**: Step-by-step instructions with expected outcomes per step.
- **Expected Outcome**: Overall expected result of the test case.
- **Postconditions**: Conditions that should hold true after test execution.
- **Tags**: Comma-separated keywords for categorization.
- **Priority**: Importance or severity level (e.g., High, Medium).
- **Test Type**: Type of test (e.g., Functional, Security).
- **Boundary Conditions**: Edge conditions related to the test scenario.
- **Side Effects**: Any side effects caused by the test execution.

## Usage
Run the script to generate the Excel template:

```bash
python create_test_case_template.py
```

After running, the following will be created:
- Directory: `examples/` (if it doesn't exist)
- File: `examples/existing_test_cases.xlsx`

The console will display a summary message, e.g.:

```
✓ Created Excel template: examples/existing_test_cases.xlsx
  - 5 sample test cases
  - Columns: ID, Title, Description, Business Rule, Preconditions, Test Steps, Expected Outcome, Postconditions, Tags, Priority, Test Type, Boundary Conditions, Side Effects
```

## Code Summary

```python
import pandas as pd
from pathlib import Path

# Define example test case data as a list of dictionaries
data = [
    {...},  # Test case 1 dictionary
    {...},  # Test case 2 dictionary
    # ...additional test cases...
]

# Convert the list of test cases into a pandas DataFrame
df = pd.DataFrame(data)

# Create output directory if it does not exist
Path("examples").mkdir(exist_ok=True)

# Export the DataFrame to an Excel file
output_path = "examples/existing_test_cases.xlsx"
df.to_excel(output_path, index=False, engine='openpyxl')

print(f"✓ Created Excel template: {output_path}")
print(f"  - {len(df)} sample test cases")
print(f"  - Columns: {', '.join(df.columns)}")
```

---

## Notes
- The script uses multiline strings for test steps to preserve formatting within Excel.
- The resulting Excel file can be modified or extended for additional test cases.
- Make sure you have installed the required libraries before running:

```bash
pip install pandas openpyxl
```

---

If you need help adapting this template for automated test management workflows or additional features, feel free to ask!

## File: scripts/format_test_cases_for_excel.py
# Module: Test Case Excel Formatter

This module provides functionality to format test cases according to user preferences and export them to an Excel file. It focuses on consolidating all test case information in a single row, organizing test steps as numbered, line-separated entries within a single Excel cell.

---

## Overview

- **Format test cases for export**: Combines test steps, expected results, and preconditions into user-friendly multiline strings.
- **Test Case categorization**: Detects and assigns test case types based on title suffixes or type flags.
- **Excel export**: Writes formatted test cases into an Excel file with custom styling and layout for readability.

---

## Dependencies

- Python 3.x
- `pandas` (for data manipulation and Excel export)
- `xlsxwriter` (Excel engine used by pandas for styling)
- Internal modules:
  - `core.models` - contains the `TestCase` class definition.
  - `core.knowledge_base` - contains the `KnowledgeBase` class for loading test cases.

---

## Functions

### `format_test_case_for_excel(tc: TestCase) -> dict`

Formats a single `TestCase` object into a dictionary suitable for Excel export.

**Parameters:**
- `tc` (`TestCase`): The test case object to format.

**Returns:**
- `dict`: A dictionary containing formatted and consolidated fields including test steps and expected results as multiline strings.

**Details:**

- Test steps are joined with line breaks and numbered (e.g., `1. Step action`).
- Expected results from each step are also joined line by line.
- Preconditions are concatenated into a single string.
- The test case scenario is derived from the title after removing known suffixes (e.g., `- Positive`, `- Negative`).
- Test case type is determined by suffix presence or the `test_type` attribute.
- Constructs a dictionary with keys:
  - `"Test Case ID"`
  - `"Layer"` (from business rule)
  - `"Test Case Scenario"`
  - `"Test Case"` (title without suffix)
  - `"Pre-Condition"`
  - `"Test Case Type"`
  - `"Test Steps"`
  - `"Expected Result"`
  - `"Priority"`

---

### `export_to_excel_format(test_cases: List[TestCase], output_path: str)`

Exports a list of test cases into a formatted Excel spreadsheet at the specified file path.

**Parameters:**
- `test_cases` (`List[TestCase]`): List of test cases to export.
- `output_path` (`str`): File path where the Excel file will be saved.

**Behavior:**

- Calls `format_test_case_for_excel` on each test case to prepare data.
- Converts formatted data into a pandas DataFrame.
- Writes DataFrame to an Excel sheet called "Test Cases" using the `xlsxwriter` engine.
- Applies custom formatting:
  - Header with bold white text on blue background, centered and wrapped.
  - Cells with borders, left-aligned, top vertical alignment, and text wrapping.
  - Sets column widths for optimal display based on column contents.
  - Sets row heights to improve readability for wrapped multiline cells.
- Prints status updates to console during operation.

**Notes:**

- The method ensures all test case information is displayed clearly in single rows.
- Test steps and expected results are shown with step numbering and line breaks inside cells.

---

## Usage Example (as script)

When run as a standalone script, the module:

1. Instantiates a `KnowledgeBase`.
2. Retrieves all test cases from a default suite.
3. Exits with an error message if no test cases are found.
4. Creates an output directory if it does not exist.
5. Exports all test cases to `"output/test_cases_formatted.xlsx"`.
6. Prints success messages with the output file path.

---

## Classes Used (from external modules)

- `TestCase`: Represents a test case with attributes like:
  - `id`
  - `title`
  - `description`
  - `preconditions`
  - `test_steps` (list of steps, each having `step_number`, `action`, `expected_result`)
  - `business_rule`
  - `test_type`
  - `priority`

- `KnowledgeBase`: Provides method `get_all_test_cases(suite_name)` to fetch test cases.

---

## Logging and Output

- Informational print statements show progress:
  - Number of test cases being formatted.
  - Confirmation of Excel file creation.
  - Final success message including number of exported test cases and file path.

---

## Example of formatted Excel output structure

| Test Case ID | Layer | Test Case Scenario | Test Case       | Pre-Condition            | Test Case Type | Test Steps                 | Expected Result                 | Priority |
|--------------|-------|--------------------|-----------------|--------------------------|----------------|----------------------------|--------------------------------|----------|
| TC001        | UI    | Login functionality | Login Scenario  | User is on login page    | Positive       | 1. Enter username<br>2. Enter password<br>3. Click login | 1. Fields accept input<br>2. Validated<br>3. Redirect | High     |

*Test steps and expected results appear within single cells, formatted with line breaks.*

---

## Summary

This module streamlines exporting structured test case data into a well-formatted Excel sheet fitting user preferences. It helps QA teams and stakeholders review test scenarios, steps, expected outcomes, and related metadata clearly at a glance.

## File: scripts/test_llm_apis.py
# API Diagnostics Test Script Documentation

This Python script performs a comprehensive diagnostic check on the key components required for a Retrieval-Augmented Generation (RAG) test case generation system. It verifies connectivity and functionality for large language model (LLM) APIs from Anthropic and OpenAI, embedding services via sentence-transformers, and basic internet connectivity.

---

## Overview

The script is designed to be run as a standalone diagnostic tool. It:

- Loads API keys and environment variables from a `.env` file
- Tests the Anthropic Claude LLM API connection
- Tests the OpenAI GPT API connection
- Tests embedding service functionality
- Checks internet connectivity to critical external endpoints
- Prints detailed results and recommendations based on the test outcomes

---

## Requirements

- Python 3.7+
- Environment variables configured for API keys:
  - `ANTHROPIC_API_KEY`
  - `OPENAI_API_KEY`
- Python libraries:
  - [anthropic](https://github.com/anthropics/anthropic-python)
  - [openai](https://pypi.org/project/openai/) or compatible OpenAI client (here it's from `openai` package)
  - [python-dotenv](https://pypi.org/project/python-dotenv/)
  - [sentence-transformers](https://www.sbert.net/) (only if testing embeddings)
  - Optional: `torch` (required for sentence-transformers embedding models)

---

## Script Structure & Functions

### Environment Setup

- Loads environment variables from `.env` using `load_dotenv()`.
- Retrieves API keys from environment variables `ANTHROPIC_API_KEY` and `OPENAI_API_KEY`.

---

### 1. `test_anthropic()`

**Purpose:** Test the connection and functionality of the Anthropic Claude API.

**Behavior:**

- Creates a client with the Anthropic API key.
- Sends a test message prompting the model `claude-3-sonnet-20240229` to respond with a confirmation phrase.
- Extracts and prints the response text, model used, and token usage.
- Handles and reports:
  - Authentication errors
  - Rate limiting
  - Other exceptions with descriptive messages

**Returns:** `True` if test successful, `False` otherwise.

---

### 2. `test_openai()`

**Purpose:** Test the connection and functionality of the OpenAI GPT API.

**Behavior:**

- Creates a client with the OpenAI API key.
- Sends a test chat completion request to the `gpt-4o-mini` model with a confirmation prompt.
- Prints the response content, model, and token usage.
- Handles exceptions and provides specific recommendations based on error text, such as:
  - Authentication failure (401)
  - Rate limiting (429)
  - Model not found or access denial (404)
  - Other errors

**Returns:** `True` if test successful, `False` otherwise.

---

### 3. `test_embedding_service()`

**Purpose:** Verify embedding generation capability for the RAG system.

**Behavior:**

- Dynamically imports `SentenceTransformer` from `sentence_transformers`.
- Loads the embedding model `all-MiniLM-L6-v2`.
- Generates an embedding vector for a test sentence.
- Prints model details and embedding size.
- Handles exceptions if the package is missing or an error occurs and suggests installation steps.

**Returns:** `True` if test successful, `False` otherwise.

---

### 4. `test_internet_connectivity()`

**Purpose:** Test basic network reachability to critical external services.

**Behavior:**

- Attempts TCP socket connections with a 5-second timeout to:
  - Anthropic API (`api.anthropic.com`, 443)
  - OpenAI API (`api.openai.com`, 443)
  - HuggingFace domain (`huggingface.co`, 443) (for embeddings)
  - Google DNS (`8.8.8.8`, 53)
- Reports success or failure for each endpoint.

**Returns:** `True` if all endpoints reachable, `False` if any fail.

---

### 5. `main()`

**Purpose:** Orchestrates running all diagnostic tests and outputs summary results.

**Behavior:**

- Runs all four tests.
- Collects results and prints a detailed summary with pass/fail statuses.
- Provides actionable recommendations tailored to the specific failures encountered.
- Indicates overall system readiness.
- Returns `True` if all tests pass, otherwise `False`.

---

## Execution

Run this script directly from the command line:

```bash
python test_api_connections.py
```

Exit code:

- `0` if all tests pass (indicating readiness)
- `1` if any test fails (indicating issues that need attention)

---

## Example Output Snippet

```
================================================================================
RAG TEST CASE GENERATION SYSTEM - API DIAGNOSTICS
================================================================================

Testing connections to:
  • Anthropic Claude (primary LLM)
  • OpenAI GPT (fallback LLM)
  • Sentence Transformers (embeddings)
  • Internet connectivity
================================================================================
TEST 1: Anthropic Claude API
================================================================================
Model: claude-3-sonnet-20240229

Sending test message...
✓ Anthropic API working!
  Response: Anthropic connection successful!
  Model: claude-3-sonnet-20240229
  Tokens used: 15 in, 20 out

... (similar output for other tests) ...

================================================================================
DIAGNOSTIC SUMMARY
================================================================================
  Internet             ✅ PASS
  Anthropic            ✅ PASS
  OpenAI               ✅ PASS
  Embeddings           ✅ PASS

================================================================================
RECOMMENDATIONS
================================================================================

✅ ALL SYSTEMS GO!
   • Both LLM APIs are working
   • Embedding service is operational
   • Internet connectivity is stable

   Your RAG test case generation system is ready!

================================================================================
```

---

## Notes

- Modify `.env` with valid API keys before running the script.
- Network access permissions and firewall settings may affect connectivity tests.
- Model names used reflect current availability and may need updating as APIs evolve.
- Embedding service depends on additional Python packages; ensure these are installed in your environment.

---

## Summary

This script provides an essential health-check and validation mechanism for core components of a RAG system relying on Anthropic and OpenAI LLMs, sentence-transformers embeddings, and network availability. It helps to quickly identify configuration issues and connectivity problems before usage.

## File: test_distribution.py
# Test Script for Verifying Test Case Distribution

## Overview
This script serves as a verification tool to check the distribution of different categories of test cases based on a predefined configuration. It uses the `calculate_test_distribution` utility function to compute how test cases should be allocated across various categories, then prints detailed information including counts, percentages, and a formatted distribution string intended for consumption by a language model (LLM).

## Purpose
- To validate the configured minimum, maximum, and default number of test cases.
- To calculate and display how the total default test cases are distributed among categories.
- To present the distribution both numerically and as a formatted string.
- To compute and show the percentage breakdown of each test case category.

## Dependencies
- `core.utils.calculate_test_distribution`: Function that accepts the total number of test cases and returns a dictionary with distribution details.
- `config.config.Config`: Configuration object containing constants related to test case counts:
  - `DEFAULT_TEST_CASES`: Default number of test cases to be distributed.
  - `MIN_TEST_CASES`: Minimum allowed test cases.
  - `MAX_TEST_CASES`: Maximum allowed test cases.

## Script Flow

1. **Print Header**  
   Prints a visual header labeled "TEST CASE DISTRIBUTION VERIFICATION" for clarity in output logs.

2. **Configuration Check**  
   Prints the configured values of default, minimum, and maximum test cases for transparency and confirmation.

3. **Distribution Calculation**  
   Calls `calculate_test_distribution` with the default test case count and receives a distribution dictionary with these keys:  
   - `positive`  
   - `negative`  
   - `ui`  
   - `security`  
   - `edge_case`  
   - `distribution_string`: A formatted string summarizing the distribution for input to an LLM.

4. **Print Distribution Counts**  
   Outputs the count of test cases per category, sums them to verify total consistency.

5. **Print Distribution String**  
   Displays the pre-formatted string summarizing the distribution, intended to be sent to a language model for further processing.

6. **Print Percentages**  
   Calculates and prints the percentage breakdown across the categories, showing relative proportions.

7. **Footer**  
   Prints a closing separator line to finalize the output.

## Usage
Run this script in an environment where the dependency modules (`core.utils` and `config.config`) are accessible. It outputs all information to the standard output (console).

```bash
python test_distribution_verification.py
```

## Example Output

```
============================================================
TEST CASE DISTRIBUTION VERIFICATION
============================================================

1. Configuration Check:
   DEFAULT_TEST_CASES: 100
   MIN_TEST_CASES: 20
   MAX_TEST_CASES: 200

2. Distribution Calculation for 100 test cases:
   Positive: 40
   Negative: 20
   UI: 15
   Security: 15
   Edge Case: 10
   ---
   Total: 100

3. Distribution String that will be sent to LLM:
Positive: 40, Negative: 20, UI: 15, Security: 15, Edge Case: 10

4. Percentages:
   Positive: 40.0%
   Negative: 20.0%
   UI: 15.0%
   Security: 15.0%
   Edge Case: 10.0%

============================================================
```

---

## Notes
- The script assumes `calculate_test_distribution` returns a consistent and correct dictionary relative to the requested total number of test cases.
- Any discrepancies in totals or calculation errors should be handled inside the utility function or configuration settings.
- This script is intended for testing and debug purposes, not part of the production runtime.

## File: test_user_format_generation.py
# Script Documentation: Test Case Generation and Export to Excel in User's Preferred Format

## Overview

This script automates the generation of test cases based on a given user story, categorizes and summarizes the generated test cases, and exports them into an Excel file formatted to the user's preferences. The generated test cases support quality assurance activities by providing diverse coverage aligned with business rules and acceptance criteria defined in the user story.

---

## Script Purpose

- Generate a set of test cases automatically from a textual user story describing feature requirements.
- Classify test cases by type (e.g., Positive, Negative, UI) and provide a summary count.
- Display detailed information for a sample of generated test cases on the console.
- Export the test cases into an Excel spreadsheet structured for easy consumption and integration into test management workflows.

---

## Detailed Description

### Modules and Dependencies

- `sys`, `os`: Used to adjust the module search path and handle file system operations.
- `engines.test_case_generator.TestCaseGenerator`: Core engine to produce test cases from text input.
- `core.utils.export_test_cases_user_format`: Utility function to export the generated test cases into Excel in the user’s desired format.
- `config.config.Config`: (Imported but not explicitly used here) Presumably holds configuration settings for the project.

### User Story Input

The script works on a single user story input defined as a multi-line string `user_story`. This user story includes:

- A role and feature description from the user perspective (Financial Advisor performing bulk asset uploads).
- Acceptance criteria specifying mandatory fields, validation rules, file formats, and business processes.
- Business rules elaborating compliance, backend validation needs, transactional behavior, and error management.

### Workflow Steps

1. **Initialization**  
   - Print banner and user story for clarity.
   - Instantiate the `TestCaseGenerator`.

2. **Test Case Generation**  
   - Generates 12 diverse test cases from the textual user story using `generate_from_text()` method.
   - The test cases encapsulate varied coverage, presumably reflecting different scenarios mentioned in the acceptance criteria and business rules.

3. **Summary and Categorization**  
   - Counts test cases by their type, inferred by parsing their title suffix:
     - Negative
     - Positive
     - UI
     - Security
     - Edge Case
     - Other (default)
   - Displays the distribution of test cases by category.

4. **Sample Display**  
   - Outputs detailed information for the first three test cases including:
     - Title
     - Layer (mapped business rule or area)
     - Type
     - Priority
     - Description (scenario)
     - A preview of preconditions (first 3)
     - Number of test steps and the first 3 steps with partial action text

5. **Export**  
   - Creates an output directory `output`, if absent.
   - Exports the test cases to `output/generated_user_format.xlsx` in the user’s specified Excel format using `export_test_cases_user_format()`.

6. **User Guidance**  
   - Prints out the Excel column layout to orient users on the file structure.
   - Provides next steps on how to review the test cases and use them, including how to start the Streamlit app for further generation.

---

## Excel Output Format

The exported Excel file includes the following columns:

1. Test Case ID  
2. Layer  
3. Test Case Scenario  
4. Test Case  
5. Pre-Condition  
6. Test Case Type  
7. Test Steps  
8. Expected Result  
9. Priority  

---

## Usage Instructions

1. Run the script in a Python environment where dependencies (`engines`, `core`, and `config` modules) are resolvable.  
2. Review console output summarizing and displaying test cases.  
3. Open the generated Excel file at `output/generated_user_format.xlsx`.  
4. Upload or import the Excel file into your test management system for execution planning.  
5. For extended functionality, use the Streamlit UI app:
   ```bash
   streamlit run ui/app.py
   ```
   to generate additional test cases interactively.

---

## Notes

- The number of test cases generated (`num_test_cases=12`) and their content rely on the capabilities of `TestCaseGenerator`.  
- The script assumes the `export_test_cases_user_format` function correctly handles the formatting for Excel export.  
- The console display truncates long descriptions and actions for readability.

---

## Summary

This script is designed to streamline the conversion of textual user requirements into structured, categorized test cases and supports further test process automation by exporting to a standardized Excel format ready for review and system integration.

## File: tests/__init__.py
# Test Files Documentation

## Overview
This module contains test files designed to verify the functionality, performance, and stability of the application. The tests cover a range of scenarios including API validation, performance benchmarking, and regression checks for previously identified bugs.

## Contents
- **API Tests**: Ensure that all API endpoints respond correctly, handle inputs as expected, and return appropriate error messages.
- **Performance Tests**: Measure response times and resource usage under various load conditions to validate that the system meets performance requirements.
- **Bug Fix Tests**: Verify that previously reported bugs have been resolved and confirm that fixes do not introduce new issues.

## Usage
Run these test files as part of your continuous integration process to maintain code quality and system reliability. Typically executed using a test runner such as `pytest` or equivalent based on the project setup.

```bash
pytest tests/
```

## Contribution
When adding new functionality or fixing bugs, please include relevant tests in this suite to ensure comprehensive coverage.

---

*Note*: This is a placeholder description. For detailed information, each test file and case should have its own documentation.

## File: tests/test_api.py
# FastAPI Test Script Documentation

This Python script provides a suite of test functions designed to validate the behavior of various FastAPI endpoints. It uses the `requests` library to perform HTTP requests against a locally running FastAPI server, by default assumed to be accessible at `http://localhost:8000`.

---

## Overview

- **Purpose:** To test and verify key API endpoints such as health check, requirement processing, user story processing, test case retrieval, suite listing, statistics fetching, and configuration thresholds.
- **Usage:** Run the script while the FastAPI server is active. Some tests require additional external dependencies (e.g., Azure OpenAI credentials) and are commented out by default.

---

## Configuration

- `BASE_URL` (string): Base URL for the API server. Default is `http://localhost:8000`.

---

## Test Functions

### 1. `test_health()`

**Description:**  
Tests the `/health` endpoint to verify if the API is running and responsive.

**Behavior:**  
- Sends a GET request to `/health`.
- Prints HTTP status code.
- Prints prettified JSON response.

---

### 2. `test_process_requirement()`

**Description:**  
Tests processing of a software requirement via the `/process/requirement` POST endpoint.

**Payload:**  
- `requirement_text`: Multi-line string describing feature, requirements, and business rules.
- `suite_name`: Name of the test suite (e.g., `"authentication"`).
- `auto_apply`: Boolean flag indicating whether changes should be automatically applied.

**Behavior:**  
- Sends POST request with JSON payload.
- On success (HTTP 200), prints:
  - Operation success status.
  - Number of total test cases generated.
  - Counts broken down by categories ("same", "add-on", "new").
- On failure, prints error response.

**Note:** Requires valid API setup with relevant backend support (e.g., Azure OpenAI credentials).

---

### 3. `test_process_user_story()`

**Description:**  
Tests processing of a user story via the `/process/user-story` POST endpoint.

**Payload:**  
- `title`: Title of the user story.
- `description`: User story description.
- `acceptance_criteria`: List of acceptance criteria strings.
- `business_rules`: List of business rule strings.
- `context`: Contextual information string.
- `suite_name`: Test suite name (e.g., `"checkout"`).
- `auto_apply`: Boolean flag indicating whether to apply changes automatically.

**Behavior:**  
- Sends POST request with JSON payload.
- On HTTP 200 success, prints:
  - Operation success status.
  - Number of test cases generated.
  - List of action strings taken by the backend.
- On failure, prints the error response.

**Note:** Also requires additional backend credentials/configuration.

---

### 4. `test_get_test_cases()`

**Description:**  
Retrieves test cases associated with a suite from `/test-cases` GET endpoint.

**Query Parameters:**  
- `suite_name`: Name of the suite to filter test cases, e.g., `"authentication"`.

**Behavior:**  
- Makes GET request.
- On success, lists the count and first three test cases with title and ID.
- On failure, prints error message.

---

### 5. `test_get_suites()`

**Description:**  
Gets a list of all suites from the `/suites` GET endpoint.

**Behavior:**  
- Sends GET request.
- On success, lists the number and names of all suites.
- On failure, prints error message.

---

### 6. `test_get_statistics()`

**Description:**  
Fetches overall test case statistics from `/statistics`.

**Behavior:**  
- Sends GET request.
- On HTTP 200, prints total number of test cases from the knowledge base.
- On failure, prints error message.

---

### 7. `test_get_thresholds()`

**Description:**  
Retrieves configuration thresholds related to test case classification from `/config/thresholds`.

**Behavior:**  
- Sends GET request.
- On success, prints the "same" threshold and the range for "add-on" thresholds.
- On failure, prints error message.

---

## Execution Flow (`__main__`)

When executed as a script, the following occurs:

- A header and basic instructions about starting the API server are printed.
- Tests executed by default:
  - Health check.
  - Thresholds retrieval.
  - Suites retrieval.
  - Statistics retrieval.
- Processing-related and test-case retrieval tests are commented out because they may require specific API credentials or setup.
- Handles and reports connection errors (API server not running) and other unexpected exceptions gracefully.

---

## Setup Instructions

1. Ensure the FastAPI server is running locally at `http://localhost:8000`.  
   Example commands:
   ```bash
   python api.py
   # or
   uvicorn api:app --reload
   ```

2. Install required Python package if missing:
   ```bash
   pip install requests
   ```

3. (Optional) Update tests that require Azure OpenAI credentials or other backend dependencies.

---

## Notes

- This script is primarily intended for local development and testing.
- Adjust `BASE_URL` if the API server runs on a different host or port.
- Print statements help visibility during command-line execution; for automated CI/CD, consider adapting tests to assert statements or use a testing framework like `pytest`.

---

## Example Output Snippet

```plaintext
============================================================
FastAPI Test Suite
============================================================

Make sure the API is running: python api.py
or: uvicorn api:app --reload

=== Testing Health Endpoint ===
Status: 200
Response: {
  "status": "ok",
  "uptime": "12345 seconds"
}

=== Testing Thresholds ===
Status: 200
Same threshold: 0.85
Add-on range: 0.7 - 0.8

...
Tests completed!
============================================================
```

---

This documentation explains the purpose, behavior, and usage of each test function in the FastAPI test script, enabling developers and testers to understand and extend the testing suite promptly.

## File: tests/test_description_validation.py
# Module: Test Suite for Verifying Non-Blank Descriptions in Test Case Imports

This module contains automated tests designed to verify that descriptions in test cases are **never blank** when test cases are parsed or imported from various sources such as JSON objects, Excel files, and JSON files.

---

## Overview

Test cases often have a `description` field that provides important context for the test. This suite ensures the system correctly handles scenarios where descriptions might:
- Be empty strings
- Be missing entirely
- Contain only whitespace
- Have both `title` and `description` blank

The expected behavior is that the parsed or imported test case descriptions will never be blank or meaningless; if the description is missing or empty, a default fallback description is set, usually containing a reference to the test case `title` or a generic phrase.

This suite exercises:
- Parsing individual test case JSON objects.
- Importing test cases from Excel spreadsheets.
- Importing test cases from JSON files.

---

## Imports

- `sys`, `os`: To manipulate the Python path for imports.
- `pandas`: For Excel file generation and reading.
- `tempfile`: For creating temporary files to simulate import files.
- Functions from `core.utils`:
  - `parse_test_case_json`
  - `import_from_excel`
  - `import_from_json`

---

## Functions

### `test_parse_test_case_with_blank_description()`

**Purpose:**  
Verify the behavior of `parse_test_case_json()` when test case data has blank or missing descriptions, or empty titles with blank descriptions.

**Test Cases:**  
Includes five scenarios:
- Blank description but valid title.
- Missing description key.
- Description that contains only whitespace.
- Both title and description blank.
- Valid description (control case, should remain unchanged).

**Validation:**  
Checks that the parsed test case's `description` property is:
- Non-empty after trimming whitespace.
- Not equal to string `"nan"`.
- Contains (case-insensitive) the expected pattern (usually the title or fallback phrase).

**Output:**  
Prints test case details, validation results, and a summary pass/fail message.

**Returns:**  
`True` if all test cases passed, `False` otherwise.

---

### `test_excel_import_with_blank_descriptions()`

**Purpose:**  
Verify that test cases imported from an Excel file have non-blank descriptions after import, even if the source Excel cells are blank or whitespace.

**Setup:**  
Creates a temporary Excel file with sample test cases, some having blank or whitespace descriptions.

**Validation:**  
Iterates over imported test cases and checks that each description is:
- Non-empty after trimming whitespace.
- Not string `"nan"`.

**Output:**  
Prints details for each test case and overall pass/fail status.

**Returns:**  
`True` if all descriptions are valid, `False` otherwise.

---

### `test_json_import_with_blank_descriptions()`

**Purpose:**  
Verify that test cases imported from JSON files have non-blank descriptions, handling cases where descriptions are empty, whitespace, or missing.

**Setup:**  
Creates a temporary JSON file with a variety of test cases including missing or blank descriptions.

**Validation:**  
For each imported test case, checks:
- Description is non-empty after trimming whitespace.
- Not string `"nan"`.

**Output:**  
Prints details and pass/fail status.

**Returns:**  
`True` if all descriptions are valid, `False` otherwise.

---

## Main Execution Block

When executed as the main program, the module runs all three test functions in sequence:

1. `test_parse_test_case_with_blank_description()`
2. `test_excel_import_with_blank_descriptions()`
3. `test_json_import_with_blank_descriptions()`

It then prints a consolidated summary showing pass/fail status for each category and an overall success message if all pass.

---

## Notes

- The actual logic that enforces non-blank descriptions is assumed to be inside the imported functions `parse_test_case_json`, `import_from_excel`, and `import_from_json`.
- Temporary files are cleaned up after tests.
- Uses simple print statements to output test progression and statuses with clear emoji indicators.

---

# Example Usage

Run this module directly to execute all tests:

```bash
python test_description_not_blank.py
```

You will see verbose output describing each test case, whether the description validation passed, and the final summary.

---

# Summary

This test suite ensures reliability and quality of test case imports/parsing by making sure meaningful descriptions are always present, aiding downstream test execution, reporting, and documentation clarity.

## File: tests/test_end_to_end_numbering.py
# Module: End-to-End Test for Importing Test Cases and Verifying Double Numbering

This module defines end-to-end tests for importing test cases, parsing their steps, verifying that no double numbering occurs in step descriptions, formatting them to text, and optionally storing them in a Retrieval-Augmented Generation (RAG) engine for search.

---

## Overview

The tests simulate importing test cases with differently formatted numbered steps, verify their parsing correctness relative to numbering, validate the output of their text serialization, and demonstrate (commented out) how to store them in a RAG vector database for information retrieval use cases.

These tests help ensure that step numbering in test cases is clean (no double numbering such as "Step 1: 1.") and that the parsing and formatting logic is robust against various step numbering styles.

---

## Imports and Setup

- Adjusts `sys.path` to include parent directory so that local modules can be imported.
- Imports:
  - `parse_test_case_json` from `core.utils` — Parses raw test case JSON/dict into `TestCase` objects.
  - `RAGEngine` from `engines.rag_engine` — Manages storage and search of test cases in a vector database.
  - `TestCaseGenerator` from `engines.test_case_generator` — Not directly used in tests here.
  - `TestCase` from `core.models` — Model class representing a test case.

---

## Functions

### `test_import_and_rag_search()`

**Purpose:**  
Performs an end-to-end simulation of importing raw test case JSON data, parsing it into structured `TestCase` objects, verifying no double numbering in the step actions, formatting the test cases to text output, and optionally storing them in a RAG engine.

**Details:**

1. **Simulated Test Case Input:**  
   Three test cases with differently formatted step numbering:
   - Strict numbering with "1.", "2.", etc.
   - Numbering as "Step 1:", "Step 2:", etc.
   - Mixed and inconsistent formats including no numbering, "(4)", "5 - ", etc.

2. **Parsing Test Cases:**
   - Calls `parse_test_case_json` on each raw test case dictionary.
   - Prints the number of steps and checks each step's `action` string for double numbering patterns:
     - Looks for prefixes like "1.", "2)", etc. inside step actions that may indicate redundant numbering.
   - Prints warning if double numbering is detected, otherwise confirms steps are clean.

3. **Testing `to_text()` Output:**
   - Calls the `to_text()` method of each parsed `TestCase`.
   - Checks for patterns like `"Step 1: 1."` that indicate double numbering would appear in textual serialization.
   - Prints pass/fail status for the absence/presence of double numbering in output.

4. **RAG Engine Storage (Commented Out):**
   - Illustrates how to store the parsed test cases in the RAG engine for vector storage and retrieval.
   - This is skipped by default to avoid modifying the local ChromaDB database.

5. **Summary:**
   - Prints a recap of total parsed test cases.
   - Confirms all steps are clean.
   - Confirms text serialization is correct.
   - Indicates the fix for double numbering is working.

---

### `test_edge_cases()`

**Purpose:**  
Tests parsing of test cases that represent edge or unusual input scenarios related to test steps and numbering formats.

**Edge-case Scenarios Tested:**

- Empty steps list.
- Steps with no numbering at all.
- Mixed step formats: string-only steps and dictionary steps with `action` and `expected_result` keys.
- Steps containing special characters and quotes, with various numbering styles like "2)", "3:".

**Behavior:**

- Adds minimal required fields to each simulated edge case for parsing.
- Attempts to parse and print out summary information on the number of steps and a preview of each step.
- Catches and reports any exceptions during parsing.

---

## Usage

Run as a script to perform the tests:

```bash
python <this_script>.py
```

It will:

- Run `test_import_and_rag_search()` to validate normal and complex step numbering.
- Run `test_edge_cases()` to confirm system behavior with unusual test step inputs.

---

## Notes

- RAG storage is disabled (commented out) to avoid unwanted modification of the vector DB during testing. Enable if you want to test database interaction.
- The tests mainly validate the parsing logic (`parse_test_case_json`) and the `TestCase.to_text()` method for clean step numbering.
- The prints provide clear visual feedback on test results and any double numbering issues found.

---

## Summary of Key Classes/Functions Used

| Name                 | Description                                       |
|----------------------|-------------------------------------------------|
| `parse_test_case_json` | Parses raw test case dict into `TestCase` instance |
| `TestCase`           | Model with properties like `id`, `title`, `test_steps`; supports `to_text()` output |
| `RAGEngine`          | Vector database interface for storing/searching test cases (usage shown but disabled) |

---

# End of Documentation

## File: tests/test_fixes.py
# Test Script: JSON Parsing and Business Rule Handling Verification

This test script is designed to verify fixes related to JSON parsing and business rule handling in the test case generation and comparison processes.

---

## Overview

The script performs four main tests:

1. **Test 1:** Generating test cases without explicit business rules.
2. **Test 2:** Generating test cases with explicit business rules.
3. **Test 3:** Verifying JSON parsing and comparison engine functionality.
4. **Test 4:** Parsing JSON representations of test cases when the `business_rule` field is missing.

The tests utilize various modules and classes including:
- `TestCaseGenerator` (for generating test cases from textual requirements)
- `ComparisonEngine` (for comparing test cases)
- `TestCase`, `TestStep` (models representing test cases and their steps)
- `parse_test_case_json` (utility to parse JSON into `TestCase` objects)

Each test prints its progress and results to the console and returns a boolean indicating success or failure.

---

## Functions

### 1. `test_generate_without_business_rules()`

**Purpose:**  
Generate a set of test cases from a requirement text that does not explicitly state business rules, ensuring that the system can handle such inputs gracefully.

**Behavior:**  
- Creates an instance of `TestCaseGenerator`.
- Defines a requirement describing a user profile page.
- Calls `generate_from_text(requirement)` to generate test cases.
- Prints details of all generated test cases (title, business rule, description).
- Returns `True` on success, `False` on exception.

---

### 2. `test_generate_with_business_rules()`

**Purpose:**  
Generate test cases from a requirement that includes explicit business rules and acceptance criteria, validating correct parsing and generation when business rules exist.

**Behavior:**  
- Initializes `TestCaseGenerator`.
- Defines a requirement about user login featuring business rules and acceptance criteria.
- Generates test cases from this requirement.
- Prints each test case's title, business rule, and priority.
- Returns `True` on success, `False` on failure.

---

### 3. `test_comparison_json_parsing()`

**Purpose:**  
Test the `ComparisonEngine` to verify correct JSON parsing and comparison of two test cases.

**Behavior:**  
- Manually constructs two `TestCase` objects with multiple `TestStep` entries.
  - `tc1`: test for user login.
  - `tc2`: test for user login with "remember me" feature.
- Invokes `ComparisonEngine.compare_test_cases(tc1, tc2)` to get comparison results.
- Prints the decision, similarity score (as a percentage), business rule match, behavior match, and detailed reasoning.
- Returns `True` if comparison completes without exceptions, else `False`.

---

### 4. `test_parse_json_without_business_rule()`

**Purpose:**  
Ensure the JSON parser correctly handles a test case JSON object lacking the `business_rule` field, without failing.

**Behavior:**  
- Defines a JSON dictionary representing a test case with no `business_rule`.
- Uses `parse_test_case_json` to parse the JSON into a `TestCase` object.
- Prints test case title, business rule (should handle missing gracefully), and description.
- Returns `True` if parsing is successful, `False` on error.

---

### 5. `main()`

**Purpose:**  
Run all defined tests consecutively and report a summary of the results.

**Behavior:**  
- Prints heading.
- Executes each test function, capturing their success/failure.
- Displays a summary table listing each test and its pass/fail status.
- Prints final status indicating whether all tests passed or if some failed.
- Returns `True` if all tests pass, `False` otherwise.

---

## Execution

The script can be executed as a standalone program. When run, it will:

- Perform all tests in order.
- Print detailed output to the console for each test.
- Exit with status code `0` if all tests pass, `1` otherwise.

---

## Dependencies

- `test_case_generator.TestCaseGenerator`
- `comparison_engine.ComparisonEngine`
- `models.TestCase`
- `models.TestStep`
- `utils.parse_test_case_json`

These modules/classes must be implemented and available in the environment for the script to function.

---

## Summary

This test script is critical for validating that:

- Test case generation works properly both with and without explicit business rules.
- JSON parsing (especially handling missing fields like `business_rule`) is robust.
- The test case comparison engine correctly interprets and compares test cases as expected.

Successful execution ensures stability and correctness in the test management tooling related to business rules and JSON data processing.

## File: tests/test_numbering_fix.py
# Documentation for Smart Numbering Test Module

## Overview
This module contains a suite of test functions designed to verify the prevention of **double numbering** in test step descriptions within test case definitions. Double numbering refers to scenarios where steps are both explicitly numbered and also prefixed with a numbering format, leading to redundancy like `"Step 1: 1. Navigate to page"`.

The tests validate utility functions responsible for detecting, removing, and formatting step numbering, as well as parsing full test cases that may include numbered steps in various formats.

---

## Imports
- **sys, os**: For modifying the Python path to locate the core library modules.
- **core.utils**:
  - `has_existing_numbering(text: str) -> bool`: Detects if a step string already contains numbering.
  - `remove_existing_numbering(text: str) -> str`: Removes detected numbering from a step string.
  - `format_step_with_number(number: int, text: str, preserve_existing: bool = True) -> str`: Formats a step string by number, optionally preserving existing numbering.
  - `parse_test_case_json(json_data: dict) -> TestCase`: Parses a JSON-like dictionary into a `TestCase` object with clean steps.
- **core.models**:
  - `TestCase`: Data model representing a test case with attributes such as title, test steps, expected outcome, priority, etc.

---

## Test Functions

### `test_has_existing_numbering()`
Tests the `has_existing_numbering()` function's ability to detect various common numbering formats in step descriptions.

- **Test scenarios include**:
  - Number formats with suffixes (`"."`, `")"`, `"-"`)
  - Prefixes like `"Step X:"`
  - Leading spaces
  - Plain text with no numbering
- **Output**: Displays status (✅/❌), input text, detected result, and expected result.

---

### `test_remove_existing_numbering()`
Tests the `remove_existing_numbering()` function's ability to strip numbering prefixes from step descriptions.

- **Test scenarios include**:
  - Numbered steps using different numbering conventions
  - Step prefixes such as `"Step X:"`
  - Unnumbered steps to ensure no alteration
- **Output**: Displays status, original text, cleaned text, and expected cleaned text.

---

### `test_format_step_with_number()`
Tests `format_step_with_number()` which formats a step with a given number, considering whether to preserve existing numbering or normalize it.

- **Two modes tested**:
  - **preserve_existing=True (default)**: Keeps existing formatting if numbering is detected.
  - **preserve_existing=False**: Overwrites any existing numbering with normalized numbering.
- **Test scenarios include**:
  - Steps that already include numbering (should be preserved or normalized accordingly)
  - Steps without numbering (should receive correct numbering)
- **Output**: Status, step number, input text, formatted result, and expected output.

---

### `test_parse_test_case_with_numbered_steps()`
Tests parsing a test case JSON object containing *string steps* that include explicit numbering.

- **Verifies**:
  - Proper parsing into `TestCase` object
  - Steps' `action` texts are cleaned of double numbering
  - Output of `TestCase.to_text()` to ensure no double numbering appears in serialized text
- **Example Input**: Steps numbered as `"1. Navigate to login page"`, `"Step 2: Click button"`, etc.
- **Output includes**:
  - Print out each step with numbering and action
  - Error detection if double numbering is still present
  - Confirmation whether the final text representation is clean

---

### `test_parse_test_case_with_dict_steps()`
Tests parsing a test case JSON object where the steps are dictionaries containing `step_number`, `action`, and optionally `expected_result`.

- **Verifies**:
  - Numbering is properly cleaned from the `action` string even if already numbered
  - Correct association between step number, action, and expected result
  - Ensures no residual numbering artifacts remain in step actions
- **Output**:
  - Shows step number, cleaned action, and expected result
  - Indicates if numbering removal was successful

---

### `test_mixed_numbering()`
Tests parsing a test case with a mixture of numbered and unnumbered steps, including different styles of numbering.

- **Covers cases where**:
  - Some steps are explicitly numbered (e.g., `"1. Navigate to page"`)
  - Others have no numbering (e.g., `"Enter credentials"`)
  - Mixed formats like `"3) Click submit"` and `"Step 5: Log out"`
- **Checks**:
  - That each step's action text is properly cleaned of numbering regardless of input style
  - Step numbering is correctly assigned numerically without duplicates or double numbering
- **Output**:
  - Validates cleaned action texts against expected unnumbered strings
  - Indicates success or failure per step

---

## Execution Entry Point

When the module is executed as `__main__`, it runs all the above test functions sequentially, printing informative output including success/failure status for each test case.

---

## Summary

This module ensures robust handling of test step numbering for test cases defined in JSON-like formats:

- Detects if step descriptions already have numbering to avoid redundant prefixes.
- Cleans numbering from step descriptions when necessary.
- Formats step strings either preserving or normalizing numbering.
- Parses entire test cases with steps in various formats, preventing double numbering.
- Provides feedback via printed output to assist developers in verifying correctness.

It is intended as a self-contained validation tool for smart numbering fixes in test automation frameworks.

---

## Usage

Run the module directly to perform all tests:

```bash
python test_smart_numbering.py
```

Watch console output for detailed pass/fail information for each test scenario.

---

## Notes

- This test module depends on the `core.utils` and `core.models` modules (not included here).
- Output includes Unicode checkmarks and crosses (`✅`, `❌`) for easy identification of passed and failed tests.
- The tests cover a wide range of common numbering styles found in manual test case documentation.

---

# End of Documentation

## File: tests/test_performance.py
# Performance Testing Script Documentation

## Overview
This script is designed to evaluate the performance of the optimized system for generating test cases from user stories. It focuses on measuring the initialization time of the `TestCaseManager` and the time taken to process a user story into test cases, including a performance improvement estimate compared to a sequential baseline.

---

## Requirements
- Python 3.x
- Modules:
  - `test_case_manager` (providing `TestCaseManager`)
  - `models` (providing `UserStory`)

---

## Usage

Run the script directly:

```bash
python performance_test_script.py
```

It will execute a single test function that performs the following:

- Initialize the `TestCaseManager`.
- Create a sample `UserStory` representing a "User Login Feature".
- Use the manager to generate test cases based on the user story.
- Print detailed timing and effectiveness metrics.
- Estimate and display the performance improvement over a hypothetical sequential processing model.

---

## Code Breakdown

### `test_performance()`

This is the main function driving the performance testing flow.

#### Steps:

1. **Initialization**
   - Instantiates `TestCaseManager`.
   - Measures and outputs the time taken to initialize.

2. **User Story Definition**
   - Creates a `UserStory` instance with:
     - `id`: `"test-001"`
     - `title`: `"User Login Feature"`
     - `description`: Functional description of the feature.
     - `acceptance_criteria`: List of acceptance conditions for login.
     - `business_rules`: Security and validation constraints.

3. **Test Case Generation**
   - Calls `manager.process_user_story()` with:
     - The user story.
     - Suite name `"performance_test"`.
     - `auto_apply=False` to avoid automatic application of modifications.
   - Captures the number of generated test cases and time taken.
   - Calculates and prints average time per test case.

4. **Results Summary**
   - Extracts and displays detailed summary statistics from the results, including:
     - Total test cases generated.
     - Counts and percentages of test case categories:
       - Same (unchanged test cases)
       - Add-on (additional test cases)
       - New (completely new test cases)

5. **Performance Metrics**
   - Prints measured timing details:
     - Initialization time.
     - Test case generation time.
     - Combined total time.

6. **Estimated Improvement**
   - Estimates a sequential processing time assuming 10 seconds per test case.
   - Calculates percentage improvement comparing sequential vs actual parallel processing.
   - Prints the estimated performance gain.

7. **Completion Message**
   - Prints markers indicating the end of the test.

---

## Function Signature

```python
def test_performance() -> None
```

- No arguments.
- Returns nothing.
- Output is printed to the console.

---

## Example Output (Excerpt)

```
============================================================
PERFORMANCE TEST - RAG Test Case Manager
============================================================

1. Initializing Test Case Manager...
   ✓ Initialization completed in 0.58s

2. Generating test cases from user story...
   ✓ Generated 15 test cases in 2.10s
   ✓ Average time per test case: 0.14s

3. Results Summary:
   - Total Test Cases: 15
   - Same: 8 (53.3%)
   - Add-on: 4 (26.7%)
   - New: 3 (20.0%)

4. Performance Metrics:
   - Total Processing Time: 2.10s
   - Initialization Time: 0.58s
   - Total Time: 2.68s

5. Estimated Performance Improvement:
   - Sequential Processing (estimated): 150.00s
   - Parallel Processing (actual): 2.10s
   - Improvement: 98.6% faster

============================================================
PERFORMANCE TEST COMPLETED
============================================================
```

---

## Notes

- The actual performance gain depends heavily on implementation details in `TestCaseManager.process_user_story` which are not shown here.
- The sequential time estimate (10 seconds per test case) is an arbitrary heuristic used solely for comparison.
- This script is useful for regression testing and benchmarking optimization efforts in test case generation workflows.

---

## Extensibility

- You can customize the `UserStory` input to test different features.
- Adjust timing metrics or add profiling hooks for deeper analysis.
- Integrate with continuous integration systems to monitor performance trends over time.

## File: tests/test_type_positive_negative.py
# Documentation for Test Type Validation and Import Tests

This module contains automated tests to ensure that **test types** conform strictly to the allowed values: `"Positive"` or `"Negative"`. Invalid or unrecognized test types should default to `"Positive"`. It validates this rule across multiple functions and import mechanisms in the system.

---

## Overview

- **Purpose:** To verify that test types are correctly validated, parsed, and imported from Excel files, enforcing the rule:  
  > _Test types may only be `"Positive"` or `"Negative"`. Any other value defaults to `"Positive"`._

- **Dependencies:**  
  - `validate_test_type(str) -> str`: A utility function that normalizes and validates test type strings.  
  - `parse_test_case_json(dict) -> TestCase`: Parses JSON-like dictionaries into test case objects, including test type validation.  
  - `import_from_excel(str) -> List[TestCase]`: Imports test cases from an Excel file, invoking validation on test types.

- **Third-party:** Uses `pandas` for DataFrame manipulation and `tempfile` for creating temporary Excel files.

---

## Functions and Tests

### 1. `test_validate_function()`

**Description:**  
Tests the `validate_test_type` function with various input strings to confirm it returns either `"Positive"` or `"Negative"`, normalizing different cases and trimming spaces. Invalid values are tested to confirm they default to `"Positive"`.

**Test Cases Covered:**  
- Valid Types (case-insensitive, with spaces):  
  - `"Positive"`, `"positive"`, `"POSITIVE"`, `"  Positive  "`  
  - `"Negative"`, `"negative"`, `"NEGATIVE"`, `"  negative  "`  
- Invalid Types:  
  - `"Functional"`, `"Integration"`, `"Security"`, `"Performance"`, empty strings, and random other strings.

**Expected Behavior:**  
- Valid inputs return canonical `"Positive"` or `"Negative"`.  
- Invalid inputs return `"Positive"` by default.

---

### 2. `test_parse_json()`

**Description:**  
Validates the `parse_test_case_json` function correctly applies the test type validation rule when parsing test case data provided as dictionaries.

**Test Cases Covered:**  
- Test cases with various `test_type` fields including valid, lowercase, uppercase, invalid, and empty strings:
  - `"Positive"`, `"Negative"`, `"positive"`, `"NEGATIVE"`, `"Functional"`, `""`  

**Expected Behavior:**  
- The resulting `TestCase` object’s `test_type` attribute should always be `"Positive"` or `"Negative"`, defaulting invalid inputs to `"Positive"`.

---

### 3. `test_excel_import()`

**Description:**  
Tests the `import_from_excel` function for correctness when importing test cases from an Excel file containing a variety of test types.

**Test Data:**  
Five test cases with the following `Test Type` values:
- `"Positive"`  
- `"Negative"`  
- `"Functional"` (Invalid, expects to default to `"Positive"`)  
- `""` (Empty string, expects `"Positive"`)  
- `"negative"` (Lowercase, expects `"Negative"`)

**Process:**  
- Creates an in-memory Excel file using `pandas` and `tempfile`.  
- Imports the test cases using `import_from_excel`.  
- Verifies that each imported test case has the correct normalized test type.

**Expected Behavior:**  
- Test cases with valid types maintain their normalized forms.  
- Invalid or empty test types default to `"Positive"`.

---

## Script Execution

When run as a standalone script (i.e., executed directly):

- Prints a descriptive banner about the testing rules and defaults.
- Runs all three tests sequentially:
  - `test_validate_function`  
  - `test_parse_json`  
  - `test_excel_import`  
- Prints individual and final test results, clearly indicating pass/fail status.
- Summarizes the enforcement of test type rules and whether all tests passed.

---

## Summary

- **Assertions:** Test types must be exactly `"Positive"` or `"Negative"` (case normalized).  
- **Defaulting:** Any other inputs must default strongly to `"Positive"`.  
- **Test Coverage:** Validation function, JSON parsing, and Excel import are all verified for this behavior.

---

## Usage Notes

- This test module depends on implementation details of functions within `core.utils`: specifically `validate_test_type`, `parse_test_case_json`, and `import_from_excel`.
- Make sure these functions handle test type normalization consistently with this test logic.
- Requires Python environment with `pandas` and `openpyxl` installed for Excel operations.
- Temporary files created during tests are cleaned up automatically.

---

## Example Output Snippet

```
======================================================================
TEST 1: validate_test_type() Function
======================================================================
✅ 'Positive'                 -> Positive   (expected: Positive)
✅ 'positive'                 -> Positive   (expected: Positive)
✅ 'NEGATIVE'                 -> Negative   (expected: Negative)
❌ 'Functional'               -> Positive   (expected: Positive)
...

======================================================================
TEST 2: parse_test_case_json() Function
======================================================================
✅ Input: 'Positive'          -> Result: Positive   (expected: Positive)
✅ Input: 'Functional'        -> Result: Positive   (expected: Positive)
...

======================================================================
TEST 3: Excel Import with Test Type Validation
======================================================================
✅ Row 1: Input='Positive', Result='Positive', Expected='Positive'
✅ Row 3: Input='Functional', Result='Positive', Expected='Positive'
...

======================================================================
FINAL RESULTS
======================================================================
validate_test_type():  ✅ PASS
parse_test_case_json(): ✅ PASS
Excel Import:           ✅ PASS

🎉 ALL TESTS PASSED!
✅ Test types are strictly limited to: Positive or Negative
✅ All invalid types default to: Positive
```

---

This documentation should enable maintainers and developers to understand the intent, usage, and coverage of the testing logic focused on enforcing strict test type constraints in the system.

## File: ui/__init__.py
# UI Components - Streamlit App and API

## Overview
This module contains the UI components for the application, implemented using Streamlit. It also includes the API layer that facilitates communication between the frontend UI and backend services, enabling interactive and dynamic user experiences.

## Components

### Streamlit App
- **Purpose**: Provides a user-friendly web-based interface leveraging Streamlit's capabilities for rapid UI development.
- **Features**:
  - Interactive widgets for user input.
  - Real-time updates and visualizations.
  - Integration with backend APIs to fetch and display data.

### API
- **Purpose**: Acts as an intermediary between the Streamlit frontend and backend services.
- **Features**:
  - HTTP endpoints handling data requests and responses.
  - Data validation and error handling.
  - Facilitates smooth data flow for frontend components.

## Usage
1. **Run the Streamlit App**
   ```bash
   streamlit run app.py
   ```
2. **API Endpoints**
   - Access the API endpoints as documented in the API specification for data retrieval and manipulation.

## Dependencies
- Streamlit
- Requests (or relevant HTTP client libraries)
- Backend service SDKs (if applicable)

## Notes
- Ensure backend services are running and accessible before launching the Streamlit app.
- Proper error handling is implemented to guide users in case of connectivity or data issues.

---

*This documentation provides a high-level understanding of the UI components implemented with Streamlit and the associated API services.*

## File: ui/api.py
# RAG Test Case Manager API Documentation

## Overview

The RAG Test Case Manager API is a FastAPI-based RESTful service designed to facilitate intelligent test case management using Retrieval-Augmented Generation (RAG) techniques. It processes requirement texts and user stories to generate and manage test cases within defined test suites. The API supports decision application, querying, filtering, export operations, and provides health and configuration endpoints.

---

## Table of Contents

- [General Endpoints](#general-endpoints)
- [Processing Endpoints](#processing-endpoints)
- [Test Case Endpoints](#test-case-endpoints)
- [Test Suite Endpoints](#test-suite-endpoints)
- [Statistics Endpoint](#statistics-endpoint)
- [Export Endpoints](#export-endpoints)
- [Configuration Endpoint](#configuration-endpoint)
- [Models](#models)
- [Running the API](#running-the-api)

---

## General Endpoints

### `GET /`
**Description:** Root endpoint providing basic API info.  
**Response Example:**
```json
{
  "message": "RAG Test Case Manager API",
  "version": "1.0.0",
  "docs": "/docs",
  "health": "/health"
}
```

---

### `GET /health`
**Tags:** General  
**Response Model:** `HealthResponse`  
**Description:** Returns the health status, current timestamp, configuration validity, and total number of test cases in the knowledge base.  
**Response Example:**
```json
{
  "status": "healthy",
  "timestamp": "2024-04-26T15:30:00",
  "config_valid": true,
  "total_test_cases": 150
}
```

---

## Processing Endpoints

### `POST /process/requirement`
**Tags:** Processing  
**Request Model:** `RequirementTextRequest`  
**Response Model:** `ProcessingResult`  
**Description:** Process raw requirement text to generate test cases. Supports specifying suite name, automatic decision application, and number of test cases to generate.

**Request Body Fields:**

| Field           | Type    | Required | Description                                |
|-----------------|---------|----------|--------------------------------------------|
| requirement_text| string  | Yes      | The requirement text to process            |
| suite_name      | string  | No       | Test suite name (default: `"default"`)    |
| auto_apply     | bool    | No       | Automatically apply decisions (default: false) |
| num_test_cases | int     | No       | Number of test cases to generate (5-30, optional) |

**Response Fields:**

| Field               | Type      | Description                                      |
|---------------------|-----------|-------------------------------------------------|
| success             | bool      | Indicates if processing was successful          |
| message             | string    | Status message                                  |
| generated_test_cases | List[TestCase] | List of generated test cases                   |
| results             | List[dict]| Detailed processing results                      |
| actions_taken       | List[string] | Actions performed during processing             |
| summary             | dict      | Summary information                              |

---

### `POST /process/user-story`
**Tags:** Processing  
**Request Model:** `UserStoryRequest`  
**Response Model:** `ProcessingResult`  
**Description:** Process user story, including title, description, acceptance criteria, and business rules to generate test cases.

**Request Body Fields:**

| Field               | Type           | Required | Description                                |
|---------------------|----------------|----------|--------------------------------------------|
| title               | string         | Yes      | User story title                           |
| description         | string         | Yes      | User story description                     |
| acceptance_criteria  | List[string]   | No       | List of acceptance criteria (default empty list) |
| business_rules      | List[string]   | No       | List of business rules (default empty list) |
| context             | string or null | No       | Additional context (optional)              |
| suite_name          | string         | No       | Test suite name (default: `"default"`)    |
| auto_apply          | bool           | No       | Automatically apply decisions (default: false) |
| num_test_cases      | int or null    | No       | Number of test cases to generate (5-30, optional) |

---

### `POST /apply-decision`
**Tags:** Processing  
**Request Model:** `ApplyDecisionRequest`  
**Description:** Apply a decision on a specific test case based on a comparison result.

**Request Body Fields:**

| Field         | Type               | Required | Description                      |
|---------------|--------------------|----------|----------------------------------|
| test_case     | `TestCase`         | Yes      | The test case in question         |
| comparison    | `ComparisonResult` | Yes      | Result of comparison              |
| suite_name    | string             | No       | Test suite name (default: `"default"`) |
| user_approved | bool               | No       | Whether user approves the decision (default: true) |

**Response Example:**
```json
{
  "success": true,
  "message": "Decision applied successfully",
  "action": "added to suite"
}
```

---

## Test Case Endpoints

### `GET /test-cases`
**Tags:** Test Cases  
**Description:** Retrieve all test cases within a specified suite.  
**Query Parameters:**

| Parameter  | Type   | Default   | Description                  |
|------------|--------|-----------|------------------------------|
| suite_name | string | "default" | Name of the test suite to query |

**Response:** List of `TestCase` objects.

---

### `GET /test-cases/{test_case_id}`
**Tags:** Test Cases  
**Description:** Retrieve a specific test case by its ID from a specified suite.  
**Path Parameter:**

| Parameter     | Type   | Description                     |
|---------------|--------|---------------------------------|
| test_case_id  | string | ID of the test case             |

**Query Parameter:**

| Parameter  | Type   | Default   | Description                  |
|------------|--------|-----------|------------------------------|
| suite_name | string | "default" | Name of the test suite to query |

**Response:** A single `TestCase` object.  
**Errors:** Returns 404 if test case is not found.

---

### `GET /test-cases/filtered`
**Tags:** Test Cases  
**Description:** Retrieve filtered test cases from a suite based on optional criteria.

**Query Parameters:**

| Parameter    | Type     | Default   | Description                                                   |
|--------------|----------|-----------|---------------------------------------------------------------|
| suite_name   | string   | "default" | Name of the test suite                                         |
| priorities   | string   | None      | Comma-separated priorities (e.g., "High,Critical")            |
| test_types   | string   | None      | Comma-separated test types (e.g., "Functional,Integration")   |
| tags         | string   | None      | Comma-separated tags (e.g., "login,authentication")           |
| is_regression| bool     | None      | Filter regression tests: true=only regression, false=non-regression |

**Response:** List of filtered `TestCase` objects.

**Usage Examples:**

- Get only regression tests:  
  `/test-cases/filtered?is_regression=true`
- Get high priority regression tests:  
  `/test-cases/filtered?priorities=High,Critical&is_regression=true`

---

## Test Suite Endpoints

### `GET /suites`
**Tags:** Test Suites  
**Description:** List all available test suites in the knowledge base.  
**Response:** List of suite names (`List[str]`).

---

## Statistics Endpoint

### `GET /statistics`
**Tags:** Statistics  
**Description:** Retrieve system-level statistics including knowledge base data, and possibly other aggregate metrics.  
**Response:** JSON object containing statistics.

---

## Export Endpoints

### `POST /export/test-suite`
**Tags:** Export  
**Request Model:** `ExportRequest`  
**Description:** Export an entire test suite into a file with the specified format.

**Request Body Fields:**

| Field      | Type   | Default   | Description                             |
|------------|--------|-----------|---------------------------------------|
| suite_name | string | "default" | Test suite to export                   |
| format     | string | "excel"   | Export format: `excel` (xlsx), `csv`, or `json` |

**Response:** Downloads the exported file as an attachment.

---

### `POST /export/filtered-test-suite`
**Tags:** Export  
**Request Model:** `FilteredExportRequest`  
**Description:** Export a subset of test cases filtered by priorities, test types, tags, and regression flag.

**Request Body Fields:**

| Field       | Type         | Default   | Description                                                  |
|-------------|--------------|-----------|--------------------------------------------------------------|
| suite_name  | string       | "default" | Test suite name                                              |
| format      | string       | "excel"   | Export format: `excel`, `csv`, or `json`                    |
| priorities  | List[string] | None      | Filter by priorities (e.g., `["High", "Critical"]`)          |
| test_types  | List[string] | None      | Filter by test types (e.g., `["Functional", "Integration"]`) |
| tags        | List[string] | None      | Filter by tags (test case must have at least one matching tag) |
| is_regression| bool        | None      | Filter regression tests (`true` for only regression, `false` for only non-regression) |

**Sample Request Body:**
```json
{
    "suite_name": "default",
    "format": "excel",
    "priorities": ["High", "Critical"],
    "is_regression": true
}
```

**Response:** Downloads the filtered exported file.

---

## Configuration Endpoint

### `GET /config/thresholds`
**Tags:** Configuration  
**Description:** Returns the current configured similarity thresholds used internally by the system.

**Response Example:**

```json
{
  "threshold_same": 0.85,
  "threshold_addon_min": 0.7,
  "threshold_addon_max": 0.9
}
```

---

## Models

### RequirementTextRequest
- `requirement_text: str` — Requirement text to process.
- `suite_name: str` — Test suite name (default: `"default"`).
- `auto_apply: bool` — Whether to auto-apply decisions (default: `false`).
- `num_test_cases: Optional[int]` — Number of test cases to generate (5 to 30).

### UserStoryRequest
- `title: str` — User story title.
- `description: str` — User story description.
- `acceptance_criteria: List[str]` — Acceptance criteria.
- `business_rules: List[str]` — Business rules.
- `context: Optional[str]` — Additional context.
- `suite_name: str` — Test suite name (default: `"default"`).
- `auto_apply: bool` — Auto-apply decisions (default: `false`).
- `num_test_cases: Optional[int]` — Number of test cases to generate.

### ProcessingResult
- `success: bool` — Success status.
- `message: str` — Message describing result.
- `generated_test_cases: List[TestCase]` — Generated test cases.
- `results: List[dict]` — Detailed processing outputs.
- `actions_taken: List[str]` — Actions performed.
- `summary: dict` — Summary information.

### ApplyDecisionRequest
- `test_case: TestCase` — Test case to apply decision on.
- `comparison: ComparisonResult` — Comparison result information.
- `suite_name: str` — Test suite name.
- `user_approved: bool` — User approval flag.

### ExportRequest
- `suite_name: str` — Test suite name.
- `format: str` — Export format (`excel`, `csv`, or `json`).

### FilteredExportRequest
- `suite_name: str` — Test suite name.
- `format: str` — Export format.
- `priorities: Optional[List[str]]` — Priorities filter.
- `test_types: Optional[List[str]]` — Test types filter.
- `tags: Optional[List[str]]` — Tags filter.
- `is_regression: Optional[bool]` — Regression test filter.

### HealthResponse
- `status: str` — Health status.
- `timestamp: datetime` — Time of the health check.
- `config_valid: bool` — Whether config is valid.
- `total_test_cases: int` — Number of test cases in knowledge base.

---

## Running the API

Run the API server using the following command:

```bash
uvicorn api:app --host 0.0.0.0 --port 8000 --reload --log-level info
```

**Note:** Ensure Azure OpenAI credentials and other configurations are correctly set up in your `.env` file. The system will alert if configuration validation fails.

API Documentation is accessible at: `http://localhost:8000/docs`

Health check endpoint available at: `http://localhost:8000/health`

---

## Notes and Best Practices

- **CORS Settings:** Current CORS middleware allows all origins, suitable for development but recommended to restrict origins in production environments.
- **Auto-Apply Decisions:** Use with caution; manual review is often advised to ensure test case quality.
- **Exported Files:** Are stored temporarily in the configured output directory and served as downloadable files.
- **Filtering:** Supports flexible combinations of filters to retrieve or export targeted subsets of test cases.
- **Error Handling:** The API uses HTTPException to indicate errors, returning appropriate HTTP status codes and messages.
- **Test Suite Naming:** Use consistent suite names when managing sets of related test cases.

---

This documentation outlines all major functionalities exposed by the RAG Test Case Manager API for building, improving, and managing test cases effectively within an intelligent framework.

## File: ui/app.py
# Documentation for Streamlit UI: RAG-based Test Case Management System

## Overview

This Streamlit-based UI serves as a frontend for a Retrieval-Augmented Generation (RAG) powered Test Case Management System. It facilitates importing existing test cases, processing requirements (user stories or free text) to generate and analyze test cases, viewing and managing test suites, and exporting test data with various filters and formats.

---

## Module: `ui/app.py`

### Imports and Setup

- Standard libraries:
  - `os`, `sys`: For filesystem and path manipulations.
  - `tempfile`: To handle temporary files.
  - `shutil`: For file operations like deleting directories.
  - `datetime`: For timestamping exported files.

- Third-party:
  - `streamlit as st`: Web UI framework for interactive apps.

- Project modules:
  - `core.models`: Defines domain models such as `UserStory`, `TestCase`, and `DecisionType`.
  - `engines.test_case_manager`: Contains the main engine `TestCaseManager` for processing and managing test cases.
  - `config.config`: Configuration settings and validation, including Azure OpenAI credentials and file paths.
  - `core.utils`: Utility functions like `generate_id`.

### Streamlit Page Configuration

- Sets page title to **"RAG Test Case Manager"**, with wide layout and expanded sidebar.

### Custom CSS

- Defines CSS classes for header styles, metric cards, and styling different decision types (same, add-on, new).

### Session State Initialization

- Initializes session state attributes:
  - `manager`: Instance of `TestCaseManager`.
  - `results`: Stores processing results from test case generation and analysis.
  - `suite_name`: Name of the current test suite, defaulting to `"default"`.

---

## Functions

### `initialize_manager() -> bool`

Initializes the `TestCaseManager` instance in session state.

- Checks if the ChromaDB persistence directory exists and whether it might be corrupted.
- Attempts to initialize the `TestCaseManager`. On failure related to database corruption:
  - Deletes the ChromaDB directory with retries.
  - Recreates necessary directories.
  - Attempts to reinitialize.
- Displays Streamlit status/info messages for success, warnings, or errors.
- Returns `True` on success, `False` on failure.

### `main()`

Main Streamlit app function containing the entire UI layout and logic.

- Contains header, sidebar, and four main tabs for different application areas.

---

## UI Layout and Features

### Sidebar: Configuration and Export

- Displays configuration validity status (specifically for Azure OpenAI credentials).
- Calls `initialize_manager()` to set up backend engine.
- Displays statistics such as total test cases in knowledge base.
- Provides export functionality:
  - Export all test cases.
  - Export all regression tests.
  - Advanced export filters by priority, test type, tags, and regression status.
  - Download exported Excel files.

### Tabs

#### Tab 0: 📥 Import KB (Existing Test Cases)

- Allows uploading Excel (`.xlsx`, `.xls`) or JSON files containing test cases.
- Displays format requirements for Excel and JSON uploads.
- Imports test cases into the knowledge base (default test suite).
- Shows import results summary, including failures and test case details (up to 10).
- Updates and displays updated statistics after import.

#### Tab 1: 📝 Process Requirements

- Two input methods:
  - **Text Input:** Freeform requirements text (e.g., User Story, Business Requirement Spec, PRD).
  - **User Story Form:** Structured form capturing title, description, acceptance criteria, business rules, and context.
- Options to "auto-apply" decisions during processing.
- On processing requirement or user story:
  - Invokes the TestCaseManager to analyze input and generate test cases.
  - Stores results in session state and displays success message.
  - Reruns to refresh statistics.
- Displays processing results including summary metrics:
  - Total test cases, Same, Add-on, and New counts with percentages.
- Provides buttons for exporting results:
  - Multi-sheet Excel export (All, Modified, New).
  - User format Excel export (custom column format).
- Displays each test case result with decision details, reasoning, recommendations, and test case details.
- Allows manual decision application if auto-apply is off.

#### Tab 2: 📋 View Test Cases

- Lists all test cases in the current suite.
- Provides export button for user format Excel export of the entire suite.
- Displays detailed information per test case including steps, expected outcomes, preconditions, version, creation/update timestamps.

#### Tab 3: 🎯 Regression Suite

- Displays statistics on total tests, regression tests, high/critical priority regression, and critical-only tests.
- Shows a progress bar for regression coverage percentage.
- Allows filtering to view all regression tests, high & critical only, or critical only.
- Displays detailed information of filtered regression test cases.
- Provides tips when no regression tests are found.

---

## Key Classes and Data Structures Used

- `UserStory`: Represents a user story input by the user with attributes like id, title, description, acceptance criteria (list), business rules (list), and optional context.
- `TestCase`: Represents a test case with metadata, steps, and outcomes.
- `DecisionType`: Enum representing decision categories for comparing generated test cases with existing ones (`same`, `addon`, `new`).
- `TestCaseManager`: Encapsulates logic for:
  - Importing test cases.
  - Processing requirement text or user stories.
  - Getting statistics and test cases.
  - Exporting test cases and results.
  - Applying decisions manually or automatically.

---

## Configuration (`Config`)

- Contains paths for:
  - `CHROMA_PERSIST_DIRECTORY`: Directory where the vector DB is persisted.
  - `KNOWLEDGE_BASE_PATH`: Directory for KB data.
  - `TEST_SUITE_OUTPUT`: Path to save exported files.
- Includes methods to validate required environment variables, especially Azure OpenAI credentials.

---

## Usage Instructions

1. **Setup Config**:
   - Ensure `.env` file has Azure OpenAI API keys and required settings.
2. **Run App**:
   - From project root: `streamlit run ui/app.py`
3. **Import Test Cases**:
   - Use Tab 0 to upload existing test cases from Excel or JSON.
4. **Process Requirements**:
   - Use Tab 1 to input requirements as free text or structured user stories.
   - Generate and analyze test cases.
5. **View and Export Test Cases**:
   - Use Tab 2 to view all test cases with details and export options.
6. **Manage Regression Suite**:
   - Use Tab 3 to view, filter, and export regression test cases.
7. **Export Data**:
   - Use export buttons in sidebar or tabs to save files for external use.

---

## Error Handling & User Guidance

- Detects corrupted vector database and attempts recovery.
- Provides clear UI warnings and error messages.
- Suggests restarting Streamlit server to reset database connections when needed.
- Explains file format requirements on import.
- Limits displayed import results to avoid UI overload but informs user.
- Provides tips for regression test case management.

---

## Development Notes

- Uses Streamlit's session state to maintain app state across reruns.
- Uses temporary file storage for uploads.
- Utilizes modular backend engine, allowing UI to remain focused on interaction handling.

---

# Summary

This UI is a comprehensive interface to a RAG-based intelligent test case management platform. It enables users to import, generate, analyze, view, filter, and export test cases efficiently, with robust handling of configuration, persistence, and error conditions. The design leverages Streamlit for responsive and interactive web app behavior.

