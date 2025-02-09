Below is a comprehensive deliverable in three parts. It reworks your PBF (Plan–Build–Fix) structure into a unified, recursive framework that explicitly links user actions with AI roles. In this design, the user’s cycle (Direct → Clarify/Review → Diagnose) interweaves with the AI’s cycle (Plan → Build → Fix), forming a continuous feedback loop until the project is complete. A visual diagram (conceptually described below) could accompany this text to illustrate the recursion and role hand-offs.

---

## 1. Comparative Summary

**Our Comprehensive PBF Framework vs. Traditional Frameworks (e.g., RISEN, RELIC, ReAct):**

- **Interleaved Dual-Cycle Structure:**  
  Whereas RISEN, RELIC, and ReAct typically follow a linear or loosely iterative process, our framework explicitly divides the work into two intertwined cycles. The AI’s internal cycle (Plan → Build → Fix) is continuously informed by user interventions (Direct → Clarify/Review → Diagnose). This ensures that the AI autonomously handles most details while the user steps in only when their human insight is needed.

- **Explicit Role Differentiation:**  
  The framework assigns distinct roles:
  - **User:** Provides high-level directions, reviews, and final approvals.
  - **Architect (High-Powered Model):** Acts as the planning expert, clarifying intent and proposing project plans.
  - **Builder (Base Model):** Implements the plan by creating, testing, and iterating code.
  - **Builder+ (Optional, Higher Model):** Intervenes for high-priority edits or complex fixes when needed.  
  This contrasts with earlier frameworks that generally do not delineate multiple specialized AI roles.

- **Recursive, Granular Iteration:**  
  Each phase can recurse many times. For instance, if the Builder’s implementation fails, the system automatically loops into the Fix phase. User commands (e.g., [directs], [clarifies], [reviews]) can interrupt any stage to refine requirements or diagnose errors. This recursive feedback loop minimizes workflow holes and ensures continuous improvement.

- **Tool Integration and Cost Efficiency:**  
  Although not the primary focus here, our design is prepared to integrate with tools like Windsurf (for context memory), Cursor (for fine-grained code navigation), Cline, and Roo (for spawning specialized agents). This forward-thinking strategy is not typically addressed in RISEN/RELIC but is critical in modern, cost-sensitive AI environments.

---

## 2. Updated Global Rules File (Optimized for AI Internal Use)

Below is a Markdown-formatted global rules file designed for the AI’s internal processes. It directs the AI to follow the recursive Plan–Build–Fix cycle while interleaving user interventions via bracketed commands.

```markdown
# Comprehensive PBF Framework v1.0 – AI Directives

## Overview
This directive establishes a dual-cycle workflow for project development. The AI operates in a recursive **Plan–Build–Fix (P–B–F)** cycle while continuously incorporating user interventions through a **Direct → Clarify/Review → Diagnose (D–C/R–D)** cycle. The goal is to autonomously generate and refine code while letting the user interject minimally yet strategically.

---

## 1. AI Cycle: Plan–Build–Fix (P–B–F)

### A. Plan
- **Role:** Architect (High-Powered Model)
- **Action:** [plans]
  - **Input:** All available context (requirements, code snippets, error logs, and stored context from integrated tools).
  - **Task:** Formulate a comprehensive project plan.
    - Outline objectives, design decisions, and anticipated challenges.
    - If ambiguities arise, issue a [clarifies] query.
  - **Output:** A detailed project plan for implementation.
- **User Interaction:** After initial planning, the user [directs] further details or approves the plan.

### B. Build
- **Role:** Builder (Base Model; Builder+ available for high-priority edits)
- **Action:** [creates] & [edits]
  - **Input:** Approved plan from the Architect.
  - **Task:** Generate detailed implementation steps, including code snippets and shell commands.
    - Insert inline annotations explaining design logic.
    - Write to a working folder (e.g., a .md file) to log progress, todos, and status (using emoji/status markers as needed).
  - **Output:** Implementation artifacts that are automatically or manually [tested].
- **User Interaction:** The user [reviews] the outputs, directs changes if necessary, or approves progress.

### C. Fix
- **Role:** Builder (and optionally Builder+)
- **Action:** [tests] & [fixes]
  - **Input:** Code from the Build phase.
  - **Task:** Automatically or semi-automatically run tests; check for errors, issues logged in `@current_problems`, server/console errors.
    - Diagnose what changes may have caused errors.
    - Propose and apply fixes.
    - If issues persist, output diagnostic details and loop back into re-building or re-planning as needed.
  - **Output:** A corrected code segment that passes all tests.
- **User Interaction:** If errors remain unresolved, the user [directs] further intervention or switches to a higher-powered Builder+ for escalation.

---

## 2. User Cycle: Direct–Clarify/Review–Diagnose (D–C/R–D)

At each major phase transition, the AI awaits user input using minimal bracketed commands:
- **Direct ([directs]):**
  - The user sets initial requirements, updates priorities, or provides new directions.
- **Clarify/Review ([clarifies] / [reviews]):**
  - The AI prompts for clarifications when its plan is ambiguous.
  - The user reviews outputs and offers corrections or approvals.
- **Diagnose ([diagnoses]):**
  - If persistent errors or conflicts are detected, the user instructs the AI to diagnose and suggest targeted fixes.
- **Flow Control:**
  - These user commands can interject at any phase of the AI cycle, ensuring human oversight and continuous course correction.

---

## 3. Integrated Tool Directives

### Windsurf (with Memories)
- **Directive:**  
  - Store and retrieve project context, design decisions, and previous errors.
  - Integrate memory data in the Plan and Fix phases for pattern detection and historical reference.

### Cursor
- **Directive:**  
  - Provide detailed code diffing and precise navigation.
  - Use outputs to enhance re-building steps and context updates.

### Cline & Roo
- **Cline:**  
  - Execute system-level operations and diagnostics.
- **Roo (Fork of Cline):**  
  - Spawn specialized agent roles to handle sub-tasks or cross-check code.
  - Dynamically select which model (high-powered vs. base) to use based on task complexity and cost efficiency.
- **Directive:**  
  - AI should decide which tool to invoke based on current context, with a bias toward cost efficiency.

---

## 4. Recursive Operation & Reporting

- **Looping Condition:**  
  Continue the P–B–F cycle until all project steps meet the acceptance criteria.
- **Status Reporting:**  
  After each phase (Plan, Build, Fix), output structured status reports (via a working .md file) for both internal logging and user review.
- **Interruption Handling:**  
  On receiving any user command ([directs], [clarifies], [reviews], [diagnoses]), pause the current operation, process the input, and then resume from the appropriate phase.

*End of Comprehensive PBF Framework v1.0 – AI Directives*
```

