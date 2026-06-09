
#store score data is .json
#When program runs: read score json, parse data, and update object(player data)
# Date to create from "class Scores": Total Wins, Total Losses, Total Ties, Top Winning Move, Top Losing Move
class Scores:
    def __init__(self, name):
        self.name = name
        self.move_stats = {
            "rock": {"win": 0, "loss": 0},
            "paper": {"win": 0, "loss": 0},
            "scissors": {"win": 0, "loss": 0}
        }


# Names(.lower) Wins, losses, Ties, Total Rounds Played - GLaDOS, Player Names - Most common hand wins, most common hand loss "R", "P", "S".lower()
# Calculate for AI: Most winning hands, Most losing hands, How many times in a row before losing (Collect game data, in order)