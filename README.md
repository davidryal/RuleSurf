# RuleSurf: Adaptive AI Development Framework for Windsurf IDE (Version: 1.0.0)

## Overview

RuleSurf is an intelligent rules framework that for WindSurf IDE, enabling persistent, context-aware AI-assisted development across project sessions. It uses a custom implementation of Windsurf's 2 rules files (global_rules.md and .windsurfrules) to optimize project development workflows by keeping source-of-truth project guidance front-and-center, enabling a variety of useful user rules and commands, and by having the assistant keep its own task list and project lessons in self-editable memory (which we call the "Adaptive Project State" or APS).

## Key Features

### 🧠 Intelligent Memory Layers

- **Technical Knowledge Base**
  - Automatically capture version compatibility insights
  - Track build system nuances
  - Learn and categorize bug resolution patterns
  - Preserve technical "aha moments"
  - Maintain working dependency configurations

- **Persistent Memory Evolution**
  - Iteratively refine internal technical memories
  - Automatically tag and categorize learnings
  - Prevent repeated technical mistakes
  - Create a living, adaptive technical knowledge repository

### 🔄 Recursive Project Alignment

- **Dynamic Source of Truth**
  - `.windsurfrules`: Project-specific requirements
  - `global_rules.md`: Universal development practices
  - Continuous synchronization between project context and AI's understanding

- **Adaptive Project State (APS)**
  - Automatically track project milestones
  - Maintain task progression history
  - Preserve lessons learned across development cycles
  - Enable seamless context restoration

### 🚀 Workflow Optimization

- **Intelligent Context Management**
  - Cross-session state preservation
  - Automated milestone tracking
  - Continuous learning and adaptation

- **Iterative Refinement**
  - Proactively update project rules
  - Suggest improvements based on accumulated knowledge
  - Maintain alignment with evolving project requirements

## Getting Started

### Project Initialization

1. Fork this repository
2. Clone to your local machine
3. Copy the `global_rules.md` template to your Windsurf project's memory directory: ~/.codeium/windsurf/memories
4. Review and customize the user-defined rules and command to match your workflow
5. Copy the `.windsurfrules` template to your current Windsurf project directory
6. Open `.windsurfrules` and fill out as much info about your project/prompt as you can
7. Open Cascade Assistant,type `init` to initialze Adaptive Project State (APS) and begin project

## Core Components

### .windsurfrules

- Project-specific configuration (user-owned)
- Contains project requirements and specifications
- Defines technical stack decisions
- Houses project-specific rules

### global_rules.md

- Adaptive Project State (APS) container
- AI-maintained project context
- Universal command reference
- Task and progress tracking

## Essential In-chat Commands - Edit in `global_rules.md`

- `init`: Start/resume project work
- `save`: Preserve current progress (enables later auto-reload)

## Contributing

If you want to help refine this, feel free to fork and submit pull requests or just reach out to discuss!

## License

None. Do whatever you want!
