# Project Architecture & Flow Diagrams

*Generated on: Mon Feb 16 17:05:20 IST 2026*

## Table of Contents

1. [System Architecture](#system-architecture)
2. [Module Dependencies](#module-dependencies)
3. [Class Diagram](#class-diagram)
4. [Sequence Diagram](#sequence-diagram)
5. [Process Flowchart](#process-flowchart)
6. [AI-Generated Architecture](#ai-generated-architecture)

## System Architecture

Overview of the system's high-level architecture:

```mermaid
flowchart TD
    Start([Start]) --> Input[User Input: Requirements]
    Input --> Parse[Parse Requirements]
    Parse --> Search[Search Knowledge Base]
    Search --> Decision{Similar Cases Found?}
    
    Decision -->|Yes| Analyze[Analyze Similarity Score]
    Decision -->|No| Generate[Generate New Test Cases]
    
    Analyze --> Score{Score > 0.99?}
    Score -->|Yes| Return[Return Existing Cases]
    Score -->|No| Enhance{Score 0.60-0.85?}
    
    Enhance -->|Yes| Augment[Augment with Add-ons]
    Enhance -->|No| Generate
    
    Augment --> Combine[Combine Existing + New]
    Generate --> Store[Store in Vector DB]
    Combine --> Store
    Return --> Format[Format Output]
    Store --> Format
    Format --> End([End])
    
    style Start fill:#90EE90
    style End fill:#FFB6C1
    style Decision fill:#FFD700
    style Score fill:#FFD700
    style Enhance fill:#FFD700
```

## Module Dependencies

Dependency graph showing relationships between modules:

```mermaid
graph TB
    M0[create_regression_suite]
    M1[generate_docs]
    M2[test_user_format_generation]
    M3[test_distribution]
    M4[generate_diagrams]
    subgraph ui_dir[ui]
        M5[__init__]
        M6[api]
        M7[app]
    end
    subgraph core_dir[core]
        M8[knowledge_base]
        M9[models]
        M10[__init__]
        M11[utils]
    end
    subgraph config_dir[config]
        M12[config]
        M13[__init__]
    end
    subgraph tests_dir[tests]
        M14[test_description_validation]
        M15[__init__]
        M16[test_type_positive_negative]
        M17[test_performance]
        M18[test_fixes]
        M19[test_api]
        M20[test_end_to_end_numbering]
        M21[test_numbering_fix]
    end
    subgraph engines_dir[engines]
        M22[test_case_manager]
        M23[__init__]
        M24[embeddings]
        M25[rag_engine]
        M26[context_engineering]
        M27[test_case_generator]
        M28[comparison_engine]
        M29[test_case_updater]
    end
    subgraph examples_dir[examples]
        M30[example_context_engineering]
        M31[import_example]
        M32[__init__]
        M33[example]
    end
    subgraph scripts_dir[scripts]
        M34[test_llm_apis]
        M35[create_excel_template]
        M36[add_diverse_test_cases]
        M37[format_test_cases_for_excel]
        M38[__init__]
    end
    M1 --> M16
    M2 --> M16
    M2 --> M27
    M2 --> M11
    M2 --> M12
    M3 --> M11
    M3 --> M12
    M4 --> M16
    M6 --> M16
    M6 --> M9
    M6 --> M22
    M6 --> M12
    M6 --> M11
    M7 --> M16
    M7 --> M9
    M7 --> M22
    M7 --> M12
    M7 --> M11
    M7 --> M11
    M7 --> M11
    M7 --> M11
    M8 --> M16
    M8 --> M9
    M8 --> M11
    M8 --> M12
    M8 --> M11
    M10 --> M9
    M10 --> M11
    M10 --> M8
    M11 --> M0
    M11 --> M9
    M11 --> M12
    M11 --> M16
    M11 --> M9
    M12 --> M16
    M13 --> M12
    M14 --> M16
    M14 --> M11
    M16 --> M16
    M16 --> M11
    M16 --> M11
    M17 --> M22
    M17 --> M9
    M18 --> M27
    M18 --> M28
    M18 --> M9
    M18 --> M11
    M20 --> M16
    M20 --> M11
    M20 --> M25
    M20 --> M27
    M20 --> M9
    M21 --> M16
    M21 --> M11
    M21 --> M9
    M22 --> M16
    M22 --> M9
    M22 --> M25
    M22 --> M27
    M22 --> M28
    M22 --> M8
    M22 --> M12
    M22 --> M11
    M22 --> M11
    M22 --> M11
    M23 --> M25
    M23 --> M24
    M23 --> M28
    M23 --> M27
    M23 --> M22
    M23 --> M26
    M24 --> M16
    M24 --> M12
    M25 --> M16
    M25 --> M9
    M25 --> M24
    M25 --> M12
    M26 --> M16
    M26 --> M9
    M26 --> M12
    M27 --> M16
    M27 --> M12
    M27 --> M9
    M27 --> M11
    M27 --> M26
    M27 --> M0
    M27 --> M0
    M28 --> M16
    M28 --> M12
    M28 --> M9
    M28 --> M24
    M28 --> M26
    M28 --> M11
    M28 --> M0
    M30 --> M16
    M30 --> M27
    M30 --> M25
    M30 --> M26
    M31 --> M16
    M31 --> M22
    M31 --> M9
    M31 --> M11
    M33 --> M16
    M33 --> M9
    M33 --> M22
    M33 --> M11
    M34 --> M16
    M36 --> M16
    M36 --> M11
    M37 --> M16
    M37 --> M9
    M37 --> M8
```

## Class Diagram

Main classes and their methods:

```mermaid
classDiagram
    class RequirementTextRequest {
    }
    class UserStoryRequest {
    }
    class ProcessingResult {
    }
    class ApplyDecisionRequest {
    }
    class ExportRequest {
    }
    class FilteredExportRequest {
    }
    class HealthResponse {
    }
    class KnowledgeBase {
        +__init__()
        +_load_existing_suites()
        +create_test_suite()
        +get_test_suite()
        +add_test_case_to_suite()
    }
    class DecisionType {
        +to_text()
        +add_test_case()
        +get_test_case_by_id()
        +update_test_case()
    }
    class TestStep {
        +to_text()
        +add_test_case()
        +get_test_case_by_id()
        +update_test_case()
    }
    class TestCase {
        +to_text()
        +add_test_case()
        +get_test_case_by_id()
        +update_test_case()
    }
    class ComparisonResult {
        +to_text()
        +add_test_case()
        +get_test_case_by_id()
        +update_test_case()
    }
    class TestSuite {
        +to_text()
        +add_test_case()
        +get_test_case_by_id()
        +update_test_case()
    }
    class UserStory {
        +to_text()
        +add_test_case()
        +get_test_case_by_id()
        +update_test_case()
    }
    class Config {
        +validate()
        +create_directories()
    }
```

## Sequence Diagram

Typical workflow sequence:

```mermaid
sequenceDiagram
    participant User
    participant API
    participant RAGEngine
    participant KnowledgeBase
    participant TestGenerator
    participant VectorDB
    
    User->>API: Request test case generation
    API->>RAGEngine: Initialize with requirements
    RAGEngine->>KnowledgeBase: Load existing test cases
    KnowledgeBase->>VectorDB: Query similar cases
    VectorDB-->>KnowledgeBase: Return matches
    KnowledgeBase-->>RAGEngine: Provide context
    RAGEngine->>TestGenerator: Generate new tests
    TestGenerator->>TestGenerator: Apply templates
    TestGenerator-->>RAGEngine: Return generated tests
    RAGEngine->>VectorDB: Store new embeddings
    RAGEngine-->>API: Return test cases
    API-->>User: Display results
```

## Process Flowchart

Detailed process flow:

```mermaid
flowchart TD
    Start([Start]) --> Input[User Input: Requirements]
    Input --> Parse[Parse Requirements]
    Parse --> Search[Search Knowledge Base]
    Search --> Decision{Similar Cases Found?}
    
    Decision -->|Yes| Analyze[Analyze Similarity Score]
    Decision -->|No| Generate[Generate New Test Cases]
    
    Analyze --> Score{Score > 0.99?}
    Score -->|Yes| Return[Return Existing Cases]
    Score -->|No| Enhance{Score 0.60-0.85?}
    
    Enhance -->|Yes| Augment[Augment with Add-ons]
    Enhance -->|No| Generate
    
    Augment --> Combine[Combine Existing + New]
    Generate --> Store[Store in Vector DB]
    Combine --> Store
    Return --> Format[Format Output]
    Store --> Format
    Format --> End([End])
    
    style Start fill:#90EE90
    style End fill:#FFB6C1
    style Decision fill:#FFD700
    style Score fill:#FFD700
    style Enhance fill:#FFD700
```

## AI-Generated Architecture

AI-generated comprehensive architecture diagram:


## Module Summary

Total Modules: 39

| Module | Classes | Functions | Imports |
|--------|---------|-----------|----------|
| config/__init__.py | 0 | 0 | 1 |
| config/config.py | 1 | 2 | 3 |
| core/__init__.py | 0 | 0 | 3 |
| core/knowledge_base.py | 1 | 11 | 9 |
| core/models.py | 6 | 4 | 4 |
| core/utils.py | 0 | 21 | 11 |
| create_regression_suite.py | 0 | 2 | 3 |
| engines/__init__.py | 0 | 0 | 6 |
| engines/comparison_engine.py | 1 | 7 | 12 |
| engines/context_engineering.py | 1 | 9 | 7 |
| engines/embeddings.py | 1 | 5 | 8 |
| engines/rag_engine.py | 1 | 10 | 9 |
| engines/test_case_generator.py | 1 | 9 | 12 |
| engines/test_case_manager.py | 1 | 16 | 13 |
| engines/test_case_updater.py | 0 | 0 | 0 |
| examples/__init__.py | 0 | 0 | 0 |
| examples/example.py | 0 | 2 | 5 |
| examples/example_context_engineering.py | 0 | 3 | 6 |
| examples/import_example.py | 0 | 3 | 6 |
| generate_diagrams.py | 0 | 7 | 4 |
| generate_docs.py | 0 | 0 | 2 |
| scripts/__init__.py | 0 | 0 | 0 |
| scripts/add_diverse_test_cases.py | 0 | 1 | 6 |
| scripts/create_excel_template.py | 0 | 0 | 2 |
| scripts/format_test_cases_for_excel.py | 0 | 2 | 6 |
| scripts/test_llm_apis.py | 0 | 5 | 7 |
| test_distribution.py | 0 | 0 | 3 |
| test_user_format_generation.py | 0 | 0 | 5 |
| tests/__init__.py | 0 | 0 | 0 |
| tests/test_api.py | 0 | 7 | 2 |
| tests/test_description_validation.py | 0 | 3 | 6 |
| tests/test_end_to_end_numbering.py | 0 | 2 | 7 |
| tests/test_fixes.py | 0 | 5 | 5 |
| tests/test_numbering_fix.py | 0 | 6 | 4 |
| tests/test_performance.py | 0 | 1 | 3 |
| tests/test_type_positive_negative.py | 0 | 3 | 6 |
| ui/__init__.py | 0 | 0 | 0 |
| ui/api.py | 7 | 0 | 13 |
| ui/app.py | 0 | 2 | 14 |
