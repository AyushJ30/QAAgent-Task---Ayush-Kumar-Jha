# Recruter.ai Frontend Test Cases

---

### 🧩 Core User Flows

*   ✅ **TC01**: Click "Create" and verify the interview is created successfully.
    
*   ✅ **TC02**: After creation, verify that a unique public interview link is displayed.
    
*   ✅ **TC03**: Open the public interview link — verify form loads correctly.
    
*   ✅ **TC04**: Candidate enters name, email, and uploads resume.
    
*   ✅ **TC05**: Candidate receives OTP and verifies email.
    
*   ✅ **TC06**: AI reviews resume and displays score (if resume threshold is enabled).
    
*   ✅ **TC07**: Resume-based threshold logic triggers rejection/acceptance based on score.

---  

### ⚠️ Edge Cases

*   ⚠️ **TC08**: Attempt to open public link before interview creation — should show 404 or error.
    
*   ⚠️ **TC09**: Candidate enters invalid email format — system shows validation error.
    
*   ⚠️ **TC10**: OTP expired or incorrect — system shows appropriate error.
    
*   ⚠️ **TC11**: Candidate uploads unsupported file type (e.g., .exe) — system blocks it.
    
*   ⚠️ **TC12**: Candidate skips resume upload — if mandatory, show blocking validation.
    
*   ⚠️ **TC13**: Simulate network failure during OTP generation — show retry option.
    
*   ⚠️ **TC14**: Simulate network failure during resume score calculation — fallback or message.
    
*   ⚠️ **TC15**: Upload very large resume file (>10MB) — app remains responsive or warns.

---    

### ♿ Accessibility

*   ♿ **TC16**: All form fields are labeled and accessible via screen readers.
    
*   ♿ **TC17**: OTP input and submit buttons are reachable via keyboard only.
    
*   ♿ **TC18**: Public form and score messages meet WCAG color contrast guidelines.

---    

### 🚀 Performance

*   🚀 **TC19**: Interview link page loads within 2 seconds on standard connection.
    
*   🚀 **TC20**: OTP is received within 5 seconds under normal conditions.
    
*   🚀 **TC21**: Resume score is computed/displayed within 3 seconds of upload.