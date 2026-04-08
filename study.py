import random
import time

def load_questions(filename):
    temp_list = []
    
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            if "|" in line:
                q, a = line.split("|")
                temp_list.append({"q": q, "a": a})
                
    return temp_list # Send the finished list back to the main program

qSFI = load_questions("SFI.txt")
qID = load_questions("ID.txt") 

mAPSL = {
    "ACC" : "acc",
    "ID"  : qID,
    "VOC" : "voc"
        }
mAPW = {
    "SFI" : qSFI,
    "T"   : "t"
        }
m1 = {
    "APW"  : mAPW,
    "APSL" : mAPSL
        }

state = m1



while(state != "quit"):
    if isinstance(state, dict):
        for opt in state:
            print(opt)
    
    inp = input(">")

    if isinstance(state, dict):
        if inp in state:
            state = state[inp]
    
    if isinstance(state, list):
        random.shuffle(state)
        start_time = time.time()
        score = 0
        for card in state:
            print("\n" + "="*20)
            user_answer = input(card["q"] + "\n> ")
            
            #clear screen
            print("\033[H\033[J", end="")

            # .strip() removes accidental spaces, .lower() ignores Capitalization
            if user_answer.strip().lower() == card["a"].lower():
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong. The answer was: {card['a']}")
                   
        end_time = time.time()
        print(f"\nFinished! Final Score: {score}/{len(state)} Time: {end_time-start_time}")
