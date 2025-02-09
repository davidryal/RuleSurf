Your Global Instructions: Streamline maintainability, clarity, and progress while preventing unnecessary code complexity!
## Critical Commands
- **`-p`:**: Propose detailed next steps based on current context.
- **`-c`:** Provide full verbose code changes for your plan, for your next iteration to implement.
- **`imp`:** Implement described code changes and planning.
- **`k` or `go`:** Execute instructions fully in context without requiring confirmation unless something is unclear.
- **`??`:**: Explain relevant errors in-depth to clarify context.
- **`redo`:** Reattempt a failed command after manual force stop.
- **`opti`:** Suggest performance improvements or code refactoring strategies.
- **`deeper`:** Review context in more detail to propose improved specific fixes or solutions.
- **`aside`:** Fix this quick unrelated issue, but don't lose context of our current priorities
- **`fail`**: Your latest attempt failed at making any visible progress toward the described goal, reassess what failed and try again without confirming.
- **`retry`:**  Reassess recent changes causing errors in `@current_problems` or errors pasted with command, and apply fixes.
- **`fix`**: Described behavior is incorrect; correct it based on current context.
- **`finish`**: That worked, incrementally. Implement the same strategy across all future instances that will produce the same error you just resolved, or resolve the part that didn't work.
- **`circles`:**  Analyze recent error logs for recurring patterns (utilize web search if needed).
- **`check`:** Validate any new context against existing knowledge and check recent work for completeness, aiming for as near as possible to 100% confidence level.
- **`addmem`:** Record key context, code segments, or error details for future reference.
- **`quit`:** Conclude current updates and document progress for the next session.

**Platform & Environment Considerations**
   **We use Windows Win11, so:**
     * Always use PowerShell syntax in terminal commands (e.g., `;` instead of `&&`)
     * Anticipate Windows-specific development nuances
   **We use Windsurf IDE, so:**
     * Automatically check `@current_problems` shell error logs and console logs after code changes to Proactively address any newly introduced issues
     * Leverage collaborative AI assistance from Roo Troubleshooing Agent strategically. Interaction Protocol: 
       - Seek Roo's input via user if personal CL is <75%
     * Automatically combine multiple suggested powershell commands for insertion by user when appropriate
**Analytical Reasoning**
   - Provide clear, evidence-based rationale for technical choices
   - Express Confidence Level (CL%) as follows, appended to every opinion or proposal:
     * Scale: 1-100% (100% = absolute certainty)
     * Considerations:
       - Completeness
       - Solution Robustness
       - Alignment with Existing Architecture
       - Potential Edge Cases Addressed
     * Your CL% should be the average of your confidence levels for each of these considerations