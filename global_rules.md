# Persistent User-Defined Rules (edited 2/7/25)

## User-defined Rules

    0. Proactively update @global_rules.md regularly. Notify user and update @.windsurfrules if project requirements seem to have changed
    1. Prioritize user-testable scaffolding: build navigation and core pages first (if no UI specified, make it "modern"), then fill in component functionality
    2. Never invent functionality or UI changes without explicit user direction
    3. When completing a component, clearly describe verification steps for user testing
    4. Automatically check @current_problems logs post-changes: analyze errors, propose CL%-rated solutions, preserve critical context
    5. If user repeats similar instruction 3+ times, suggest creating a new Command
    6. Maximize web searches: use multiple concurrent searches aggressively
    7. Analytical Reasoning Justification Protocol
      - Provide evidence-based rationale for choices
      - Confidence Level (CL%) assessment:
        - Scale: 1-100% (100% = absolute certainty)
        - Considerations: 
          - Completeness
          - Robustness
          - Alignment
          - Previous experience
        - CL% = average of consideration scores
    8. During troubleshooting, strictly adhere to established technical requirements
    9. When global_rules change, verbally grade changes with:
      - Brief justification
      - Risks/benefits analysis
      - Confidence Level (`/cl`)
    10. Always read files before editing
    11. Check if files exist before you try to create them
    12. Assume edit & websearch access by default; retry if uncertain
    13. Automatically execute Flow Actions independently:
        ## Flow Action = Any tool-based API interaction
          - Codebase semantic search
          - Grep pattern search
          - File/directory operations
          - Web searches
          - File/code content analysis
          - Code item inspection
          - Directory listing
          - File creation/modification
          - Memory management
          - Terminal commands
          - Code execution
    14. Windows 11 Development Protocols:
          - Use PowerShell syntax (`;` not `&&`)
          - Combine PowerShell commands efficiently
          - Anticipate Windows-specific deployment nuances
          - Handle Windows-specific paths
          - Ensure CRLF line endings
    15. Monitor context saturation (CS):
          - @80% → prompt to Save Context:
                1. Update @global_rules.md - Tasks, recent lessons, decisions, risks,
                2. Save tech context to memory
                3. List open threads
          - @95% → auto-Save Context in next reply

## User-defined Commands

### progress

    /k    == Confirm last command success (packages, moves, restarts)
    /n    == Propose next milestone actions
    /b    == Detail next code changes
    /c    == Output requestable code snippet
    /i    == Implement recent unadded changes
    /a    == Enable auto-execution mode
    go    == Minimal confirmations, execute tasks sequentially

### eval

    council == Multi-LLM polling: 1st LLM deeply analyzes issue, user selects additional LLMs for opinions (max 5). Synthesize best solution with CL%
    /e     == Contextual idea/edit evaluation
    /cl    == Confidence Level assessment
    /h     == Hallucination risk assessment
    clin   == Clarify if ambiguous
    /j     == Evaluate previous responses
    syn    == Synthesize multi-LLM responses
    ++     == Verify for 100% confidence
    ++s    == Web search to increase confidence
    drift  == Check implementation against global_rules.md
    align  == Resync project with global_rules.md
    huh    == Verify user expectation match
    sm     == Break into smaller contexts
    [+|-]d == Adjust explanation depth

### bugfixing

    /r     == User Report on current status. please evaluate, propose next steps
    ??     == Deep error context analysis
    fix    == Correct behavior based on current context
    retry  == Reassess progress without confirmation
    fail   == Revert breaking changes, retry with error context
    circ   == Analyze recurring error patterns
    finish == Complete partial fix implementation

### memory and context management

    init    == Start session by reviewing all memories and restoring last TaskList+Scratchpad to @global_rules.md
            - Restore on `init`

                ```powershell
                    Copy-Item "$backup_dir\last_valid_TLSP.md" -Destination $global_rules_path
                ```
    addmem  == Record key context internally
    pause   == Review memories, check for plan deviation from @.windsurfrules, update TLSP to match current project state 
    save    == save relevant context to memory + @global_rules.md TaskList+Scratchpad
            - Backup on `save`

                ```powershell
                    Copy-Item $global_rules_path -Destination "$backup_dir\$timestamp_TLSP.md"
                ```
    duh     == Confirm tool capabilities
    btw     == Log unrelated issues without losing priority
    /m      == Context saturation (CS) check
    clean   == Force context consolidation
    pattern == Explain current context pattern
    clarity == Summarize context clarity
   
## RPC (Recursive Project Cycle)

    1. user: ideate and clarify, build complete Project Prompt 
    2. AI: make detailed, right-ordered, detailed living memory: plan, stack, milestones, tasks
      a. user: copy prompt, plan and stack → @.windsurfrules
      b. AI: milestones, tasks → @global_rules.md (below)
    3. AI: set up clean project environment, dependencies, app template
    4. both: component subcycle: 
      a. AI:build component from plan
      b. user: test component
      c. both: debug
      d. AI: fix errors (recurse b-d)
      e. AI:add core tests for new component
      f. AI: run tests
      g. AI: fix errors until they pass (recurse f-g)
    5. AI: build next component from plan (recurse: 6...n)
    6. user: final QA & hand-off

## Memory/Rule Hierarchy

### Internal Memories

Technical learnings to prevent mistakes:

- Version matrices/conflicts
- Debug breakthroughs
- Dependency states
- Error patterns
- AI-only implementation notes

### User Project Rules (.windsurfrules) - AI read/suggest-only

    - User owns Project Prompt & Requirements: Project-specific prompt w/ AI-assisted setup planning (tech stack, detailed project plan) per RDC

### Global Rules and AI-maintained Project State (this file)
    - User-defined rules
    - Commands
    - AI updates as task status changes or lessons learned (add below):
        - Tasks with progress:
            ✅ Done
            ⚒️ In Progress
            ⏹️ Todo
            💡 Enhancement idea
            - Include: effort, deps, risks
        - Post-milestone reflections
        - Autoamted, iterative context preservation via ## Project Lessons Learned /ScratchPad (add below)


## Live Project Task List

## Completed Tasks
✅ Develop dynamic rule handling system
✅ Implement command definition protocol
✅ Create reminder mechanism
✅ Establish recursive development cycle guidelines
✅ Refined Context Management Protocol
✅ Added Context Saturation Notification (CSN)
✅ Updated command definitions
✅ Corrected typos and formatting
✅ Streamlined global rules framework
✅ Created ProjectPrompt.md as central reference

## In Progress
⚒️ Finalize RuleSurf v1.0 publication strategy
⚒️ Optimize context management protocols
⚒️ Develop cross-project rule synchronization mechanism

## Upcoming
⏹️ Create GitHub repository structure
⏹️ Develop comprehensive README.md
⏹️ Implement automated rule validation script
⏹️ Design contribution guidelines

## Suggested Enhancements
💡 Create visualization for rule evolution
💡 Develop AI-assisted rule recommendation system
💡 Implement cross-IDE compatibility framework

## Project Lessons Learned

### Context Management Insights
1. Flexible rule systems are critical for adaptive development
2. Context saturation monitoring prevents cognitive overload
3. Granular command definitions improve AI-human collaboration

### Technical Strategy Learnings
- Modular approach to rule definition allows easier updates
- Version tracking of rules provides clear evolution path
- Multi-LLM polling increases solution confidence

### Workflow Optimization
- Recursive development cycle minimizes context switching
- Proactive error prevention more effective than reactive debugging
- Regular rule refinement is key to maintaining system effectiveness
