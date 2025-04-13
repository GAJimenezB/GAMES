import random
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def table(fila_1, fila_2, fila_3):
    print("------------------TIK TAK TOK-------------------")
    print("\n")
    print(fila_1)
    print(fila_2)
    print(fila_3)
    print("\n")
def game():
    fila_1 = [1, 2, 3]
    fila_2 = [4, 5, 6]
    fila_3 = [7, 8, 9]
    table(fila_1, fila_2, fila_3)
    while( True ):
        while(True):
            print("-------------------PLAYER---------------------\n")
            choice = int(input("CHOOSE A FREE PLACE \n"));
            if (choice == 1 and fila_1[0] not in ["X", "O"]):
                fila_1[0]="X"
                break
            elif (choice == 2 and fila_1[1] not in ["X", "O"]):
                fila_1[1]="X"
                break
            elif (choice == 3 and fila_1[2] not in ["X", "O"]):
                fila_1[2]="X"
                break
            elif(choice == 4 and fila_2[0] not in ["X", "O"]):
                fila_2[0]="X"
                break
            elif(choice == 5 and fila_2[1] not in ["X", "O"]):
                fila_2[1]="X"
                break
            elif(choice == 6 and fila_2[2] not in ["X", "O"]):
                fila_2[2]="X"
                break
            elif(choice == 7 and fila_3[0] not in ["X", "O"]):
                fila_3[0]="X"
                break
            elif(choice == 8 and fila_3[1] not in ["X", "O"]):
                fila_3[1]="X"
                break
            elif(choice == 9 and fila_3[2] not in ["X", "O"]):
                fila_3[2]="X"
                break
            else:
                print("ERROR, CHOOSE A FREE PLACE")
            print("\n")
        print(fila_1)
        print(fila_2)
        print(fila_3)
        print("\n-------------- IA ---------------------")
        while(True):
            choice = random.randint(0,8)
            if (choice == 0 and fila_1[0] not in ["X", "O"]):
                fila_1[0]="O"
                break
            elif (choice == 1 and fila_1[1] not in ["X", "O"]):
                fila_1[1]="O"
                break
            elif (choice == 2 and fila_1[2] not in ["X", "O"]):
                fila_1[2]="O"
                break
            elif(choice == 3 and fila_2[0] not in ["X", "O"]):
                fila_2[0]="O"
                break
            elif(choice == 4 and fila_2[1] not in ["X", "O"]):
                fila_2[1]="O"
                break
            elif(choice == 5 and fila_2[2] not in ["X", "O"]):
                fila_2[2]="O"
                break
            elif(choice == 6 and fila_3[0] not in ["X", "O"]):
                fila_3[0]="O"
                break
            elif(choice == 7 and fila_3[1] not in ["X", "O"]):
                fila_3[1]="O"
                break
            elif(choice == 8 and fila_3[2] not in ["X", "O"]):
                fila_3[2]="O"
                break
            else:
                choice = random.randint(0,8)
        print(fila_1)
        print(fila_2)
        print(fila_3)
        HSX = (fila_1[0] == "X")&(fila_1[1] == "X")&(fila_1[2] == "X")
        HIX = (fila_3[0] == "X")&(fila_3[1] == "X")&(fila_3[2] == "X")
        LIX = (fila_1[0] == "X")&(fila_2[0] == "X")&(fila_3[0] == "X")
        LDX = (fila_1[2] == "X")&(fila_2[2] == "X")&(fila_3[2] == "X")
        XDX = (fila_1[0] == "X")&(fila_2[1] == "X")&(fila_3[2] == "X")
        XIX = (fila_1[2] == "X")&(fila_2[1] == "X")&(fila_3[0] == "X")
        
        HSO = (fila_1[0] == "O")&(fila_1[1] == "O")&(fila_1[2] == "O")
        HIO = (fila_3[0] == "O")&(fila_3[1] == "O")&(fila_3[2] == "O")
        LIO = (fila_1[0] == "O")&(fila_2[0] == "O")&(fila_3[0] == "O")
        LDO = (fila_1[2] == "O")&(fila_2[2] == "O")&(fila_3[2] == "O")
        XDO = (fila_1[0] == "O")&(fila_2[1] == "O")&(fila_3[2] == "O")
        XIO = (fila_1[2] == "O")&(fila_2[1] == "O")&(fila_3[0] == "O")
        
        if ((HSX == True) or (HIX == True) or (LIX == True) or (LDX == True) or (XDX == True) or (XIX == True)):
            print("\n-------------------PLAYER WON----------------\n")
            break
        elif ((HSO == True) or (HIO == True) or (LIO == True) or (LDO == True) or (XDO == True) or (XIO == True)):
            print("\n------------------IA WON------------------\n")
            break
while(True):
    time.sleep(3)
    clear_console()
    game()