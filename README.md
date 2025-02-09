# RuleSurf: Adaptive AI Development Framework (Version: 1.0.0)

## Overview

RuleSurf is an intelligent development framework that enables persistent, context-aware AI-assisted development across project sessions.

## Getting Started

### Project Initialization

1. Fork this repository
2. Clone to your local machine
3. Copy `.windsurfrules.template` to `.windsurfrules`
4. Fill out project details in `.windsurfrules`
5. Initialize Adaptive Project State (APS) with `init` command

### How This Works

- `.windsurfrules`: Your project configuration (you own this)
- `global_rules.md`: Adaptive Project State (AI maintains this)
- Commands: Use these to interact with AI

### Key Commands

- `init`: Start/resume project work
- `/d`: Get next steps + code changes
- `/c`: Get copyable code snippet
- `save`: Preserve current progress

### Prerequisites

- Windsurf IDE (recommended)
- Python 3.9+
- Git

## Setup for Windsurf Users

### Initial Configuration

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/RuleSurf.git
   cd RuleSurf
   ```

2. Configure Windsurf IDE:
   - Copy `.windsurfrules` to your Windsurf project directory
   - Review and customize `global_rules.md` to match your development workflow
   - Copy contents of `global_rules.md` to WindSurf settings -> Set Global AI rules or move to your /.codeium/windsurf/memories directory

### File Purpose Guide

- `.windsurfrules`: Project source of truth (user-owned)
  - Project requirements and specifications
  - Technical stack decisions
  - AI-assisted setup planning
  - User-defined project rules

- `global_rules.md`: Adaptive Project State (APS)
  - AI-maintained project state
  - Command reference
  - Task tracking with standardized status markers:
    - [ ] Todo
    - [⚒️] In Progress
    - [✓] Complete
    - [!] Blocked
    - [~] Deferred

### Customization Tips

- Always maintain separation between project-specific and global rules
- Use `global_rules.md` for universal guidelines
- Use `.windsurfrules` for project-specific configurations

## Key Features

- **Adaptive Context Management**
  - Persistent project state tracking
  - Intelligent context preservation
  - Seamless cross-session continuity

- **Recursive Development Cycle**
  - Iterative progress tracking
  - Continuous learning and adaptation
  - Automated milestone management

- **Intelligent Memory Layers**
  - Project-specific source of truth
  - Dynamic task and insight tracking
  - Automated context restoration

- **Workflow Optimization**
  - Proactive task management
  - Automatic lesson learning
  - Continuous improvement protocols

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/[yourusername]/RuleSurf.git
   cd RuleSurf
   ```

2. Explore the project structure:
   - `global_rules.md`: Adaptive Project State (APS)
   - `.windsurfrules`: Project source of truth (user-owned)

## Usage

### Command Reference

- `/n`: Propose next milestone actions
- `/d`: Detail next code changes and flow actions
- `/c`: Output copyable code snippet
- `/i`: Implement recent unadded changes
- `/a`: Enable auto-execution mode

The AI assistant will:

- Maintain your Adaptive Project State
- Track tasks and project insights
- Provide continuous context management
- Guide you through development cycles

For a complete list of commands, refer to `global_rules.md`

## Contributing

Love RuleSurf and want to help improve it? Awesome!

While this project is primarily a personal tool, I'm totally open to collaboration. If you have ideas, suggestions, or improvements:

1. Fork the repository
2. Create a branch for your feature
3. Make your changes
4. Open a pull request or issue

Your contributions are welcome, whether it's a typo fix, documentation improvement, or a cool new feature. Let's make RuleSurf even better together!

## Project Status

Under Active Development

Suggestions and feedback are always appreciated!
