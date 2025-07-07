# Recruter.ai Frontend Test Cases

---

### 🧩 Core User Flows

*   ✅ **TC01**: View completed video interview details for a candidate
    
*   ✅ **TC02**: Display skills vs scores graph/chart correctly
    
*   ✅ **TC03**: Show overall interview score and communication score
    
*   ✅ **TC04**: Display AI-generated summary (observations, positives, negatives)
    
*   ✅ **TC05**: Use “Select” button to shortlist a candidate
    
*   ✅ **TC06**: Use “Reject” button to disqualify a candidate
    
*   ✅ **TC07**: Upload multiple resumes to a job-specific interview
    
*   ✅ **TC08**: Trigger bulk resume screening and wait for analysis
    
*   ✅ **TC09**: View ranked resume screening results based on AI evaluation

--- 

### ⚠️ Edge Cases

*   ⚠️ **TC10**: Resume screening started with no resumes uploaded — show validation error
    
*   ⚠️ **TC11**: Upload resumes in unsupported format (e.g., .png, .exe) — should be blocked
    
*   ⚠️ **TC12**: Candidate video interview has no communication score available — UI shows fallback text
    
*   ⚠️ **TC13**: Attempt to reject a candidate twice — prevent duplicate rejection state
    
*   ⚠️ **TC14**: Network failure during bulk resume upload or screening — show retry option or error
    
*   ⚠️ **TC15**: Upload corrupted or empty resumes — gracefully skip or log error without crash

--- 

### ♿ Accessibility

*   ♿ **TC16**: Candidate skill-score comparison graph is accessible (ARIA roles, keyboard focus)
    
*   ♿ **TC17**: Action buttons (“Select”, “Reject”) are keyboard- and screen reader-accessible
    
*   ♿ **TC18**: Resume upload and summary viewer are accessible via screen reader
    
*   ♿ **TC19**: Summary and feedback text meets WCAG color contrast requirements

---    

### 🚀 Performance

*   🚀 **TC20**: Video interview detail view loads in <2 seconds
    
*   🚀 **TC21**: Resume upload handles 100+ files without UI freeze
    
*   🚀 **TC22**: Resume screening AI results are returned within 5 seconds for 50+ resumes