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
    wrong=[]
    wrong_word=[]

    while chance > 0:
        print(''.join(guess),'\n')
        guessed = input("Devinez la lettre/ le mot ! \n")
        
        if guessed.upper() in wrong:
            print('Vous avez déjà introduit cette lettre')
            time.sleep(1)
            os.system('cls')

        else:
                
            if len(guessed) == 1:
            
                if guessed.upper() in word:
                    for i in range(len(word)):
                        if word[i]==guessed.upper():
                            guess[i]=guessed.upper()
                    print(''.join(guess))
                    time.sleep(1)
                    os.system('cls')
                    
                elif guessed.upper() not in word :
                    wrong.append(guessed.upper())
                    print('Vous avez entrez la mauvaise lettre')
                    chance-=1
                    time.sleep(1)
                    os.system('cls')
            else:
                
                if guessed.upper() == word:
                    print("Félicitation, vous avez trouvé le mot", guessed.upper())
                
                else:
                    wrong_word.append(guessed.upper())
                    print('Vous avez entrez le mauvais mot')
                    chance-=1
                    time.sleep(1)
                    os.system('cls')
            
        if len(wrong) > 0 and chance > 0:
            print('Voici les mauvaises lettres que vous avez déjà introduit \n','[',','.join(wrong),']','\n','Et il vous reste ',chance,' chance(s)','\n',sep='')
                
    if chance ==0:
        print("Vous avez perdu !")
        print("Le mot à trouver était ",word)
        
play()
       