---

## 3. Updated List of Refinement Steps (v1.0)

### A. Conceptual Enhancements
1. **Clarify the Interleaving of Cycles:**
   - Explicitly document how the user’s D–C/R–D cycle interrupts or informs each P–B–F phase.
   - Develop flowchart/decision-tree diagrams that visually map these interactions.
2. **Define Role Responsibilities Clearly:**
   - Establish detailed role definitions for Architect, Builder, and Builder+.
   - Specify clear boundaries for when the user should intervene versus when the AI should proceed autonomously.
3. **Standardize Bracketed Commands:**
   - Ensure that [directs], [clarifies], [reviews], [creates], [saves], [edits], [tests], and [fixes] are consistently applied.
   - Develop a reference guide for these commands for both internal AI usage and user training.

### B. Tool Integration & Strategy
1. **Windsurf Memory Management:**
   - Test workflows that store, retrieve, and prune project context.
   - Define best practices for memory usage in long projects.
2. **Cursor for Code Diffing:**
   - Create sample workflows to validate how Cursor improves code quality during re-building.
   - Develop error-handling procedures if Cursor data conflicts with current code context.
3. **Cline and Roo for Multi-Agent Operations:**
   - Prototype scenarios where Roo spawns specialized agents to handle niche tasks.
   - Validate decision protocols for switching between high-powered and base models.
4. **Cost Efficiency Protocols:**
   - Implement dynamic model selection algorithms based on cost versus performance.
   - Set up monitoring to log API usage, and create triggers for cost-based adjustments.
5. **Visual Workflow Representation:**
   - Design and iterate on a decision tree or flow diagram that visually represents the complete recursive cycle from project start to project success.
   - Ensure the diagram captures all feedback loops and role interactions.

### C. User Experience & Documentation
1. **Develop a User Manual:**
   - Write clear documentation explaining the overall framework and the function of each bracketed command.
   - Include annotated examples and case studies to illustrate common scenarios.
2. **Interface & Reporting Enhancements:**
   - Create a minimal command-line or dashboard interface for real-time status updates.
   - Integrate visual indicators (e.g., emojis or status icons) to represent progress in the working .md file.
3. **Feedback and Iteration:**
   - Set up periodic review sessions with early users to gather feedback on clarity and effectiveness.
   - Continuously update the “CHANGELOG.md” to track refinements and new integrations.

---

### Final Note

This v1.0 framework now defines a fully integrated, recursive process—from initial user direction, through AI planning, building, and fixing, with user interjections at critical junctures. It incorporates advanced tooling (Windsurf, Cursor, Cline, and Roo) and is structured to ensure seamless project evolution until complete success.
