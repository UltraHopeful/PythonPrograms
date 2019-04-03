import random
from colorama import init, Fore, Back, Style 
init(convert=True)
p1w=0
p2w=0
Player1=input("Player1 enter your name: ")
Player2=input("Player2 enter your name: ")
def rps(b1,b2):
    global p1w,p2w
    p1=int(n1[b1])%3
    p2=int(n2[b2])%3
    if(p_1[p1]==p_2[p2]):
        print(Fore.RED+"Draw \n"+Fore.BLUE+Player1+" chooses :"+p_1[p1]+Fore.MAGENTA+"\t"+Player2+" chooses:",p_2[p2])
    elif(p_1[p1]=="Rock" and p_2[p2]=="Scissor"):
        p1w=p1w+1
        print(Fore.RED+Player1+" won \n"+Fore.BLUE+Player1+" chooses :"+p_1[p1]+Fore.MAGENTA+"\t"+Player2+" chooses:",p_2[p2])
    elif(p_1[p1]=="Rock" and p_2[p2]=="Paper"):
        p2w=p2w+1
        print(Fore.RED+Player2+" won \n"+Fore.BLUE+Player1+" chooses :"+p_1[p1]+Fore.MAGENTA+"\t"+Player2+" chooses:",p_2[p2])
    elif(p_1[p1]=="Paper" and p_2[p2]=="Rock"):
        p1w=p1w+1
        print(Fore.RED+Player1+" won\n"+Fore.BLUE+Player1+" chooses :"+p_1[p1]+Fore.MAGENTA+"\t"+Player2+" chooses:",p_2[p2])
    elif(p_1[p1]=="Paper" and p_2[p2]=="Scissor"):
        p2w=p2w+1
        print(Fore.RED+Player2+" won \n"+Fore.BLUE+Player1+" chooses :"+p_1[p1]+Fore.MAGENTA+"\t"+Player2+" chooses:",p_2[p2])
    elif(p_1[p1]=="Scissor" and p_2[p2]=="Rock"):
        p2w=p2w+1
        print(Fore.RED+Player2+" won \n"+Fore.BLUE+Player1+" chooses :"+p_1[p1]+Fore.MAGENTA+"\t"+Player2+" chooses:",p_2[p2])
    elif(p_1[p1]=="Scissor" and p_2[p2]=="Paper"):
        p1w=p1w+1
        print(Fore.RED+Player1+" won \n"+Fore.BLUE+Player1+" chooses :"+p_1[p1]+Fore.MAGENTA+"\t"+Player2+" chooses:",p_2[p2])
    print(Style.RESET_ALL)
p_1={0:'Rock',1:'Paper',2:'Scissor'}
p_2={0:'Paper',1:'Scissor',2:'Rock'}
n1=input("Player one, enter ur choices : ")
n2=input("Player two, enter ur choices : ")
while (1):
    random.shuffle(p_1)
    random.shuffle(p_2)
    print("Player one, enter ur seceret bit between 0 to",len(n1)," : ")
    b1=int(input())
    print("Player two, enter ur seceret bit between 0 to",len(n2),": ")
    b2=int(input())
    rps(b1,b2)
    ch=input("Continue (y/n)?")
    if(ch=='n'):
        print(Fore.BLUE+Player1+" won",p1w,"times"+Fore.MAGENTA+"\n"+Player2+" won",p2w,"times")
        break
print(Style.RESET_ALL)
