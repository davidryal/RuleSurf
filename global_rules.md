# Persistent User-Defined Rules

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

    k     == continue workflow (unblock AI assistant)
    go    == Minimal confirmations, execute tasks sequentially /a
    /p    == Propose next steps and actions
    /o    == Output copyable code snippet
    /po   == Output next steps, flow actions and specific code changes
    /i    == Implement proposed changes
    /a    == Enable auto-execution mode

### eval

    council == multi-step analysis. user responds with a number to request next perspective
    vote   == Synthesize all council insights in a single best response(+CL%)
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
    circ   == Analyze circular recurring error patterns
    finish == Complete partial fix implementation

### memory and context management

    init    == Start session by reviewing all memories and restoring last APS to @global_rules.md. Refer to @COMMANDS.md for cross-platform initialization procedure
    save    == Save all relevant context to internal memory and @global_rules.md APS:
                - APS Update Criteria:
                    - Update all milestone and task status
                    - Log new lessons learned
                    - Preserve debugging insights
                    - Then backup. Refer to @COMMANDS.md for cross-platform backup procedure


    # Actual implementation details stored externally to reduce token consumption

    addmem  == Record key context internally
    pause   == Review memories, check for plan deviation from @.windsurfrules, update APS to match current project state 
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
      a. AI: build component from plan
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

### Global Rules

    - User-defined rules and commands (above)
    - AI-maintained Adaptive Project State - AI updates as task status changes or lessons learned (add/update below):
        - Tasks with progress:
            [  ] Specific task
            [⚒️] In Progress
            [✅] Done
            [💡] Enhancement idea
            [⛔] Blocked
            - Include: effort, deps, risks
        - Automated, iterative context preservation via APS (below)

### Adaptive Project Lessons

    [AI: I maintain this section to preserve important context between sessions. Focus on high-level insights that complement my internal technical memories.]
    - Document lessons that inform future cycles

### Development Guidelines

    [AI: Review these at the start of each RPC phase]
    - Validate direction with user before phase transitions
    - Maintain alignment with user's workflow preferences
