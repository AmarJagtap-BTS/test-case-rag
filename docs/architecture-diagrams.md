# Project Architecture & Flow Diagrams

*Generated on: Tue Feb 24 11:01:21 UTC 2026*

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
    M0[test_user_format_generation]
    M1[create_regression_suite]
    M2[generate_diagrams]
    M3[generate_docs]
    M4[test_distribution]
    subgraph examples_dir[examples]
        M5[example]
        M6[import_example]
        M7[__init__]
        M8[example_context_engineering]
    end
    subgraph engines_dir[engines]
        M9[embeddings]
        M10[test_case_updater]
        M11[context_engineering]
        M12[test_case_generator]
        M13[test_case_manager]
        M14[rag_engine]
        M15[__init__]
        M16[comparison_engine]
    end
    subgraph scripts_dir[scripts]
        M17[add_diverse_test_cases]
        M18[test_llm_apis]
        M19[__init__]
        M20[create_excel_template]
        M21[format_test_cases_for_excel]
    end
    subgraph ui_dir[ui]
        M22[api]
        M23[app]
        M24[__init__]
    end
    subgraph core_dir[core]
        M25[utils]
        M26[__init__]
        M27[models]
        M28[knowledge_base]
    end
    subgraph tests_dir[tests]
        M29[test_performance]
        M30[test_end_to_end_numbering]
        M31[test_api]
        M32[test_numbering_fix]
        M33[test_fixes]
        M34[test_description_validation]
        M35[__init__]
        M36[test_type_positive_negative]
    end
    subgraph config_dir[config]
        M37[config]
        M38[__init__]
    end
    M0 --> M36
    M0 --> M12
    M0 --> M25
    M0 --> M37
    M2 --> M36
    M3 --> M36
    M4 --> M25
    M4 --> M37
    M5 --> M36
    M5 --> M27
    M5 --> M13
    M5 --> M25
    M6 --> M36
    M6 --> M13
    M6 --> M27
    M6 --> M25
    M8 --> M36
    M8 --> M12
    M8 --> M14
    M8 --> M11
    M9 --> M36
    M9 --> M37
    M11 --> M36
    M11 --> M27
    M11 --> M37
    M12 --> M36
    M12 --> M37
    M12 --> M27
    M12 --> M25
    M12 --> M11
    M12 --> M1
    M12 --> M1
    M13 --> M36
    M13 --> M27
    M13 --> M14
    M13 --> M12
    M13 --> M16
    M13 --> M28
    M13 --> M37
    M13 --> M25
    M13 --> M25
    M13 --> M25
    M14 --> M36
    M14 --> M27
    M14 --> M9
    M14 --> M37
    M15 --> M14
    M15 --> M9
    M15 --> M16
    M15 --> M12
    M15 --> M13
    M15 --> M8
    M16 --> M36
    M16 --> M37
    M16 --> M27
    M16 --> M9
    M16 --> M11
    M16 --> M25
    M16 --> M1
    M17 --> M36
    M17 --> M25
    M18 --> M36
    M21 --> M36
    M21 --> M27
    M21 --> M28
    M22 --> M36
    M22 --> M27
    M22 --> M13
    M22 --> M37
    M22 --> M25
    M23 --> M36
    M23 --> M27
    M23 --> M13
    M23 --> M37
    M23 --> M25
    M23 --> M25
    M23 --> M25
    M23 --> M25
    M25 --> M1
    M25 --> M27
    M25 --> M37
    M25 --> M36
    M25 --> M27
    M26 --> M27
    M26 --> M25
    M26 --> M28
    M28 --> M36
    M28 --> M27
    M28 --> M25
    M28 --> M37
    M28 --> M25
    M29 --> M13
    M29 --> M27
    M30 --> M36
    M30 --> M25
    M30 --> M14
    M30 --> M12
    M30 --> M27
    M32 --> M36
    M32 --> M25
    M32 --> M27
    M33 --> M12
    M33 --> M16
    M33 --> M27
    M33 --> M25
    M34 --> M36
    M34 --> M25
    M36 --> M36
    M36 --> M25
    M36 --> M25
    M37 --> M36
    M38 --> M37
