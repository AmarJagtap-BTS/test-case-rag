import os
import ast
from openai import AzureOpenAI
from typing import Dict, List, Set

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY", ""),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2025-01-01-preview"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", "")
)

def analyze_project_structure():
    """Analyze the project structure and relationships."""
    structure = {
        'modules': {},
        'dependencies': {},
        'classes': {},
        'functions': {}
    }
    
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories and common non-code directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules', 'venv', 'env']]
        
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                relative_path = filepath[2:]  # Remove './'
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        tree = ast.parse(content)
                        
                        # Extract imports
                        imports = []
                        for node in ast.walk(tree):
                            if isinstance(node, ast.Import):
                                for alias in node.names:
                                    imports.append(alias.name)
                            elif isinstance(node, ast.ImportFrom):
                                if node.module:
                                    imports.append(node.module)
                        
                        # Extract classes and functions
                        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
                        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
                        
                        structure['modules'][relative_path] = {
                            'imports': imports,
                            'classes': classes,
                            'functions': functions
                        }
                except Exception as e:
                    print(f"Error analyzing {filepath}: {e}")
    
    return structure

def generate_mermaid_architecture_diagram(structure: Dict) -> str:
    """Generate a Mermaid architecture diagram."""
    mermaid = "```mermaid\ngraph TB\n"
    
    # Group modules by directory
    directories = {}
    for module_path in structure['modules'].keys():
        dir_name = os.path.dirname(module_path) or 'root'
        if dir_name not in directories:
            directories[dir_name] = []
        directories[dir_name].append(module_path)
    
    # Create subgraphs for each directory
    node_counter = 0
    module_to_id = {}
    
    for dir_name, modules in directories.items():
        if dir_name == 'root':
            for module in modules:
                node_id = f"M{node_counter}"
                module_to_id[module] = node_id
                module_name = os.path.basename(module).replace('.py', '')
                mermaid += f"    {node_id}[{module_name}]\n"
                node_counter += 1
        else:
            mermaid += f"    subgraph {dir_name.replace('/', '_')}_dir[{dir_name}]\n"
            for module in modules:
                node_id = f"M{node_counter}"
                module_to_id[module] = node_id
                module_name = os.path.basename(module).replace('.py', '')
                mermaid += f"        {node_id}[{module_name}]\n"
                node_counter += 1
            mermaid += "    end\n"
    
    # Add dependencies (limit to internal imports)
    for module_path, info in structure['modules'].items():
        if module_path not in module_to_id:
            continue
        source_id = module_to_id[module_path]
        for imp in info['imports']:
            # Try to find matching internal module
            for target_path in structure['modules'].keys():
                if imp in target_path or target_path.replace('/', '.').replace('.py', '') == imp:
                    if target_path in module_to_id:
                        target_id = module_to_id[target_path]
                        mermaid += f"    {source_id} --> {target_id}\n"
                        break
    
    mermaid += "```\n"
    return mermaid

def generate_mermaid_class_diagram(structure: Dict) -> str:
    """Generate a Mermaid class diagram for main classes."""
    mermaid = "```mermaid\nclassDiagram\n"
    
    # Collect all classes with their modules
    classes_info = []
    for module_path, info in structure['modules'].items():
        for class_name in info['classes']:
            classes_info.append({
                'name': class_name,
                'module': os.path.basename(module_path).replace('.py', ''),
                'functions': info['functions'][:5]  # Limit to first 5 functions
            })
    
    # Add classes to diagram (limit to avoid overcrowding)
    for class_info in classes_info[:15]:  # Limit to 15 classes
        class_name = class_info['name']
        mermaid += f"    class {class_name} {{\n"
        for func in class_info['functions'][:5]:
            mermaid += f"        +{func}()\n"
        mermaid += "    }\n"
    
    mermaid += "```\n"
    return mermaid

def generate_mermaid_sequence_diagram() -> str:
    """Generate a sequence diagram for typical workflow."""
    mermaid = """```mermaid
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
"""
    return mermaid

def generate_mermaid_flowchart() -> str:
    """Generate a flowchart for the main process."""
    mermaid = """```mermaid
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
"""
    return mermaid

