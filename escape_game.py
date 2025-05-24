from puzzle import *
from utils import *
import time
class Room:
    def __init__(self, name, description, puzzle_func):
        self.name = name
        self.puzzle_func = puzzle_func
        self.description = description
        self.is_solved = False

class Player:
    def __init__(self):
        self.progress = []
        self.current_stage = 0
        self.score = 0

# Start game
def play_room(room, player):
    print(room.name)
    print(room.description)

    if room.puzzle_func():
        print("✅ Puzzle solved!")
        room.is_solved = True
        player.progress.append(room.name)
        player.current_stage += 1
        player.score += 10
    else:
        print("❌ Failed. Try again later.")
    time.sleep(1)


def main():
    player = Player()
    rooms = [
        Room("Room 1: The Math Gate", "Solve a math puzzle.", math),
        Room("Room 2: The Riddle Wall", "Answer the ancient riddle.", words),
        Room("Room 3: Memory Chamber", "Recall the color sequence.", memory),
        Room("Room 4: Command Console", "Enter the correct terminal command.", code)
    ]
    print("🎮 Welcome to the Escape Room!")
    print("Solve all puzzles to escape. Good luck!\n")

    for i, room in enumerate(rooms):
        print_map(i, len(rooms))
        play_room(room, player)
        print_progress(player.current_stage, len(rooms))
        if not room.is_solved:
            print(room.is_solved)
            print("\n💀 You’re stuck! Come back stronger.")
            break
    if all(r.is_solved for r in rooms):
        print("\n🎉 You escaped successfully!")
    save_result(player)
    print("Result saved to escape_results.txt")

if __name__ == "__main__":
    main()