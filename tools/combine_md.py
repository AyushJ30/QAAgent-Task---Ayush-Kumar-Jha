import os

folder_path = "test_case_chunks"  # <-- your folder with chunk_1.md, chunk_2.md, etc.
output_file = "test_cases.md"

# Add a top-level heading (optional but nice for display)
with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write("# Recruter.ai Frontend Test Cases\n\n")
    
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".md"):
            # Optional: auto-generate chunk section headers
            chunk_title = filename.replace(".md", "").replace("_", " ").title()
            outfile.write(f"## {chunk_title}\n\n")  # H2 for chunk sections
            
            # Append the markdown content from the file
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as infile:
                outfile.write(infile.read().strip() + "\n\n---\n\n")  # Add separator between chunks

print("✅ Combined Markdown saved to test_cases.md")
