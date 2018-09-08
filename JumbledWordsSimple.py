# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 22:12:26 2018

@author: Ultra_Hopeful
"""

import random

def choose():
    words=['rainbow','computer','science','programming','mathematics','player','condition','reverse','water','board','games','engineering','institute','level','muzzle','zigzag','buzzer','health','wealth','sport','cricket','football','baseball']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled=" ".join(random.sample(word,len(word)))
    return jumbled

def thank_2(p1n,p2n,p1,p2):
    if p1==p2:
        print("Game draw")
    elif p1>p2:
        print(p1n+" won the game.")
    else:
        print(p2n+" won the game.")
    print(p1n,'your score is',p1)
    print(p2n,'your score is',p2)
    print('Thanks for playing.')
    
def thank_1(p1n_1,p1_1):
    print(p1n_1+" your score is ",p1_1)

def play():
    n=int(input("Enter no of player 1/2 : "))
    if(n==1):
        p1name=input("Player1, please enter your name : ")
        pp1_1=0
        while(1):
        #player1
            picked_word=choose()
            qn=jumble(picked_word)
            print("\n jumbled word is '"+qn+"'")
            print("--------------",p1name,"your turn------------")
            ans=input('What is on my mind?')
            if ans==picked_word:
                pp1_1=pp1_1+1
                print(p1name,"Your score is",pp1_1)
            else:
                print("Better luck next time.The word is '"+picked_word+"'")
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
            print("\n jumbled word is '"+qn+"'")
            print("--------------",p1name,"your turn------------")
            ans=input('What is on my mind?')
            if ans==picked_word:
                pp1=pp1+1
                print(p1name,"Your score is",pp1)
            else:
                print("Better luck next time.The word is '"+picked_word+"'")
                
            #player2
            picked_word=choose()
            qn=jumble(picked_word)
            print("\n jumbled word is '"+qn+"'")
            print("---------------",p2name,"your turn---------------")
            ans=input('What is on my mind?')
            if ans==picked_word:
                pp2=pp2+1
                print(p2name,"Your score is",pp2)
            else:
                print("Better luck next time.The word is '"+picked_word+"'")
            c=int(input('Press 1 to continue and 0 to quit : '))
            if c==0:
                thank_2(p1name,p2name,pp1,pp2)
                break
play()
