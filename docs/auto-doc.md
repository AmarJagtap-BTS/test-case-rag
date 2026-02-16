# Auto Generated Documentation

*Complete project documentation - Generated on: Mon Feb 16 11:56:27 UTC 2026*

## File: config/__init__.py
# Configuration Management Module

This module provides access to the core configuration management functionality.

## Overview

The `Configuration management` module serves as a centralized place to handle application configurations. It exposes the `Config` class from the internal `config` submodule, which contains the main logic for managing application settings.

## Contents

- `Config`: The primary class responsible for managing configuration data.

## Usage

```python
from configuration_management import Config

config = Config()
# Use config to access or modify application settings
```

## Details

- The module imports the `Config` class from the relative internal `.config` module.
- The `__all__` variable restricts the public API to only include `Config`, ensuring encapsulation and clarity of the exported interface.

## File: config/config.py
# Module: Configuration Management for RAG-based Test Case System

This module provides centralized configuration management for a Retrieval-Augmented Generation (RAG) based test case system. It reads application settings from environment variables (with defaults) and provides utility functions for validation and directory setup.

---

## Overview

The `Config` class encapsulates all necessary configuration parameters required for:

- Connecting with Azure OpenAI services
- Managing vector database persistence
- Defining similarity thresholds and scoring weights for hybrid semantic + language model ranking
- Configuring RAG retrieval behavior
- Configuring test case generation parameters, including parallelization and test distribution statistics
- Managing storage paths and collection names used across the system

---

## Environment Variable Loading

