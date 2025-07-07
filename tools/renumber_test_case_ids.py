import json

# Load the original test cases
with open("test_cases.json", "r", encoding="utf-8") as f:
    test_cases = json.load(f)

# Renumber the IDs
for i, case in enumerate(test_cases, start=1):
    case["id"] = f"TC{str(i).zfill(3)}"  # TC001, TC002, etc.

# Save the updated list
with open("test_cases_renumbered.json", "w", encoding="utf-8") as f:
    json.dump(test_cases, f, indent=2)

print(f"✅ Updated {len(test_cases)} test case IDs and saved to test_cases_renumbered.json")
