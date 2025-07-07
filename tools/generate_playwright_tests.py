import os
import json
import re

# Load the test cases
with open("test_cases_renumbered.json", "r", encoding="utf-8") as f:
    test_cases = json.load(f)

# Output folder
output_dir = "playwright_tests"
os.makedirs(output_dir, exist_ok=True)

# Template for each test
test_template = """import {{ test, expect }} from '@playwright/test';

test('{title}', async ({{ page }}) => {{
  // Step-by-step actions
{steps}
}});
"""

# Generate .spec.ts files
for case in test_cases:
    test_id = case.get("id", "TCXXX")
    title = case.get("description", "No description").replace("'", "")
    steps = case.get("steps", [])

    # Convert steps into Playwright-style comments
    step_code = "\n".join([f"  // {i+1}. {step}" for i, step in enumerate(steps)])

    # Final test content
    test_code = test_template.format(title=title, steps=step_code)

    # Save as .spec.ts
    safe_title = re.sub(r'[^a-zA-Z0-9_]+', '_', title.lower())[:30]
    file_name = f"{test_id}_{safe_title}.spec.ts"
    file_path = os.path.join(output_dir, file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(test_code)

print(f"✅ Generated {len(test_cases)} Playwright tests in '{output_dir}' folder.")