def generate_ai_diagrams(structure: Dict) -> str:
    """Use AI to generate comprehensive diagrams."""
    
    # Prepare project summary for AI
    summary = f"Project has {len(structure['modules'])} modules.\n\n"
    summary += "Main modules:\n"
    for module, info in list(structure['modules'].items())[:10]:
        summary += f"- {module}: {len(info['classes'])} classes, {len(info['functions'])} functions\n"
    
    prompt = f"""Based on this project structure, generate a comprehensive Mermaid diagram showing:
1. System architecture
2. Data flow
3. Component interactions

{summary}

Generate a complete Mermaid diagram that best represents the system."""
    
    try:
        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4.1-mini"),
            messages=[
                {"role": "system", "content": "You are an expert software architect who creates clear, comprehensive Mermaid diagrams."},
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content or ""
    except Exception as e:
        print(f"Error generating AI diagrams: {e}")
        return ""

def main():
    print("Analyzing project structure...")
    structure = analyze_project_structure()
    
    print(f"Found {len(structure['modules'])} Python modules")
    
    # Generate diagrams
    print("Generating diagrams...")
    
    diagram_content = "# Project Architecture & Flow Diagrams\n\n"
    diagram_content += f"*Generated on: {os.popen('date').read().strip()}*\n\n"
    
    # Table of Contents
    diagram_content += "## Table of Contents\n\n"
    diagram_content += "1. [System Architecture](#system-architecture)\n"
    diagram_content += "2. [Module Dependencies](#module-dependencies)\n"
    diagram_content += "3. [Class Diagram](#class-diagram)\n"
    diagram_content += "4. [Sequence Diagram](#sequence-diagram)\n"
    diagram_content += "5. [Process Flowchart](#process-flowchart)\n"
    diagram_content += "6. [AI-Generated Architecture](#ai-generated-architecture)\n\n"
    
    # 1. System Architecture
    diagram_content += "## System Architecture\n\n"
    diagram_content += "Overview of the system's high-level architecture:\n\n"
    diagram_content += generate_mermaid_flowchart()
    diagram_content += "\n"
    
    # 2. Module Dependencies
    diagram_content += "## Module Dependencies\n\n"
    diagram_content += "Dependency graph showing relationships between modules:\n\n"
    diagram_content += generate_mermaid_architecture_diagram(structure)
    diagram_content += "\n"
    
    # 3. Class Diagram
    diagram_content += "## Class Diagram\n\n"
    diagram_content += "Main classes and their methods:\n\n"
    diagram_content += generate_mermaid_class_diagram(structure)
    diagram_content += "\n"
    
    # 4. Sequence Diagram
    diagram_content += "## Sequence Diagram\n\n"
    diagram_content += "Typical workflow sequence:\n\n"
    diagram_content += generate_mermaid_sequence_diagram()
    diagram_content += "\n"
    
    # 5. Process Flowchart (already added as System Architecture)
    diagram_content += "## Process Flowchart\n\n"
    diagram_content += "Detailed process flow:\n\n"
    diagram_content += generate_mermaid_flowchart()
    diagram_content += "\n"
    
    # 6. AI-Generated Architecture
    diagram_content += "## AI-Generated Architecture\n\n"
    diagram_content += "AI-generated comprehensive architecture diagram:\n\n"
    ai_diagram = generate_ai_diagrams(structure)
    diagram_content += ai_diagram
    diagram_content += "\n"
    
    # Module Summary
    diagram_content += "## Module Summary\n\n"
    diagram_content += f"Total Modules: {len(structure['modules'])}\n\n"
    diagram_content += "| Module | Classes | Functions | Imports |\n"
    diagram_content += "|--------|---------|-----------|----------|\n"
    for module, info in sorted(structure['modules'].items()):
        diagram_content += f"| {module} | {len(info['classes'])} | {len(info['functions'])} | {len(info['imports'])} |\n"
    
    # Save to file
    os.makedirs("docs", exist_ok=True)
    output_file = "docs/architecture-diagrams.md"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(diagram_content)
    
    print(f"\nDiagrams generated successfully!")
    print(f"Output saved to: {output_file}")
    print(f"Total modules analyzed: {len(structure['modules'])}")

if __name__ == "__main__":
    main()
