import random

#Snake Water Gun or Rock Paper and Scissors

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "s":
            return True
        elif you == "g":
            return False
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True

print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
RandNo = random.randint(1, 3)

if RandNo == 1:
    comp = "s"
elif RandNo == 2:
    comp = "w"
elif RandNo == 3:
    comp = "g"

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, you)
print(f"Computer Choose '{comp}'")
print(f"You Choose '{you}' ")

if a is None:
    print("The Game is tie...")
elif a:
    print("You Win This Game")
else:
    print("You Lose This Game")