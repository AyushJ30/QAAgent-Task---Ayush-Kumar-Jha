import os
import json

# Change this to your actual folder name
folder_path = "test_case_chunks"
output_file = "test_cases.json"

combined_cases = []

for filename in sorted(os.listdir(folder_path)):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)

                # Some files may be single dict, some a list
                if isinstance(data, list):
                    combined_cases.extend(data)
                elif isinstance(data, dict):
                    combined_cases.append(data)
                else:
                    print(f"⚠️ Skipping unknown format: {filename}")

            except json.JSONDecodeError as e:
                print(f"❌ Error parsing {filename}: {e}")

# Save combined output
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(combined_cases, f, indent=2)

print(f"✅ Combined {len(combined_cases)} test cases into {output_file}")
