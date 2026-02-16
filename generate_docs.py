import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read changed files list
with open("changed_files.txt", "r") as f:
    files = f.read().splitlines()

doc_content = "# Auto Generated Documentation\n\n"

for file in files:
    if file.endswith(".java") or file.endswith(".py") or file.endswith(".js"):
        with open(file, "r", encoding="utf-8") as code_file:
            code = code_file.read()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a senior software architect."},
                {"role": "user", "content": f"Generate documentation for this code:\n{code}"}
            ],
        )

        doc_content += f"## File: {file}\n"
        doc_content += response.choices[0].message.content
        doc_content += "\n\n"

# Create docs folder if not exists
os.makedirs("docs", exist_ok=True)

with open("docs/auto-doc.md", "w", encoding="utf-8") as f:
    f.write(doc_content)