This module uses the [`python-dotenv`](https://pypi.org/project/python-dotenv/) package to load environment variables from a `.env` file (if present) when the module is imported.

---

## Class: `Config`

A static configuration holder providing all required values as class variables.

### Azure OpenAI Configuration

- `AZURE_OPENAI_API_KEY` (`str`): Azure OpenAI API key.
- `AZURE_OPENAI_ENDPOINT` (`str`): Endpoint URL for Azure OpenAI service.
- `AZURE_OPENAI_DEPLOYMENT_NAME` (`str`, default `"gpt-4.1-mini"`): Deployment name of the OpenAI model.
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT` (`str`, default `"text-embedding-ada-002"`): Deployment name for embedding model.
- `AZURE_OPENAI_API_VERSION` (`str`, default `"2024-08-01-preview"`): API version used in requests.

### Vector Database Configuration

- `CHROMA_PERSIST_DIRECTORY` (`str`, default `"./chroma_db"`): Path for persisting the Chroma vector database.

### Similarity Thresholds

- `THRESHOLD_SAME` (`float`, default `0.99`): Threshold to consider two items as the same.
- `THRESHOLD_ADDON_MIN` (`float`, default `0.60`): Minimum similarity for addon considerations.
- `THRESHOLD_ADDON_MAX` (`float`, default `0.85`): Maximum similarity for addon considerations.

### Hybrid Scoring Weights

Weights used to combine semantic similarity and LLM-based context similarity in scoring:

- `SEMANTIC_WEIGHT` (`float`, default `0.60`): Weight for embedding-based similarity (speed-focused).
- `LLM_WEIGHT` (`float`, default `0.40`): Weight for LLM-based semantic similarity.

### RAG Configuration

- `RAG_TOP_K` (`int`, default `10`): Number of top candidates to retrieve in RAG; tuned for speed.

### Test Case Generation Configuration

- `USE_PARALLEL_GENERATION` (`bool`, default `True`): Flag to enable parallel test case generation.
- `PARALLEL_BATCH_SIZE` (`int`, default `10`): Number of test cases generated in one batch.
- `BATCH_TIMEOUT_SECONDS` (`int`, default `45`): Timeout in seconds for batch generation.

### Test Case Generation Limits

- `MIN_TEST_CASES` (`int`, default `8`): Minimum number of test cases to generate.
- `MAX_TEST_CASES` (`int`, default `25`): Maximum number of test cases to generate.
- `DEFAULT_TEST_CASES` (`int`, default `12`): Default number of test cases to generate.

### Test Case Type Distribution (Percentages)

Defines proportion ranges for different test case types, expressed as floats between 0.0 and 1.0:

- `POSITIVE_MIN_PERCENT`, `POSITIVE_MAX_PERCENT` (default `0.50` each)
- `NEGATIVE_MIN_PERCENT`, `NEGATIVE_MAX_PERCENT` (default `0.30` each)
- `UI_MIN_PERCENT`, `UI_MAX_PERCENT` (default `0.20` each)
- `SECURITY_MIN_PERCENT`, `SECURITY_MAX_PERCENT` (default `0.00` each)
- `EDGE_CASE_MIN_PERCENT`, `EDGE_CASE_MAX_PERCENT` (default `0.00` each)

### Storage Paths

- `KNOWLEDGE_BASE_PATH` (`str`, default `"./knowledge_base"`): Directory for knowledge base files.
- `TEST_SUITE_OUTPUT` (`str`, default `"./output"`): Directory for generated test suite outputs.

### Collection Names

- `CHROMA_COLLECTION_NAME` (`str`, fixed to `"test_cases"`): Name of the vector database collection for test cases.

---

### Methods

#### `@classmethod validate() -> bool`

Checks if critical configuration parameters are provided and non-empty.

- Validates presence of:
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`

**Returns:**  
`True` if all required fields are present, otherwise `False`.

#### `@classmethod create_directories() -> None`

Ensures all required storage directories exist, creating them if necessary:

- `CHROMA_PERSIST_DIRECTORY`
- `KNOWLEDGE_BASE_PATH`
- `TEST_SUITE_OUTPUT`

---

## Module-level Initialization

Upon import, the module automatically invokes `Config.create_directories()` to guarantee all necessary directories are in place for the application to function properly.

---

## Usage Example

```python
from config_module import Config

if not Config.validate():
    raise RuntimeError("Missing required configuration!")

# Access configs anywhere in the application
api_key = Config.AZURE_OPENAI_API_KEY

# Paths are guaranteed to exist
persist_dir = Config.CHROMA_PERSIST_DIRECTORY
```

---

## Notes

- Environment variables override the default values if present.
- Directory paths are relative by default but can be overridden using environment variables.
- Similarity thresholds and weights are tuned for balancing speed and accuracy.
- Test case generation is optimized via parallel processing with adjustable batch size and timeout.

---

This configuration module promotes consistent and centralized management of settings critical to the RAG test case generation system's operation and extensibility.

## File: core/__init__.py
"""
Core Business Logic and Data Models Module
=========================================

This module contains the primary business logic components and data models utilized throughout the application. It consolidates key classes, utility functions, and knowledge base management to support core functionalities such as test case handling, user story management, decision making, and data export.

Exports
-------

- Classes:
    - `TestCase`: Represents an individual test case with its attributes and methods.
    - `UserStory`: Encapsulates user story details relevant to product requirements.
    - `ComparisonResult`: Defines the outcomes of test case or data comparisons.
    - `DecisionType`: Enumerates different types of decisions used within the business logic.
    - `KnowledgeBase`: Manages the domain knowledge and rule-based information supporting decision-making processes.

- Utility Functions:
    - `generate_id()`: Generates unique identifiers for entities within the system.
    - `load_json(filepath)`: Loads JSON data from a specified file path.
    - `save_json(data, filepath)`: Saves given data to a JSON file at the specified path.
    - `parse_test_case_json(json_data)`: Parses JSON formatted test case data into `TestCase` instances.
    - `export_to_excel(data, filepath)`: Exports provided data into an Excel spreadsheet file.
    - `export_to_csv(data, filepath)`: Exports provided data into a CSV formatted file.

Usage
-----

This module serves as a central point to import and interact with core entities and helper functions such as:

```python
from core_module import TestCase, generate_id, KnowledgeBase

# Example usage
new_test_case = TestCase(...)
unique_id = generate_id()
kb = KnowledgeBase()
```

Note
----

The concrete implementations and detailed usage of each class and function can be found in their respective definition files (`models.py`, `utils.py`, `knowledge_base.py`). This module simplifies importing and promotes a cleaner namespace for core functionalities.

"""

## File: core/knowledge_base.py
# KnowledgeBase Class Documentation

## Module Overview
This module provides management capabilities for a knowledge base of test cases organized into test suites. It allows creating, retrieving, updating, and exporting test suites and test cases, persisting the information on disk using JSON serialization.

---

## Class: `KnowledgeBase`

Manages storage and retrieval of test cases grouped by test suites.

### Attributes
- `base_path: str`  
  Base directory path where test suite JSON files are stored. Configured via `Config.KNOWLEDGE_BASE_PATH`.

- `test_suites: Dict[str, TestSuite]`  
  In-memory dictionary of test suites, keyed by suite name.

---

### Methods

#### `__init__(self)`

Initializes the knowledge base by setting the storage path and loading existing test suites from disk.

---

#### `_load_existing_suites(self) -> None`

Loads existing test suite JSON files from the `base_path` directory and deserializes them into `TestSuite` objects stored in `test_suites`.

- Creates the directory if it does not exist.
- Prints errors if any suite fails to load.

---

#### `create_test_suite(self, name: str, description: str = "") -> TestSuite`

Creates a new test suite with given name and optional description, saves it to disk, and stores it in memory.

- **Args**:
  - `name`: Name of the test suite.
  - `description`: Description text for the test suite (default is empty).
- **Returns**: The newly created `TestSuite` instance.

---

#### `get_test_suite(self, name: str) -> Optional[TestSuite]`

Retrieves a test suite by name.

- **Args**:
  - `name`: Name of the test suite.
- **Returns**: The `TestSuite` instance if found, otherwise `None`.

---

#### `add_test_case_to_suite(self, suite_name: str, test_case: TestCase) -> None`

Adds a `TestCase` to the specified test suite. If the suite does not exist, it creates a new suite first.

- **Args**:
  - `suite_name`: Name of the target test suite.
  - `test_case`: The `TestCase` object to add.

---

#### `update_test_case_in_suite(self, suite_name: str, test_case: TestCase) -> None`

Updates an existing test case in the specified suite, identified by the test case's ID.

- **Args**:
  - `suite_name`: Name of the test suite.
  - `test_case`: Updated `TestCase` object.

- If the suite does not exist, this method does nothing.

---

#### `get_test_case_from_suite(self, suite_name: str, test_case_id: str) -> Optional[TestCase]`

Retrieves a test case by its ID from the specified test suite.

- **Args**:
  - `suite_name`: Name of the test suite.
  - `test_case_id`: ID of the test case.
- **Returns**: The `TestCase` if found, otherwise `None`.

---

#### `get_all_test_cases(self, suite_name: Optional[str] = None) -> List[TestCase]`

Retrieves all test cases either from a specific suite or from all suites if no suite is specified.

- **Args**:
  - `suite_name`: Optional suite name to filter the test cases.
- **Returns**: List of `TestCase` objects.

---

#### `list_suites(self) -> List[str]`

Lists the names of all test suites currently loaded in the knowledge base.

- **Returns**: List of suite names.

---

#### `_save_suite(self, suite: TestSuite) -> None`

Serializes and saves a `TestSuite` object to disk as a JSON file.

- **Args**:
  - `suite`: The `TestSuite` to save.
- The file is named after the suite name with spaces replaced by underscores.

---

#### `export_suite(self, suite_name: str, output_path: str, format: str = "json") -> None`

Exports a test suite to an external file in one of several formats: JSON, Excel, or CSV.

- **Args**:
  - `suite_name`: Name of the test suite to export.
  - `output_path`: File path where to save the exported data.
  - `format`: Output file format, which can be `"json"` (default), `"excel"`, or `"csv"`.
- **Raises**:
  - `ValueError` if the suite does not exist or if an unsupported format is specified.

---

## Usage Example

```python
kb = KnowledgeBase()

# Create a new test suite
suite = kb.create_test_suite("Login Features", "Test suite for login scenarios")

# Add a test case
test_case = TestCase(id=generate_id(), name="Valid Login", steps=["Enter username", "Enter password", "Click login"], expected_result="User logged in")
kb.add_test_case_to_suite("Login Features", test_case)

# Retrieve and update a test case
case = kb.get_test_case_from_suite("Login Features", test_case.id)
if case:
    case.expected_result = "User logged into dashboard"
    kb.update_test_case_in_suite("Login Features", case)

# Export suite to Excel
kb.export_suite("Login Features", "login_features.xlsx", format="excel")
```

---

# Additional Notes

- This module depends on external project-specific classes and utilities:
  - `TestCase` and `TestSuite` from `core.models`
  - JSON save/load helpers and export functions from `core.utils`
  - Configuration from `config.config`
- The suite files are persisted as JSON files in the configured `KNOWLEDGE_BASE_PATH`.
- The module assumes `TestSuite` supports methods like `add_test_case`, `update_test_case`, and `get_test_case_by_id`.
- Export to Excel and CSV relies on utils, which must support receiving a list of test cases.

## File: core/models.py
# Pydantic Models for Test Case Management System

This module defines a set of Pydantic models for representing and managing test cases, test suites, test comparisons, and related artifacts in a test case management system.

---

## Enum: `DecisionType`

Decision types used to classify the relationship between two test cases during comparison.

| Member  | Value    | Description                      |
|---------|----------|---------------------------------|
| SAME    | `"same"` | Test cases are considered the same. |
| ADDON   | `"add-on"` | New test case adds coverage on top of existing one. |
| NEW     | `"new"`  | Test case is entirely new, no match found. |

---

## Model: `TestStep`

Represents an individual step within a test case.

### Attributes

- `step_number: int`  
  Sequential number of the test step.

- `action: str`  
  Action to be performed in this step.

- `expected_result: str`  
  Expected result or outcome after performing the action.

---

## Model: `TestCase`

Structured model representing a comprehensive test case.

### Attributes

- `id: str`  
  Unique identifier for the test case. Default: `""`.

- `title: str`  
  Brief descriptive title.

- `description: str`  
  Detailed description of the test case's purpose.

- `business_rule: str`  
  Business rule or functional requirement the test case validates. Default: `"Functional requirement validation"`.

- `preconditions: List[str]`  
  List of conditions that must be met before executing the test case.

- `test_steps: List[TestStep]`  
  Ordered list of test steps outlining the test procedure.

- `expected_outcome: str`  
  The expected result after executing all test steps.

- `postconditions: List[str]`  
  Conditions expected to hold true after test case execution.

- `tags: List[str]`  
  Arbitrary tags for categorizing or filtering test cases.

- `priority: str`  
  Priority level of the test case (e.g., Low, Medium, High). Default: `"Medium"`.

- `test_type: str`  
  Type/category of the test (Functional, Integration, E2E, API, Security, Performance, UI, Regression, Smoke, etc.). Default: `"Functional"`.

- `is_regression: bool`  
  Flag indicating if this test case verifies regression functionality. Default: `False`.

- `boundary_conditions: List[str]`  
  List of boundary conditions or edge cases covered.

- `side_effects: List[str]`  
  Possible side effects resulting from test execution.

- `created_at: datetime`  
  Timestamp when the test case was created.

- `updated_at: datetime`  
  Timestamp when the test case was last updated.

- `version: int`  
  Version number of the test case. Default: `1`.

- `source_document: Optional[str]`  
  Optional reference to the originating requirements or specification document.

### Methods

- `to_text() -> str`  
  Converts the test case details into a formatted string optimized for text search or display.  
  Includes title, description, business rules, pre/postconditions, test steps (with step number, action, expected result), expected outcome, boundary conditions, side effects, and tags.

---

## Model: `ComparisonResult`

Represents the result of comparing two test cases.

### Attributes

- `new_test_case_id: str`  
  Identifier of the new or incoming test case.

- `existing_test_case_id: Optional[str]`  
  Identifier of the existing test case matched against, if any.

- `similarity_score: float`  
  Numeric score representing similarity between test cases (scale typically 0 to 1).

- `decision: DecisionType`  
  Final decision about test case relation (same, add-on, new).

- `reasoning: str`  
  Explanation or rationale behind the decision.

- `business_rule_match: bool`  
  Indicates whether business rules matched between test cases.

- `behavior_match: bool`  
  Indicates whether behavioral aspects matched between test cases.

- `coverage_expansion: List[str]`  
  List of coverage areas expanded or enhanced by the new test case.

- `confidence_score: float`  
  Confidence level of the comparison decision.

- `timestamp: datetime`  
  When the comparison was performed.

---

## Model: `TestSuite`

Represents a collection or grouping of test cases.

### Attributes

- `name: str`  
  Name of the test suite.

- `description: str`  
  Description or purpose of the test suite.

- `test_cases: List[TestCase]`  
  List of included test cases. Defaults to empty list.

- `created_at: datetime`  
  Timestamp when the test suite was created.

- `updated_at: datetime`  
  Timestamp when the test suite was last updated.

- `version: int`  
  Version number of the test suite. Default: `1`.

### Methods

- `add_test_case(test_case: TestCase)`  
  Adds a new test case to the suite and updates `updated_at` timestamp.

- `get_test_case_by_id(test_case_id: str) -> Optional[TestCase]`  
  Retrieves a test case by its identifier. Returns `None` if not found.

- `update_test_case(test_case: TestCase)`  
  Updates an existing test case in the suite by matching the ID.  
  Increments the test case version and updates its `updated_at` timestamp. Also updates suite's `updated_at`.

---

## Model: `UserStory`

Represents a user story or requirement document linked to test cases.

### Attributes

- `id: str`  
  Unique identifier for the user story.

- `title: str`  
  Short descriptive title.

- `description: str`  
  Detailed description of the user story or requirement.

- `acceptance_criteria: List[str]`  
  List of acceptance criteria to satisfy for the story.

- `business_rules: List[str]`  
  Business rules associated with this user story.

- `context: Optional[str]`  
  Optional contextual information or background.

- `created_at: datetime`  
  Timestamp when the user story was created.

---

# Summary

These models enable structured representation, manipulation, and comparison of test cases, supporting organized software testing processes. They also assist in linking test artifacts to requirements and managing test suites. The use of Pydantic facilitates data validation and serialization for APIs or storage.

## File: core/utils.py
# Utility Functions for Test Case Management System

This module provides a set of utility functions designed to assist with the management,
validation, import/export, and formatting of test cases and test steps within a test case management system.

---

## Table of Contents

- [ID Generation](#id-generation)
- [Test Distribution Calculation](#test-distribution-calculation)
- [Test Type Validation](#test-type-validation)
- [Numbering Handling in Steps](#numbering-handling-in-steps)
- [JSON File Handling](#json-file-handling)
- [Export Functions](#export-functions)
- [Import Functions](#import-functions)
- [Test Case Parsing](#test-case-parsing)
- [Text Similarity and Timestamp](#text-similarity-and-timestamp)

---

## ID Generation

```python
def generate_id(text: str) -> str
```

Generate a unique 12-character ID hash from a given text string.

- **Args**:
  - `text`: Input string to hash.

- **Returns**:
  - A 12-character hexadecimal string derived from MD5 hash of the input text.

---

## Test Distribution Calculation

```python
def calculate_test_distribution(num_test_cases: int) -> Dict[str, Any]
```

Calculate the distribution of different test case types based on configured minimum percentages and total count.

- **Args**:
  - `num_test_cases`: Total number of test cases to generate.

- **Returns**:
  - A dictionary containing the count of each test type (`positive`, `negative`, `ui`, `security`, `edge_case`),
    total count, and a formatted multi-line string summarizing the distribution.

- **Details**:
  - The function reads configured minimum percentage constants from `Config` and ensures at least one test case
    per category.
  - Positive cases take up the remainder of the total count after deducting the minimums of other categories.
  - If the sum exceeds total, positive test cases are adjusted down.

---

## Test Type Validation

```python
def validate_test_type(test_type: str) -> str
```

Validate and normalize a given test type string.

- **Args**:
  - `test_type`: The input test type string.

- **Returns**:
  - Normalized test type string, stripped of whitespace.
  - Defaults to `"Functional"` if the input is empty or only whitespace.

- **Supported Types**:
  - Functional, Integration, E2E, API, Security, Performance,
    UI, Regression, Smoke, Unit, System, Acceptance, etc.

---

## Numbering Handling in Steps

### Check for numbering

```python
def has_existing_numbering(text: str) -> bool
```

Detect if a given text starts with numbering patterns typical in test step descriptions.

- **Args**:
  - `text`: Input string to check.

- **Returns**:
  - `True` if the text starts with numbering (e.g., "1.", "Step 2:", "3-", etc.), else `False`.

### Remove numbering

```python
def remove_existing_numbering(text: str) -> str
```

Remove existing numbering prefixes from a step text.

- **Args**:
  - `text`: Step description potentially containing numbering.

- **Returns**:
  - The input string after stripping all detected numbering prefixes (supports multiple levels).
  
- **Note**: Limits iterations to 5 to avoid infinite loops.

### Format step with numbering

```python
def format_step_with_number(number: int, text: str, preserve_existing: bool = True) -> str
```

Format a test step with a given step number, optionally preserving existing numbering.

- **Args**:
  - `number`: Step number to apply.
  - `text`: Step text.
  - `preserve_existing`: If `True`, returns the original text if it already has numbering.
    Otherwise, removes existing numbering and applies a standard `"N. text"` format.
  
- **Returns**:
  - Formatted step text including the numbering.

---

## JSON File Handling

### Load JSON

```python
def load_json(file_path: str) -> Dict[str, Any]
```

Load a JSON file from an absolute or relative path.

- **Args**:
  - `file_path`: Path or filename of the JSON file.

- **Behavior**:
  - If the `file_path` is just a filename without path, looks inside the `config` folder of the project root.

- **Returns**:
  - Parsed JSON content as Python dictionary or list.

### Save JSON

```python
def save_json(data: Any, file_path: str)
```

Write data to a JSON file with human-readable formatting.

- **Args**:
  - `data`: Python object to serialize to JSON.
  - `file_path`: Path where the JSON file will be saved.

---

## Export Functions

### Export to Excel (standard format)

```python
def export_to_excel(test_cases: List[TestCase], output_path: str)
```

Export a list of test cases to an Excel file.

- **Args**:
  - `test_cases`: List of `TestCase` model instances.
  - `output_path`: File path to save the Excel file.

- **Format**:
  - Combines all test steps into single cell per test case using numbering and "action -> expected result" format.
  - Includes fields like ID, Title, Description, Business Rule, Preconditions, Tags, Priority, Test Type, etc.
  - Uses `openpyxl` engine for Excel writing.

### Export Results to Excel with Sheets

```python
def export_results_to_excel_with_sheets(results: Dict[str, Any], output_path: str)
```

Export test case results with decisions into multiple Excel sheets.

- **Args**:
  - `results`: Dictionary containing test case results including decision types and comparison data.
  - `output_path`: Excel file output path.

- **Sheets**:
  - **All Test Cases:** All test cases with detailed fields and comparison metrics.
  - **Modified:** Test cases marked as ADDON (modifications).
  - **New:** Test cases marked as NEW (new additions).

- **Additional Features**:
  - Adjusts columns' widths for readability.
  - Includes decision, similarity, confidence, reasoning, and coverage expansion fields where applicable.

### Export to Excel (User Format)

```python
def export_test_cases_user_format(test_cases: List[TestCase], output_path: str)
```

Export test cases to Excel adhering to end user preferred format.

- **Args**:
  - `test_cases`: List of `TestCase` instances.
  - `output_path`: Excel file path.

- **Format**:
  - Columns: Test Case ID, Layer, Test Case Scenario, Test Case, Pre-Condition,
    Test Case Type, Test Steps, Expected Result, Priority.
  - Test steps and expected results are multi-line strings with numbered steps.
  - Text wrapping enabled.
  - Custom widths set for better readability.

### Export to CSV

```python
def export_to_csv(test_cases: List[TestCase], output_path: str)
```

Export test cases to CSV format.

- **Args**:
  - `test_cases`: List of `TestCase` instances.
  - `output_path`: File path for CSV.

- **Details**:
  - Test steps and pre/post-conditions are joined with `" | "` separator.
  - Suitable for data import/export where Excel is not required.

---

## Import Functions

### Import from Excel

```python
def import_from_excel(file_path: str) -> List[TestCase]
```

Import test cases from an Excel file supporting multiple column naming conventions.

- **Args**:
  - `file_path`: Path to the Excel file.

- **Returns**:
  - List of parsed `TestCase` instances.

- **Features**:
  - Supports standard columns (`Title`, `Description`, `Test Steps`, `Expected Outcome`, `Priority`, etc.)
    and user/custom formats (`Test Case ID`, `Layer`, `Test Case Scenario`, etc.).
  - Parses test steps from multiline cells splitting on lines and "action -> expected_result" format.
  - Automatically generates IDs if missing.
  - Parses lists of tags/preconditions/postconditions from comma-separated strings.
  - Infers `is_regression` flag based on explicit column or priority.
  - Handles missing or invalid rows gracefully with warnings.

---

### Import from JSON

```python
def import_from_json(file_path: str) -> List[TestCase]
```

Import test cases from a JSON file.

- **Args**:
  - `file_path`: Path to JSON file containing test cases.

- **Returns**:
  - List of `TestCase` parsed objects.

- **Supported JSON Formats**:
  - Array of test case objects.
  - Object with `test_cases` or `testCases` field containing an array.
  - Single test case object.

- **Error Handling**:
  - Skips and logs warnings for invalid cases.

---

## Test Case Parsing

```python
def parse_test_case_json(json_data: Dict[str, Any]) -> TestCase
```

Parse JSON dictionary into a `TestCase` model instance.

- **Args**:
  - `json_data`: Dictionary representing a single test case.

- **Returns**:
  - `TestCase` instance.

- **Details**:
  - Converts test steps from string or dict formats, removing unwanted numbering.
  - Generates ID if missing (hashing title + description).
  - Parses lists (tags, preconditions, side effects) from various formats.
  - Validates and sets test type, defaults to 'Functional'.
  - Handles missing descriptions by fallback text.
  - Ensures expected outcome is string, formats dicts accordingly.
  - Infers regression flag from priority.

---

## Text Similarity and Timestamp

### Calculate Text Similarity

```python
def calculate_text_similarity(text1: str, text2: str) -> float
```

Compute a fallback simple similarity score between two texts using Jaccard similarity on words.

- **Args**:
  - `text1`: First text string.
  - `text2`: Second text string.

- **Returns**:
  - Similarity score as a float between 0.0 (no similarity) and 1.0 (identical).

---

### Format Timestamp

```python
def format_timestamp(dt: datetime) -> str
```

Format a `datetime` object into a string `"YYYY-MM-DD HH:MM:SS"`.

- **Args**:
  - `dt`: A `datetime` object.

- **Returns**:
  - Formatted datetime string.

---

# Summary

This module consolidates essential operations for working with test cases: it facilitates import/export in multiple formats, handles step formatting and numbering, validates and normalizes test types, processes JSON files, calculates distributions, and prepares data for reporting and analysis workflows within the test case management environment.

## File: create_regression_suite.py
# Documentation: Regression Test Suite Creation Script

## Overview

This script automates the creation and export of a regression test suite by interacting with an API server. It performs the following core functions:

- Waits for the API server to become available.
- Retrieves existing test cases and verifies regression-marked tests.
- Exports high-priority regression test cases in Excel format.
- Exports all regression test cases regardless of priority, also in Excel format.
- Summarizes regression test cases by priority and test type.
- Provides guidance on next steps for test suite management.

---

## Usage

### Prerequisites

- Ensure the API server is running locally on `http://localhost:8000`.
- Run this script **after** starting the API server.
- Python 3 with `requests` library installed (`pip install requests`).

### Running the Script

```bash
python create_regression_suite.py
```

The script prints progress updates to stdout, exports Excel files with the regression test suites, and provides a summary with guidance at the end.

---

## Script Structure and Functionality

### Constants

- `API_BASE`  
  Base URL of the API server. Default: `http://localhost:8000`.

### Functions

#### `wait_for_api() -> bool`

Waits up to 30 seconds for the API server to respond to a health check.

- Sends GET requests to `http://localhost:8000/health`.
- Retries every second until success or timeout.
- Returns `True` if the API responds with HTTP 200 status.
- Returns `False` if the API does not respond within 30 seconds.

#### `create_regression_suite()`

Main function that orchestrates the creation/export of the regression test suite by performing multiple steps:

1. **Check API availability**  
   Calls `wait_for_api()`. If unavailable, instructs user to start API and exits.

2. **Check existing test cases**  
   Sends GET request to `/test-cases` endpoint for the default suite.  
   - Counts total test cases and those marked as regression (`is_regression` field).  
   - If no regression tests found, advises to generate new test cases which the AI will mark as critical regression tests.

3. **Export high-priority regression tests**  
   Sends POST request to `/export/filtered-test-suite` with filter:  
   - Suite: `default`  
   - Format: `excel`  
   - Priorities: `High` and `Critical`  
   - `is_regression: True`  
   Saves response content as `regression_suite_high_critical.xlsx`.

4. **Export all regression tests of any priority**  
   Sends POST request to `/export/filtered-test-suite` with filter:  
   - Suite: `default`  
   - Format: `excel`  
   - `is_regression: True`  
   Saves response content as `regression_suite_all.xlsx`.

5. **Summary of regression tests**  
   Requests filtered test cases with `is_regression=True`.  
   Prints:  
   - Total count of regression tests.  
   - Counts broken down by priority levels: Critical, High, Medium, Low.  
   - Counts by test type.

6. **Next steps and guidance**  
   Informs the user to review exported files, import into test management tools, and integrate into CI/CD pipelines.  
   References additional documentation `HOW_TO_CREATE_REGRESSION_SUITE.md` for detailed instructions.

---

## API Endpoints Utilized

- `GET /health`  
  Health check endpoint to verify API server availability.

- `GET /test-cases`  
  Retrieves test cases from a test suite, filtered by query parameters (e.g., `suite_name`).

- `GET /test-cases/filtered`  
  Retrieves filtered test cases, supporting filters like `is_regression`.

- `POST /export/filtered-test-suite`  
  Requests export of filtered test suites.  
  Request JSON includes:  
  - `suite_name`: string  
  - `format`: string (e.g., `"excel"`)  
  - `priorities`: optional list of priority strings (e.g., `["High", "Critical"]`)  
  - `is_regression`: optional boolean to filter regression tests

---

## Output Files

- `regression_suite_high_critical.xlsx`  
  Excel file containing high and critical priority regression tests.

- `regression_suite_all.xlsx`  
  Excel file containing all regression tests regardless of priority.

---

## Error Handling

- If the API is not available within the timeout period, the script prints a helpful message and aborts.
- Network or API errors during GET or POST requests are caught and printed.
- Non-200 HTTP responses are reported with status code and truncated response text.
- Warnings are displayed if no regression tests match the filter (potentially empty exports).

---

## Summary of Console Messages

- Status emojis and descriptive texts indicate progress (e.g., ⏳ Waiting, ✅ Success, ❌ Failure, ⚠️ Warnings).
- Steps are clearly marked with headings and separators.
- Detailed counts and configurations are shown before exports.
- Summary includes counts broken down by priority and type.
- Next steps guide the user towards integrating the outputs.

---

## Extensibility

- The script is easily adaptable to different API base URLs by modifying `API_BASE`.
- Export filters and formats can be adjusted in the export request payload.
- Additional steps can be added following the provided structure.
- Integration with CI/CD pipelines can be automated by embedding this script in build or test stages.

---

## Conclusion

This script streamlines the workflow for managing regression test suites via an API. It automates verification, export, and reporting of regression test cases, enabling teams to easily generate up-to-date regression suites for continuous testing and quality assurance.

For further customization and detailed instructions, please refer to the accompanying `HOW_TO_CREATE_REGRESSION_SUITE.md` document.

## File: engines/__init__.py
# AI Engines Module

This module provides a collection of AI engine components designed to support various tasks such as retrieval-augmented generation (RAG), embeddings generation, comparison operations, test case generation, test case management, and context engineering. Each component is implemented as a separate class, which can be imported individually or collectively from this module.

## Available Components

- **RAGEngine**  
  Implements Retrieval-Augmented Generation functionality, facilitating AI models that combine retrieval mechanisms with generative capabilities to improve response relevance and accuracy.

- **EmbeddingGenerator**  
  Responsible for generating embeddings from input data. These embeddings are often used for semantic search, similarity comparison, clustering, and other downstream AI tasks.

- **ComparisonEngine**  
  Provides tools to perform comparison operations between data representations, such as embedding similarity matching or difference analysis.

- **TestCaseGenerator**  
  Automates the creation of test cases based on input specifications or previous outputs, aiding in efficient and scalable testing workflows.

- **TestCaseManager**  
  Manages and organizes test cases, including storage, retrieval, and lifecycle operations, to support continuous testing and validation.

- **ContextEngineer**  
  Offers functionality to engineer and manipulate context data for AI processes, enhancing context awareness and relevance in AI-driven tasks.

## Usage

You can import individual components as needed:

```python
from ai_engines import RAGEngine, EmbeddingGenerator
```

Alternatively, import all provided engines:

```python
from ai_engines import *
```

## Module Structure

```
ai_engines/
├── rag_engine.py           # Contains RAGEngine class
├── embeddings.py           # Contains EmbeddingGenerator class
├── comparison_engine.py    # Contains ComparisonEngine class
├── test_case_generator.py  # Contains TestCaseGenerator class
├── test_case_manager.py    # Contains TestCaseManager class
└── context_engineering.py  # Contains ContextEngineer class
```

Each submodule encapsulates the implementation details of its respective engine, promoting modularity and maintainability.

## Summary

This module consolidates core AI engine functionalities to provide a coherent toolkit for building comprehensive AI solutions involving generation, embedding, comparison, and evaluation workflows.

## File: engines/comparison_engine.py
# ComparisonEngine Documentation

## Overview

The `ComparisonEngine` class provides functionality to compare two test cases and determine their relationship using a combination of semantic similarity and advanced context engineering through Large Language Models (LLMs). It integrates embedding-based similarity computations with deep contextual analysis to make robust decisions about test case equivalences, expansions, or novelty.

---

## Class: `ComparisonEngine`

### Description:
Compares test cases to determine relationships (e.g., identical, expanded, new) by leveraging a hybrid approach combining embeddings similarity and LLM-based context engineering.

### Constructor:
```python
ComparisonEngine(use_context_engineering: bool = True)
```
- **use_context_engineering** (`bool`, optional): Enable or disable the use of advanced context engineering techniques with LLMs. Default is `True`.

### Attributes:
- `client`: Azure OpenAI client instance for accessing LLM services.
- `deployment`: Azure OpenAI deployment name used for the model.
- `embedding_generator`: Instance of `EmbeddingGenerator` for producing embeddings and similarity calculations.
- `prompts`: Loaded prompt templates for interaction with LLM.
- `use_context_engineering`: Flag indicating if context engineering is enabled.
- `context_engineer`: Instance of `ContextEngineer` (initialized only if `use_context_engineering` is `True`).

---

## Methods

### `compare_test_cases(new_test_case: TestCase, existing_test_case: TestCase, historical_decisions: Optional[List[Dict]] = None) -> ComparisonResult`

Compare two test cases using a hybrid approach combining semantic similarity, LLM deep analysis, and context engineering.

- **Parameters:**
  - `new_test_case` (`TestCase`): The new test case to evaluate.
  - `existing_test_case` (`TestCase`): Existing test case from the knowledge base.
  - `historical_decisions` (`List[Dict]`, optional): Past decisions data that can assist the analysis.

- **Returns:**
  - `ComparisonResult`: Contains IDs of test cases, similarity scores, final decision, reasoning, matches on business rule and behavior, coverage expansions, and confidence score.

- **Process:**
  1. Calculate semantic similarity using embeddings.
  2. Obtain deep contextual analysis from LLM with optional context engineering.
  3. Compute LLM similarity score based on analysis.
  4. Weight and combine semantic and LLM similarities into a hybrid similarity score.
  5. Make a decision (`SAME`, `ADDON`, `NEW`) based on hybrid score and analysis.
  6. Generate human-readable reasoning for the decision.
  7. Calculate confidence score based on multiple factors.

---

### `_analyze_with_llm(new_test_case: TestCase, existing_test_case: TestCase, historical_decisions: Optional[List[Dict]] = None) -> Dict[str, Any]`

Use the configured LLM (Azure OpenAI) to analyze the relationship between two test cases with optional context engineering enhancements.

- **Parameters:**
  - `new_test_case` (`TestCase`): New test case to analyze.
  - `existing_test_case` (`TestCase`): Existing test case for comparison.
  - `historical_decisions` (`List[Dict]`, optional): Historical decisions used for augmenting context.

- **Returns:**
  - `Dict[str, Any]`: Dictionary containing analysis results including keys like:
    - `"business_rule_match"` (`bool`): Whether business rules match.
    - `"behavior_match"` (`bool`): Whether behavior matches.
    - `"coverage_expansion"` (`List[str]`): List of coverage expansion elements.
    - `"relationship"` (`str`): Relationship category (`identical`, `expanded`, `similar`, `related`, `different`).
    - `"reasoning"` (`str`): Textual explanation of the relationship.

- **Details:**  
  - If context engineering is enabled, it enhances prompts dynamically with semantic similarity and historical data.
  - Extracts and parses JSON output from LLM's response robustly.
  - Handles JSON parsing errors gracefully and falls back to a default analysis structure.
  - Catches exceptions and provides a default fallback analysis.

---

### `_calculate_llm_similarity(analysis: Dict[str, Any]) -> float`

Convert LLM analysis outcomes into a numerical similarity score ranging from 0.0 to 1.0.

- **Parameters:**
  - `analysis` (`Dict[str, Any]`): Output dictionary from `_analyze_with_llm`.

- **Returns:**
  - `float`: Similarity score representing semantic understanding from LLM.

- **Scoring Logic:**
  Maps relationship types to base scores:
  - `identical`: 1.0
  - `expanded`: 0.75
  - `similar`: 0.60
  - `related`: 0.45
  - `different`: 0.20  
  Adds incremental boosts for matching business rule (+0.15) and behavior (+0.10), capped at 1.0.

---

### `_make_decision(hybrid_similarity: float, semantic_similarity: float, analysis: Dict[str, Any]) -> DecisionType`

Determines the final decision on test case relationship based on similarity scores and analysis.

- **Parameters:**
  - `hybrid_similarity` (`float`): Weighted similarity score combining semantic and LLM results.
  - `semantic_similarity` (`float`): Embedding-only semantic similarity.
  - `analysis` (`Dict[str, Any]`): LLM analysis results.

- **Returns:**
  - `DecisionType`: Enumeration indicating the relationship:
    - `SAME`: Tests are effectively equivalent.
    - `ADDON`: New test expands or adds coverage to existing.
    - `NEW`: Test case is new/different.

- **Decision Criteria:**
  - `SAME`: High hybrid and semantic similarity with matching business rules, behaviors, and an “identical” relationship.
  - `ADDON`: Medium-high hybrid similarity with business rules matched and expanded coverage or “expanded” relationship.
  - `NEW`: Default if similarities are low or business rules differ.

---

### `_generate_reasoning(decision: DecisionType, hybrid_similarity: float, semantic_similarity: float, llm_similarity: float, analysis: Dict[str, Any]) -> str`

Generates a human-readable text explaining why a decision was made.

- **Parameters:**
  - `decision` (`DecisionType`): The determined decision.
  - `hybrid_similarity` (`float`): Combined similarity score.
  - `semantic_similarity` (`float`): Embedding similarity.
  - `llm_similarity` (`float`): LLM-based similarity score.
  - `analysis` (`Dict[str, Any]`): LLM analysis details.

- **Returns:**
  - `str`: Explanation text generated by the LLM. Falls back to a basic explanation if the LLM call fails.

---

### `_calculate_confidence(hybrid_similarity: float, semantic_similarity: float, llm_similarity: float, analysis: Dict[str, Any]) -> float`

Computes a confidence score (0 to 1) reflecting the certainty of the decision.

- **Parameters:**
  - `hybrid_similarity` (`float`): Overall combined similarity.
  - `semantic_similarity` (`float`): Embedding-only similarity.
  - `llm_similarity` (`float`): LLM semantic similarity.
  - `analysis` (`Dict[str, Any]`): Deep analysis results.

- **Returns:**
  - `float`: Confidence value, capped at 1.0.

- **Confidence Calculation:**
  - Base confidence = hybrid similarity.
  - Added bonus if semantic and LLM scores agree closely (up to +0.1).
  - Additional increments if business rule and behavior matches are present.

---

## External Dependencies

- `AzureOpenAI` — Client for Azure OpenAI API usage.
- `Config` — Module holding configuration constants such as API keys, deployment names, and thresholds.
- `EmbeddingGenerator` — Generates vector embeddings and calculates similarity.
- `ContextEngineer` — Enhances prompts with domain-specific context information.
- `TestCase`, `ComparisonResult`, `DecisionType` — Core data models for test cases, comparison output, and decision enumerations.
- `load_json` — Utility to load prompt templates JSON.

---

## Summary

The `ComparisonEngine` class provides a highly adaptive mechanism to assess the similarity and relationship between software test cases. By marrying embedding-based semantic similarity with LLM-powered reasoning and domain-specific context engineering, it supports nuanced decisions about test case equivalencies, additions, or newness that can improve test management and reduce redundancy.

## File: engines/context_engineering.py
# ContextEngineer Module Documentation

## Overview
The **ContextEngineer** module provides advanced context engineering techniques designed to enhance Retrieval-Augmented Generation (RAG) based test case creation, comparison, and merging. It leverages sophisticated prompting strategies such as few-shot learning, chain-of-thought prompting, dynamic example selection, and role-based conventions to produce high-quality, comprehensive test cases and optimize test suites.

---

## Module Contents

### Class: ContextEngineer

#### Description
Advanced context engineering for RAG-based test case management. Implements techniques including:
- Few-shot learning (providing example test cases)
- Chain-of-thought prompting (stepwise analytic guidance)
- Context augmentation (domain, technical, and quality contexts)
- Dynamic example selection (based on requirement matching)
- Role-based prompting (expert QA engineer persona)

---

### Initialization

```python
ContextEngineer()
```

- **Purpose**: Initialize the engineer with predefined few-shot examples and context templates.
- **Details**:
  - Loads categorized example test cases for CRUD operations, API integrations, and complex workflows.
  - Loads templates for domain, technical, and quality contexts.

---

### Methods

#### `_load_examples() -> Dict[str, Dict[str, Any]]`
- Loads a dictionary containing sample test cases grouped by scenario types: `simple_crud`, `api_integration`, `complex_workflow`.
- Each example includes rich data such as requirement description, detailed preconditions, test steps, expected outcomes, boundary conditions, and side effects.
- Used for few-shot learning to guide prompt enhancement.

#### `_load_context_templates() -> Dict[str, str]`
- Returns string templates for different context categories:
  - Domain (industry, application type, user roles, compliance, integrations)
  - Technical (tech stack, architecture, databases, APIs, security)
  - Quality (test coverage goals, priority areas, risk, performance, accessibility)

---

#### `enhance_generation_prompt(...) -> Dict[str, str]`
Enhances a test case generation prompt with contextual and instructive information to improve the quality and relevance of generated test cases.

- **Arguments**:
  - `requirement` (str): Raw requirement description text.
  - `requirement_type` (str, default `"user_story"`): Type of requirement, e.g., user_story, brs, api.
  - `domain_context` (Optional[Dict[str, Any]]): Domain-specific background information.
  - `similar_examples` (Optional[List[TestCase]]): Similar test cases for few-shot learning.
  - `focus_areas` (Optional[List[str]]): Highlights focus areas such as security or performance.
  - `num_test_cases` (int, default 12): Number of test cases to be generated.
  - `test_distribution` (str): Instructions on test case type distribution.

- **Returns**:
  - Dictionary with keys `"system"` and `"user"` containing respective prompt strings for LLM input.

- **Key Features**:
  - Chain-of-thought reasoning steps (analyze, identify scenarios, learn, focus, generate).
  - Injection of domain context.
  - Inclusion of few-shot example test cases matched by requirement type.
  - Strict output format instructions and test case schema enforcement.
  - Detailed rules to ensure test case structure, tagging, and prioritization are consistent and actionable.

---

#### `enhance_comparison_prompt(...) -> Dict[str, str]`
Generates a prompt for analyzing and comparing two test cases to decide their relationship (identical, expanded, or different).

- **Arguments**:
  - `new_test_case` (TestCase): The new test case being considered.
  - `existing_test_case` (TestCase): The reference test case from the knowledge base.
  - `similarity_score` (float): Semantic similarity score between the two test cases embeddings (0 to 1).
  - `historical_decisions` (Optional[List[Dict]]): Past decisions on similar comparisons to provide context.

- **Returns**:
  - Dictionary with `"system"` and `"user"` prompts guiding a detailed chain-of-thought analysis including semantic similarity, business rule matching, behavior comparison, coverage analysis, and final relationship determination.
  - Output mandates JSON format answer with explicit fields for business rule and behavior matches, coverage expansions, relationship type, and detailed reasoning.

---

#### `enhance_merge_prompt(...) -> Dict[str, str]`
Generates a prompt for merging two similar test cases intelligently, ensuring coverage is maintained or expanded without redundancy.

- **Arguments**:
  - `existing_test_case` (TestCase): Base test case to merge into.
  - `new_test_case` (TestCase): New test case providing additional coverage.
  - `coverage_expansion` (List[str]): List of unique coverage areas identified during comparison.

- **Returns**:
  - Dictionary containing prompts that:
    - Direct the merging of business rules, preconditions, and test steps with parameterization considerations.
    - Suggest integration of new coverage items as additional steps or boundary conditions.
    - Handle metadata updates such as versioning, tags, and priority.
    - Request a merged test case JSON output preserving all key details without information loss.

---

#### `_match_requirement_to_example(requirement: str) -> str`
Internal function that heuristically matches a free-text requirement to an example category for few-shot learning.

- Checks keywords related to APIs, workflows, or defaults to CRUD.
- Returns one of: `"api_integration"`, `"complex_workflow"`, `"simple_crud"`.

---

#### `extract_domain_context(existing_test_cases: List[TestCase]) -> Dict[str, Any]`

Analyzes a collection of existing test cases to extract domain-level context useful for prompt enhancement.

- **Parameters**:
  - `existing_test_cases`: List of test cases to analyze.
  
- **Returns**:
  - Dictionary summarizing:
    - Most common tags (top 5)
    - Primary test types (top 3)
    - Total test case count
    - Average number of test steps per test case
    - Count of high priority test cases
    
- **Purpose**:
  - To feed relevant domain knowledge back into the prompt to improve generation relevance.

---

#### `get_focus_areas(requirement: str) -> List[str]`
Identifies key focus areas for testing based on keyword analysis in the requirement text.

- **Parameters**:
  - `requirement`: Requirement description string.
  
- **Returns**:
  - List of suggested focus areas such as:
    - Security testing
    - Performance testing
    - Data integrity
    - Integration testing
    - UI/UX testing
    - Error handling
    
- Defaults to `"Comprehensive functional testing"` if no keywords match.

---

## Supporting Types

- **TestCase**: Data model for test cases imported from `core.models`.
- **UserStory**: (Imported but not used directly in shown code).
- **Config**: (Imported, presumably for configuration, but unused in this module).

---

## Usage Suggestions

- Instantiate `ContextEngineer` to access advanced prompt building capabilities for test case tasks.
- Use `enhance_generation_prompt()` to create well-structured, context-rich prompts driving quality test case generation.
- Use `enhance_comparison_prompt()` to audit test case duplicates and optimize suites.
- Use `enhance_merge_prompt()` to intelligently consolidate overlapping test cases ensuring full coverage without redundancy.
- Leverage `extract_domain_context()` and `get_focus_areas()` to prepare rich contextual inputs automatically from past test cases or requirements.

---

## Notes

- The module enforces strict quality and formatting rules for test cases to standardize output for automated processing.
- The heavy use of chain-of-thought prompting helps LLMs reason stepwise, providing explainable and maintainable outputs.
- The embedded few-shot examples and dynamic example selection ensure that generation is relevant to the domain and requirement style.
- This module is designed to function within a Retrieval-Augmented Generation (RAG) architecture to maximize reuse of knowledge base content.

---

# End of Documentation

## File: engines/embeddings.py
# EmbeddingGenerator

A class to generate embeddings for test case texts using Azure OpenAI embeddings API. It supports both single and batch embedding generation with local caching to reduce redundant API calls, and provides a method to compute similarity between embeddings.

---

## Overview

The `EmbeddingGenerator` class leverages the Azure OpenAI API to create vector embeddings from input text data. It includes:

- Initialization of Azure OpenAI client using configurations.
- Single text embedding generation with caching.
- Batch embedding generation with caching and batching to handle rate limits.
- Cosine similarity calculation between embeddings.
- Cache management.

---

## Dependencies

- `openai.AzureOpenAI`: Azure OpenAI client for embeddings generation.
- `config.config.Config`: Configuration module containing Azure credentials and deployment details.
- `numpy`: For similarity calculations.
- `hashlib`: Used to hash texts as cache keys.
- Standard libraries including `os`, `sys`, `typing`.

---

## Class: `EmbeddingGenerator`

### `__init__(self)`

Initializes the embedding generator with Azure OpenAI API client and necessary configuration.

- Sets up client with API key, endpoint, and version.
- Reads the embedding deployment/model name from config.
- Initializes an in-memory cache dictionary.

---

### `generate_embedding(self, text: str) -> List[float]`

Generate an embedding vector for a single input text.

#### Parameters

- `text` (`str`): The input text to embed.

#### Returns

- `List[float]`: The embedding vector representing the input text.

#### Behavior

- Generates a hash key of the input text for caching (handles long texts).
- Checks if the embedding is cached, returns from cache if found.
- Otherwise, calls Azure OpenAI's embeddings endpoint (truncates input to 8000 characters to comply with token limits).
- Stores and returns the generated embedding.
- Raises exceptions on API call failures (after printing an error message).

---

### `generate_embeddings_batch(self, texts: List[str]) -> List[List[float]]`

Generate embeddings for multiple texts in batches.

#### Parameters

- `texts` (`List[str]`): List of input texts to embed.

#### Returns

- `List[List[float]]`: List of embedding vectors corresponding to each input text.

#### Behavior

- Processes the inputs in batches of size 16 to prevent rate limits.
- Checks which texts are already cached and only sends uncached texts to the API.
- Updates the cache with newly generated embeddings.
- Returns embeddings for all input texts in original order (using cache and newly generated embeddings).
- Raises exceptions on API call failures.

---

### `calculate_similarity(self, embedding1: List[float], embedding2: List[float]) -> float`

Computes cosine similarity between two embedding vectors.

#### Parameters

- `embedding1` (`List[float]`): First embedding vector.
- `embedding2` (`List[float]`): Second embedding vector.

#### Returns

- `float`: Similarity score between 0 and 1 (normalized cosine similarity).

#### Details

- Uses numpy to compute dot product and norms.
- If either embedding is a zero vector, returns 0.0.
- Cosine similarity originally ranges from -1 to 1; this method normalizes it to 0 to 1 by: `(similarity + 1) / 2`.

---

### `clear_cache(self)`

Clears the in-memory embedding cache.

Useful to free memory or reset cached embeddings when needed.

---

## Usage Example

```python
from embedding_generator import EmbeddingGenerator

generator = EmbeddingGenerator()

# Generate embedding for one text
embedding = generator.generate_embedding("Example test case text")

# Generate embeddings in batch
texts = ["Test case 1", "Test case 2"]
embeddings = generator.generate_embeddings_batch(texts)

# Calculate similarity between two embeddings
similarity = generator.calculate_similarity(embeddings[0], embeddings[1])

# Clear cache when done or to reset
generator.clear_cache()
```

---

## Notes

- Input text is truncated at 8000 characters during embedding generation to respect token limits enforced by Azure OpenAI.
- Cache keys for single texts use MD5 hash of the text, but batch caching uses the raw text as key; this could be inconsistent if texts are very long or numerous.
- Error handling prints error message and re-raises exceptions on API failure.
- Cache is stored in-process and is lost when the instance or program terminates.

---

This class provides a convenient interface to generate and manage embeddings for test case-related texts, improving efficiency with caching and batch processing, while integrating seamlessly with Azure OpenAI services.

## File: engines/rag_engine.py
# RAGEngine Documentation

## Overview

`RAGEngine` is a Retrieval-Augmented Generation engine designed for storing, managing, and retrieving test cases using a vector database backed by ChromaDB. It supports adding, updating, deleting, and searching for similar test cases based on their semantic embeddings generated from text representations.

---

## Dependencies

- **chromadb**: Vector database client library used for storing and querying embeddings.
- **core.models.TestCase**: Model representing a test case object.
- **engines.embeddings.EmbeddingGenerator**: Utility to generate vector embeddings from text.
- **config.config.Config**: Configuration values including paths and constants.

---

## Class: `RAGEngine`

### Initialization

```python
__init__(self)
```

Initializes the `RAGEngine`. Sets up the ChromaDB client with persistence enabled, retrieves or creates the collection for storing test case embeddings, and initializes an embedding generator instance.

---

### Methods

#### add_test_case

```python
add_test_case(self, test_case: TestCase) -> None
```

Adds a single test case to the knowledge base.

- Converts the `TestCase` instance to text.
- Generates an embedding vector for the text.
- Adds the embedding, text document, and associated metadata to the ChromaDB collection.

**Args:**

- `test_case` (`TestCase`): The test case to be added.

---

#### add_test_cases_batch

```python
add_test_cases_batch(self, test_cases: List[TestCase]) -> None
```

Adds multiple test cases to the knowledge base in a batch operation.

- Converts all test cases to their text representation.
- Generates embeddings for all texts in batch.
- Adds all embeddings, documents, and metadata to the collection.

**Args:**

- `test_cases` (`List[TestCase]`): List of test cases to add.

---

#### search_similar_test_cases

```python
search_similar_test_cases(self, test_case: TestCase, top_k: Optional[int] = None) -> List[Dict[str, Any]]
```

Retrieves test cases similar to the provided test case based on embedding similarity.

- Converts given test case to text and embeds it.
- Queries the collection to find nearest neighbors based on embedding similarity.
- Returns up to `top_k` most similar test cases with similarity scores.

**Args:**

- `test_case` (`TestCase`): The query test case to find similar test cases for.
- `top_k` (`Optional[int]`): Number of results to return; defaults to `Config.RAG_TOP_K` if not specified.

**Returns:**

- A list of dictionaries with keys:

  - `id`: Test case ID.
  - `document`: Text representation of the test case.
  - `metadata`: Metadata dictionary for the test case.
  - `similarity`: Similarity score (float between 0 and 1).

---

#### get_test_case_by_id

```python
get_test_case_by_id(self, test_case_id: str) -> Optional[Dict[str, Any]]
```

Retrieves a single test case by its ID.

**Args:**

- `test_case_id` (`str`): ID of the test case to retrieve.

**Returns:**

- A dictionary with keys `id`, `document`, and `metadata` if found; otherwise `None`.

---

#### update_test_case

```python
update_test_case(self, test_case: TestCase) -> None
```

Updates an existing test case by deleting the previous version and adding the updated test case.

**Args:**

- `test_case` (`TestCase`): Updated test case instance.

---

#### delete_test_case

```python
delete_test_case(self, test_case_id: str) -> None
```

Deletes a test case from the knowledge base by its ID.

**Args:**

- `test_case_id` (`str`): ID of the test case to delete.

---

#### get_all_test_cases

```python
get_all_test_cases(self) -> List[Dict[str, Any]]
```

Retrieves all test cases stored in the knowledge base.

**Returns:**

- List of dictionaries for each test case with keys `id`, `document`, and `metadata`.

---

#### count

```python
count(self) -> int
```

Returns the total number of test cases currently stored.

---

#### reset

```python
reset(self) -> None
```

Resets the knowledge base by deleting the existing collection and creating a new empty one.

---

## Example Usage

```python
from core.models import TestCase

rag_engine = RAGEngine()

# Add a test case
test_case = TestCase(id="001", title="Login Test", ...)
rag_engine.add_test_case(test_case)

# Search similar test cases
results = rag_engine.search_similar_test_cases(test_case, top_k=5)
for r in results:
    print(r["id"], r["similarity"])

# Update a test case
test_case.title = "Updated Login Test"
rag_engine.update_test_case(test_case)

# Delete a test case
rag_engine.delete_test_case("001")

# Get count
print(f"Total test cases: {rag_engine.count()}")

# Reset the knowledge base
rag_engine.reset()
```

---

## Notes

- The engine leverages semantic text embeddings for similarity search, making it effective in retrieving test cases based on meaning rather than exact keyword matches.
- The `EmbeddingGenerator` implementation details affect the quality of results.
- Persistence in ChromaDB is controlled via `Config.CHROMA_PERSIST_DIRECTORY`.
- Metadata stored includes test case properties such as version, timestamps, and tags for rich querying and filtering.

---

This documentation covers the purpose, functionality, interfaces, and usage of `RAGEngine` for managing test case knowledge bases using ChromaDB and embeddings.

## File: engines/test_case_generator.py
# TestCaseGenerator Module Documentation

This module provides a sophisticated test case generation system utilizing Azure OpenAI's language models enhanced with advanced context engineering techniques. It converts user stories or textual requirements into structured test cases using configurable generation strategies, including support for parallel batch generation and enhanced prompt engineering to ensure robust and focused outputs.

---

## Module Overview

- **Main class:** `TestCaseGenerator`  
- **Dependencies:** Azure OpenAI client, domain models (`TestCase`, `UserStory`), utilities, and context engineering module.

---

## `TestCaseGenerator` Class

Generates structured test cases from user stories or textual requirements using Azure OpenAI models with optional advanced context engineering for enhanced prompt formulation and focused generation.

### Initialization

```python
TestCaseGenerator(use_context_engineering: bool = True)
```

- **Parameters:**
  - `use_context_engineering` (bool, optional): Enables advanced prompt enhancement and context-aware generation techniques. Defaults to `True`.

- **Behavior:**
  - Initializes the AzureOpenAI client using credentials and configurations from the `Config` module.
  - Loads prompt templates from `prompts.json`.
  - Instantiates the `ContextEngineer` if context engineering is enabled.

---

### Public Methods

#### `generate_from_user_story`

```python
generate_from_user_story(user_story: UserStory, num_test_cases: Optional[int] = None) -> List[TestCase]
```

Generate test cases directly from a `UserStory` object.

- **Parameters:**
  - `user_story` (`UserStory`): The user story containing title, description, acceptance criteria, business rules, and optional context.
  - `num_test_cases` (int, optional): Specific number of test cases to generate. Defaults to system default if omitted.

- **Returns:**
  - `List[TestCase]`: Generated list of `TestCase` objects derived from the user story.

- **Details:**  
  Builds a formatted textual requirement summary from the user story fields, including optional context, then delegates to `generate_from_text`.

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

Generate test cases from free-form textual requirements with optional domain and example context.

- **Parameters:**
  - `requirement_text` (str): Text description of the requirement or user story.
  - `source_document` (str, optional): Identifier of the source document or user story ID.
  - `similar_examples` (List[`TestCase`], optional): Previously generated or related test cases to guide generation (RAG - Retrieval-Augmented Generation).
  - `domain_context` (dict, optional): Domain-specific contextual information to steer generation.
  - `num_test_cases` (int, optional): Number of test cases to generate; constrained by configured min/max.

- **Returns:**
  - `List[TestCase]`: List of generated test cases.

- **Details:**
  - Respects global configuration for number of test cases.
  - Supports parallel batch generation if enabled, falling back to single request on failure.
  - Integrates context engineering for prompt enhancement if enabled.
  - Processes and sanitizes the OpenAI response to extract valid JSON test cases.
  - Implements robust error handling and JSON repair heuristics to handle imperfect LLM output.

---

#### `extract_business_rule`

```python
extract_business_rule(test_case: TestCase) -> str
```

Extracts or infers the business rule related to a given test case using the LLM.

- **Parameters:**
  - `test_case` (`TestCase`): The test case from which to extract the business rule.

- **Returns:**
  - `str`: The extracted business rule text, or empty string if extraction fails.

- **Details:**
  - Uses dedicated prompts for business rule extraction.
  - Calls the Azure OpenAI chat completion endpoint with low temperature for consistent output.

---

#### `merge_test_cases`

```python
merge_test_cases(existing_test_case: TestCase, new_test_case: TestCase) -> TestCase
```

Merges two test cases into a single parameterized test case, enhancing maintainability and reuse.

- **Parameters:**
  - `existing_test_case` (`TestCase`): Original test case to merge into.
  - `new_test_case` (`TestCase`): New test case to integrate.

- **Returns:**
  - `TestCase`: Resulting merged test case with incremented version and combined data.

- **Details:**
  - Leverages LLM with explicit merging prompts.
  - Parses and validates output JSON to create merged test case.
  - Preserves the existing test case identifier and versions accordingly.

---

### Internal/Helper Methods

#### `_generate_single_request`

```python
_generate_single_request(
    requirement_text: str,
    source_document: Optional[str],
    similar_examples: Optional[List[TestCase]],
    domain_context: Optional[Dict[str, Any]],
    num_test_cases: Optional[int]
) -> List[TestCase]
```

Generates test cases with a single API request.

- Handles prompt construction (enhanced or basic), calls Azure OpenAI, and parses response.
- Implements extensive JSON cleaning and error recovery to handle model output inconsistencies.
- Enforces prompt structure and generation constraints.
- Includes detailed debug prints for test distribution and generation method.

---

#### `_generate_with_parallel_batches`

```python
_generate_with_parallel_batches(
    requirement_text: str,
    source_document: Optional[str],
    similar_examples: Optional[List[TestCase]],
    domain_context: Optional[Dict[str, Any]],
    num_test_cases: Optional[int]
) -> List[TestCase]
```

Generates test cases by splitting the workload into focused parallel batches to improve reliability and coverage.

- **Parallel Batches:** Positive paths, negative paths, UI, security, edge cases.
- Uses `ThreadPoolExecutor` to send concurrent generation requests.
- Collects and aggregates results, with timeout and error handling per batch.
- Summarizes successful vs failed batches.
- If all batches fail, raises an exception to trigger fallback.

---

#### `_generate_single_batch`

```python
_generate_single_batch(
    requirement_text: str,
    focus: str,
    count: str,
    description: str,
    source_document: Optional[str],
    similar_examples: Optional[List[TestCase]],
    domain_context: Optional[Dict[str, Any]]
) -> List[TestCase]
```

Internal method to generate test cases focused on a single aspect in a batch.

- Constructs an explicit prompt highlighting the focus area and count.
- Validates and fixes test case titles to avoid empty or generic titles.
- Parses and cleans JSON responses robustly.
- Returns a list of validated `TestCase` objects for the batch.

---

#### `_clean_json_content`

```python
_clean_json_content(content: str) -> str
```

Sanitizes and repairs raw JSON strings obtained from LLM responses to increase parse success rates.

- Removes inconsistencies such as trailing commas, missing commas, comments, wrong quote styles.
- Corrects Python literals (`True`, `None`, `False`) to JSON format.
- Trims extraneous markdown or text outside the JSON payload.
- Attempts to balance brackets and braces in truncated inputs.
- Removes non-printable characters and fixes common escaping errors.

---

## Configurable Constants (from `Config`)

- `AZURE_OPENAI_API_KEY`  
- `AZURE_OPENAI_API_VERSION`  
- `AZURE_OPENAI_ENDPOINT`  
- `AZURE_OPENAI_DEPLOYMENT_NAME`  
- `DEFAULT_TEST_CASES` (default number of test cases to generate)  
- `MIN_TEST_CASES`  
- `MAX_TEST_CASES`  
- `USE_PARALLEL_GENERATION` (enable parallel batch generation)  
- `PARALLEL_BATCH_SIZE` (max concurrent batches)  
- `BATCH_TIMEOUT_SECONDS` (timeout for each batch request)

---

## Usage Summary

1. Instantiate `TestCaseGenerator`, optionally disabling context engineering.
2. Use `generate_from_user_story` or `generate_from_text` to create test cases.
3. Optionally extract business rules for test cases or merge overlapping test cases.
4. Internally, the generator optimizes prompts, handles response parsing with error recovery, and supports scalable parallel generation.

---

## Error Handling and Debugging

- Extensive debug printing provides insight on:
  - Test case distribution per category
  - Prompt types used (basic vs context engineered)
  - Batch generation progress and failures
  - JSON parsing errors with attempted corrections
- Problematic JSON snippets are saved to `problematic_json.txt` for offline inspection.
- Connection and timeout errors are wrapped with actionable messages guiding credential and network checks.

---

## Summary

`TestCaseGenerator` is a robust, context-aware test automation artifact creator leveraging AI to translate software requirements into actionable test scenarios. Its design balances generation fidelity, parallelization for efficiency, and defensive programming to manage imperfect LLM outputs, making it suitable for integration in automated QA pipelines or agile development toolchains.

## File: engines/test_case_manager.py
# TestCaseManager

`TestCaseManager` is the main orchestration class responsible for managing the lifecycle of test cases from generation, analysis, comparison, decision application, storage, and exporting. It integrates various components such as the RAG engine for semantic search, a test case generator, a comparison engine, and a knowledge base for storing and retrieving test cases.

---

## Class: `TestCaseManager`

### Overview

- Manages generating test cases from user stories or requirement texts.
- Performs similarity search against existing test cases to classify new test cases as `SAME`, `ADDON`, or `NEW`.
- Provides recommendations and applies decisions automatically or manually.
- Supports parallel processing to improve performance.
- Allows import/export of test cases with filtering and format options.
- Provides statistics for knowledge base content.

---

### Initialization

```python
TestCaseManager()
```

Instantiates and initializes all required engines and the knowledge base:
- `RAGEngine` for semantic search and retrieval,
- `TestCaseGenerator` for generating test cases,
- `ComparisonEngine` for detailed test case comparison,
- `KnowledgeBase` to manage test case storage.

---

### Methods

---

#### `_analyze_new_test_case(new_test_case: TestCase, top_k: Optional[int]) -> ComparisonResult`

Analyzes a newly generated test case by searching for similarity within the knowledge base and comparing against the most similar test case found.

- **Args**:
  - `new_test_case`: The newly generated `TestCase` to analyze.
  - `top_k`: Optional limit to number of similar cases to consider; defaults to `Config.RAG_TOP_K`.
- **Returns**: A `ComparisonResult` indicating similarity and decision (`SAME`, `ADDON`, or `NEW`).

---

#### `_get_recommendation(comparison_result: ComparisonResult) -> str`

Provides a textual recommendation based on the comparison decision.

- **Args**:
  - `comparison_result`: The result of test case comparison.
- **Returns**: Recommendation string advising on what to do with the new test case.

---

#### `_reconstruct_test_case(similar_case_data: dict) -> TestCase`

Rebuilds a `TestCase` object from raw data (e.g., from ChromaDB search results) to enable detailed comparisons.

- **Args**:
  - `similar_case_data`: Dictionary containing metadata and document text of the similar case.
- **Returns**: A reconstructed `TestCase`.

---

#### `process_user_story(user_story: UserStory, suite_name: str = "default", auto_apply: bool = False, num_test_cases: Optional[int] = None) -> dict`

Generates and analyzes test cases from a given user story, optionally applying decisions automatically.

- **Args**:
  - `user_story`: The `UserStory` to generate test cases from.
  - `suite_name`: Target test suite to store results (default `"default"`).
  - `auto_apply`: Whether to automatically apply decisions (default `False`).
  - `num_test_cases`: Optional number of test cases to generate.
- **Returns**: A dict containing:
  - Original user story,
  - Generated test cases,
  - Analysis results (comparison + recommendations),
  - Actions taken if auto_apply is enabled,
  - Summary statistics.

---

#### `process_requirement_text(requirement_text: str, suite_name: str = "default", auto_apply: bool = False, num_test_cases: Optional[int] = None) -> dict`

Generates and analyzes test cases from free-form requirement text, similar to `process_user_story`.

- **Args**:
  - `requirement_text`: Raw requirement text to generate test cases from.
  - `suite_name`: Target test suite name.
  - `auto_apply`: Automatically apply decisions flag.
  - `num_test_cases`: Optional number of test cases to generate.
- **Returns**: Dictionary similar to `process_user_story` result.

---

#### `apply_decision(test_case: TestCase, comparison: ComparisonResult, suite_name: str = "default", user_approved: bool = True) -> str`

Applies the decision result for a single test case, optionally respecting user approval.

- **Args**:
  - `test_case`: The test case to act on.
  - `comparison`: Comparison result that drives the decision.
  - `suite_name`: The test suite name.
  - `user_approved`: If user-approved (currently always applied regardless).
- **Returns**: Description of action taken.

---

#### `_apply_decision(test_case: TestCase, comparison: ComparisonResult, suite_name: str) -> str`

Internal helper that performs actual test case updates in knowledge base and RAG engine based on the decision:

- `SAME`: Keeps existing test case.
- `ADDON`: Merges new test case coverage with existing one.
- `NEW`: Adds new test case to knowledge base.
  
Returns an informative status string.

---

#### `_generate_summary(results: List[Dict[str, Any]]) -> dict`

Creates a summary of processed test cases and decisions.

- **Args**:
  - `results`: List of analysis results.
- **Returns**: Summary dict including counts and percentages of `SAME`, `ADDON`, and `NEW` decisions.

---

#### `get_test_suite(suite_name: str = "default") -> List[TestCase]`

Retrieves all test cases in a specified test suite.

- **Args**:
  - `suite_name`: Test suite to retrieve.
- **Returns**: List of `TestCase` objects.

---

#### `get_filtered_test_cases(suite_name: str = "default", priorities: Optional[List[str]] = None, test_types: Optional[List[str]] = None, tags: Optional[List[str]] = None, is_regression: Optional[bool] = None) -> List[TestCase]`

Filters test cases in a suite based on priorities, types, tags, and regression flags.

- **Args**:
  - `suite_name`: Suite to filter.
  - `priorities`: List of priority strings to include.
  - `test_types`: List of test types to include.
  - `tags`: List of tags; test case must have at least one.
  - `is_regression`: Filter by regression test flag (`True`, `False`, or `None` for no filter).
- **Returns**: Filtered list of test cases.

---

#### `export_test_suite(suite_name: str, output_path: str, format: str = "excel", priorities: Optional[List[str]] = None, test_types: Optional[List[str]] = None, tags: Optional[List[str]] = None, is_regression: Optional[bool] = None)`

Exports a test suite or filtered subset to file.

- **Args**:
  - `suite_name`: Name of the suite to export.
  - `output_path`: File path to save export.
  - `format`: Export file format (`excel`, `csv`, or `json`).
  - `priorities`: Optional filter by priority.
  - `test_types`: Optional filter by test type.
  - `tags`: Optional filter by tags.
  - `is_regression`: Optional filter by regression status.
- **Raises**: `ValueError` if an unsupported format is specified.

---

#### `get_statistics() -> Dict[str, Any]`

Returns summary statistics regarding the knowledge base contents.

- **Returns**: Dictionary with:
  - `total_test_cases`: Total count of indexed test cases,
  - `test_suites`: List of available test suites.

---

#### `import_existing_test_cases(file_path: str, suite_name: str = "imported", file_format: str = "auto") -> Dict[str, Any]`

Imports and indexes existing test cases from external files.

- **Args**:
  - `file_path`: Path to the file containing test cases.
  - `suite_name`: Target suite name to import into.
  - `file_format`: File format: `'excel'`, `'json'`, or `'auto'` (detect from extension).
- **Returns**: Dictionary containing:
  - `success`: Whether import was successful.
  - `imported_count`: Number of test cases imported to knowledge base.
  - `failed_count`: Number of failed imports.
  - `errors`: List of error messages if any.
  - `test_cases`: List of imported `TestCase` objects.

- **Functionality**:
  - Supports `.xlsx`/`.xls` Excel and `.json` files.
  - Adds test cases to knowledge base and RAG engine for semantic search.
  - Reports detailed import results.

---

## Enums and Data Classes Used

- `TestCase`: Data class representing an individual test case.
- `UserStory`: Data class representing a user story.
- `ComparisonResult`: Result of comparing two test cases, including similarity score and decision.
- `DecisionType`: Enum with values: `SAME`, `ADDON`, `NEW`.

---

## Notes

- Parallel processing via `ThreadPoolExecutor` is used to improve performance during test case analysis.
- The system is designed to flexibly ingest both structured user stories and raw requirement text.
- Import/export utilities leverage external helper functions - they should be implemented accordingly.
- Import function performs batch addition to RAG engine for efficiency.
- Confidence scores and similarity thresholds are controlled through configuration (`Config` module).
- The manager assumes test cases can be merged to expand coverage when decision is `ADDON`.
- Recommendations guide human users or automated workflows for test case lifecycle.

---

This class is a central integration point managing the flow of test case creation, validation against existing knowledge, and updates to the system, enabling continuous intelligence-driven test case management.

## File: engines/test_case_updater.py
Sure! Please provide the code you'd like me to generate documentation for.

## File: examples/__init__.py
# Example Scripts Demonstrating System Usage

This module contains example scripts that illustrate how to use the system's various features and components. These examples serve as practical guides to help users understand the system's capabilities and how to integrate or interact with it in their own projects.

## File: examples/example.py
# Documentation for RAG Test Case Management Example Usage

## Overview

This script demonstrates example usage of the **RAG Test Case Management System**, showcasing how to process user stories and requirement texts to generate, compare, and manage test cases using the system's API.

It includes two main examples:

- **User Story Processing**: Creating a user story object, processing it to generate test cases, reviewing and applying decisions, exporting results, and viewing statistics.
- **Requirement Text Processing**: Processing plain text requirements to automatically generate and apply test cases, followed by action summary output.

---

## Module Imports

- `os`, `sys`: Used to modify Python path to locate core modules.
- `core.models.UserStory`: Data model for defining user stories.
- `engines.test_case_manager.TestCaseManager`: The main engine class for managing test cases.
- `core.utils.generate_id`: Utility function to generate unique identifiers.

---

## Functions

### `example_user_story()`

**Purpose:**  
Demonstrates creating a `UserStory` object and using the `TestCaseManager` to process it into test cases. It also shows detailed test case comparison results, manual decision application, exporting the test suite, and retrieving knowledge base statistics.

**Steps:**

1. **User Story Creation:**  
   Constructs a `UserStory` with:
   - An ID generated based on a feature name `"login_feature"`.
   - Title, description, acceptance criteria, business rules, and context as per a typical login feature.

2. **Test Case Manager Initialization:**  
   Creates an instance of `TestCaseManager`.

3. **Process User Story:**  
   Calls `process_user_story` on the manager with:
   - The created user story.
   - Suite name `"authentication"`.
   - `auto_apply=False` to manually review and apply decisions.

4. **Display Results Summary:**  
   Prints the total number of generated test cases, broken down by category:
   - Same (existing test cases matched)
   - Add-on (test cases that add onto existing coverage)
   - New (completely new test cases)

5. **Display Detailed Results:**  
   Iterates through each test case result, printing:
   - Test case title
   - Decision (same/add-on/new)
   - Similarity and confidence scores
   - Explanation reasoning
   - System recommendation

6. **Apply Decisions Manually:**  
   Applies each decision by calling `apply_decision` with `user_approved=True` to confirm actions.

7. **Export Test Suite:**  
   Saves the test suite to an Excel file at `./output/authentication_test_suite.xlsx`.

8. **Display Knowledge Base Statistics:**  
   Outputs the total number of test cases and the list of test suites managed by the knowledge base.

---

### `example_requirement_text()`

**Purpose:**  
Demonstrates processing plain textual requirements into test cases, with automated decision application and output of the summary of actions taken.

**Steps:**

1. **Requirement Text Definition:**  
   A multi-line string representing a feature specification for "Shopping Cart Checkout" including:
   - Feature description
   - Functional requirements
   - Business rules

2. **Test Case Manager Initialization:**  
   As before, creates an instance of `TestCaseManager`.

3. **Process Requirement Text:**  
   Calls `process_requirement_text` with:
   - The requirement string.
   - Suite name `"checkout"`.
   - `auto_apply=True` to automatically apply all generated decisions.

4. **Display Summary:**  
   Prints the number of generated test cases (total, same, add-on, new) and the number of actions applied, followed by listing each action.

---

## Main Execution

When run as a script (`__main__`), the program:

- Prints a title banner.
- Prompts the user to select which example to run:
  - `1`: Run user story example (`example_user_story`).
  - `2`: Run requirement text example (`example_requirement_text`).
  - Any other input defaults to user story example.

---

## Example Output

Basic flow for User Story example:

```
================================================================================
RAG TEST CASE MANAGEMENT SYSTEM - EXAMPLE USAGE
================================================================================

Select example:
1. User Story Example
2. Requirement Text Example

Enter choice (1 or 2): 1
Initializing Test Case Manager...

Processing user story: User Login Feature

================================================================================
RESULTS
================================================================================

Generated 10 test cases:
  - Same: 4 (40.0%)
  - Add-on: 3 (30.0%)
  - New: 3 (30.0%)

--------------------------------------------------------------------------------
DETAILED RESULTS
--------------------------------------------------------------------------------

1. Test Case Title 1
   Decision: SAME
   Similarity: 92.00%
   Confidence: 87.00%
   Reasoning: Matched existing login validations.
   Recommendation: Use existing test case.

...

================================================================================
APPLYING DECISIONS
================================================================================
✓ Added new test case: Login lockout verification
✓ Updated test case: Validate email format
...

================================================================================
EXPORTING
================================================================================
✓ Exported test suite to ./output/authentication_test_suite.xlsx

================================================================================
STATISTICS
================================================================================

Knowledge Base:
  - Total test cases: 150
  - Test suites: authentication, checkout, profile
```

---

## Dependencies and Assumptions

- `core.models.UserStory` class supports standard attributes like `id`, `title`, `description`, `acceptance_criteria`, `business_rules`, and `context`.
- `TestCaseManager` provides:
  - `process_user_story(user_story, suite_name, auto_apply)` -> returns dict with test case generation results.
  - `process_requirement_text(text, suite_name, auto_apply)` similarly for plain text input.
  - `apply_decision(test_case, comparison, suite_name, user_approved)` to apply user-approved decisions.
  - `export_test_suite(suite_name, output_path, format)` to save test suites.
  - `get_statistics()` to get knowledge base and suite stats.
- `generate_id` is a utility to create unique string identifiers.

---

## Summary

This example script acts as a hands-on tutorial for developers or QA engineers to integrate with the RAG Test Case Management System, illustrating:

- Defining user stories programmatically.
- Parsing requirement documents.
- Generating test cases informed by similarity/deduplication analysis.
- Reviewing and applying changes to a test suite.
- Exporting data for external use.
- Querying system knowledge base statistics.

It provides a strong starting point for building larger test automation workflows around user requirements.

---

# End of Documentation

## File: examples/example_context_engineering.py
# Module: Context Engineering Examples in Test Case Generation

This module provides demonstration scripts illustrating the use of **context engineering** in generating test cases from software requirements. It compares basic generation methods with advanced context-aware approaches using domain knowledge and related examples to improve test case quality, coverage, and relevance.

---

## Overview

- **Basic generation**: Generates test cases directly from textual requirements without context enrichment.
- **Advanced generation**: Utilizes *context engineering* by supplying domain context and similar cases to the test case generator for more targeted, comprehensive test cases.
- **Additional utilities**: Automatic detection of focus areas in requirements and usage of reusable context templates for domain and technical details.

The examples highlight the impact of context engineering on automated test case generation within a Retrieval-Augmented Generation (RAG) system framework.

---

## Imports and Setup

- **Standard libraries**: `os`, `sys`, `json`
- **Project modules (added to sys.path dynamically)**:
  - `TestCaseGenerator` — main class for generating test cases.
  - `RAGEngine` — retrieval engine (imported but not directly used in examples).
  - `ContextEngineer` — provides context engineering utilities like focus detection and templates.

---

## Functions

### example_basic_vs_advanced()

**Purpose:**  
Demonstrates the difference between generating test cases **without** and **with** context engineering.

**Functionality:**

1. Defines a sample requirement for user login functionality.
2. Generates test cases in **basic mode**:
   - Initializes `TestCaseGenerator` with `use_context_engineering=False`.
   - Prints summary statistics (number of test cases, average steps, boundary conditions).
   - Displays details of the first 3 generated test cases.
3. Generates test cases in **advanced mode**:
   - Initializes `TestCaseGenerator` with `use_context_engineering=True`.
   - Supplies domain-specific context (e.g., industry type, user roles).
   - Supplies similar examples (empty in this demo).
   - Prints summary statistics and sample test cases, similar to basic generation.
4. Compares metrics between basic and advanced modes, calculating improvements in counts and averages.
5. Prints key insights on benefits of context engineering such as improved coverage and edge case detection.

---

### example_auto_focus_detection()

**Purpose:**  
Illustrates how focus areas within test requirements can be automatically detected using `ContextEngineer`.

**Functionality:**

- Creates a `ContextEngineer` instance.
- Defines a list of various test requirements for use cases spanning authentication, API responses, concurrency, security.
- For each requirement:
  - Invokes `get_focus_areas()` to extract key focus areas automatically.
  - Prints the requirement and its detected focus areas.

---

### example_context_templates()

**Purpose:**  
Shows how predefined context templates for different contexts (domain, technical) can be used and formatted.

**Functionality:**

- Instantiates `ContextEngineer`.
- Defines sample domain context and technical context dictionaries with parameters like industry, user roles, technology stack, architectures.
- Formats and prints:
  - Domain context template filled with provided domain info.
  - Technical context template filled with provided technical info.

These formatted templates illustrate reusable, standardized contextual information that can be incorporated into test case generation prompts or documentation.

---

## Main Script Execution

Runs all three example functions sequentially inside a try-except block:

1. `example_basic_vs_advanced()`
2. `example_auto_focus_detection()`
3. `example_context_templates()`

Prints overall progress messages and errors with guidance on setting up Azure OpenAI credentials if execution fails.

---

## Summary

This module provides practical demonstrations of how **context engineering techniques** enhance test case generation by:

- Leveraging domain-specific knowledge and historic examples.
- Automatically extracting focus areas from requirements text.
- Using standardized context templates for consistent, professional outputs.

It serves as a learning tool and baseline for integrating advanced context-aware methods in RAG-backed test case management systems.

---

# Example Usage

```bash
python context_engineering_examples.py
```

Expected output:

- Detailed comparison of generated test cases with and without context engineering.
- Detected focus areas for sample requirements.
- Rendered domain and technical context templates.
- Summary of key benefits and improvements.

---

# Dependencies and Requirements

- Python 3.x
- Access to `engines` module with `TestCaseGenerator`, `RAGEngine`, `ContextEngineer`.
- Properly configured environment variables for Azure OpenAI credentials (.env file recommended).

---

# Notes

- This is a demonstration script. In production, domain context and similar examples would be sourced from actual knowledge bases or vector search systems.
- Error handling is minimal; expected to be extended in integration projects.

---

This documentation facilitates understanding and maintaining the context engineering examples for generating high-quality automated test cases aligned with domain knowledge and project standards.

## File: examples/import_example.py
# Module: Import Existing Test Cases into Knowledge Base

This module provides example scripts demonstrating how to import existing test cases from Excel or JSON files into a Knowledge Base (KB) using the `TestCaseManager` class. It also shows how to process a new user story and compare it against imported test cases.

---

## Overview

The examples cover:

- Importing test cases from an Excel file
- Importing test cases from a JSON file
- Using imported test cases for automated comparison with a new user story
- Interactive CLI menu to run individual or all examples

---

## Imports and Setup

```python
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engines.test_case_manager import TestCaseManager
```

- Adds the parent directory to `sys.path` to access `TestCaseManager`.
- Uses `pathlib.Path` for file path handling.

---

## Functions

### `import_from_excel_example()`

**Purpose**  
Imports test cases from an Excel spreadsheet into the Knowledge Base.

**Description**  
- Checks if the specified Excel file exists (`./examples/existing_test_cases.xlsx`).
- If the file is missing, prints instructions on required and optional columns.
- Uses `TestCaseManager.import_existing_test_cases` with `file_format="auto"` to import.
- Prints success or failure details, including:
  - Number of imported and failed test cases
  - Import errors (if any)
  - Updated KB statistics (total test cases, test suites)
  - Sample details of the first 3 imported test cases from the imported test suite

**Required Excel Columns**  
- Title  
- Description  
- Test Steps  
- Expected Outcome  

**Optional Excel Columns**  
- Business Rule  
- Preconditions  
- Postconditions  
- Tags  
- Priority  
- Test Type  
- Boundary Conditions  
- Side Effects  
- ID  

**Usage Example**  
```python
import_from_excel_example()
```

---

### `import_from_json_example()`

**Purpose**  
Imports test cases from a JSON file into the Knowledge Base.

**Description**  
- Checks if the specified JSON file exists (`./examples/existing_test_cases.json`).
- If missing, prints a warning.
- Calls `TestCaseManager.import_existing_test_cases` with `file_format="json"`.
- Prints a summary of the import results, and displays titles of the first 3 imported test cases.
- Prints errors in case of failure.

**Usage Example**  
```python
import_from_json_example()
```

---

### `test_with_imported_cases()`

**Purpose**  
Demonstrates importing test cases and processing a new user story to compare generated test cases against existing ones.

**Description**  
- Imports existing test cases from an Excel file (`./examples/existing_test_cases.xlsx`) into the suite named `"authentication"`.
- If import fails or no test cases available, skips further processing.
- Creates a new `UserStory` object representing a "User Login Feature" with acceptance criteria and business rules.
- Calls `TestCaseManager.process_user_story` to generate and compare test cases from the user story against the imported suite.
- Prints a summary of the comparison:
  - Total generated test cases
  - Counts and percentages of test cases classified as SAME, ADD-ON, or NEW
- Displays detailed comparison results (first 3 test cases), including:
  - Decision taken (`SAME`, `ADD-ON`, `NEW`)
  - Hybrid similarity score
  - Confidence score

**Assumed Imports**  
```python
from models import UserStory
from utils import generate_id
```

**Usage Example**  
```python
test_with_imported_cases()
```

---

## Execution as Script

When run as a standalone program, presents a simple menu:

```
RAG TEST CASE MANAGEMENT - IMPORT EXAMPLES

Select example:
1. Import from Excel
2. Import from JSON
3. Test with imported cases
4. Run all examples
```

- User inputs choice (1-4).
- Executes the corresponding example(s).
- Defaults to Excel import example on invalid input.

---

## Summary of Key Classes and Methods Used

- **TestCaseManager**  
  Manages test case operations including import, storage, statistics, and processing user stories.

- **import_existing_test_cases(file_path, suite_name, file_format="auto")**  
  Imports test cases from the given file into the specified test suite.  
  Returns a result dictionary:
  - `'success'`: `bool`  
  - `'imported_count'`: number of successful imports  
  - `'failed_count'`: number of failures  
  - `'errors'`: list of error messages  
  - Optionally `'test_cases'`: imported test case objects (used in JSON import example)

- **get_statistics()**  
  Returns KB statistics dictionary with fields like:
  - `knowledge_base['total_test_cases']`  
  - `knowledge_base['test_suites']`

- **get_test_suite(suite_name)**  
  Returns a list of test cases in the given suite.

- **process_user_story(user_story, suite_name, auto_apply=False)**  
  Generates and compares test cases based on the user story and the existing suite. Returns a detailed results dictionary with summary and individual comparison results.

---

## Notes

- Example files (`.xlsx` and `.json`) are expected to be present in `./examples/`.
- Excel import expects well-structured sheets with specific columns for successful import.
- JSON import expects properly formatted JSON representing test cases.
- This example aims primarily at demonstrating usage and command-line interaction, not full UI or error handling.
- The underlying implementations of `TestCaseManager`, `UserStory`, and ID generation are assumed to exist in respective modules.

---

## Example Run Snippet

```bash
$ python import_test_cases.py

RAG TEST CASE MANAGEMENT - IMPORT EXAMPLES

Select example:
1. Import from Excel
2. Import from JSON
3. Test with imported cases
4. Run all examples

Enter choice (1-4): 1

================================================================================
IMPORTING TEST CASES FROM EXCEL
================================================================================

Importing from: ./examples/existing_test_cases.xlsx

================================================================================
IMPORT RESULTS
================================================================================

✓ Successfully imported 25 test cases

--------------------------------------------------------------------------------
KNOWLEDGE BASE STATISTICS
--------------------------------------------------------------------------------
Total test cases in KB: 120
Test suites: existing_tests, authentication, regression

--------------------------------------------------------------------------------
IMPORTED TEST CASES (showing first 3)
--------------------------------------------------------------------------------

1. Validate user login
   ID: TC-101
   Business Rule: Password must be at least 8 characters
   Priority: High
   Description: Verify that the user can successfully log in with valid credentials...
```

---

# End of Documentation

## File: generate_diagrams.py
# Project Architecture and Diagram Generator Documentation

## Overview

This Python script analyzes the structure of a Python project and generates a rich set of architectural diagrams using Mermaid syntax. It includes system architecture charts, module dependency graphs, class diagrams, sequence diagrams, and process flowcharts. Additionally, it leverages Azure OpenAI to generate AI-assisted comprehensive architecture diagrams. The output is saved as a markdown document containing embedded Mermaid diagrams for easy visualization.

---

## Requirements

- Python 3.6+
- `openai` Python SDK with AzureOpenAI client
- Environment variables:
  - `AZURE_OPENAI_API_KEY` — Azure OpenAI API Key
  - `AZURE_OPENAI_API_VERSION` — API version (default: `"2025-01-01-preview"`)
  - `AZURE_OPENAI_ENDPOINT` — Azure OpenAI endpoint URL
  - `AZURE_OPENAI_DEPLOYMENT` — Deployment name for the model (default: `"gpt-4.1-mini"`)

---

## Modules and Functions

### Initialization

- **`client`**  
  An instance of `AzureOpenAI` initialized with authentication and endpoint configuration from environment variables.

---

### `analyze_project_structure() -> Dict`

Analyzes the current directory (and subdirectories) recursively to build a dictionary describing the project organization.

- **Process:**
  - Walks through all directories (excluding hidden and common non-code folders like `__pycache__`, `node_modules`, `venv`, `env`).
  - For each `.py` file:
    - Parses Python AST for:
      - Import statements (both `import` and `from ... import ...`)
      - Class definitions
      - Function definitions
  - Collects:
    - Module relative path
    - List of imported modules
    - List of classes
    - List of functions
- **Returns:**  
  A dictionary with keys:  
  - `'modules'` mapping module paths to their imports, classes, and functions  
  - `'dependencies'`, `'classes'`, `'functions'` (currently initialized but unused)

---

### `generate_mermaid_architecture_diagram(structure: Dict) -> str`

Generates a Mermaid graph representing module dependency architecture.

- **Input:**  
  The structure dict from `analyze_project_structure()`
- **Process:**  
  - Groups modules by directory
  - Creates Mermaid subgraphs for directories
  - Maps each module to a node
  - Draws arrows representing imports between modules if the import matches an internal module path
- **Output:**  
  Mermaid code block string with a top-bottom (`graph TB`) graph of module dependencies.

---

### `generate_mermaid_class_diagram(structure: Dict) -> str`

Generates a Mermaid class diagram of main classes and their key methods.

- **Input:**  
  Project structure dictionary
- **Process:**  
  - Extracts class names and up to first 5 functions per module
  - Generates Mermaid `classDiagram` syntax 
  - Limits to a maximum of 15 classes to avoid overcrowding
- **Output:**  
  Mermaid class diagram as a markdown code block string.

---

### `generate_mermaid_sequence_diagram() -> str`

Produces a static Mermaid sequence diagram illustrating a typical workflow of the application components.

- **Participants:** User, API, RAGEngine, KnowledgeBase, TestGenerator, VectorDB
- **Purpose:** Outline a typical flow of test case generation from user request to response delivery.
- **Output:**  
  A hardcoded Mermaid sequence diagram in a markdown code block.

---

### `generate_mermaid_flowchart() -> str`

Generates a flowchart diagram describing the main process flow for handling user input to test case generation.

- **Includes:**
  - Decision points for existing similar cases
  - Logic for augmenting or generating new test cases
  - Steps to store and format results
- **Output:**  
  Static Mermaid flowchart diagram wrapped in a markdown code block.

---

### `generate_ai_diagrams(structure: Dict) -> str`

Uses Azure OpenAI's chat completion endpoint to generate a comprehensive Mermaid diagram based on the project structure.

- **Input:**  
  Project structure dictionary
- **Process:**  
  - Summarizes project info (number of modules, top modules with class/function counts)
  - Constructs a prompt requesting a Mermaid diagram showing system architecture, data flow, and component interactions
  - Submits prompt to OpenAI Azure service
- **Output:**  
  Mermaid diagram content string (or empty string on error)

---

### `main()`

Entrypoint for the script which coordinates all tasks:

1. Analyze project structure by calling `analyze_project_structure()`.
2. Print the number of modules found.
3. Generate multiple Mermaid diagrams:
   - System architecture (process flowchart)
   - Module dependencies
   - Class diagram
   - Sequence diagram
   - Process flowchart (repeated for emphasis)
   - AI-generated architecture
4. Build a markdown document that includes:
   - Title and generation timestamp
   - Table of contents linking to sections
   - Mermaid diagrams under respective headers
   - Module summary table listing module names with counts of classes, functions, and imports
5. Save generated markdown file to `docs/architecture-diagrams.md`
6. Print success messages and file location

---

## Output

The script generates a file:

```
docs/architecture-diagrams.md
```

This markdown contains:

- Diagrams rendered as Mermaid code blocks
- Summary of project modules and structure
- AI-generated architecture diagram from Azure OpenAI completion

---

## Usage

Run the script from the root of your Python project:

```bash
python script_name.py
```

Make sure environment variables for Azure OpenAI authentication are set prior:

```bash
export AZURE_OPENAI_API_KEY="your_api_key"
export AZURE_OPENAI_API_VERSION="2025-01-01-preview"
export AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
export AZURE_OPENAI_DEPLOYMENT="gpt-4.1-mini"
```

---

## Notes

- The AST parsing is done using Python's built-in `ast` module ensuring accuracy in detecting imports, classes, and functions.
- The dependency matching considers module names heuristically based on paths and import names.
- The AI-generated architecture depends on successful communication with the Azure OpenAI service.
- Mermaid diagrams can be rendered in markdown viewers supporting Mermaid (e.g., VSCode with Mermaid Preview, GitHub, Obsidian).
- Error handling during file reading and AI requests logs to console but does not halt execution.

---

## Possible Improvements

- Expand dependency analysis to accurately resolve imports including relative imports.
- Parse class methods more thoroughly (including visibility and parameters).
- Handle additional code artifacts such as enums, dataclasses, or async functions.
- Cache AI responses or append incremental results instead of overwriting the output file.
- Add CLI arguments to customize output location, included diagrams, or verbosity.

---

## Summary

This script automates Python project analysis and produces detailed architecture documentation enriched with Mermaid diagrams both generated statically and enhanced through AI. It helps software architects and developers visualize, understand, and communicate system design efficiently.

## File: generate_docs.py
# Auto Documentation Generator

This Python script automates the generation of code documentation for a software project by leveraging Azure OpenAI's GPT-based models. It processes changed source code files and produces a Markdown document summarizing the code, helping maintain up-to-date project documentation.

---

## Overview

- Reads a list of changed source files from `changed_files.txt`.
- Determines if it should generate full project documentation or incremental updates based on the presence of the existing documentation file.
- For each relevant source file (`.java`, `.py`, `.js`), sends the code to the Azure OpenAI GPT model to generate documentation.
- Aggregates all generated documentation into a single Markdown file located at `docs/auto-doc.md`.

---

## Prerequisites

- Python 3.7+
- Required Python packages:
  - `openai` (specifically, the Azure OpenAI Python SDK or `openai` package supporting Azure endpoints)
- Environment variables set:
  - `AZURE_OPENAI_API_KEY` - Your Azure OpenAI API key.
  - `AZURE_OPENAI_API_VERSION` - Azure OpenAI API version (default `"2025-01-01-preview"`).
  - `AZURE_OPENAI_ENDPOINT` - Your Azure OpenAI resource endpoint URL.
  - `AZURE_OPENAI_DEPLOYMENT` - Name of the deployed GPT model (default `"gpt-4.1-mini"`).

---

## How it Works

1. **Initialization**  
   Initializes an Azure OpenAI client with provided API credentials and endpoint.

2. **Input Files**  
   Reads `changed_files.txt`, which must contain a list of file paths indicating changed or new source files.

3. **Documentation Type Detection**  
   - If `docs/auto-doc.md` **does not exist**, it treats the process as a **full documentation generation** for the entire project.
   - If the file exists, it treats the process as an **incremental update** to the documentation for changed files only.

4. **Processing Files**  
   For each changed file with extensions `.java`, `.py`, or `.js`:
   - Reads the source code.
   - Submits the code to Azure OpenAI's chat completion endpoint with the system prompt:  
     `"You are a senior software architect."`
   - Requests the model to generate documentation for the given code snippet.
   - Appends the returned documentation under a section header labeled with the filename in the output Markdown.

5. **Error Handling**  
   If fetching the documentation fails for any file, the script logs the error and inserts an error message in place of the documentation section.

6. **Output**  
   Creates the `docs` directory if it does not exist and writes the accumulated documentation content to `docs/auto-doc.md`.

---

## File Structure Assumptions

- `changed_files.txt` should be in the same directory where this script is executed.
- The source files listed in `changed_files.txt` should be accessible from the current working directory.
- Documentation output will go to `docs/auto-doc.md`.

---

## Environment Variables

| Variable                  | Description                             | Default                   |
|---------------------------|-------------------------------------|--------------------------|
| `AZURE_OPENAI_API_KEY`    | API key for Azure OpenAI             | (no default, required)   |
| `AZURE_OPENAI_API_VERSION`| Version of Azure OpenAI API          | `"2025-01-01-preview"`   |
| `AZURE_OPENAI_ENDPOINT`   | Endpoint URL of the Azure OpenAI resource | (no default, required)   |
| `AZURE_OPENAI_DEPLOYMENT` | Deployment name of the GPT model     | `"gpt-4.1-mini"`         |

---

## Example Usage

1. Export environment variables:

```bash
export AZURE_OPENAI_API_KEY="your_api_key_here"
export AZURE_OPENAI_API_VERSION="2025-01-01-preview"
export AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com/"
export AZURE_OPENAI_DEPLOYMENT="gpt-4.1-mini"
```

2. Prepare a `changed_files.txt` file listing source code files to document, for example:

```
src/main.py
src/utils.py
src/helpers.js
```

3. Run the script:

```bash
python generate_docs.py
```

4. Generated documentation will be saved to `docs/auto-doc.md`.

---

## Code Summary

```python
import os
from openai import AzureOpenAI

# Initialize AzureOpenAI client with environment variables
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY", ""),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2025-01-01-preview"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", "")
)

# Read list of changed files
with open("changed_files.txt", "r") as f:
    files = f.read().splitlines()

# Determine if full or incremental documentation
doc_file_path = "docs/auto-doc.md"
is_full_documentation = not os.path.exists(doc_file_path)

# Initialize doc content with header and timestamp
if is_full_documentation:
    doc_content = "# Auto Generated Documentation\n\n"
    doc_content += f"*Complete project documentation - Generated on: {os.popen('date').read().strip()}*\n\n"
    print(f"Generating complete documentation for {len(files)} files...")
else:
    doc_content = "# Auto Generated Documentation\n\n"
    doc_content += f"*Last updated: {os.popen('date').read().strip()}*\n\n"
    print(f"Generating documentation for {len(files)} changed files...")

# Process each source file
for file in files:
    if file.endswith((".java", ".py", ".js")):
        print(f"Processing: {file}")
        try:
            with open(file, "r", encoding="utf-8") as code_file:
                code = code_file.read()

            # Request documentation generation from Azure OpenAI
            response = client.chat.completions.create(
                model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4.1-mini"),
                messages=[
                    {"role": "system", "content": "You are a senior software architect."},
                    {"role": "user", "content": f"Generate documentation for this code:\n{code}"}
                ],
            )

            # Append documentation to the output
            doc_content += f"## File: {file}\n"
            doc_content += response.choices[0].message.content or ""
            doc_content += "\n\n"
        except Exception as e:
            print(f"Error processing {file}: {str(e)}")
            doc_content += f"## File: {file}\n"
            doc_content += f"*Error generating documentation: {str(e)}*\n\n"

# Ensure docs folder exists and write Markdown output
os.makedirs("docs", exist_ok=True)
with open("docs/auto-doc.md", "w", encoding="utf-8") as f:
    f.write(doc_content)
```

---

## Notes & Recommendations

- Modify the `changed_files.txt` generation to integrate with your source control (e.g., git diff) for automated incremental updates.
- Ensure your Azure OpenAI deployment is correctly set up and that the deployment name matches `AZURE_OPENAI_DEPLOYMENT`.
- The script currently uses system commands like `date` which may be platform-dependent; consider using Python's `datetime` module for better portability.
- You can extend supported file types or customize prompts for more specialized documentation output.
- For large files or many files, batching or rate limiting may be needed to handle API usage limits gracefully.

---

If you need further customization or integration assistance, feel free to ask!

## File: scripts/__init__.py
# Utility Scripts for Setup, Diagnosis, and Maintenance

This module provides a collection of utility scripts designed to assist with various tasks related to system setup, diagnostic checks, and routine maintenance. These scripts aim to streamline and automate common processes to improve efficiency and reduce the likelihood of errors.

## Contents

- **Setup Utilities:** Scripts to automate the initial configuration and installation tasks.
- **Diagnosis Utilities:** Tools for checking system status, identifying issues, and gathering diagnostic data.
- **Maintenance Utilities:** Scripts to perform routine cleanup, updates, and health checks.

## Usage

Each utility script can be run independently depending on the task you need to accomplish. Typically, these scripts are intended to be executed by system administrators or automated processes.

## Examples

```bash
# Run setup script
./setup.sh

# Perform system diagnosis
./diagnose.sh

# Execute maintenance tasks
./maintenance.sh
```

## Notes

- Ensure you have the necessary permissions to execute these scripts.
- Review each script before running to understand its impact on your system.
- Logs generated by these scripts can be found in the `logs/` directory for troubleshooting and auditing purposes.

---

_For detailed documentation on individual scripts, refer to their respective headers or inline comments._

## File: scripts/add_diverse_test_cases.py
# Script: Add Diverse Test Case Examples to Knowledge Base

## Overview

This script adds a curated set of diverse test case examples to an existing knowledge base JSON file. The goal is to enrich the knowledge base with varied test case types to improve retrieval quality in Retrieval-Augmented Generation (RAG) systems, which rely on diverse and comprehensive examples for reasoning and generation.

---

## Contents

- Diverse test case examples covering multiple categories:

  - Negative test cases
  - UI test cases
  - Security test cases
  - Edge case test cases
  - Positive test cases

- A function to load the existing knowledge base, append the new test cases, and save back the updated knowledge base file.

---

## Dependencies

- Python standard library modules:
  - `sys`
  - `os`
  - `json`
  - `datetime`
  - `pathlib.Path`

- Project module:
  - `core.utils.generate_id`: Function to generate unique IDs based on test case title strings.

---

## Data Structure: Diverse Test Cases

Each test case is represented as a dictionary containing the following keys:

| Key                | Description                                                       | Example Value              |
|--------------------|-------------------------------------------------------------------|----------------------------|
| `id`               | Unique identifier, generated via `generate_id(title)`             | `"TC_abc123"`              |
| `title`            | Brief descriptive title of the test case                          | `"Login with Empty Username Field - Negative"` |
| `description`      | Detailed explanation of the test purpose                          | `"Verify system prevents login when username field is left empty"` |
| `business_rule`    | The business or functional rule the test verifies                 | `"All required authentication fields must be populated before login submission"` |
| `preconditions`    | List of conditions that must be true before executing the test   | `["User is on the login page", "Username and password fields are visible"]` |
| `test_steps`       | Ordered list of steps with:
                      - `step_number` (int)
                      - `action` (string)
                      - `expected_result` (string)                                     | See example below          |
| `expected_outcome` | Overall expected result of the test                               | `"User remains on login page with appropriate validation error"` |
| `postconditions`   | List of system states after test completion                       | `["User is not authenticated", "Error message is visible"]` |
| `tags`             | List of tags/categorical keywords                                 | `["Authentication", "Negative", "Validation"]` |
| `priority`         | Priority level of the test case                                   | `"High"`                   |
| `test_type`        | Category/type of test case (Negative, UI, Security, Edge_Case, Positive) | `"Negative"`               |
| `is_regression`    | Boolean indicating if test is suitable for regression suites     | `True`                    |
| `boundary_conditions` | List of boundary conditions or edge inputs                       | `["Empty string input", "Field validation"]` |
| `side_effects`     | Possible side effects or secondary impacts                        | `["Login attempt is logged"]` |
| `created_at`       | Timestamp of test case creation (ISO 8601 format)                 | `"2024-05-02T15:04:05.000Z"` |
| `updated_at`       | Timestamp of last update (ISO 8601 format)                        | `"2024-05-02T15:04:05.000Z"` |
| `version`          | Version number of the test case                                   | `1`                        |
| `source_document`  | Reference source of the example                                   | `"diverse_examples"`       |

### Example test step entry:

```json
{
  "step_number": 1,
  "action": "Navigate to login page",
  "expected_result": "Login page displays with username and password fields"
}
```

---

## Main Function: `add_diverse_test_cases()`

### Purpose:

- Loads an existing knowledge base JSON file from `knowledge_base/default.json`
- Validates the structure of the knowledge base file (expects a dictionary with a `"test_cases"` key or a list of test cases)
- Appends the diverse test case examples to the current test cases
- Saves the updated knowledge base back to the same file
- Prints summary information about test cases added

### Workflow:

1. Print a header indicating the operation.
2. Check if the knowledge base file exists. If missing, display an error message and exit.
3. Load the JSON content from the file.
4. Normalize data structure so the test cases are in a list under `"test_cases"`.
5. Report the number of existing test cases.
6. Append the new diverse test cases from the script.
7. Save the updated data back to the JSON file, format with indentation and UTF-8 encoding.
8. Print a summary of the addition, including the count of each test type added.

### Error Handling:

- If file not found, stops and reports.
- If knowledge base format is unexpected, stops and reports.

---

## Usage

Run as a standalone script:

```bash
python add_diverse_test_cases.py
```

This command will add the new test cases to the knowledge base stored at `knowledge_base/default.json` if the file exists.

---

## Notes

- The script assumes that the `generate_id` function produces consistent unique identifiers based on the test case title.
- Timestamps use the current datetime at the time of script execution.
- It is intended to be run in the root directory of the project or adjusted accordingly to locate the `knowledge_base/default.json` file.
- Existing test cases remain untouched; new examples are appended.
- The script outputs progress and summary information to the console for user feedback.

---

## Example Console Output Snippet

```
======================================================================
ADD DIVERSE TEST CASE EXAMPLES TO KNOWLEDGE BASE
======================================================================

 Loading existing knowledge base...
 Found 12 existing test cases

 Adding 12 diverse test case examples...

 Saving updated knowledge base...
Successfully saved knowledge base

======================================================================
SUMMARY
======================================================================
 Previous test cases: 12
 New test cases added: 12
 Total test cases: 24

 Added test case types:
   ✓ 3 Negative test cases
   ✓ 3 UI test cases
   ✓ 2 Security test cases
   ✓ 2 Edge Case test cases
   ✓ 1 Positive test cases

 Knowledge base updated successfully!
======================================================================
```

---

## Summary

This script is a utility to enhance the test cases knowledge base with a predefined set of diverse examples spanning negative, UI, security, edge case, and positive testing categories. It ensures the knowledge base is comprehensive to support automated reasoning systems in software testing and quality assurance workflows.

## File: scripts/create_excel_template.py
# Script: Create Sample Excel Template for Importing Test Cases

## Overview
This Python script generates a sample Excel template populated with example test cases to facilitate the import of test cases into a test management system or other testing tools. It creates a structured spreadsheet containing detailed test case attributes illustrating a variety of common testing scenarios.

## Features
- Defines a set of five comprehensive test cases covering functional, security, and session management scenarios.
- Organizes test case details such as ID, Title, Description, Preconditions, Test Steps, Expected Outcomes, and other metadata.
- Outputs the test cases into an Excel workbook (`existing_test_cases.xlsx`) within an `examples/` directory.
- Uses the `pandas` library for data manipulation and the `openpyxl` engine to write Excel files.
- Ensures the output directory exists before saving.

## Dependencies
- `pandas` (for DataFrame handling)
- `openpyxl` (Excel writer engine for `.xlsx` format)
- `pathlib` (file system operations)

Ensure these packages are installed in your Python environment:
```bash
pip install pandas openpyxl
```

## Code Breakdown

### Data Definition
- The `data` list contains dictionaries, each representing a single test case.
- Each test case includes the following keys:
  - `ID`: Unique test case identifier.
  - `Title`: Brief descriptive title of the test case.
  - `Description`: Explanation of what is being verified.
  - `Business Rule`: Underlying rule or policy related to the test.
  - `Preconditions`: Conditions that must be true before testing starts.
  - `Test Steps`: Numbered procedural steps with expected intermediate results.
  - `Expected Outcome`: The outcome expected if the test passes.
  - `Postconditions`: State of the system after test execution.
  - `Tags`: Comma-separated keywords for classification.
  - `Priority`: Indication of test importance (e.g., High, Medium).
  - `Test Type`: Category of the test (Functional, Security, etc.).
  - `Boundary Conditions`: Specific scenarios related to limits or thresholds.
  - `Side Effects`: Other effects resulting from the test.

### DataFrame Creation
- The list `data` is converted into a pandas `DataFrame` for structured data handling.

### Output Directory Preparation
- The script uses `Path("examples").mkdir(exist_ok=True)` to create an `examples` directory if it does not already exist.

### Saving to Excel
- The DataFrame is saved as an Excel file named `existing_test_cases.xlsx` inside the `examples` folder.
- The `openpyxl` engine is specified explicitly for compatibility with `.xlsx` files.

### User Feedback
- After saving, the script prints a confirmation message, including the filename, number of test cases, and the column headers exported.

## Usage
Run the script directly with Python:

```bash
python create_test_cases_template.py
```

This generates the file `examples/existing_test_cases.xlsx` ready for use as a test case import template.

## Example Output
The resulting Excel file contains:

| ID    | Title                              | Description                                      | Business Rule                       | Preconditions                                                                       | Test Steps                                                                                   | Expected Outcome                                      | Postconditions                                | Tags                       | Priority | Test Type  | Boundary Conditions                               | Side Effects                      |
|-------|-----------------------------------|-------------------------------------------------|-----------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------|-----------------------------------------------|----------------------------|----------|------------|--------------------------------------------------|---------------------------------|
| TC001 | Valid User Login                  | Verify that users can successfully log in ...  | User authentication and sess ... | User account exists, User has valid credentials                                    | 1. Navigate to login page -> Login form ... 4. Click 'Login' button -> User is authenticated ... | User successfully logs in and is redirected ...     | User session is created, User is logged in    | login, authentication, positive | High     | Functional |                                                  |                                 |
| ...   | ...                               | ...                                             | ...                               | ...                                                                                | ...                                                                                         | ...                                                 | ...                                           | ...                        | ...      | ...        | ...                                              | ...                             |

(And so on for other test cases.)

---

## Contact
If you have questions or need enhancements, please contact the script author or maintainer.

## File: scripts/format_test_cases_for_excel.py
# Documentation for test case Excel export module

This module provides functionality to format test cases for Excel export according to a user's preferred layout. The key features include combining multi-step test actions and expected results into single Excel cells with line breaks, and exporting all test case data into a well-formatted Excel spreadsheet.

---

## Module Overview

The module consists of the following components:

- **format_test_case_for_excel(tc: TestCase) -> dict**  
  Converts a single `TestCase` object into a dictionary formatted for Excel export. This includes combining test steps and expected results into multiline strings within single cells and extracting or inferring test case types.

- **export_to_excel_format(test_cases: List[TestCase], output_path: str)**  
  Takes a list of `TestCase` objects, formats them using `format_test_case_for_excel`, and writes the result to an Excel file at the specified output path. The exported Excel sheet includes cell formatting, column widths, wrapped text, and row heights optimized for readability.

- **Main script execution**  
  When run as a script, it loads test cases from a `KnowledgeBase` using a default test suite, then exports them to `output/test_cases_formatted.xlsx`.

---

## Dependencies

- `pandas` for DataFrame manipulation and Excel writing.  
- `xlsxwriter` engine for advanced Excel formatting (used internally by Pandas).  
- Internal modules: `core.models` (defines `TestCase`), `core.knowledge_base` (provides test case retrieval).

---

## Functions Detail

### `format_test_case_for_excel(tc: TestCase) -> dict`

Formats a single test case for export with these adjustments:

- **Test Steps:**  
  Combined into one multiline string, each line prefixed by the step number (e.g., "1. Open app").
  
- **Expected Results:**  
  Combined multiline string of expected results corresponding to each step. Empty expected results are included as blank lines.
  
- **Preconditions:**  
  Joined into a single space-separated string.
  
- **Test Case Scenario:**  
  Taken from `tc.description`.
  
- **Test Case Title:**  
  Extracts and cleans the test case title by removing specific suffixes such as " - Positive", " - Negative", etc.
  
- **Test Case Type:**  
  Inferred from the title suffix or explicitly from `tc.test_type`. Possible values include: Negative, Positive, UI, Security, Edge Case, or original type if none match.
  
- **Returns:**  
  Dictionary with keys:  
  - `"Test Case ID"`  
  - `"Layer"` (business rule)  
  - `"Test Case Scenario"`  
  - `"Test Case"` (cleaned title)  
  - `"Pre-Condition"`  
  - `"Test Case Type"`  
  - `"Test Steps"` (numbered and multiline)  
  - `"Expected Result"` (multiline)  
  - `"Priority"`

---

### `export_to_excel_format(test_cases: List[TestCase], output_path: str)`

Exports the collection of formatted test cases to an Excel file:

- **Process:**  
  1. Formats all test cases into dictionaries via `format_test_case_for_excel`.  
  2. Creates a Pandas DataFrame from these dictionaries.  
  3. Uses `xlsxwriter` through Pandas ExcelWriter to write the DataFrame to an Excel file.  
  
- **Excel Formatting:**  
  - Header row: bold font, blue background, white text, centered alignment, wrapped text.  
  - Data rows: bordered cells, left-aligned, top vertical alignment, wrapped text for multiline content.  
  - Column widths tailored per data type for better readability.  
  - Row heights increased significantly in data rows to allow multiline text visibility.
  
- **Output:**  
  Excel file saved at `output_path`.

- **Console Feedback:**  
  Prints progress messages and confirms file creation.

---

## Usage as a Script

When executed directly, the module:

1. Initializes a `KnowledgeBase` instance.  
2. Loads all test cases from the "default" test suite.  
3. Exits if no test cases found.  
4. Creates an output directory if it doesn't exist.  
5. Exports the test cases to `output/test_cases_formatted.xlsx` using user-preferred format.  
6. Prints success message with export summary.

---

## Example

```bash
$ python export_test_cases.py

 Formatting 25 test cases for Excel...
✅ Excel file created: output/test_cases_formatted.xlsx
   Format: User's preferred layout with test steps in single cells

 Successfully exported 25 test cases!
 File saved to: output/test_cases_formatted.xlsx
```

---

## Notes

- The formatting assumes that each `TestCase` object includes a collection of `test_steps` where each step has a `step_number`, `action`, and optionally an `expected_result`.
- The user's preferred format keeps all test steps and expected results consolidated in a single cell for easier review in Excel.
- The module requires that the `core` package with `models` and `knowledge_base` is accessible in the Python path.

---

If you have further questions about extending or customizing the formatting, feel free to ask!

## File: scripts/test_llm_apis.py
# API Diagnostic Test Script Documentation

This Python script is a diagnostic tool designed to verify connectivity and functionality of key components used in a Retrieval-Augmented Generation (RAG) test case generation system. It tests direct API connections to Anthropic Claude and OpenAI GPT language models, embedding generation service, and basic internet connectivity.

---

## Overview

The script performs the following checks:

1. **Anthropic Claude API** - Tests the connection and authentication with the Anthropic Claude API.
2. **OpenAI GPT API** - Tests the connection and authentication with the OpenAI GPT API.
3. **Embedding Service** - Tests local embedding generation using the `sentence-transformers` library.
4. **Internet Connectivity** - Verifies network reachability to essential external endpoints.

Based on these tests, it provides a summary of results and recommendations for any failures detected.

---

## Prerequisites

- Python 3.6+
- Environment variables set in `.env` file:
  - `ANTHROPIC_API_KEY` - API key for Anthropic.
  - `OPENAI_API_KEY` - API key for OpenAI.
- Required Python packages:
  - `anthropic`
  - `openai` (or `openai` compatible client library)
  - `python-dotenv`
  - `sentence-transformers`
  - `torch` (may be required by `sentence-transformers`)

Ensure packages can be installed via:

```bash
pip install anthropic openai python-dotenv sentence-transformers torch
```

---

## Module Dependencies

- **dotenv**: To load API keys from `.env`
- **anthropic**: To interface with Anthropic Claude API
- **openai**: To interface with OpenAI GPT API using OpenAI client
- **sentence_transformers**: To generate embeddings locally for RAG
- **socket**: For internet connectivity checks

---

## Functions

### 1. `test_anthropic() -> bool`

Tests the connectivity to the Anthropic Claude API using the provided API key.

- Sends a test prompt: `Say 'Anthropic connection successful!'`
- Uses model: `claude-3-sonnet-20240229`
- Prints diagnostic info including tokens used.
- Handles common errors:
  - Authentication failures
  - Rate limits
  - Other exceptions

**Returns:** `True` if successful, else `False`.

---

### 2. `test_openai() -> bool`

Tests the connectivity to the OpenAI GPT API.

- Sends a test message: `Say 'OpenAI connection successful!'`
- Uses model: `gpt-4o-mini`
- Prints diagnostic info including tokens used (if available).
- Handles error cases including authentication failure, rate limits, model not found.

**Returns:** `True` if successful, else `False`.

---

### 3. `test_embedding_service() -> bool`

Tests the local embedding service used for RAG (Retrieval-Augmented Generation).

- Loads pre-trained `sentence-transformers` model: `all-MiniLM-L6-v2`
- Encodes a test sentence `"Test sentence for embedding"`
- Prints embedding dimension and confirms successful embedding generation.
- Handles exceptions like missing package or runtime errors.

**Returns:** `True` if successful, else `False`.

---

### 4. `test_internet_connectivity() -> bool`

Checks basic internet connectivity by attempting TCP socket connections to:

- `api.anthropic.com` (443)
- `api.openai.com` (443)
- `huggingface.co` (443) — for embedding model downloads
- `8.8.8.8` (53) — Google DNS as a general internet test

Prints success/failure for each endpoint.

**Returns:** `True` if all reachable, else `False`.

---

### 5. `main() -> bool`

Runs all diagnostic tests in sequence:

- Internet connectivity
- Anthropic API
- OpenAI API
- Embedding service

Prints a detailed diagnostic summary with pass/fail status for each component, followed by tailored recommendations if any tests fail.

Returns overall success status — `True` if all tests pass, otherwise `False`.

---

## Usage

Run the script directly from the command line:

```bash
python test_api_connections.py
```

Exit code:

- `0` on all tests passing
- `1` if any test fails

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
  Tokens used: 10 in, 12 out

================================================================================
TEST 2: OpenAI GPT API
================================================================================
Model: gpt-4o-mini

Sending test message...
✓ OpenAI API working!
  Response: OpenAI connection successful!
  Model: gpt-4o-mini
  Tokens used: 9 in, 11 out

================================================================================
TEST 3: Embedding Service (for RAG)
================================================================================
Loading embedding model...
Generating test embedding...
✓ Embedding service working!
  Model: all-MiniLM-L6-v2
  Embedding dimensions: 384

================================================================================
TEST 4: Internet Connectivity
================================================================================
✓ Can reach Anthropic API (api.anthropic.com:443)
✓ Can reach OpenAI API (api.openai.com:443)
✓ Can reach HuggingFace (huggingface.co:443)
✓ Can reach Internet (Google DNS) (8.8.8.8:53)

================================================================================
DIAGNOSTIC SUMMARY
================================================================================
  Internet            ✅ PASS
  Anthropic           ✅ PASS
  OpenAI              ✅ PASS
  Embeddings          ✅ PASS

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

- The script assumes environment variables are loaded via `.env`; make sure this file exists and contains valid API keys.
- If embedding service fails, consider installing `sentence-transformers` and `torch`.
- Network/firewall issues can cause internet connectivity or API connection failures.
- The Anthropic and OpenAI models used are examples and may require access permissions.
- The script helps quickly isolate configuration issues in the RAG test case generation system stack.

---

## License

No license specified. Use and adapt as needed.

---

# End of Documentation

## File: test_distribution.py
"""
Test Script: Test Case Distribution Verification

This script verifies the distribution of test cases based on pre-defined configuration values.
It exercises the `calculate_test_distribution` utility function to ensure test cases are allocated
correctly across different categories such as positive, negative, UI, security, and edge cases.

Modules Used:
- sys: Provides access to system-specific parameters and functions (imported but unused in this script).
- core.utils: Contains the `calculate_test_distribution` function responsible for computing test distribution.
- config.config: Provides configuration constants like DEFAULT_TEST_CASES, MIN_TEST_CASES, and MAX_TEST_CASES.

Script Workflow:
1. Prints a header indicating the purpose of the test.
2. Displays the configured test case parameters (`DEFAULT_TEST_CASES`, `MIN_TEST_CASES`, `MAX_TEST_CASES`).
3. Calculates the distribution of test cases by calling `calculate_test_distribution` with `DEFAULT_TEST_CASES`.
4. Outputs the number of test cases allocated to each category.
5. Summarizes the total number of test cases to verify correctness.
6. Shows the distribution string generated for integration with a Language Learning Model (LLM).
7. Computes and prints the percentage share of each test case category relative to the total.

Usage:
Run this script to validate that the test case distribution logic aligns with the current configuration.
It helps in ensuring balanced and proper coverage across several test categories before executing or generating test cases.

Example Output Structure:
============================================================
TEST CASE DISTRIBUTION VERIFICATION
============================================================

1. Configuration Check:
   DEFAULT_TEST_CASES: 100
   MIN_TEST_CASES: 50
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
   <distribution_string_content>

4. Percentages:
   Positive: 40.0%
   Negative: 20.0%
   UI: 15.0%
   Security: 15.0%
   Edge Case: 10.0%

============================================================
"""

## File: test_user_format_generation.py
# Test Case Generation and Export Script

## Overview
This script automates the generation of test cases based on a user story specified in natural language. It leverages an AI-powered test case generation engine to create diverse test cases covering positive, negative, UI, security, edge cases, and more. Finally, it exports the generated test cases into an Excel file formatted according to the user's preferences.

The primary use case demonstrated here involves validating asset batch upload functionality in a financial application, specifically focusing on mandatory PAN field validation and associated business rules.

---

## Key Functionalities

- **User Story Definition**: Defines the scope, acceptance criteria, and business rules for asset batch uploads.
- **Test Case Generation**: Uses `TestCaseGenerator` to create a set number of test cases covering different scenarios derived from the user story.
- **Test Case Categorization**: Counts and summarizes the generated test cases by type (Positive, Negative, UI, Security, Edge Case, Other).
- **Sample Display**: Prints detailed information about the first three generated test cases to the console.
- **Excel Export**: Saves the entire batch of generated test cases into an Excel file using a custom export utility, tailored to user preferences.
- **Next Steps & Instructions**: Provides guidance on how to open, review, upload, and further generate test cases using a Streamlit app.

---

## Detailed Description

### User Story Definition
The script starts by defining a multi-line string representing a user story for asset batch upload validation, capturing:

- The role ("Financial Advisor")
- Objectives ("Bulk upload of client asset details via Excel")
- Acceptance Criteria (PAN mandatory, validation, error logs, file format restrictions, etc.)
- Business Rules (KYC compliance, database atomicity, error handling)

This user story acts as the primary input for generating relevant test cases.

### Initialization
- Modifies `sys.path` to ensure project modules (`engines`, `core`, `config`) can be imported.
- Imports:
  - `TestCaseGenerator` for AI-driven test generation
  - `export_test_cases_user_format` for exporting results to Excel
  - `Config` for configuration settings (though unused in this script)
- Instantiates the `TestCaseGenerator`

### Generating Test Cases
- Calls `generator.generate_from_text(user_story, num_test_cases=12)` to produce 12 test cases.
- Outputs progress and confirmation messages to the console.

### Categorizing and Summarizing Test Cases
- Iterates over the generated test cases to classify each based on title markers such as "`- Positive`", "`- Negative`", "`- UI`", etc.
- Aggregates counts by category.
- Prints a summary table showing counts for each test type.

### Displaying Samples
- Prints detailed information for the first three test cases, including:
  - Title
  - Business rule associated ("Layer")
  - Test type and priority
  - Description (scenario)
  - Pre-conditions (limited to first 3 for brevity)
  - Test steps (limited to first 3 for brevity)

### Exporting to Excel
- Creates the output directory `output/` if it doesn’t exist.
- Exports all generated test cases to `output/generated_user_format.xlsx`.
- Prints a confirmation message and lists the columns included in the Excel file:
  1. Test Case ID
  2. Layer
  3. Test Case Scenario
  4. Test Case
  5. Pre-Condition
  6. Test Case Type
  7. Test Steps
  8. Expected Result
  9. Priority

### Next Steps Instructions
- Instructs user to open the Excel file and review the test cases.
- Suggests uploading them to a test management system.
- Mentions how to generate more test cases by running the Streamlit-based UI application:
  ```
  streamlit run ui/app.py
  ```

---

## Prerequisites & Dependencies

- Python environment with access to:
  - `engines.test_case_generator.TestCaseGenerator`
  - `core.utils.export_test_cases_user_format`
  - `config.config.Config`
- Proper project directory structure to resolve relative imports.
- Streamlit installed if intending to use the UI app for further generation.
- Excel file reading capability in the environment where the exported file will be reviewed.

---

## Usage

Run this script from the command line:

```bash
python path/to/this_script.py
```

The script will generate test cases automatically, print summaries and samples to the console, export them to an Excel file, and display next steps.

---

## Extensibility

- Modify `user_story` to generate test cases for other business features.
- Adjust number of test cases generated by changing `num_test_cases` argument.
- Extend categorization logic to include additional test case types.
- Integrate with automated test management systems by extending the export functionality.

---

## Example Output (Console)

```
================================================================================
GENERATING TEST CASES IN USER'S FORMAT
================================================================================

User Story:
As a Financial Advisor,
I want to upload asset details in bulk using an Excel file,
...

--------------------------------------------------------------------------------

🔄 Generating 12 test cases with diverse coverage...

✅ Generated 12 test cases!

Test Case Summary:
--------------------------------------------------------------------------------
  Negative        : 4 test cases
  Positive        : 5 test cases
  UI              : 1 test case
  Edge Case       : 1 test case
  Security        : 1 test case

--------------------------------------------------------------------------------

Sample Test Cases:
================================================================================

[1] Validate missing PAN - Negative
    Layer: Backend Validation
    Type: Negative
    Priority: High
    Scenario: Verify that batch upload rejects records where PAN is missing.
    Preconditions (3):
      User has access to upload dashboard...
      Excel file prepared with 10 records...
      Network connection stable...
    Steps: 5
      1. Open the upload page...
      2. Select file with missing PAN...
      3. Click upload button...
--------------------------------------------------------------------------------

...

📤 Exporting to Excel in user's format...

✅ SUCCESS! Test cases exported to: output/generated_user_format.xlsx

📋 Excel columns:
   1. Test Case ID
   2. Layer
   3. Test Case Scenario
   4. Test Case
   5. Pre-Condition
   6. Test Case Type
   7. Test Steps
   8. Expected Result
   9. Priority

================================================================================
NEXT STEPS:
================================================================================
1. Open the Excel file: output/generated_user_format.xlsx
2. Review the test cases
3. Upload to your test management system
4. Run the Streamlit app to generate more test cases

Command to start app: streamlit run ui/app.py
================================================================================
```

---

# End of Documentation

## File: tests/__init__.py
# Test Files Documentation

This module contains test files designed to validate different aspects of the system:

- **API Tests**: Verify the correctness, reliability, and compliance of the application programming interface.
- **Performance Tests**: Measure and ensure the system meets performance criteria under expected workloads.
- **Bug Fix Tests**: Confirm that identified defects are resolved and do not recur.

These tests play a critical role in maintaining software quality and stability throughout the development lifecycle.

## File: tests/test_api.py
# FastAPI Endpoint Test Script Documentation

This Python script provides a set of test functions for validating the functionality of various FastAPI endpoints in a local API server running at `http://localhost:8000`. It uses the `requests` library to send HTTP requests and display formatted responses, serving as a lightweight integration test suite.

---

## Overview

- **Base URL:** `http://localhost:8000`
- **Purpose:** Test connectivity and feature endpoints of a FastAPI service.
- **Usage:** Run the script directly to execute a series of health checks and data retrieval tests.
- **Dependencies:**  
  - `requests` — for making HTTP requests  
  - `json` — for pretty-printing JSON responses

---

## Test Functions

### 1. `test_health()`

- **Description:**  
  Tests the `/health` endpoint to verify if the API service is running and responsive.
  
- **Method:**  
  `GET /health`
  
- **Output:**  
  - HTTP status code  
  - JSON response content (pretty-printed)

---

### 2. `test_process_requirement()`

- **Description:**  
  Tests the endpoint that processes a textual software requirement and generates related test cases.
  
- **Method:**  
  `POST /process/requirement`
  
- **Request Payload:**

  ```json
  {
    "requirement_text": "...",         // Multiline string describing feature requirements, rules, etc.
    "suite_name": "authentication",   // Suite to which generated test cases will belong
    "auto_apply": false                // Flag to auto-apply generated test cases (false disables auto-apply)
  }
  ```
  
- **Output:**  
  - HTTP status code  
  - On success:  
    - `success`: Boolean indicating success  
    - `summary`: Statistics on generated test cases (`total_test_cases`, `same_count`, `addon_count`, `new_count`)  
  - On failure: Error message text

- **Note:** Requires Azure OpenAI credentials and proper backend configuration.

---

### 3. `test_process_user_story()`

- **Description:**  
  Tests processing of a user story to generate corresponding test cases.
  
- **Method:**  
  `POST /process/user-story`
  
- **Request Payload:**

  ```json
  {
    "title": "Shopping Cart Checkout",
    "description": "As a user, I want to checkout my shopping cart so that I can complete my purchase",
    "acceptance_criteria": [
      "User can review cart items",
      "System calculates total with tax",
      "User can apply discount codes",
      "Payment is processed securely"
    ],
    "business_rules": [
      "Minimum order value: $10",
      "Free shipping over $50",
      "Discount codes can only be used once"
    ],
    "context": "E-commerce checkout flow",
    "suite_name": "checkout",
    "auto_apply": true
  }
  ```
  
- **Output:**  
  - HTTP status code  
  - On success:  
    - `success`: Boolean  
    - `summary`: Statistics regarding generated test cases (`total_test_cases`)  
    - `actions_taken`: List of action descriptions performed during processing  
  - On failure: Error message text

- **Note:** Also requires Azure OpenAI credentials and backend readiness.

---

### 4. `test_get_test_cases()`

- **Description:**  
  Retrieves existing test cases for a specified test suite.
  
- **Method:**  
  `GET /test-cases?suite_name=authentication`
  
- **Output:**  
  - HTTP status code  
  - On success:  
    - Number of test cases found  
    - Displays title and ID of up to the first 3 test cases  
  - On failure: Error message text

---

### 5. `test_get_suites()`

- **Description:**  
  Lists all test suites available in the system.
  
- **Method:**  
  `GET /suites`
  
- **Output:**  
  - HTTP status code  
  - On success:  
    - Number of suites and a comma-separated list of their names  
  - On failure: Error message text

---

### 6. `test_get_statistics()`

- **Description:**  
  Retrieves statistics about the knowledge base, including the total number of test cases.
  
- **Method:**  
  `GET /statistics`
  
- **Output:**  
  - HTTP status code  
  - On success:  
    - Total number of test cases under `knowledge_base` key  
  - On failure: Error message text

---

### 7. `test_get_thresholds()`

- **Description:**  
  Fetches configuration thresholds used by the API, such as similarity thresholds for test case matching.
  
- **Method:**  
  `GET /config/thresholds`
  
- **Output:**  
  - HTTP status code  
  - On success:  
    - `threshold_same`: Threshold value for "same" classification  
    - `threshold_addon_min` and `threshold_addon_max`: Range values for "add-on" classification  
  - On failure: Error message text

---

## Main Execution Logic

- Prints header and instructions.
- Runs a subset of tests by default:
  - Health check  
  - Thresholds  
  - List suites  
  - Statistics
- Processing tests (`test_process_requirement`, `test_process_user_story`, `test_get_test_cases`) are commented out by default because they require additional setup/configuration.
- Catches and handles:
  - Connection errors (when API is not reachable)  
  - Other generic exceptions with error message output

---

## Prerequisites

- The FastAPI API server must be running locally on port 8000.  
  You can start it with:  
  ```
  python api.py
  ```
  or    
  ```
  uvicorn api:app --reload
  ```
- If testing processing endpoints (`_process_requirement`, `_process_user_story`), ensure Azure OpenAI credentials and API access are configured correctly.

---

## How to Use This Script

1. Ensure dependencies are installed:  
   ```
   pip install requests
   ```
2. Start the API server locally.
3. Run this script:  
   ```
   python test_script.py
   ```
4. Observe the printed output for status codes and response contents to verify endpoint behavior.

---

## Notes

- The script is synchronous and uses print statements for clarity.
- Designed for local development and debugging.
- Extensible for additional tests or automated integration into CI pipelines.

---

# End of Documentation

## File: tests/test_description_validation.py
# Module Documentation: Description Validation in Test Case Imports

## Overview

This module contains automated tests to verify that descriptions in test cases are never blank or effectively empty when test cases are generated or imported. The tests cover scenarios involving:

- Parsing individual test cases from JSON-like dictionaries.
- Importing test cases from Excel files.
- Importing test cases from JSON files.

The goal is to ensure that every test case has a meaningful description, falling back to the title or a default phrase if the description is missing or empty.

---

## Functions

### `test_parse_test_case_with_blank_description()`

**Purpose:**
Test the behavior of the `parse_test_case_json` utility function when given test case data with blank or missing descriptions.

**Details:**
- Defines multiple test cases with variations in the `description` and `title` fields:
  - Blank description with a valid title.
  - Missing description key.
  - Description containing only whitespace.
  - Both title and description blank.
  - Valid description (should remain unchanged).
- Calls `parse_test_case_json` to parse each test case dictionary.
- Checks that the resulting `description`:
  - Is non-empty after stripping whitespace.
  - Is not the string `'nan'` (common placeholder for missing data).
  - Contains the expected pattern (usually the title or a default phrase like "functional requirement").
- Prints detailed pass/fail status per test case.
- Returns `True` if all sub-tests pass, otherwise `False`.

---

### `test_excel_import_with_blank_descriptions()`

**Purpose:**
Test importing test cases from an Excel file where some descriptions might be blank or whitespace.

**Details:**
- Constructs a temporary Excel file using a pandas DataFrame with columns:
  - `Title`
  - `Description`
  - `Test Steps`
  - `Expected Outcome`
  - `Priority`
  - `Test Type`
- The `Description` column includes empty strings and whitespace-only strings.
- Uses `import_from_excel` to parse the Excel file into test case objects.
- Validates that each imported test case has a non-blank, non-whitespace description.
- Cleans up the temporary Excel file after testing.
- Prints detailed pass/fail for each test case and returns overall pass status.

---

### `test_json_import_with_blank_descriptions()`

**Purpose:**
Test importing test cases from a JSON file where descriptions can be blank or missing.

**Details:**
- Creates a temporary JSON file containing a list of test case dictionaries with:
  - Blank `description`.
  - Missing `description` key.
  - Description with only whitespace.
- Uses `import_from_json` to read test cases from the temporary JSON file.
- Checks similarly for non-blank, meaningful descriptions.
- Cleans up the temporary JSON file after testing.
- Prints detailed test results and returns overall pass status.

---

## Execution: Main Block

When executed as a standalone script, this module:

1. Runs all three tests in sequence:
   - Parsing individual JSON test case dictionaries.
   - Excel import.
   - JSON import.
2. Prints a summary of results indicating pass/fail status per test.
3. Displays an overall success or failure message.
4. Ensures users have confidence that test case descriptions never remain blank through any import or parsing process.

---

## Dependencies

- **Python Standard Library:** `sys`, `os`, `tempfile`, `json`
- **Third-party Libraries:** `pandas` (used for Excel test case generation with DataFrame)
- **Local module:** Utilities from `core.utils` module:
  - `parse_test_case_json`
  - `import_from_excel`
  - `import_from_json`

These imported utilities are assumed to define the core logic for parsing and importing test cases.

---

## Summary

This test module is a quality assurance tool that verifies the robustness of test case description handling. It ensures descriptions are properly populated from various input data sources and formats, preventing empty or meaningless descriptions in the test management lifecycle. The detailed, printed output aids developers in debugging and validating parsing and import functionality.

## File: tests/test_end_to_end_numbering.py
# Documentation for `test_import_and_rag_search.py`

This module provides end-to-end and edge case tests for importing, parsing, formatting, and verifying test cases, focusing on avoiding double numbering in test steps. It also includes optional integration tests with a Retrieval-Augmented Generation (RAG) engine for vector storage and search of test cases.

---

## Overview

The main goals of this testing script are to:

- Import sample test case data with various step numbering formats.
- Parse test cases using a utility function, ensuring steps are normalized.
- Detect and prevent double numbering of test steps.
- Validate the textual output formatting of test cases using their `to_text()` method.
- (Optional) Test storing parsed test cases into a RAG engine and verify search functionality.
- Test edge cases involving unusual or inconsistent step formats.

---

## Imports and Setup

- The script adds the parent directory to the Python path to allow importing project modules.
- Imports core utilities and models:
  - `parse_test_case_json` from `core.utils` — Parses JSON dictionaries into `TestCase` objects.
  - `RAGEngine` from `engines.rag_engine` — Handles storage and search of test cases using a vector database (e.g., ChromaDB).
  - `TestCaseGenerator` from `engines.test_case_generator` — (Imported but not directly used here.)
  - `TestCase` from `core.models` — Data model for test cases.

---

## Functions

### test_import_and_rag_search()

**Purpose:**  
Runs an end-to-end integration test that:

- Imports predefined test cases with different step numbering styles.
- Parses each test case and checks for double numbering in test step action strings.
- Tests the `to_text()` method output for any remaining double numbering patterns.
- Optionally, demonstrates how to add test cases to the RAG engine (commented out by default to avoid unintended DB changes).
- Summarizes the test results.

**Test Data:**  
Three sample test cases with varied step number formats:

1. Numbered steps with `1.`, `2.`, ... format.
2. Steps numbered as `"Step 1: ..."`.
3. Steps with mixed or missing numbering, e.g., `"4)"`, `"5 -"`, or no numbering at all.

**Key Validation Logic:**

- Detect if step actions begin with redundant numbering like `"1."` or `"1)"` when the step number is already tracked separately.
- Validate that `to_text()` output does not contain double numbering patterns such as `"Step 1: 1."` or `"Step 2: Step 2"`.
- RAG engine storage test is skipped by default to avoid side effects but shows placeholder code for real integration.

**Output:**

- Logs detailed parsing results, highlighting any double numbering issues.
- Prints results of the textual formatting checks.
- Summarizes the verification status with success marks.

---

### test_edge_cases()

**Purpose:**  
Test the parsing utility and step normalization logic using different edge cases and unusual input formats.

**Edge Cases Covered:**

- Empty steps list.
- Steps with no numbering.
- Steps that mix dictionaries (with keys like `"action"` and `"expected_result"`) and strings.
- Steps containing special characters and quotes.

**Process:**

- Each edge case is converted to a `TestCase` object via `parse_test_case_json`.
- Prints basic info about the resulting test case and its steps.
- Catches and reports any exceptions during parsing.

---

## How to Run

The script can be run standalone:

```bash
python test_import_and_rag_search.py
```

Output will display test progress, detected issues if any, and a summary section.

---

## Assumptions and Dependencies

- Requires project modules: `core.utils`, `engines.rag_engine`, and `core.models`.
- The `parse_test_case_json` function must accept a dictionary and return a `TestCase` object with normalized step numbering.
- The `TestCase` model must have a `to_text()` method producing human readable test case text.
- The RAG engine (`RAGEngine`) depends on an external vector DB like ChromaDB; actual insertion calls are commented out to prevent database changes.

---

## Summary

This test script is designed primarily to verify that test cases imported from JSON-like structures are properly parsed to avoid redundant step numbering both in memory and in text output formats. It also provides groundwork for more complex vector-based search integration. The included edge case tests improve robustness against unusual input formats common in manual test case collections.

---

## Example Output Snippet

```
======================================================================
END-TO-END TEST: Import -> Parse -> RAG Storage -> Search
======================================================================

1️⃣  PARSING TEST CASES
---------------------------------------------------------------------

📋 User Login with Valid Credentials (TC_001)
   Steps: 5
   ✅ All steps clean (no double numbering)

📋 User Login with Invalid Password (TC_002)
   Steps: 5
   ❌ Step 1: 'Step 1: Navigate to login page' - DOUBLE NUMBERING!
   ❌ Step 2: 'Step 2: Enter valid email' - DOUBLE NUMBERING!
   ...
   
...

2️⃣  TESTING to_text() OUTPUT
---------------------------------------------------------------------

✅ User Login with Valid Credentials: No double numbering in text output
❌ User Login with Invalid Password: Found 'Step 1: 1.' in text output
...

======================================================================
SUMMARY
======================================================================
✅ Parsed 3 test cases successfully
✅ All test steps properly cleaned (no double numbering)
✅ to_text() output validated

🎉 All checks passed! The fix is working correctly.
======================================================================
```

---

This documentation should help understand the purpose and workings of the testing code and assist in maintaining or extending the test suite.

## File: tests/test_fixes.py
# Test Script Documentation

## Overview

This test script is designed to verify the correctness of JSON parsing and handling of business rules within the test case generation and comparison engine systems. It includes several automated test functions that validate core functionalities like generating test cases from text (with and without explicit business rules), parsing JSON representations of test cases (including those missing business rules), and comparing test cases using the comparison engine.

---

## Modules and Imports

- **test_case_generator**: Provides the `TestCaseGenerator` class which generates test cases from textual requirements.
- **comparison_engine**: Contains the `ComparisonEngine` class used to compare test cases and determine their similarity and business logic consistency.
- **models**: Defines data models, including `TestCase` and `TestStep`, representing test case structure and individual test steps respectively.
- **utils**: Includes utility functions like `parse_test_case_json` for safely parsing JSON into `TestCase` instances.

---

## Function Descriptions

### `test_generate_without_business_rules()`

- **Purpose**: Tests the generation of test cases from a plain textual requirement without any explicit business rules.
- **Process**:
  - Instantiates `TestCaseGenerator`.
  - Defines a simple user profile viewing requirement.
  - Calls `generate_from_text` to generate test cases.
  - Prints the number of generated test cases and details of each including title, business rule (which may be empty), and description.
- **Success Criteria**: Test cases are generated without throwing exceptions.
- **Returns**: `True` if successful, otherwise `False`.

---

### `test_generate_with_business_rules()`

- **Purpose**: Tests generation of test cases from a requirement that explicitly defines business rules and acceptance criteria.
- **Process**:
  - Instantiates `TestCaseGenerator`.
  - Defines a login requirement which includes a set of business rules and acceptance criteria.
  - Calls `generate_from_text` to get test cases.
  - Prints information including title, business rule, and priority of each test case.
- **Success Criteria**: Test cases correctly generated with associated business rules.
- **Returns**: `True` if successful, otherwise `False`.

---

### `test_comparison_json_parsing()`

- **Purpose**: Tests the functionality of the `ComparisonEngine` in comparing two `TestCase` objects, focusing on JSON parsing and result interpretation.
- **Process**:
  - Manually creates two test case objects (`tc1` and `tc2`) with similar but distinct steps and outcomes.
  - Uses `ComparisonEngine.compare_test_cases` to compare them.
  - Prints comparison results, including decision, similarity percentage, business rule matching, behavior matching, and reasoning.
- **Success Criteria**: Comparison runs without errors and outputs meaningful comparison metrics.
- **Returns**: `True` if successful, otherwise `False`.

---

### `test_parse_json_without_business_rule()`

- **Purpose**: Verifies that the JSON parser (via `parse_test_case_json`) can handle input JSON that lacks the `business_rule` field gracefully.
- **Process**:
  - Defines a JSON dictionary representing a test case without a `business_rule`.
  - Parses the JSON into a `TestCase` object.
  - Prints parsed test case details to verify correctness.
- **Success Criteria**: Parsing completes without exceptions, and the missing business rule does not cause failures.
- **Returns**: `True` if successful, otherwise `False`.

---

### `main()`

- **Purpose**: Orchestrates the execution of all above tests and reports summary results.
- **Process**:
  - Prints an introductory header.
  - Executes all individual test functions and collects boolean results.
  - Prints a summary table indicating pass/fail status for each test.
  - Reports overall success or failure.
- **Returns**: `True` if all tests pass, otherwise `False`.

---

## Script Execution

- The script entry point is guarded by `if __name__ == "__main__":`.
- Runs `main()` and exits with code `0` if all tests pass or `1` otherwise.

---

## Summary

This test suite is essential to ensure:

- Robust generation of test cases both with and without defined business rules.
- Correct parsing of test case JSON formats, including edge cases where expected fields (like business rules) are missing.
- Accurate comparison between test cases that assesses similarity, business rule adherence, and behavioral equivalence.

Passing these tests helps maintain confidence in the underlying test case generation and comparison infrastructure, particularly following recent fixes to JSON parsing and business rule handling logic.

## File: tests/test_numbering_fix.py
# Documentation for `test_double_numbering.py`

## Overview

This module provides a suite of tests to verify that double numbering in test step descriptions is properly identified and prevented. It exercises utility functions responsible for detecting existing numbering, removing it, formatting steps with correct numbering, and parsing test cases containing steps that may have inconsistent numbering formats.

The main focus is to ensure that when test steps are processed—whether as strings or dictionaries—no duplicated or redundant numbering prefixes appear in the final representation.

## Imports

- `sys`, `os`: Used to modify the Python path so that the `core` package can be imported.
- From `core.utils`:
  - `has_existing_numbering`: Detects if a step string already contains numbering.
  - `remove_existing_numbering`: Strips numbering from a step string.
  - `format_step_with_number`: Formats a step string by adding numbering intelligently.
  - `parse_test_case_json`: Parses JSON-formatted test case data into `TestCase` objects, processing steps to prevent double numbering.
- From `core.models`:
  - `TestCase`: The model representing a test case, including its steps.

## Test Functions

### 1. `test_has_existing_numbering()`

**Purpose:**  
Check that `has_existing_numbering()` correctly identifies strings that have existing numeric prefixes in various formats, such as:

- `"1. Some action"`
- `"1) Some action"`
- `"Step 1: Some action"`
- `"1 - Some action"`

and correctly return `False` for unnumbered steps.

**Behavior:**  
Prints test results for multiple cases, showing whether the detection matches expectations.

---

### 2. `test_remove_existing_numbering()`

**Purpose:**  
Verify that `remove_existing_numbering()` properly removes various numbering formats from step strings, leaving only the textual action.

**Examples:**

- Input: `"1. Navigate to page"`  
  Output: `"Navigate to page"`

- Input: `"Step 10: Complex action"`  
  Output: `"Complex action"`

**Behavior:**  
Runs multiple test cases and prints pass/fail status.

---

### 3. `test_format_step_with_number()`

**Purpose:**  
Test the behavior of `format_step_with_number(number, text, preserve_existing=True|False)` which applies numbering to a step intelligently:

- When `preserve_existing=True` (default), it preserves existing numbering if detected.
- When `preserve_existing=False`, it normalizes the numbering by removing existing prefixes and adding the correct number.

**Cases tested:**

- Step with existing numbering preserved or normalized.
- Step without any numbering, adding numbering appropriately.

**Behavior:**  
Prints all outcomes with pass/fail status for both modes.

---

### 4. `test_parse_test_case_with_numbered_steps()`

**Purpose:**  
Test `parse_test_case_json()` function with test case JSON data where steps are strings containing numbering prefixes.

**Key checks:**

- The parsed `TestCase` object has properly numbered steps.
- Step actions have numbering removed to prevent double numbering.
- The `to_text()` method of `TestCase` generates output without redundant numbering.

**Behavior:**

- Prints details of parsed steps.
- Checks for any double numbering errors.
- Prints output from `to_text()` method and confirms absence of double numbering.

---

### 5. `test_parse_test_case_with_dict_steps()`

**Purpose:**  
Check `parse_test_case_json()` with test step data given as dictionaries including explicit `step_number`, `action`, and `expected_result` fields.

**Key validations:**

- Step actions with numbering prefixes are cleaned (numbering removed where appropriate).
- `step_number` fields are respected.
- No double numbering remains after parsing.

**Behavior:**

- Prints all steps and associated expected results.
- Reports if numbering was improperly left in action strings.

---

### 6. `test_mixed_numbering()`

**Purpose:**  
Validate parsing of test cases where there is a mixture of numbered and unnumbered steps in arbitrary order.

**Checks:**

- All parsed step actions are cleaned of numbering.
- Step numbering is assigned accordingly.
- Actions match expected cleaned strings without numbering prefixes.

**Behavior:**

- Prints parsed steps side-by-side with expected clear text.
- Flag mismatches with failure icons.

---

## Main Execution Block

When run as a script, all test functions execute sequentially, and results are displayed with clear separators and status indicators (`✅` for pass, `❌` for fail).

## Summary

This testing module ensures that utilities for numbering detection, removal, and formatting work cohesively to prevent duplicated numbering in automated test steps. It supports both string-based and structured dictionary step formats and confirms consistent, clean numbering in parsed test case objects.

---

# Example Usage

Run as a standalone script:

```bash
python test_double_numbering.py
```

This will perform all included tests and output detailed results to the console, helping maintain robustness in handling step numbering within the testing framework.

## File: tests/test_performance.py
# Performance Testing Script Documentation

## Overview

This script benchmarks the performance of the optimized test case generation system, specifically focusing on the `TestCaseManager` class and its ability to process a `UserStory` object. The test measures initialization time, test case generation time, and estimated performance improvements compared to a hypothetical sequential processing baseline.

---

## Script Description

The script defines a function `test_performance()` which:

1. Initializes an instance of `TestCaseManager`.
2. Constructs a sample `UserStory` representing a "User Login Feature" with detailed acceptance criteria and business rules.
3. Uses the `TestCaseManager` to generate test cases from the `UserStory`.
4. Records and reports detailed timings, counts of generated test cases, and a breakdown of result categories.
5. Estimates the performance improvement against a baseline sequential processing time (assumed 10 seconds per test case).

Finally, the script runs `test_performance()` when executed as the main program.

---

## Dependencies

- `time` — standard Python library for tracking execution duration.
- `test_case_manager.TestCaseManager` — the class responsible for managing and generating test cases.
- `models.UserStory` — a data model representing user stories with related metadata.

---

## Function: `test_performance()`

```python
def test_performance():
    """Test the performance of the optimized system"""
```

### Description

Runs a comprehensive performance test of the `TestCaseManager` system by processing a predefined `UserStory`. Outputs include initialization time, test case generation timing, summary statistics, and an estimated performance improvement metric.

### Behavior and Output

- Prints section headers and progress updates to the console.
- Measures and prints:
  - Initialization time of `TestCaseManager`.
  - Time taken to generate test cases from the `UserStory`.
  - Number of test cases generated.
  - Average time spent per test case.
  - Summary counts and percentages of test case categories: same, add-on, and new.
  - Aggregate performance metrics including total processing time and combined initialization plus processing time.
  - Estimated performance improvement percentage assuming a 10-second sequential baseline per test case.

### Input

- No external inputs; the `UserStory` is hardcoded within the function.
  
### Output

- Console output detailing timing and result statistics.

---

## Example Output

```
============================================================
PERFORMANCE TEST - RAG Test Case Manager
============================================================

1. Initializing Test Case Manager...
   ✓ Initialization completed in 0.10s

2. Generating test cases from user story...
   ✓ Generated 15 test cases in 4.50s
   ✓ Average time per test case: 0.30s

3. Results Summary:
   - Total Test Cases: 15
   - Same: 10 (66.7%)
   - Add-on: 3 (20.0%)
   - New: 2 (13.3%)

4. Performance Metrics:
   - Total Processing Time: 4.50s
   - Initialization Time: 0.10s
   - Total Time: 4.60s

5. Estimated Performance Improvement:
   - Sequential Processing (estimated): 150.00s
   - Parallel Processing (actual): 4.50s
   - Improvement: 97.0% faster

============================================================
PERFORMANCE TEST COMPLETED
============================================================
```

---

## Usage

To run the performance test, execute the script directly:

```bash
python performance_test.py
```

Ensure that the `test_case_manager` and `models` modules are available in the Python path.

---

## Notes

- The `sequential_estimate` assumes 10 seconds per test case as a baseline for sequential processing time, which is used only for illustrative performance improvement calculations.
- The `auto_apply` parameter is set to `False` during test case generation to prevent automatic modifications or side effects during the benchmark.
- This script does not return any values and is primarily intended for manual review of printed performance metrics.

---

## Potential Extensions

- Parameterize the user story input for more flexible testing.
- Add command-line arguments to customize test case manager options.
- Integrate with a profiling tool or testing framework for automated benchmarking.
- Output results to a log file or generate visual reports/charts.

---

If you need more details on the `TestCaseManager` or `UserStory` models, please refer to their respective module documentation.

## File: tests/test_type_positive_negative.py
# Documentation for Test Type Validation Code

## Overview
This module provides comprehensive testing to ensure that test case types are correctly validated and normalized to either **"Positive"** or **"Negative"** only. Any test type outside these two valid options defaults to **"Positive"**. This ensures consistency and adherence to defined test typing rules within a testing framework.

The tests cover:
- Direct validation of test type strings.
- Parsing of test case data in JSON format.
- Importing test cases from Excel files with data validation.

## Module Contents
- Imports required utility functions and packages.
- Defines three test functions to validate various use cases.
- Runs all tests if executed as the main module, summarizing pass/fail results.

---

## Imported Utilities
- `validate_test_type(test_type: str) -> str`
  - Normalizes and validates a test type string.
  - Returns `"Positive"` or `"Negative"` based on input, defaulting to `"Positive"` for invalid inputs.
  
- `parse_test_case_json(tc_data: dict) -> TestCase`
  - Parses a test case dictionary, normalizes the test type accordingly, and returns a TestCase object.
  
- `import_from_excel(filepath: str) -> List[TestCase]`
  - Imports test cases from an Excel file, applying validation rules on the test type field.

---

## Functions

### 1. `test_validate_function() -> bool`
Tests the `validate_test_type()` function with various input strings.

- **Purpose:** Ensure the function correctly normalizes valid types and defaults invalid ones to "Positive".
- **Test cases:** A list containing variations in capitalization, whitespace, and invalid strings.
- **Output:** Prints each test input, result, expected value, and pass/fail status.
- **Return:** `True` if all tests pass, else `False`.

---

### 2. `test_parse_json() -> bool`
Tests `parse_test_case_json()` using simulated test case JSON dictionaries.

- **Purpose:** Verify that the parsing correctly applies test type validation.
- **Test cases:** Multiple test cases with valid and invalid `test_type` values.
- **Output:** Prints input test type, parsed test type, expected value, and pass/fail status.
- **Return:** `True` if all parsed test types match expected values, else `False`.

---

### 3. `test_excel_import() -> bool`
Tests importing test cases from an Excel file, ensuring test type fields are validated.

- **Purpose:** Confirm integration of Excel import functionality with test type validation.
- **Process:**
  - Creates a DataFrame simulating Excel data with mixed valid and invalid `Test Type` entries.
  - Writes DataFrame to a temporary Excel file.
  - Imports using `import_from_excel()`.
  - Checks each imported test case's `test_type` against expected normalized values.
- **Output:** Prints row number, input test type, normalized result, expected value, and pass/fail status.
- **Return:** `True` if all rows have expected normalized test types, else `False`.
- **Cleanup:** Removes the temporary Excel file after testing.

---

## Main Execution Block

When run as the main program, the script:
- Prints comprehensive headers and test rules.
- Executes the three test functions in sequence.
- Prints final pass/fail summary per test category.
- Gives an overall success or failure message summarizing the adherence to test type rules.

---

## Rule Summary

- Test types must be **"Positive"** or **"Negative"** only.
- Inputs are case-insensitive and trimmed of whitespace.
- Invalid or unknown test types default to **"Positive"**.

---

## Usage

### To run the tests:
Execute the script directly:
```bash
python test_type_validation.py
```

### Expected Behavior:
- Outputs detailed testing steps.
- Shows pass/fail indicators for each input.
- Final summary confirms whether all validations passed or not.

---

## Dependencies

- Python standard libraries: `sys`, `os`, `tempfile`
- Third-party packages: `pandas`, `openpyxl`
- `core.utils` module exporting:
  - `validate_test_type`
  - `parse_test_case_json`
  - `import_from_excel`

---

## Notes

- This testing script is designed for development and CI use to enforce strict test type rules.
- Adjustments to test types or default behavior must update both the utility functions and these tests.
- The temporary Excel file approach ensures no side-effects or manual file management during test runs.

---

# End of Documentation

## File: ui/__init__.py
# UI Components - Streamlit App and API

This module contains the UI components for a Streamlit application and its associated API. It provides user interface elements and API endpoints to support interactive web application features built with Streamlit.

## Overview

- **Streamlit App:** Defines the frontend interactive components, layout, and user input handling for the web app.
- **API:** Provides backend endpoints to support data fetching, processing, or other functionalities required by the Streamlit UI.

## Contents

- Streamlit UI components (widgets, buttons, input forms)
- API endpoints for serving and receiving data
- Integration logic between Streamlit app and API

## Usage

1. **Run the API server:** Start the API backend to serve necessary data or business logic.
2. **Launch Streamlit app:** Run the Streamlit app to load the UI components.
3. **Interact with the app:** Use UI components to interact with the API and perform intended operations.

## Example

```bash
# Run API server (example)
python api_server.py

# Run Streamlit app
streamlit run app.py
```

## Notes

- Ensure that the API endpoints are accessible from the Streamlit app environment.
- This module assumes familiarity with Streamlit framework and RESTful API design.

---

*For detailed documentation of individual components, please refer to their specific docstrings or source code comments.*

## File: ui/api.py
# RAG Test Case Manager API Documentation

This FastAPI-based REST API enables intelligent test case management using Retrieval-Augmented Generation (RAG). The API provides endpoints to process requirements and user stories to generate test cases, manage test suites, apply decisions on test case comparisons, export test suite data, and retrieve system statistics and configuration.

---

## Table of Contents
1. [Overview](#overview)
2. [Getting Started](#getting-started)
3. [API Endpoints](#api-endpoints)
    - [General](#general)
    - [Processing](#processing)
    - [Test Cases](#test-cases)
    - [Test Suites](#test-suites)
    - [Statistics](#statistics)
    - [Export](#export)
    - [Configuration](#configuration)
4. [Data Models](#data-models)
5. [Running the API](#running-the-api)
6. [Configuration](#configuration-details)
7. [Notes](#notes)

---

## Overview

The RAG Test Case Manager API helps teams create, manage, and export test cases derived from requirement texts or user stories. Key features include:

- Processing requirement texts or user stories to automatically generate test cases.
- Applying decisions automatically or manually to test case comparison results.
- Retrieving and filtering test cases and suites.
- Exporting test cases into multiple file formats with optional filters.
- Viewing system health and statistics.

---

## Getting Started

- **Base URL:** The API runs by default at `http://localhost:8000`
- **Documentation:** Interactive Swagger UI available at `/docs`
- **Redoc Documentation:** Available at `/redoc`

---

## API Endpoints

### General

#### `GET /`

Root endpoint returning basic API information.

**Response:**

```json
{
  "message": "RAG Test Case Manager API",
  "version": "1.0.0",
  "docs": "/docs",
  "health": "/health"
}
```

---

#### `GET /health`

Returns health status, current timestamp, configuration validity, and total test cases count.

**Response Model:** `HealthResponse`

```json
{
  "status": "healthy",
  "timestamp": "2024-06-27T12:00:00",
  "config_valid": true,
  "total_test_cases": 123
}
```

---

### Processing

#### `POST /process/requirement`

Processes plain requirement text and generates test cases.

**Request Model:** `RequirementTextRequest`

- `requirement_text` (str, required): The requirement text to process.
- `suite_name` (str, optional, default "default"): Test suite to add test cases.
- `auto_apply` (bool, optional, default false): Auto-apply decisions.
- `num_test_cases` (int, optional, 5-30): Number of test cases to generate (defaults to config).

**Response Model:** `ProcessingResult`

---

#### `POST /process/user-story`

Processes a user story object for test case generation.

**Request Model:** `UserStoryRequest`

- `title` (str, required): Title of the user story.
- `description` (str, required): Description text.
- `acceptance_criteria` (list of str, optional): Acceptance criteria.
- `business_rules` (list of str, optional): Associated business rules.
- `context` (str, optional): Additional context.
- `suite_name` (str, optional, default "default"): Test suite to add test cases.
- `auto_apply` (bool, optional, default false): Auto-apply decisions.
- `num_test_cases` (int, optional, 5-30): Number of test cases to generate (defaults to config).

**Response Model:** `ProcessingResult`

---

#### `POST /apply-decision`

Apply a decision from a test case comparison.

**Request Model:** `ApplyDecisionRequest`

- `test_case` (TestCase, required): The test case involved.
- `comparison` (ComparisonResult, required): Comparison data.
- `suite_name` (str, optional, default "default"): Target test suite.
- `user_approved` (bool, optional, default true): Whether user approved or rejected the decision.

**Response:**

```json
{
  "success": true,
  "message": "Decision applied successfully",
  "action": "<description_of_action_taken>"
}
```

---

### Test Cases

#### `GET /test-cases`

Retrieve all test cases in a specific suite.

**Query Parameters:**

- `suite_name` (str, optional, default "default"): Test suite name.

**Response:** List of `TestCase`

---

#### `GET /test-cases/{test_case_id}`

Retrieve a specific test case by ID.

**Path Parameter:**

- `test_case_id` (str): Test case identifier.

**Query Parameter:**

- `suite_name` (str, optional, default "default"): Test suite name.

**Response:** `TestCase`

---

#### `GET /test-cases/filtered`

Retrieve filtered test cases from a suite.

**Query Parameters:**

- `suite_name` (str, optional, default "default"): Test suite name.
- `priorities` (str, optional): Comma-separated priorities (e.g., `"High,Critical"`).
- `test_types` (str, optional): Comma-separated test types (e.g., `"Functional,Integration"`).
- `tags` (str, optional): Comma-separated tags (e.g., `"login,authentication"`).
- `is_regression` (bool, optional): Filter regression tests (`true` or `false`).

**Response:** List of `TestCase`

---

### Test Suites

#### `GET /suites`

List all available test suites.

**Response:** List of suite name strings.

---

### Statistics

#### `GET /statistics`

Returns system-level statistics including knowledge base information.

**Response:** JSON dictionary with relevant stats.

---

### Export

#### `POST /export/test-suite`

Export a full test suite into a downloadable file.

**Request Model:** `ExportRequest`

- `suite_name` (str, required): Name of the test suite to export.
- `format` (str, optional, default "excel"): Export format - one of `"excel"`, `"csv"`, or `"json"`.

**Response:** File download response (`FileResponse`)

---

#### `POST /export/filtered-test-suite`

Export a filtered subset of test suite test cases.

**Request Model:** `FilteredExportRequest`

- `suite_name` (str, required): Name of the test suite.
- `format` (str, optional, default "excel"): Export file format.
- `priorities` (list of str, optional): Filter by priorities.
- `test_types` (list of str, optional): Filter by test types.
- `tags` (list of str, optional): Filter by tags.
- `is_regression` (bool, optional): Filter regression or non-regression tests.

**Response:** File download response (`FileResponse`)

---

### Configuration

#### `GET /config/thresholds`

Retrieve current similarity threshold configuration values.

**Response Example:**

```json
{
  "threshold_same": 0.85,
  "threshold_addon_min": 0.6,
  "threshold_addon_max": 0.8
}
```

---

## Data Models

### `RequirementTextRequest`

- `requirement_text` (str): Requirement text input.
- `suite_name` (str): Test suite name.
- `auto_apply` (bool): Auto-apply decisions.
- `num_test_cases` (int, optional): Number of test cases (5-30).

### `UserStoryRequest`

- `title` (str)
- `description` (str)
- `acceptance_criteria` (list[str])
- `business_rules` (list[str])
- `context` (str, optional)
- `suite_name` (str)
- `auto_apply` (bool)
- `num_test_cases` (int, optional)

### `ApplyDecisionRequest`

- `test_case` (`TestCase`)
- `comparison` (`ComparisonResult`)
- `suite_name` (str)
- `user_approved` (bool)

### `ExportRequest`

- `suite_name` (str)
- `format` (str)

### `FilteredExportRequest`

- `suite_name` (str)
- `format` (str)
- `priorities` (list[str], optional)
- `test_types` (list[str], optional)
- `tags` (list[str], optional)
- `is_regression` (bool, optional)

### `ProcessingResult`

- `success` (bool)
- `message` (str)
- `generated_test_cases` (list[`TestCase`])
- `results` (list[dict])
- `actions_taken` (list[str])
- `summary` (dict)

### `HealthResponse`

- `status` (str)
- `timestamp` (datetime)
- `config_valid` (bool)
- `total_test_cases` (int)

**Note:** `TestCase`, `ComparisonResult`, `UserStory`, and `DecisionType` classes are imported from the internal domain models and encapsulate core domain data structures.

---

## Running the API

Run the API server with:

```bash
python api.py
```

Or using uvicorn directly:

```bash
uvicorn api:app --host 0.0.0.0 --port 8000 --reload --log-level info
```

**Startup messages:**

- Warning if Azure OpenAI credentials are missing.
- API documentation and health check URLs.

---

## Configuration Details

- **Config Validation:** The system checks if Azure OpenAI keys and other settings are valid on startup using `Config.validate()`.
- **CORS:** Configured to allow all origins (`allow_origins=["*"]`) - this should be locked down in production deployments.
- **Export Directory:** Exports are saved to a configured directory (`Config.TEST_SUITE_OUTPUT`).
- **Thresholds:** Similarity thresholds for RAG matching can be accessed and possibly tuned via `/config/thresholds`.

---

## Notes

- Error handling returns `HTTP 500` with error messages for unexpected failures.
- Exported filenames include timestamp and descriptive filters for clarity.
- Filtering in retrieval endpoints supports multiple criteria for granular access.
- The system is designed with asynchronous FastAPI endpoints, optimized for concurrency.

---

For usage examples and detailed integration info, please refer to the interactive OpenAPI documentation at `/docs`.

## File: ui/app.py
# RAG-based Test Case Management System — Streamlit UI Documentation

This module implements a Streamlit-based user interface for managing software test cases using Retrieval-Augmented Generation (RAG). It allows importing existing test cases, processing new requirements to generate and analyze test cases via AI-driven techniques, viewing test cases, and exporting test suites with advanced filtering options.

---

## Table of Contents

- [Overview](#overview)
- [Page Configuration and Styles](#page-configuration-and-styles)
- [Session State Management](#session-state-management)
- [Functions](#functions)
  - [initialize_manager()](#initialize_manager)
  - [main()](#main)
- [User Interface Layout](#user-interface-layout)
  - [Sidebar - Configuration & Export Features](#sidebar---configuration--export-features)
  - [Tabs](#tabs)
    - [Tab 1: Import Knowledge Base (KB)](#tab-1-import-knowledge-base-kb)
    - [Tab 2: Process Requirements](#tab-2-process-requirements)
    - [Tab 3: View Test Cases](#tab-3-view-test-cases)
    - [Tab 4: Regression Suite](#tab-4-regression-suite)
- [External Dependencies](#external-dependencies)
- [Error Handling and User Guidance](#error-handling-and-user-guidance)

---

## Overview

This Streamlit UI acts as the front-end for an intelligent test case management system leveraging RAG techniques to generate, analyze, and manage software test cases.

Features:

- Import existing test cases from Excel or JSON into the knowledge base.
- Process textual or structured requirements (user stories) to auto-generate test cases.
- Analyze test cases with similarity, confidence, and recommendation indicators.
- View, filter, and export test cases and regression suites.
- Handle database initialization and corrupted persistent stores robustly.

---

## Page Configuration and Styles

- Sets the Streamlit page title: **"RAG Test Case Manager"**.
- Uses a wide layout with an initially expanded sidebar.
- Defines custom CSS styles for headers, cards, and decision highlights (Same, Add-on, New) to enhance UI clarity.

---

## Session State Management

The following keys are maintained in `st.session_state`:

- `manager`: instance of `TestCaseManager` handling core logic.
- `results`: dictionary containing the latest processed test case analysis results.
- `suite_name`: string holding the current test suite name (default: `"default"`).

Initialization ensures a singleton `manager` instance for session persistence.

---

## Functions

### initialize_manager()

Initializes the test case manager (`TestCaseManager`):

- Checks existence and health of persistent directories like `Config.CHROMA_PERSIST_DIRECTORY`.
- Attempts to instantiate `TestCaseManager`.
- Detects and recovers from corrupted databases by cleaning and recreating directories.
- Displays status messages, warnings, and guidance for manual server restarts if needed.
- Returns `True` if initialization is successful; otherwise, `False`.

---

### main()

Entry point and main app rendering function:

- Displays header and app introduction.
- Builds sidebar with configuration validation, statistics, and export capabilities.
- Defines four main tabs with different functionality.
- Handles user input, triggering back-end processing, result visualization, and file exports.
- Manages user interaction, including buttons, file uploads, filters, and decision application.

---

## User Interface Layout

### Sidebar - Configuration & Export Features

Contains:

- Configuration validation (checking Azure OpenAI credentials).
- Initialization of the `TestCaseManager`.
- Shows total test cases count.
- Export section:
  - Export all test cases in Excel.
  - Export all regression tests.
  - Advanced export with filters on priorities, test types, tags, and regression inclusion.
- Downloads are offered as `.xlsx` files with proper MIME types.
- Displays success/error messages and updated statistics.

---

### Tabs

#### Tab 1: Import Knowledge Base (KB)

- Title: **Import Existing Test Cases**
- Allows file upload from Excel (`.xlsx`, `.xls`) or JSON (`.json`).
- Displays format requirements based on file type.
- Upon clicking "Import Test Cases":
  - Temporarily saves uploaded file.
  - Calls `import_existing_test_cases()` on `TestCaseManager`.
  - Displays summary with imported count and errors.
  - Shows up to first 10 imported test case details in expandable sections.
  - Updates and shows knowledge base statistics.

#### Tab 2: Process Requirements

Two input methods for processing new requirements:

- **Text Input**: multi-line text input for user stories, business requirements, or product requirements.
- **User Story Form**: structured input including title, description, acceptance criteria, business rules, and optional context.

Features:

- Option to auto-apply decisions (`auto_apply`).
- On submission, calls `process_requirement_text()` or `process_user_story()` on `TestCaseManager`.
- Displays summarized statistics of newly processed test cases: total, same, add-on, new, with metrics.
- Provides export buttons:
  - Multi-sheet Excel export including all, modified, and new test cases.
  - User format Excel export with well-structured columns.
- Shows detailed results per test case with decision, reasoning, similarity, confidence, recommendations, and coverage expansion.
- Allows manual decision application if auto-apply is off.

#### Tab 3: View Test Cases

- Displays all test cases for current suite.
- Offers export in user format.
- Each test case shown in expandable view including:
  - ID, description, business rules, priority, tags, versions, timestamps.
  - Preconditions, test steps (with expected results), expected outcome.

#### Tab 4: Regression Suite

- Focuses on test cases marked for regression.
- Shows summary metrics:
  - Total tests, regression tests, high/critical, critical only.
- Progress bar representing regression coverage percentage.
- Filters to show all regression, high & critical only, or critical only tests.
- Allows detailed viewing as expandable sections with full metadata and steps.
- If no regression tests found, provides tips for generating or importing.

---

## External Dependencies

- **Streamlit**: Web UI framework.
- Internal imports:
  - `core.models` — UserStory, TestCase, DecisionType model classes.
  - `engines.test_case_manager` — TestCaseManager core engine.
  - `config.config` — Configuration management.
  - `core.utils` — Utility functions (e.g., ID generation, export helpers).
- Standard libraries: `os`, `sys`, `tempfile`, `shutil`, `datetime`.

---

## Error Handling and User Guidance

- Extensive try-except blocks to catch initialization, import, export, and processing errors.
- On failure, displays helpful error messages and guidance for recovery steps.
- Suggests server restarts to reset connections or rebuild corrupted persistent stores.
- Warnings and info prompts to guide user interaction and input expectations.

---

# Summary

This module provides a comprehensive front-end application for AI-enhanced test case management, including seamless import, processing, review, and export capabilities with user-friendly controls, persistent state management, and robust data handling.

---

# How to Run

1. Ensure environment variables for Azure OpenAI credentials are set and `.env` file is configured.
2. Install dependencies listed in requirements, including Streamlit.
3. Run the app with:

```bash
streamlit run ui/app.py
```

4. Access UI via the local Streamlit server URL provided.

---

End of Documentation.

