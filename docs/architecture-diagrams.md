# Project Architecture & Flow Diagrams

*Generated on: Mon Jun 29 05:42:30 UTC 2026*

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
    M0[test_distribution]
    M1[test_user_format_generation]
    M2[generate_diagrams]
    M3[generate_docs]
    M4[create_regression_suite]
    subgraph core_dir[core]
        M5[__init__]
        M6[models]
        M7[utils]
        M8[knowledge_base]
    end
    subgraph scripts_dir[scripts]
        M9[__init__]
        M10[create_excel_template]
        M11[format_test_cases_for_excel]
        M12[test_llm_apis]
        M13[add_diverse_test_cases]
    end
    subgraph ui_dir[ui]
        M14[__init__]
        M15[app]
        M16[api]
    end
    subgraph config_dir[config]
        M17[__init__]
        M18[config]
    end
    subgraph engines_dir[engines]
        M19[test_case_updater]
        M20[__init__]
        M21[test_case_generator]
        M22[comparison_engine]
        M23[embeddings]
        M24[context_engineering]
        M25[test_case_manager]
        M26[rag_engine]
    end
    subgraph tests_dir[tests]
        M27[__init__]
        M28[test_api]
        M29[test_end_to_end_numbering]
        M30[test_numbering_fix]
        M31[test_fixes]
        M32[test_description_validation]
        M33[test_performance]
        M34[test_type_positive_negative]
    end
    subgraph examples_dir[examples]
        M35[__init__]
        M36[import_example]
        M37[example]
        M38[example_context_engineering]
    end
    M0 --> M7
    M0 --> M18
    M1 --> M34
    M1 --> M21
    M1 --> M7
    M1 --> M18
    M2 --> M34
    M3 --> M34
    M5 --> M6
    M5 --> M7
    M5 --> M8
    M7 --> M4
    M7 --> M6
    M7 --> M18
    M7 --> M34
    M7 --> M6
    M8 --> M34
    M8 --> M6
    M8 --> M7
    M8 --> M18
    M8 --> M7
    M11 --> M34
    M11 --> M6
    M11 --> M8
    M12 --> M34
    M13 --> M34
    M13 --> M7
    M15 --> M34
    M15 --> M6
    M15 --> M25
    M15 --> M18
    M15 --> M7
    M15 --> M7
    M15 --> M7
    M15 --> M7
    M16 --> M34
    M16 --> M6
    M16 --> M25
    M16 --> M18
    M16 --> M7
    M17 --> M17
    M18 --> M34
    M20 --> M26
    M20 --> M23
    M20 --> M22
    M20 --> M21
    M20 --> M25
    M20 --> M24
    M21 --> M34
    M21 --> M18
    M21 --> M6
    M21 --> M7
    M21 --> M24
    M21 --> M4
    M21 --> M4
    M22 --> M34
    M22 --> M18
    M22 --> M6
    M22 --> M23
    M22 --> M24
    M22 --> M7
    M22 --> M4
    M23 --> M34
    M23 --> M18
    M24 --> M34
    M24 --> M6
    M24 --> M18
    M25 --> M34
    M25 --> M6
    M25 --> M26
    M25 --> M21
    M25 --> M22
    M25 --> M8
    M25 --> M18
    M25 --> M7
    M25 --> M7
    M25 --> M7
    M26 --> M34
    M26 --> M6
    M26 --> M23
    M26 --> M18
    M29 --> M34
    M29 --> M7
    M29 --> M26
    M29 --> M21
    M29 --> M6
    M30 --> M34
    M30 --> M7
    M30 --> M6
    M31 --> M21
    M31 --> M22
    M31 --> M6
    M31 --> M7
    M32 --> M34
    M32 --> M7
    M33 --> M25
    M33 --> M6
    M34 --> M34
    M34 --> M7
    M34 --> M7
    M36 --> M34
    M36 --> M25
    M36 --> M6
    M36 --> M7
    M37 --> M34
    M37 --> M6
    M37 --> M25
    M37 --> M7
    M38 --> M34
    M38 --> M21
    M38 --> M26
    M38 --> M24
```

## Class Diagram

Main classes and their methods:

```mermaid
classDiagram
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
    class KnowledgeBase {
        +__init__()
        +_load_existing_suites()
        +create_test_suite()
        +get_test_suite()
        +add_test_case_to_suite()
    }
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

```mermaid
flowchart TD
    %% System Architecture and Components
    subgraph Core ["core"]
        direction TB
        models["models.py\n6 classes, 4 functions"]
        utils["utils.py\n0 classes, 21 functions"]
        kb["knowledge_base.py\n1 class, 11 functions"]
    end

    subgraph Scripts ["scripts"]
        direction TB
        scripts_init["__init__.py"]
    end

    subgraph Root_Files ["Root Modules"]
        direction TB
        test_dist["test_distribution.py\n0 classes, 0 functions"]
        test_user_format["test_user_format_generation.py\n0 classes, 0 functions"]
        gen_diagrams["generate_diagrams.py\n0 classes, 7 functions"]
        gen_docs["generate_docs.py\n0 classes, 0 functions"]
        regression_suite["create_regression_suite.py\n0 classes, 2 functions"]
    end

    core_init["core/__init__.py"]

    %% Architecture - show core as central library
    Root_Files --> core_init
    Scripts --> core_init
    core_init --> models
    core_init --> utils
    core_init --> kb

    %% Data Flow Annotations
    %% Assumptions based on typical architecture:

    %% generate_diagrams.py uses core models, kb, utils
    gen_diagrams --> models
    gen_diagrams --> kb
    gen_diagrams --> utils

    %% create_regression_suite.py uses core models and utils
    regression_suite --> models
    regression_suite --> utils

    %% test modules depend on core and scripts
    test_dist --> core_init
    test_user_format --> core_init

    %% generate_docs.py may depend on core (often true in doc gen)
    gen_docs --> core_init

    %% Scripts/__init__.py links to core_init (maybe helpers or extensions)
    scripts_init --> core_init

    %% Component Interactions (simplified)
    models -- provides data classes --> utils
    kb -- provides knowledge base interfaces --> models
    kb -- utility functions --> utils

    %% Data flow paths
    gen_diagrams -- generates diagrams from --> models
    gen_diagrams -- queries --> kb
    gen_diagrams -- uses utils for processing --> utils

    regression_suite -- creates regression tests using --> models
    regression_suite -- uses utility functions --> utils

    test_dist -- runs tests on --> core_init
    test_user_format -- runs tests on --> core_init

    gen_docs -- generates documentation from --> core_init

    %% Additional Notes
    classDef coreModule fill:#f9f,stroke:#333,stroke-width:2px;
    class models,utils,kb coreModule;

    classDef scriptModule fill:#bbf,stroke:#333,stroke-width:2px;
    class scripts_init scriptModule;

    classDef rootModule fill:#bfb,stroke:#333,stroke-width:2px;
    class test_dist,test_user_format,gen_diagrams,gen_docs,regression_suite rootModule;

```

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
