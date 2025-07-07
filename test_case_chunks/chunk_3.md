# Recruter.ai Frontend Test Cases

---

### 🧩 Core User Flows

*   ✅ **TC01**: User selects skills from AI suggestions
    
*   ✅ **TC02**: User manually adds a custom skill (e.g., "2 years AWS experience")
    
*   ✅ **TC03**: User sets difficulty level for questions (e.g., Easy, Moderate, Hard)
    
*   ✅ **TC04**: Company name is input and accepted by the system
    
*   ✅ **TC05**: AI analyzes job description and generates **standard** and **role-based** questions
    
*   ✅ **TC06**: User customizes options for a standard question (e.g., change notice period answers)
    
---

### ⚠️ Edge Cases

*   ⚠️ **TC07**: Add an empty skill — system should block and show error
    
*   ⚠️ **TC08**: Add skill with special characters only (e.g., “@@@###”) — should be rejected
    
*   ⚠️ **TC09**: Set question difficulty without selecting skills — verify fallback or prompt
    
*   ⚠️ **TC10**: Enter excessively long company name (>100 characters) — UI should truncate or handle gracefully
    
*   ⚠️ **TC11**: Simulate network failure during AI question generation — user should see error message with retry
    
*   ⚠️ **TC12**: Customize options for a question and refresh page — check if edits are saved or prompt to re-enter

--- 

### ♿ Accessibility

*   ♿ **TC13**: Skill selection, difficulty dropdown, and company input are accessible via keyboard navigation
    
*   ♿ **TC14**: All form fields and question cards include appropriate aria-labels for screen readers
    
*   ♿ **TC15**: Customization modal for question options has visible focus ring and ESC-to-close support
    
*   ♿ **TC16**: Text and buttons meet WCAG-compliant color contrast (4.5:1 or better)

---    

### 🚀 Performance

*   🚀 **TC17**: AI question generation completes within 3s for a medium JD (300-500 words)
    
*   🚀 **TC18**: UI remains responsive while editing multiple questions/options in quick succession
    
*   🚀 **TC19**: Skill selection UI performs well even with 50+ AI-suggested and user-added skills