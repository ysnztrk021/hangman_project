import random
import os
import time

def get_word():
    with open('mots.txt', 'r') as file:
        rando = file.read()
        rand = list(map(str, rando.split()))
        word = random.choice(rand)
        return word

word = get_word()

def dash():
    dashs=[]
    for i in range(len(word)):
        dashs.append('_')
    return dashs

dash = dash()

def play():
    chance = 6
    print("\nBIENVENUE AU JEU 'BONHOMME PENDU'\n\n")
    guess = list(dash)
    print("Voici le nombre de lettre à deviner")

    while chance > 0:
        print(''.join(guess),'\n')
        guessed = input("Devinez la lettre/ le mot ! \n")
            
        if ''.join(guess)==word:
            print("Félicitation, vous avez trouvé le mot !")
            break
            
        if guessed.upper() in word:
            for i in range(len(word)):
                if list(word)[i]==guessed.upper():
                    guess[i]+=guessed
            print(''.join(guess))
            time.sleep(1)
            os.system('cls')
            
        elif guessed not in word :
            print('Vous avez entrez la mauvaise lettre/mot')
            chance-=1
            time.sleep(1)
            os.system('cls')
                
    if chance ==0:
        print("Vous avez perdu !")
        
play()
       