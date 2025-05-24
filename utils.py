# Help Fuction
from escape_game import Player
def print_map(current: int, total_number: int):
    print("\n")
    print("Escape Map")

    line = ''
    for i in range(total_number):
        if i == current:
            print(" <-- You")
        else:
            print("[Room {}]".format(i+1))

def print_progress(current: int, total_number: int):
    bar = "[" + "#" * current + "." * (total_number - current) + f"] {current}/{total_number} solved"
    print(bar)

def save_result(player):
    with open("escape_result", "w") as f:
        f.write("Escape Game Result" + "\n")
        f.write("Solved Rood" + ", ".join(player.progress) + "\n")
        f.write("Score: {}".format(player.score) + "\n")
        f.write("Good Job" + "\n")