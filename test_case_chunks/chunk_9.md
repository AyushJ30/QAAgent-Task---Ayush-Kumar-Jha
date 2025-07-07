# Recruter.ai Frontend Test Cases

---

### 🧩 Core User Flows

*   ✅ **TC01**: View AI recommendation and decide to reject or proceed
    
*   ✅ **TC02**: Proceeding with a candidate generates a 24-hour valid interview link
    
*   ✅ **TC03**: Candidate receives and opens interview link successfully
    
*   ✅ **TC04**: Candidate submits interview before the link expires
    
*   ✅ **TC05**: Interview is marked as “Submitted” and visible to recruiter
    
*   ✅ **TC06**: Recruiter initiates the **Interview Screening** process
    
*   ✅ **TC07**: AI-generated interview summary becomes available for review

---    

### ⚠️ Edge Cases

*   ⚠️ **TC08**: Attempting to use the interview link after 24 hours → show “Link Expired” message
    
*   ⚠️ **TC09**: Candidate submits empty or corrupted video file → show appropriate error
    
*   ⚠️ **TC10**: Recruiter tries to initiate screening before interview is submitted → block or warn
    
*   ⚠️ **TC11**: Interview submission interrupted due to poor internet → autosave or retry prompt
    
*   ⚠️ **TC12**: Recruiter clicks “Reject” on already rejected candidate — prevent duplicate state

---   

### ♿ Accessibility

*   ♿ **TC13**: Interview invitation and action buttons are keyboard- and screen-reader accessible
    
*   ♿ **TC14**: Submission confirmation message is read by screen readers
    
*   ♿ **TC15**: Expired link page includes accessible alert role and navigation options

---   

### 🚀 Performance

*   🚀 **TC16**: Interview link loads in under 2 seconds on average connections
    
*   🚀 **TC17**: Video submission uploads <100MB file without UI freeze
    
*   🚀 **TC18**: Interview summary loads under 2 seconds after processing completes