# WindFlow: AI Model Management Framework

## Overview
WindFlow is an advanced AI model management system for Windsurf designed to optimize model switching, track FAC (Flow Action Credits), and provide intelligent workspace testing.

## Features
- Automated FAC Tracking
- Memory Management
- Workspace Experiment Testing
- Model Performance Analysis

## Installation
```bash
pip install windflow
```

## Quick Start
```python
from windflow.src.automation import (
    initialize_tracker, 
    initialize_memory_manager, 
    initialize_test_framework
)

# Initialize components
fac_tracker = initialize_tracker()
memory_manager = initialize_memory_manager()
test_framework = initialize_test_framework()
```

## FAC Tracking

### Reporting Format
- Premium models end each response with:
  ```
  ---
  FAC: -X (Y → Z)
  ---
  ```
- X: FACs used
- Y: Previous total
- Z: Remaining total

### Next Steps & Improvements
- [ ] Develop automated FAC tracking tool
- [ ] Create visualization for FAC usage
- [ ] Implement more granular FAC cost tracking

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License.

## Note
Session tracking files are gitignored to protect personal usage data.
