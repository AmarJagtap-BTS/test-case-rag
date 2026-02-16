import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY", ""),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2025-01-01-preview"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", "")
)

#  Read changed files list
with open("changed_files.txt", "r") as f:
    files = f.read().splitlines()

# Check if this is a full project documentation or incremental update
doc_file_path = "docs/auto-doc.md"
is_full_documentation = not os.path.exists(doc_file_path)

if is_full_documentation:
    doc_content = "# Auto Generated Documentation\n\n"
    doc_content += f"*Complete project documentation - Generated on: {os.popen('date').read().strip()}*\n\n"
    print(f"Generating complete documentation for {len(files)} files...")
else:
    doc_content = "# Auto Generated Documentation\n\n"
    doc_content += f"*Last updated: {os.popen('date').read().strip()}*\n\n"
    print(f"Generating documentation for {len(files)} changed files...")

for file in files:
    if file.endswith(".java") or file.endswith(".py") or file.endswith(".js"):
        print(f"Processing: {file}")
        try:
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
        except Exception as e:
            print(f"Error processing {file}: {str(e)}")
            doc_content += f"## File: {file}\n"
            doc_content += f"*Error generating documentation: {str(e)}*\n\n"

# Create docs folder if not exists
os.makedirs("docs", exist_ok=True)

with open("docs/auto-doc.md", "w", encoding="utf-8") as f:
    f.write(doc_content)
