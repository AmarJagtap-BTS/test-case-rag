# Auto Generated Documentation

## File: generate_docs.py
# Documentation for Auto-Documentation Script

## Overview
This script automates the generation of documentation for changed source code files in a project, using the Azure OpenAI API. It reads a list of changed files from a text file, extracts code from supported file types, sends them to the OpenAI Azure endpoint for documentation generation, and consolidates the results into a single Markdown document.

---

## Requirements
- Python 3.7+
- Azure OpenAI Python SDK (`openai` package)
- Environment variables configured for:
  - `AZURE_OPENAI_API_KEY`: Your Azure OpenAI API key
  - `AZURE_OPENAI_API_VERSION`: (Optional) API version, defaults to `"2025-01-01-preview"`
  - `AZURE_OPENAI_ENDPOINT`: Your Azure OpenAI endpoint URL
  - `AZURE_OPENAI_DEPLOYMENT`: (Optional) The deployment/model name to query, defaults to `"gpt-4.1-mini"`
- A file named `changed_files.txt` that lists the changed files, one filename per line.

---

## Script Breakdown

### Imports
```python
import os
from openai import AzureOpenAI
```
- `os` is for environment variable access, file operations, and directory management.
- `AzureOpenAI` is the client from the Azure OpenAI SDK to interact with the API.

### Client Initialization
```python
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY", ""),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2025-01-01-preview"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", "")
)
```
- Creates an API client using credentials and endpoint details fetched from environment variables.
- The API version has a default fallback in case the environment variable is not set.

### Reading Changed Files List
```python
with open("changed_files.txt", "r") as f:
    files = f.read().splitlines()
```
- Reads all filenames from `changed_files.txt` into a list called `files`.

### Documentation Content Initialization
```python
doc_content = "# Auto Generated Documentation\n\n"
```
- Initializes the markdown content with a heading.

### Processing Each Changed File
```python
for file in files:
    if file.endswith(".java") or file.endswith(".py") or file.endswith(".js"):
        with open(file, "r", encoding="utf-8") as code_file:
            code = code_file.read()

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
```
- Checks if the file extension is `.java`, `.py`, or `.js`, only processing these file types.
- Reads the entire source code content of the target file.
- Sends a request to the OpenAI chat completion endpoint with a system prompt framing the assistant as a senior software architect, and a user prompt asking to generate documentation for the provided code.
- Extracts the generated documentation from the API response.
- Appends the filename as a subsection header and the generated documentation to the final markdown content.

### Writing Output Documentation
```python
os.makedirs("docs", exist_ok=True)

with open("docs/auto-doc.md", "w", encoding="utf-8") as f:
    f.write(doc_content)
```
- Creates a `docs` directory if it does not already exist.
- Writes the generated documentation content to a file named `auto-doc.md` inside the `docs` folder.

---

## Summary
- **Input:** `changed_files.txt` — lists changed source code files.
- **Process:** For each `.java`, `.py`, or `.js` file, send the source code to the Azure OpenAI chat completion endpoint to generate documentation.
- **Output:** A single Markdown file `docs/auto-doc.md` containing generated documentation grouped by file.

---

## Usage Example
1. Set environment variables:
    ```bash
    export AZURE_OPENAI_API_KEY="your_api_key"
    export AZURE_OPENAI_API_VERSION="2025-01-01-preview"
    export AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com/"
    export AZURE_OPENAI_DEPLOYMENT="gpt-4.1-mini"
    ```
2. Ensure `changed_files.txt` exists and lists your changed `.java`, `.py`, and `.js` files.
3. Run the script.
4. Check `docs/auto-doc.md` for the generated documentation.

---

## Notes
- The script assumes all listed files in `changed_files.txt` exist and can be read.
- Files with unsupported extensions are ignored.
- The script uses UTF-8 encoding to read files.
- You may need network access and billing setup for the Azure OpenAI service.

