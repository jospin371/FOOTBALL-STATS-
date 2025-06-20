# stats_generator.py
import json
from team_manager import load_teams

STATS_PATH = "data/stats.json"

def generate_stats():
    teams = load_teams()
    best_attack = max(teams, key=lambda t: t["goals_scored"])
    best_defense = min(teams, key=lambda t: t["goals_conceded"])

    stats = {
        "best_attack": best_attack["name"],
        "best_defense": best_defense["name"],
        "teams": [{
            "name": t["name"],
            "goals_scored": t["goals_scored"],
            "goals_conceded": t["goals_conceded"],
            "avg_scored": round(t["goals_scored"] / 6, 2),
            "avg_conceded": round(t["goals_conceded"] / 6, 2),
        } for t in teams]
    }

    with open(STATS_PATH, "w") as f:
        json.dump(stats, f, indent=2)

    return stats
