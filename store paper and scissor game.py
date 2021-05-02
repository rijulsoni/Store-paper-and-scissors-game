import random
def winner(computer, player):
    if computer==player:
        return None
    elif computer=='t':
        if player=='p':
            return True
    elif player=='s':
        return False
    elif computer=='p':
        if player=='s':
            return True
    elif player=='t':
        return False
    elif computer=='s':
        if player=='t':
            return True
    elif player=='p':
        return False
print("Computer Turn: scissor(s) Paper(p) or Stone(t)?")
randnum=random.randint(1,3)
if randnum==1:
    computer='t'
elif randnum==2:
    computer='p'
elif randnum==3:
    computer='s'
player=input("Your Turn: scissor(s) Paper(p) or Stone(t)?")
a=winner(computer, player)

print(f"Computer chose {computer}")
print(f"You chose {player}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
