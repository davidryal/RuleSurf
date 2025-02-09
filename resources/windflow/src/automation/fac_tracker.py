import json
import os
from datetime import datetime
from typing import Dict, List, Optional

class FACTracker:
    def __init__(self, memories_dir: str):
        self.memories_dir = memories_dir
        self.current_session = None
        self.total_fac = 0
        self.model_usage = {}
        
    def start_session(self, initial_fac: float):
        """Initialize new session with starting FAC count"""
        self.total_fac = initial_fac
        self.current_session = datetime.now().strftime("%Y-%m-%d")
        
    def record_interaction(self, model: str, action: str, fac_cost: float) -> Dict:
        """Record model interaction and update FAC count"""
        if model not in self.model_usage:
            self.model_usage[model] = {"uses": 0, "total_fac": 0}
            
        self.model_usage[model]["uses"] += 1
        self.model_usage[model]["total_fac"] += fac_cost
        self.total_fac -= fac_cost
        
        return self._generate_report()
        
    def _generate_report(self) -> Dict:
        """Generate usage report with optimization suggestions"""
        report = {
            "current_fac": self.total_fac,
            "model_usage": self.model_usage,
            "optimization_suggestions": self._analyze_usage()
        }
        self._update_session_file(report)
        return report
        
    def _analyze_usage(self) -> List[str]:
        """Analyze usage patterns and suggest optimizations"""
        suggestions = []
        for model, stats in self.model_usage.items():
            if stats["total_fac"] > 5 and model != "@b":
                suggestions.append(f"Consider using @b for some {model} tasks")
        return suggestions
    
    def _update_session_file(self, report: Dict):
        """Update the current session's markdown file with FAC report"""
        session_file = os.path.join(self.memories_dir, 'sessions', f'{self.current_session}_session.md')
        
        try:
            with open(session_file, 'r') as f:
                content = f.read()
            
            # Update or append FAC tracking section
            fac_section = f"""
## FAC Tracking Update
- Current FAC: {report['current_fac']}
- Model Usage:
{json.dumps(report['model_usage'], indent=2)}

### Optimization Suggestions
{chr(10).join(report['optimization_suggestions'])}
"""
            
            with open(session_file, 'a') as f:
                f.write(fac_section)
        except Exception as e:
            print(f"Error updating session file: {e}")

def initialize_tracker(initial_fac: float = 2969.75) -> FACTracker:
    """Helper function to initialize tracker with default FAC"""
    tracker = FACTracker(r'c:\Users\david\code\_rules\windflow\memories')
    tracker.start_session(initial_fac)
    return tracker
