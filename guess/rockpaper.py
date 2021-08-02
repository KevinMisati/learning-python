import random

def play():
    u = input("What is your choice? r for rock,s for scissors and p for papers:")
    c  = random.choice(["r","p","s"])
    if (u == c):
        return "It is a tie"
    if (u=="r" and c== "s" or u=="s" and c =="p" or u=="p" and c=="r" ):
        return "You won"
    return "You lost"
print(play())