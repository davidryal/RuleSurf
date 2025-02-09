from typing import Dict, List
import json
import pandas as pd
from pathlib import Path
import os
import numpy as np

class WorkspaceTestFramework:
    def __init__(self, config_path: str):
        self.config = self._load_config(config_path)
        self.results_path = os.path.join(os.path.dirname(config_path), 'experiment_results.csv')
        self.results = self._load_or_create_results()
        
    def _load_config(self, config_path: str) -> Dict:
        """Load experiment configuration"""
        with open(config_path, 'r') as f:
            return json.load(f)
        
    def _load_or_create_results(self) -> pd.DataFrame:
        """Load existing results or create new DataFrame"""
        if os.path.exists(self.results_path):
            return pd.read_csv(self.results_path)
        else:
            return pd.DataFrame(columns=[
                'experiment_id', 'group', 'fac_efficiency', 
                'completion_time', 'error_rate', 'timestamp'
            ])
        
    def run_experiment(self, experiment_id: str) -> Dict:
        """Execute a workspace experiment"""
        experiment = self._get_experiment(experiment_id)
        if not experiment:
            return {"error": "Experiment not found"}
            
        metrics = self._collect_metrics(experiment)
        self._store_results(experiment_id, metrics)
        return self._analyze_results(experiment_id)
        
    def _get_experiment(self, experiment_id: str) -> Dict:
        """Retrieve specific experiment configuration"""
        for exp in self.config.get('active_experiments', []):
            if exp['id'] == experiment_id:
                return exp
        return None
        
    def _collect_metrics(self, experiment: Dict) -> Dict:
        """Simulate metrics collection for the experiment"""
        return {
            "fac_efficiency": np.random.uniform(0.7, 1.0),
            "completion_time": np.random.uniform(10, 60),
            "error_rate": np.random.uniform(0.01, 0.1),
            "group": experiment.get('group', 'experimental')
        }
        
    def _store_results(self, experiment_id: str, metrics: Dict):
        """Store experiment results"""
        metrics['experiment_id'] = experiment_id
        metrics['timestamp'] = pd.Timestamp.now()
        
        # Append new results
        new_result = pd.DataFrame([metrics])
        self.results = pd.concat([self.results, new_result], ignore_index=True)
        
        # Save to CSV
        self.results.to_csv(self.results_path, index=False)
        
    def _analyze_results(self, experiment_id: str) -> Dict:
        """Analyze experiment results and generate insights"""
        exp_data = self.results[self.results["experiment_id"] == experiment_id]
        control_data = self.results[self.results["group"] == "control"]
        
        analysis = {
            "fac_reduction": self._calculate_improvement(exp_data, control_data, "fac_efficiency"),
            "speed_improvement": self._calculate_improvement(exp_data, control_data, "completion_time"),
            "error_rate_change": self._calculate_improvement(exp_data, control_data, "error_rate"),
            "recommendations": self._generate_recommendations(exp_data)
        }
        return analysis
        
    def _calculate_improvement(self, exp_data: pd.DataFrame, control_data: pd.DataFrame, metric: str) -> float:
        """Calculate percentage improvement"""
        exp_mean = exp_data[metric].mean()
        control_mean = control_data[metric].mean()
        
        if control_mean == 0:
            return 0
        
        return ((exp_mean - control_mean) / control_mean) * 100
        
    def _generate_recommendations(self, exp_data: pd.DataFrame) -> List[str]:
        """Generate recommendations based on experiment results"""
        recommendations = []
        
        if exp_data['fac_efficiency'].mean() > 0.9:
            recommendations.append("Experiment shows high FAC efficiency. Consider expanding.")
        
        if exp_data['error_rate'].mean() < 0.05:
            recommendations.append("Low error rate indicates robust implementation.")
        
        return recommendations

def initialize_test_framework() -> WorkspaceTestFramework:
    """Helper function to initialize test framework"""
    return WorkspaceTestFramework(
        r'c:\Users\david\code\_rules\windflow\memories\workspace\experiment_config.json'
    )
