# Recruter.ai Frontend Test Cases

---

### 🧩 Core User Flows

*   ✅ **TC01**: User enters a full job description manually and saves it.
    
*   ✅ **TC02**: User uses the "Enhanced JD" feature by entering only a job title.
    
*   ✅ **TC03**: User edits the auto-generated job description before saving.
    
*   ✅ **TC04**: After saving a job description, user sees AI-generated skill recommendations.
    
*   ✅ **TC05**: User selects recommended skills to drive the interview pipeline (questions, assessments).
    
---

### ⚠️ Edge Cases

*   ⚠️ **TC06**: User clicks "Save" with an empty job description — should show validation error.
    
*   ⚠️ **TC07**: User enters only one or two words for job title — ensure Enhanced JD still works or provides feedback.
    
*   ⚠️ **TC08**: Submit overly vague title (e.g., “Engineer”) — verify skill extraction handles ambiguity gracefully.
    
*   ⚠️ **TC09**: Paste extremely long job description (>10,000 characters) — UI should handle without freezing.
    
*   ⚠️ **TC10**: Simulate network failure while generating Enhanced JD — display appropriate error or retry option.
    
*   ⚠️ **TC11**: Simulate network failure while fetching skill recommendations — graceful degradation or retry.

 ---   

### ♿ Accessibility

*   ♿ **TC12**: All input fields (JD input, job title, save button) are accessible by keyboard.
    
*   ♿ **TC13**: Enhanced JD generation is screen-reader friendly (proper labels, ARIA roles).
    
*   ♿ **TC14**: Skill recommendation list can be navigated via keyboard and read by screen readers.
    
*   ♿ **TC15**: All UI components on this screen follow WCAG contrast guidelines.

 ---   

### 🚀 Performance

*   🚀 **TC16**: Auto-generation of job description completes within 3 seconds for common titles.
    
*   🚀 **TC17**: Skill extraction happens quickly (<2s) for average job descriptions (<1000 characters).
    
*   🚀 **TC18**: UI remains responsive during generation and extraction for large inputs.