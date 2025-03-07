# Nigger Killing Machine Alpha Version
import random

y = 1
random_kill = random.randint(1,10000)
random_wrong_race = random.choice(["arabs", "niggers"])
while True:
    race = str(input("Which race do you prefer to kill, niggers or arabs? You can type 'exit' to exit the program."))
    if race.lower() not in ["niggers", "arabs", "exit"]:
        print("Sorry, I didn't get it.")
        continue
    if race.lower() == "niggers":
        nigga = int(input("How many niggers should I kill?"))
        while nigga <= 0:
            nigga = int(input("Let me rephrase myself. HOW MANY NIGGER 'WILL' I KILL?"))
        else:
            for t in range(nigga):
                print(y, "Nigger has been killed")
                y = y + 1
            break
    elif race.lower() == "arabs":
        arab = int(input("How many arab should I kill?"))
        while arab <= 0:
            arab = int(input("Let me rephrase myself. HOW MANY ARAB 'WILL' I KILL?"))
        else:
            for t in range(arab):
                print(y, "Arab has been killed")
                y = y + 1
            break
    elif race.lower() == "exit":
        print (random_kill, random_wrong_race, "Has been killed")
        break









