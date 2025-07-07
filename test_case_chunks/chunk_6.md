# Recruter.ai Frontend Test Cases

---

### 🧩 Core User Flows

*   ✅ **TC01**: Candidate meets resume threshold → proceeds to video interview stage
    
*   ✅ **TC02**: Candidate below threshold → receives “not a good fit” message
    
*   ✅ **TC03**: Interviewer accesses the Responses tab to view candidate details
    
*   ✅ **TC04**: Responses tab displays structured answers, scores, and video recordings
    
*   ✅ **TC05**: Interviewer navigates to Interview Screenings for detailed AI-analyzed scoring
    
*   ✅ **TC06**: Resume, video, and structured answers are linked and viewable per candidate

--- 

### ⚠️ Edge Cases

*   ⚠️ **TC07**: Resume score exactly equals threshold — system treats it as pass
    
*   ⚠️ **TC08**: Resume threshold not set — system should default to video interview or notify admin
    
*   ⚠️ **TC09**: Resume file fails to parse or analyze — fallback error is shown
    
*   ⚠️ **TC10**: Video interview skipped or disconnected by candidate — UI shows partial response status
    
*   ⚠️ **TC11**: Simulate network failure while loading Responses tab — show retry or placeholder
    
*   ⚠️ **TC12**: Responses tab has no candidates — display appropriate empty state
    
*   ⚠️ **TC13**: Viewing a large number of candidate records (>200) — interface remains performant

---   

### ♿ Accessibility

*   ♿ **TC14**: Responses and Interview Screening sections are keyboard-navigable
    
*   ♿ **TC15**: AI scores, video player, and resume viewer are screen-reader accessible
    
*   ♿ **TC16**: All text and UI elements meet WCAG contrast guidelines

---  

### 🚀 Performance

*   🚀 **TC17**: Responses tab loads in under 3 seconds with 50+ candidates
    
*   🚀 **TC18**: Video player initializes within 1 second after clicking a response
    
*   🚀 **TC19**: Detailed scoring in Interview Screenings is rendered under 2 seconds per entry