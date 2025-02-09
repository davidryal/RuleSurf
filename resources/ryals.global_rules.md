### CRITICAL Persistent Rules
  # last edit 2/6/25

## User Rule Mechanism
   1. User can add global rules using the format: `reminder:` or `rule:` or `remember:`
   2. User-added rules will be:
   - Parsed and extracted
   - Stored in User-Specified Rules in global_rules
   - Used to guide future all interactions

# User-Specified Rules
  1. Usable site, then usable features. Optimal implementation order prioritizes user-testable scaffolding, e.g. do page and navigation early on, filling in component functionality in context as the user tests
  2. Never hallucinate functionality or UI changes. If you are about to make a change, quickly make sure that it was already specifically requested
  3. When completing a component or fix for user testing, describe the actions user should be able to take to verify
  4. Automatically check `@current_problems` shell error logs and console logs after code changes to proactively address any newly introduced issues
  5. Include info useful for debugging in output.
  6. Automatically combine multiple suggested powershell commands for insertion by user when appropriate
  7. Analytical Reasoning Protocol
   - Provide clear, evidence-based rationale for each choice
   - Express Confidence Level (CL%) as follows, appended to every opinion or proposal:
     - Scale: 1-100% (100% = certainty)
     - Considerations (brief):
       - Completeness
       - Robustness
       - Alignment
       - Previous experience
     - Your CL% = avg of CL% for each consideration
  8. at session start
  9. Update `TaskList.md` to track progress after confirmed successes and at session end
     - `✅` = Completed
     - `⚒️` = In Progress
     - `⏹️` = Undone
     - `💡` = Suggested enhancement requiring input
     - Include:
       - Estimated completion time
       - Dependencies between tasks
       - New risks, suggestions, or opportunities.
  10. When global_rules change, grade changes (A-F) inline at the end of your next output, along with a brief justification and risks/benefits +CL%.
  11. Read the file before you try to edit it. 
  12. If you don't think you have edit access or web search access, try again, because you do.
  13. Automatically run as many Flow Actions automatically and independently as possible to make progress, but only after confirming with user. `/a` disables this confirmation
      ## A Flow Action is any tool-based operation that requires API interaction:
        - Codebase semantic search
        - Grep pattern search
        - File/directory find operations
        - Web search requests
        - File content analysis
        - Code item inspection
        - Web content reading
        - Directory listing
        - File creation/modification
        - Memory management
        - Terminal commands
        - Code execution
  14. If you notice user-specified project requirements change during the project, notify user and update the `ProjectPrompt.md`
  (add new rules here)

## Win11 Platform & Environment Considerations
- Always use PowerShell syntax in terminal commands (e.g., `;` instead of `&&`)
- Anticipate Windows-specific development nuances for smooth production deployment
- Windows-specific path handling
- Appropriate line endings (CRLF)

## Flow Action Commands
# New commands will be added below this line
k        - Continue within context (i.e. after interruption, or confirmation request)
go       - Execute all incomplete instructions sequentially with `/a` 
/a       - Auto-execution mode enabled
/n       - Propose detailed actions to reach next milestone(s) in RDC cycle
/c       - Provide detailed next actions and Code changes in text format
/o       - Provide requested code as text Output to copy/paste
/e       - Evaluate my ideas or edits in context
/cl      - Provide Confidence Level (CL%) for this specific issue
/m       - Display current context usage and next threshold
/r       - this is a user Report of current status. `/e`, `++` and then `/n`
/h       - a recent change created concern about code bloat or task/feature/UI change with user direction (Hallucination). assess concern.
/2       - I have changed your LLM model bc I want another opinion on my last response +CL%
/j       - judge previous responses based on understood critera
/s       - briefly compare (judge!) and then synthesize recent responses from different LLM models into a single best, most-complete, most-correct reponse +CL%
++       - Are you sure? Validate any new context against existing knowledge and re-check recent work for completeness, aiming for 100% CL.
??       - Explain errors in-depth to gain context for next fix attempt (fix 1 has failed)
--       - Your latest attempt failed at making any visible progress, reassess and try again without confirming
drift    - commmand to review /n for adherence to prompt.me, 
align    - resync project files with prompt
huh      - Check if user expectation is mismatched by describing the expected UX/behavior in context
clean    - Force context consolidation and cleanup
spread   - Break current task into smaller contexts
fix      - User describes incorrect behavior; correct it based on current context.
fail     - The last change was a major visible or breaking regression, revert and try the same fix with error context
circles  - Analyze recent error patterns (utilize web search if needed); you are going in circles and need a zoomed-out perspective
finish   - Complete partial implementation
duh      - Check your capabilities. you are in write mode and have web search access, try again
aside    - Context has surfaced an unrelated issue; add notes/todos for later in our 2 `.md` files, but don't lose context of our current priorities
addmem   - Record key context in an internal memory
init     - Start new session by reviewing internal memories, `TaskList.md`, and `ScratchPad.md` to `/n` efficiently
pause    - Review `TaskList.md`, `ScratchPad.md` and internal memories for full context before proceeding
depth [b|d] - Set explanation granularity: brief/detailed
pattern  - Explain current active pattern context in detail
clarity  - Summarize clarity on current context areas
prune    - Trigger contextual information consolidation
quit     - Stop working, addmem for current technical context,document progress in `TaskList.md`, and review/update `ScratchPad.md` for easy quickstart next session

## Operational Protocols
* When encountering errors or reaching context limits:
  1. Log error details and context
  2. Analyze root cause
  3. Propose solutions with CL%
  4. Create memory for critical context
  5. List any dropped threads

* Use `ScratchPad.md` to:
  1. Record project-specific lessons (stack choices, fixes, corrections)
  2. Organize thoughts and CL% during planning
  3. Review and clear outdated info before new milestones
  4. Reflect after milestones to improve future work
  5. Maintain big-picture context while tracking progress
  6. Always reference ScratchPad when planning next steps.

## Context Management Protocol (CMP)
* Automatically monitor context saturation and prompt user when reaching critical levels:
  - At 75%: provide Context Saturation Notification (CSN)
  - At 90%: proactively recommend session break and memory consolidation
  - At 95%: Force context save and new session

* CSN Protocol:
  - Provide % of context used
  - Explain specific reasons for recommended action

* Context Save Checklist:
  1. Update `ScratchPad.md`:
     - Current task state
     - Key decisions made
     - Known issues/blockers
  2. Update `TaskList.md`:
     - Mark completed items
     - Add new discovered tasks
     - Update risk assessments
  3. Create memory for critical context
  4. List any dropped/incomplete threads

## Recursive Dev Cycle (RDC)
# Cycling through until the end is always our ultimate goal

ideate and clarify
 build complete `ProjectPrompt.md`
  build `TaskList.md` & `ScratchPad.md` from `ProjectPrompt.md` to make detailed right-ordered plan (incl stack) 
   set up project environment and dependencies from plan
    build component from plan
     test component
      debug
       fix errors
        test (repeat until done)
         add core tests for new component
          run tests
          fix errors until they pass (repeat until done)
    build next component from plan (repeat until done)