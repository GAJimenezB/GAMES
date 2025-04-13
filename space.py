import random
import time
import os
import requests

#Width
W=[]
#Large
L=[]
#MAP

def sent_move(direccion,x,y,shoot):
    url = "http://localhost:5000/moves"
    data = {
        "direccion": direccion,
        "x": x,
        "y": y,
        "shoot": shoot
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("MOVE SENT CORRECTLY.")
    else:
        print("ERROR SENDING MESSAGE.")
def clean_console():
        os.system('cls' if os.name == 'nt' else 'clear')
    
def map_init():
    for i in range(0,7):
        W.append("   ")
    for i in range(0,7):
        L.append(W[:])
    for i in range(0,7):
        L[0][i]=" O "
    L[3][3]='_^_'
def map_now():
    for i in range(0,7):
        print(L[i])
    print("\n")

def move_player():
    print("------------ WELCOME - SPACE INVADERS ----------\n")
    map_init()
    map_now()
    time.sleep(0.5)
    score=0
    i=3
    j=3
    L[i][j]=''
    while(True):
        print("----------------------KEYS----------------------\n")
        choice=input("a(LEFT) w(UP) s(DOWN) d(RIGHT) || e(SHOT) q(SHOT)\n")
        k=1
        t=random.randint(1,6)
        f=random.randint(1,6)
        l=random.randint(0,6)
        r=random.randint(0,6)
        L[i][j]='   '
        #THUNDERS
        while(k<=t):
            L[k][l]= " | "
            k+=1
        k=1
        while(k<=f):
            L[k][r]= " | "
            k+=1
        #UP
        shoot = False
        if choice == "a" and j>0:
            j-=1
            direccion = "a"
        #LEFT
        elif(choice == "w" and i>0):
            i-=1
            direccion = "w"
        #DOWN
        elif(choice == "s" and i<6):
            i+=1
            direccion = "s"
        #RIGHT
        elif(choice == "d"and j<6):
            direccion = "d"
            j+=1
        elif(choice == "e" or choice == "q"):
            L[0][j] = " X "
            score+=1
            direccion = "e"
            shoot = True
        #ERROR
        else:
            print("-----WRONG KEY,ONLY a/w/s/d/q/e------\n")
        sent_move(direccion, j, i, shoot) 
        L[i][j]="_^_"
        clean_console()
        map_now()
        time.sleep(0.5)
        k=1
        if(L[i+1][j]==" | " or L[i-1][j]==" | "):
            while(k<=6):
                L[k][l]= "   "
                L[k][r]= "   "
                k+=1
            L[i][j]="   "
            print("                      SCORE = ",score)
            print("----------------------LOSER----------------------\n")
            return(False)
        if(all(celda == " X " for celda in L[0] )):
            while(k<=6):
                L[k][l]= "   "
                L[k][r]= "   "
                k+=1
            L[i][j]="   "
            print("                      SCORE = ",score)
            print("----------------------WINNER---------------------\n")
            return(False)
        while(k<=6):
            L[k][l]= "   "
            L[k][r]= "   "
            k+=1
        
def game():
    while(True):
        move_player()
game()