```

## Class Diagram

Main classes and their methods:

```mermaid
classDiagram
    class EmbeddingGenerator {
        +__init__()
        +generate_embedding()
        +generate_embeddings_batch()
        +calculate_similarity()
        +clear_cache()
    }
    class ContextEngineer {
        +__init__()
        +_load_examples()
        +_load_context_templates()
        +enhance_generation_prompt()
        +enhance_comparison_prompt()
    }
    class TestCaseGenerator {
        +__init__()
        +generate_from_user_story()
        +generate_from_text()
        +_generate_single_request()
        +_clean_json_content()
    }
    class TestCaseManager {
        +__init__()
        +_analyze_new_test_case()
        +_get_recommendation()
        +_reconstruct_test_case()
        +process_user_story()
    }
    class RAGEngine {
        +__init__()
        +add_test_case()
        +add_test_cases_batch()
        +search_similar_test_cases()
        +get_test_case_by_id()
    }
    class ComparisonEngine {
        +__init__()
        +compare_test_cases()
        +_analyze_with_llm()
        +_calculate_llm_similarity()
        +_make_decision()
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
  %% System Architecture %%
  subgraph System_Architecture["System Architecture"]

    subgraph Examples["Examples Module"]
      direction TB
      EX1["example.py\n(0 classes, 2 functions)"]
      EX2["import_example.py\n(0 classes, 3 functions)"]
      EX3["example_context_engineering.py\n(0 classes, 3 functions)"]
      EX_INIT["__init__.py\n(0 classes, 0 functions)"]
    end

    subgraph Engines["Engines Module"]
      direction TB
      EMBEDDINGS["embeddings.py\n(1 class, 5 functions)"]
    end

    subgraph CoreScripts["Core Scripts"]
      direction TB
      CREATE_REG["create_regression_suite.py\n(0 classes, 2 functions)"]
      GEN_DIAGRAMS["generate_diagrams.py\n(0 classes, 7 functions)"]
      GEN_DOCS["generate_docs.py\n(0 classes, 0 functions)"]
      TEST_USER_FORMAT["test_user_format_generation.py\n(0 classes, 0 functions)"]
      TEST_DISTRIBUTION["test_distribution.py\n(0 classes, 0 functions)"]
    end

  end

  %% Data Flow %%
  %% Data flows from examples to engines and core scripts for generation and tests %%
  EX1 -->|data/input examples| EMBEDDINGS
  EX2 -->|data/import examples| EMBEDDINGS
  EX3 -->|context data examples| EMBEDDINGS

  EMBEDDINGS -->|processed embeddings| CREATE_REG
  EMBEDDINGS -->|embedding data| GEN_DIAGRAMS

  CREATE_REG -->|regression suites| GEN_DOCS
  GEN_DIAGRAMS -->|diagrams| GEN_DOCS

  TEST_USER_FORMAT -.->|validates format| GEN_DOCS
  TEST_DISTRIBUTION -.->|validates data| CREATE_REG

  %% Component Interactions %%
  GEN_DOCS -->|documentation| EX_INIT
  CREATE_REG -->|uses embeddings| EMBEDDINGS
  GEN_DIAGRAMS -->|reads data| CREATE_REG

  %% Legends %%
  classDef module fill:#f9f,stroke:#333,stroke-width:1px
  class ExampleMod module
  class EngineMod module
  class CoreMod module

  class EX1,EX2,EX3,EX_INIT ExampleMod
  class EMBEDDINGS EngineMod
  class CREATE_REG,GEN_DIAGRAMS,GEN_DOCS,TEST_USER_FORMAT,TEST_DISTRIBUTION CoreMod

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
