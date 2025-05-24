# Define Puzzle Games
import time

def math() -> bool:
    print("Need 3 digital code to unlock the door. ")
    print("Hint: It's the result of 98 + 1 * 25")
    answer = input("Enter the code: ").strip()

    if answer.isdigit():
        return int(answer) == 123
    return False

def memory() -> bool:
    sequence = ["red", "green", "blue"]
    print("Remeber this sequence: ")
    print('->'.join(sequence))
    time.sleep(3)
    print("\n" * 20)
    answer = input("Repeat the sequence (use commas): ").strip().lower().split(",")

    if len(answer) != 3:
        return False
    return answer == sequence

def words() -> bool:
    print("'I speak without a mouth and hear without ears. What am I?'")
    answer = input("What is your answer: ").strip().lower()
    return answer == "echo"

def code() -> bool:
    print("A terminal blinks. What Lunix command you need to enter to list files. ")
    answer = input("What is your answer: ").strip().lower()
    return answer == 'ls'