import random
import time
import os
import pygame
import numpy as np

pygame.mixer.init(frequency=44100, size=-16, channels=1)

def tono(frecuency, duration_ms=500, volume=0.5):
    sample_rate = 44100
    n_samples = int(sample_rate * duration_ms / 1000)
    buffer = np.sin(2 * np.pi * np.arange(n_samples) * frecuency / sample_rate).astype(np.float32)
    sound = pygame.sndarray.make_sound((buffer * 32767 * volume).astype(np.int16))
    sound.play()
    pygame.time.delay(duration_ms)

def clean_console():
        os.system('cls' if os.name == 'nt' else 'clear')

#Octaves

def piano():
    print("--------------------- PIANO --------------------\n")
    print("            |C| |D| |E| |F| |G| |A| |B|           ")
    time.sleep(0.5)
    while(True):
        print("----------------------KEYS----------------------\n")
        choice=input("C D E F G A B \n")
        #DO
        if choice == "c" or choice == "C":
            tono(261)
        #RE
        elif choice == "d" or choice == "D":
            tono(294)
        #MI
        elif choice == "e" or choice == "E":
            tono(329)
        #FA
        elif choice == "f" or choice == "F":
            tono(349)
        #SOL
        elif choice == "g" or choice == "G":
            tono(392)
        #LA
        elif choice == "a" or choice == "A":
            tono(440)
        #SI
        elif choice == "b" or choice == "B":
            tono(493)
        else:
            print("-----WRONG KEY------\n")
        clean_console()

def game():
    while(True):
       piano()
game()