from langchain.text_splitter import RecursiveCharacterTextSplitter

# Step 1: Load transcript
with open("recruter_transcript.txt", "r", encoding="utf-8") as file:
    transcript = file.read()

# Step 2: Set up the chunker
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100,
    separators=["\n\n", "\n", ".", "!", "?", ",", " "]
)

# Step 3: Create chunks and clean up leading punctuation
raw_chunks = text_splitter.split_text(transcript)

chunks = [chunk.lstrip(". ").strip() for chunk in raw_chunks]

# Step 4: Save chunks to individual files (optional, for debugging or review)
for i, chunk in enumerate(chunks):
    with open(f"chunks/chunk_{i+1}.txt", "w", encoding="utf-8") as f:
        f.write(chunk)

# Step 5: Or save as a single JSON file
import json
with open("chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=2)

print(f"✅ Done! Split transcript into {len(chunks)} chunks.")
