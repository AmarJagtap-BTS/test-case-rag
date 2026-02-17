# Project Architecture & Flow Diagrams

*Generated on: Tue Feb 17 05:50:00 UTC 2026*

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
    M2[generate_docs]
    M3[generate_diagrams]
    M4[test_distribution]
    subgraph ui_dir[ui]
        M5[api]
        M6[__init__]
        M7[app]
    end
    subgraph tests_dir[tests]
        M8[test_fixes]
        M9[test_performance]
        M10[test_description_validation]
        M11[__init__]
        M12[test_type_positive_negative]
        M13[test_numbering_fix]
        M14[test_end_to_end_numbering]
        M15[test_api]
    end
    subgraph engines_dir[engines]
        M16[embeddings]
        M17[test_case_updater]
        M18[__init__]
        M19[rag_engine]
        M20[comparison_engine]
        M21[test_case_generator]
        M22[test_case_manager]
        M23[context_engineering]
    end
    subgraph config_dir[config]
        M24[__init__]
        M25[config]
    end
    subgraph scripts_dir[scripts]
        M26[add_diverse_test_cases]
        M27[format_test_cases_for_excel]
        M28[__init__]
        M29[test_llm_apis]
        M30[create_excel_template]
    end
    subgraph core_dir[core]
        M31[knowledge_base]
        M32[models]
        M33[utils]
        M34[__init__]
    end
    subgraph examples_dir[examples]
        M35[__init__]
        M36[import_example]
        M37[example]
        M38[example_context_engineering]
    end
    M0 --> M12
    M0 --> M21
    M0 --> M33
    M0 --> M25
    M2 --> M12
    M3 --> M12
    M4 --> M33
    M4 --> M25
    M5 --> M12
    M5 --> M32
    M5 --> M22
    M5 --> M25
    M5 --> M33
    M7 --> M12
    M7 --> M32
    M7 --> M22
    M7 --> M25
    M7 --> M33
    M7 --> M33
    M7 --> M33
    M7 --> M33
    M8 --> M21
    M8 --> M20
    M8 --> M32
    M8 --> M33
    M9 --> M22
    M9 --> M32
    M10 --> M12
    M10 --> M33
    M12 --> M12
    M12 --> M33
    M12 --> M33
    M13 --> M12
    M13 --> M33
    M13 --> M32
    M14 --> M12
    M14 --> M33
    M14 --> M19
    M14 --> M21
    M14 --> M32
    M16 --> M12
    M16 --> M25
    M18 --> M19
    M18 --> M16
    M18 --> M20
    M18 --> M21
    M18 --> M22
    M18 --> M23
    M19 --> M12
    M19 --> M32
    M19 --> M16
    M19 --> M25
    M20 --> M12
    M20 --> M25
    M20 --> M32
    M20 --> M16
    M20 --> M23
    M20 --> M33
    M20 --> M1
    M21 --> M12
    M21 --> M25
    M21 --> M32
    M21 --> M33
    M21 --> M23
    M21 --> M1
    M21 --> M1
    M22 --> M12
    M22 --> M32
    M22 --> M19
    M22 --> M21
    M22 --> M20
    M22 --> M31
    M22 --> M25
    M22 --> M33
    M22 --> M33
    M22 --> M33
    M23 --> M12
    M23 --> M32
    M23 --> M25
    M24 --> M24
    M25 --> M12
    M26 --> M12
    M26 --> M33
    M27 --> M12
    M27 --> M32
    M27 --> M31
    M29 --> M12
    M31 --> M12
    M31 --> M32
    M31 --> M33
    M31 --> M25
    M31 --> M33
    M33 --> M1
    M33 --> M32
    M33 --> M25
    M33 --> M12
    M33 --> M32
    M34 --> M32
    M34 --> M33
    M34 --> M31
    M36 --> M12
    M36 --> M22
    M36 --> M32
    M36 --> M33
    M37 --> M12
    M37 --> M32
    M37 --> M22
    M37 --> M33
    M38 --> M12
    M38 --> M21
    M38 --> M19
    M38 --> M23
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
    class EmbeddingGenerator {
        +__init__()
        +generate_embedding()
        +generate_embeddings_batch()
        +calculate_similarity()
        +clear_cache()
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
    class ContextEngineer {
        +__init__()
        +_load_examples()
        +_load_context_templates()
        +enhance_generation_prompt()
        +enhance_comparison_prompt()
    }
    class Config {
        +validate()
        +create_directories()
    }
    class KnowledgeBase {
        +__init__()
        +_load_existing_suites()
        +create_test_suite()
        +get_test_suite()
        +add_test_case_to_suite()
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
graph TD
  %% System Architecture Layers
  subgraph CLI & Scripts
    TUG[test_user_format_generation.py]
    CRS[create_regression_suite.py]
    GD[generate_docs.py]
    GDM[generate_diagrams.py]
    TD[test_distribution.py]
  end
  
  subgraph UI Layer
    UIApi[ui/api.py<br/>7 classes]
    UIInit[ui/__init__.py]
    UIApp[ui/app.py<br/>2 functions]
  end
  
  subgraph Tests
    TFixes[tests/test_fixes.py<br/>5 functions]
    TPerf[tests/test_performance.py<br/>1 function]
  end

  %% Architectural Relationships
  CRS -->|uses| UIApi
  GDM -->|uses| UIApi
  UIApp -->|imports| UIApi
  UIInit -->|initializes| UIApi

  TFixes -->|tests| UIApi
  TPerf -->|tests| UIApi
  TD -->|tests| CRS

  %% Data Flow (main data flow directions)
  TUG -->|generates| CRS
  CRS -->|outputs regression suite to| GDM
  GDM -->|creates diagrams for| UIApi
  UIApp -->|serves data to| UIApi

  %% Component Interactions
  UIApi -->|provides API to| UIApp
  UIApi -.->|interacts with| CRS
  TFixes -.->|validates input to| UIApi
  TPerf -.->|monitors performance of| UIApi

  %% Legend
  classDef module fill:#f9f,stroke:#333,stroke-width:1px;
  class TUG,CRS,GD,GDM,TD,UIApi,UIInit,UIApp,TFixes,TPerf module
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
