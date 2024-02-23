import json
import os

def process_menu(items):
    for key in items.keys():
        print("{}:{}".format(key,items[key]))
    print("==============")
    while True:
        choice=(input("enter your choice: "))
        print("==============")
        if choice in items.keys():return choice
        else:
            print("wrong choice , try again !...")


def writeJson(items, filepath):
    with open(filepath, "w") as file:
        json.dump(items, file)

def readJson(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            return json.load(file)
    else:
        return []
    
def exam(questions):
    score = 0
    print(f"This exam contains {len(questions)} questions.")
    for question in questions:
        print(question["question"])
        print("\n".join(question["options"]))
        answer = input("Your answer: ")
        print(f"You answered: {answer}")  
        if answer == question["correct_answer"]:
            score += 1
    print(f"You got {score}/{len(questions)} correct.")