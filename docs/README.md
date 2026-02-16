# Documentation Guide

Welcome to the test-case-rag project documentation! This guide helps you navigate through the auto-generated documentation and diagrams.

## 📚 Available Documentation

### 1. [Auto-Generated Code Documentation](./auto-doc.md)
Comprehensive documentation for all code files in the project, including:
- Detailed explanations of each module
- Function and class descriptions
- Usage examples
- Architecture notes

**Updated:** Automatically regenerated on every push with changes to `.py`, `.java`, or `.js` files.

### 2. [Architecture & Flow Diagrams](./architecture-diagrams.md)
Visual representations of the project structure using Mermaid diagrams:
- **System Architecture**: High-level overview of the system
- **Module Dependencies**: Shows relationships between different modules
- **Class Diagrams**: Main classes and their methods
- **Sequence Diagrams**: Typical workflow sequences
- **Process Flowcharts**: Detailed process flows
- **Module Summary**: Complete table of all modules with statistics

**Updated:** Automatically regenerated on every push.

## 🎨 Viewing Mermaid Diagrams

Mermaid diagrams can be viewed in several ways:

### Option 1: GitHub (Recommended)
GitHub natively renders Mermaid diagrams. Simply view the markdown files directly on GitHub:
- [View Architecture Diagrams on GitHub](../docs/architecture-diagrams.md)

### Option 2: VS Code
1. Install the "Markdown Preview Mermaid Support" extension
2. Open any `.md` file with Mermaid diagrams
3. Press `Ctrl+Shift+V` (Windows/Linux) or `Cmd+Shift+V` (Mac) for preview

### Option 3: Online Viewers
Copy the Mermaid code and paste it into:
- [Mermaid Live Editor](https://mermaid.live/)
- [Mermaid Chart](https://www.mermaidchart.com/)

### Option 4: Browser Extensions
- Chrome: "Mermaid Diagrams" extension
- Firefox: "Mermaid Diagram Viewer" extension

## 🔄 How Documentation is Generated

### Automatic Generation
Documentation is automatically generated via GitHub Actions on every push to `main`:

1. **Changed Files Detection**: 
   - If `auto-doc.md` doesn't exist → Generates docs for **entire project**
   - If `auto-doc.md` exists → Generates docs for **changed files only**

2. **Documentation Generation**:
   - Analyzes code structure
   - Uses Azure OpenAI to generate comprehensive documentation
   - Updates `docs/auto-doc.md`

3. **Diagram Generation**:
   - Parses Python files to extract structure
   - Generates multiple Mermaid diagrams
   - Creates module dependency graphs
   - Updates `docs/architecture-diagrams.md`

### Manual Generation
You can also generate documentation manually:

```bash
# Generate code documentation
python generate_docs.py

# Generate architecture diagrams
python generate_diagrams.py
```

## 📊 Diagram Types Explained

### System Architecture (Flowchart)
Shows the high-level process flow from user input to output, including:
- Decision points
- Data flow
- Process steps

### Module Dependencies (Graph)
Visual representation of:
- All Python modules in the project
- Import relationships between modules
- Module grouping by directory

### Class Diagram
Displays:
- Main classes in the project
- Class methods (top 5 per class)
- Class relationships

### Sequence Diagram
Illustrates:
- Typical workflow sequence
- Component interactions
- Message flow between components

### Module Summary Table
Comprehensive table showing:
- All modules in the project
- Number of classes per module
- Number of functions per module
- Number of imports per module

## 🛠️ Configuration

The documentation system uses Azure OpenAI for intelligent documentation generation. Configuration is managed through GitHub Secrets:

- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_API_VERSION`
- `AZURE_OPENAI_DEPLOYMENT`

## 📝 Contributing to Documentation

### Adding Custom Documentation
While most documentation is auto-generated, you can add custom sections:

1. Create a new markdown file in the `docs/` directory
2. Link it from this README
3. Commit and push

### Improving Generation Scripts
The generation scripts are located at:
- `generate_docs.py` - Code documentation generator
- `generate_diagrams.py` - Diagram generator

Feel free to enhance these scripts to add more diagram types or documentation features!

## 🐛 Troubleshooting

### Diagrams Not Rendering
1. Ensure you're viewing on GitHub or using a Mermaid-compatible viewer
2. Check that the markdown file contains properly formatted Mermaid code blocks
3. Try copying the diagram code to [Mermaid Live Editor](https://mermaid.live/) to validate syntax

### Documentation Out of Date
1. Push a small change to trigger the workflow
2. Or manually run: `python generate_docs.py && python generate_diagrams.py`
3. Check GitHub Actions for any errors

### Workflow Failures
1. Check GitHub Actions logs for detailed error messages
2. Verify Azure OpenAI credentials are correctly set in GitHub Secrets
3. Ensure all dependencies are listed in workflow file

## 📮 Support

For issues or questions:
1. Check existing documentation first
2. Review GitHub Actions logs for automated generation issues
3. Create an issue in the repository

---

**Last Updated:** Auto-generated on every push to main branch
**Generator Version:** 1.0
**Mermaid Version:** Compatible with latest GitHub rendering
