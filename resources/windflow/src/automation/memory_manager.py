from typing import Dict, List, Optional
import json
import re
from pathlib import Path
import os

class MemoryManager:
    def __init__(self, memories_dir: str):
        self.memories_dir = Path(memories_dir)
        self.pattern_threshold = 3
        self.confidence_threshold = 0.85
        
    def detect_patterns(self) -> List[Dict]:
        """Analyze sessions for recurring patterns"""
        patterns = []
        session_files = list(self.memories_dir.glob("sessions/*.md"))
        
        for file in session_files:
            new_patterns = self._analyze_file(file)
            patterns.extend(new_patterns)
            
        return self._filter_significant_patterns(patterns)
        
    def migrate_memory(self, pattern: Dict) -> bool:
        """Migrate detected pattern to appropriate location"""
        if pattern.get('confidence', 0) >= self.confidence_threshold:
            if pattern.get('scope') == 'system':
                return self._migrate_to_system(pattern)
            elif pattern.get('scope') == 'workspace':
                return self._migrate_to_workspace(pattern)
        return False
        
    def _analyze_file(self, file: Path) -> List[Dict]:
        """Extract patterns from individual files"""
        patterns = []
        content = file.read_text()
        
        # Look for recurring themes
        themes = re.findall(r'## Insights\n(.*?)##', content, re.DOTALL)
        for theme in themes:
            patterns.append({
                "type": "insight",
                "content": theme.strip(),
                "source": file.name,
                "confidence": self._calculate_confidence(theme),
                "scope": self._determine_scope(theme)
            })
            
        return patterns
    
    def _calculate_confidence(self, text: str) -> float:
        """Calculate confidence based on text complexity and recurrence"""
        # Simple confidence calculation
        word_count = len(text.split())
        unique_words = len(set(text.split()))
        return min(1.0, (word_count / 10) * (unique_words / word_count))
    
    def _determine_scope(self, text: str) -> str:
        """Determine if pattern is workspace or system-level"""
        workspace_keywords = ['project', 'workspace', 'local']
        system_keywords = ['global', 'universal', 'cross-workspace']
        
        text_lower = text.lower()
        if any(kw in text_lower for kw in workspace_keywords):
            return 'workspace'
        elif any(kw in text_lower for kw in system_keywords):
            return 'system'
        return 'undefined'
    
    def _filter_significant_patterns(self, patterns: List[Dict]) -> List[Dict]:
        """Filter out insignificant or low-confidence patterns"""
        return [
            pattern for pattern in patterns 
            if pattern['confidence'] >= self.confidence_threshold
        ]
    
    def _migrate_to_system(self, pattern: Dict) -> bool:
        """Migrate pattern to system-level memory"""
        system_memory_path = self.memories_dir / 'system' / 'system_patterns.md'
        
        try:
            with open(system_memory_path, 'a') as f:
                f.write(f"\n### Migrated Insight from {pattern['source']}\n")
                f.write(f"**Confidence**: {pattern['confidence']:.2f}\n")
                f.write(f"{pattern['content']}\n")
            return True
        except Exception as e:
            print(f"Error migrating to system memory: {e}")
            return False
    
    def _migrate_to_workspace(self, pattern: Dict) -> bool:
        """Migrate pattern to workspace-level memory"""
        workspace_memory_path = self.memories_dir / 'workspace' / 'workspace_patterns.md'
        
        try:
            with open(workspace_memory_path, 'a') as f:
                f.write(f"\n### Migrated Workspace Insight from {pattern['source']}\n")
                f.write(f"**Confidence**: {pattern['confidence']:.2f}\n")
                f.write(f"{pattern['content']}\n")
            return True
        except Exception as e:
            print(f"Error migrating to workspace memory: {e}")
            return False

def initialize_memory_manager() -> MemoryManager:
    """Helper function to initialize memory manager"""
    return MemoryManager(r'c:\Users\david\code\_rules\windflow\memories')
