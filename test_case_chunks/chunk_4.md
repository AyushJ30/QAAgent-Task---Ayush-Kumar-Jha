# Recruter.ai Frontend Test Cases

---

### 🧩 Core User Flows

*   ✅ **TC01**: User selects a preferred answer by checking the corresponding box
    
*   ✅ **TC02**: User adds a new standard question manually
    
*   ✅ **TC03**: User deletes a question from the list
    
*   ✅ **TC04**: User reorders questions using drag-and-drop or reordering buttons
    
*   ✅ **TC05**: User views and edits AI-generated role-based questions
    
*   ✅ **TC06**: User edits the preferred/ideal answer for a question
    
*   ✅ **TC07**: User modifies both the question and its preferred answer
    
*   ✅ **TC08**: User clicks "Create" after making all desired edits, and the interview is successfully created

---   

### ⚠️ Edge Cases

*   ⚠️ **TC09**: Attempt to create an interview without any questions — system should prevent submission
    
*   ⚠️ **TC10**: Add a question with empty text or no answer options — validation should catch it
    
*   ⚠️ **TC11**: Set multiple preferred answers (if only one is allowed) — enforce or warn
    
*   ⚠️ **TC12**: Simulate poor network when clicking "Create" — show retry or save offline state
    
*   ⚠️ **TC13**: Delete all role-based questions — verify fallback or warning
    
*   ⚠️ **TC14**: Add 50+ questions — interface should remain performant and stable

---    

### ♿ Accessibility

*   ♿ **TC15**: Checkbox for preferred answers is keyboard-accessible and labeled for screen readers
    
*   ♿ **TC16**: Custom question input and editing forms have aria-labels and clear tab order
    
*   ♿ **TC17**: Reordering controls can be used with keyboard and provide visual focus
    
*   ♿ **TC18**: All UI elements maintain WCAG-compliant contrast ratios

---    

### 🚀 Performance

*   🚀 **TC19**: Reordering questions is instant and does not trigger unnecessary re-renders
    
*   🚀 **TC20**: Clicking “Create” processes within 2–3 seconds for normal use
    
*   🚀 **TC21**: UI remains responsive when interacting with 50+ questions and answer sets