# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 23:27:33 2018

@author: Ultra_Hopeful
"""

import random
from colorama import init, Fore, Back, Style 
init(convert=True)
def choose():
    words=['rainbow','computer','science','programming','mathematics','player','condition','reverse','water','board','games','engineering','institute','level','muzzle','zigzag','buzzer','health','wealth','sport','cricket','football','baseball']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled=" ".join(random.sample(word,len(word)))
    return jumbled

def thank_2(p1n,p2n,p1,p2):
    if p1==p2:
        print(Fore.RED+Back.WHITE+"Game draw")
    elif p1>p2:
        print(Fore.BLUE+Back.WHITE+p1n+" won the game.")
    else:
        print(Fore.BLUE+Back.WHITE+p2n+" won the game.")
    print(Style.RESET_ALL)
    print(p1n,'your score is',p1)
    print(p2n,'your score is',p2)
    print('Thanks for playing.')
    
def thank_1(p1n_1,p1_1):
    print(Fore.BLUE+Back.WHITE+p1n_1+" your score is ",p1_1)
    print(Style.RESET_ALL)

def play():
    n=int(input("Enter no of player 1/2 : "))
    if(n==1):
        p1name=input("Player1, please enter your name : ")
        pp1_1=0
        while(1):
        #player1
            picked_word=choose()
            qn=jumble(picked_word)
            print("\n jumbled word is "+Fore.BLUE+Back.WHITE+qn)
            print(Style.RESET_ALL)
            print("--------------",p1name,"your turn------------")
            ans=input('What is on my mind?')
            if ans==picked_word:
                pp1_1=pp1_1+1
                print(Fore.BLUE+Back.WHITE+p1name,"Your score is",pp1_1)
                print(Style.RESET_ALL)
            else:
                print("Better luck next time.The word is "+Fore.BLUE+Back.WHITE+picked_word)
                print(Style.RESET_ALL)
            c=int(input('Press 1 to continue and 0 to quit : '))
            if c==0:
                thank_1(p1name,pp1_1)
                break
    if(n==2):
        p1name=input("Player1, please enter your name : ")
        p2name=input("Player2, please enter your name : ")
        pp1=0
        pp2=0
        while(1):
            #player1
            picked_word=choose()
            qn=jumble(picked_word)
            print("\n jumbled word is "+Fore.BLUE+Back.WHITE+qn)
            print(Style.RESET_ALL)
            print("--------------",p1name,"your turn------------")
            ans=input('What is on my mind?')
            if ans==picked_word:
                pp1=pp1+1
                print(Fore.BLUE+Back.WHITE+p1name,"Your score is",pp1)
                print(Style.RESET_ALL)
            else:
                print("Better luck next time.The word is "+Fore.BLUE+Back.WHITE+picked_word)
                print(Style.RESET_ALL)
                
            #player2
            picked_word=choose()
            qn=jumble(picked_word)
            print("\n jumbled word is "+Fore.BLUE+Back.WHITE+qn)
            print(Style.RESET_ALL)
            print("---------------",p2name,"your turn---------------")
            ans=input('What is on my mind?')
            if ans==picked_word:
                pp2=pp2+1
                print(Fore.BLUE+Back.WHITE+p2name,"Your score is",pp2)
                print(Style.RESET_ALL)
            else:
                print("Better luck next time.The word is "+Fore.BLUE+Back.WHITE+picked_word)
                print(Style.RESET_ALL)
            c=int(input('Press 1 to continue and 0 to quit : '))
            if c==0:
                thank_2(p1name,p2name,pp1,pp2)
                break
play()
