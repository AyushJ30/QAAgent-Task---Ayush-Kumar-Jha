# Recruter.ai Frontend Test Cases

---

### 🧩 Core User Flows

*   ✅ **TC01**: Upload resume and receive a skill-based resume score
    
*   ✅ **TC02**: AI provides recommendation status: **Recommended / Not Recommended**
    
*   ✅ **TC03**: Display semantic skill alignment report (highlight matching/missing skills)
    
*   ✅ **TC04**: Candidate with partial skills and high score is **not recommended** due to lack of alignment — AI explains reasoning
    
*   ✅ **TC05**: Candidate with moderate score but aligned skills is **recommended**
    
*   ✅ **TC06**: View job description used for evaluation alongside AI reasoning

---   

### ⚠️ Edge Cases

*   ⚠️ **TC07**: High resume score but candidate **not recommended** — ensure explanation is shown (e.g., domain mismatch)
    
*   ⚠️ **TC08**: Resume contains skills with synonyms (e.g., "Node.js" vs "JavaScript backend") — semantic matching should still work
    
*   ⚠️ **TC09**: Upload resume with no skill matches — score is low and AI suggests rejection with clear feedback
    
*   ⚠️ **TC10**: Candidate with similar roles but irrelevant domains — AI gives partial score and warns about mismatch
    
*   ⚠️ **TC11**: Resume uses large, complex formatting or multi-column layouts — AI still parses effectively
    
*   ⚠️ **TC12**: Network failure during resume scoring — retry option or timeout error shown

---   

### ♿ Accessibility

*   ♿ **TC13**: Resume score and recommendation are announced by screen readers
    
*   ♿ **TC14**: Semantic skill match report has proper contrast and keyboard accessibility
    
*   ♿ **TC15**: Explanation block (“Why this candidate is not recommended”) is accessible with ARIA roles

--- 

### 🚀 Performance

*   🚀 **TC16**: Resume score and recommendation load within 3 seconds after upload
    
*   🚀 **TC17**: Bulk resume evaluations (e.g. 50 resumes) complete without UI freezing
    
*   🚀 **TC18**: Semantic analysis report is responsive even with lengthy resumes (5+ pages)