#importujemy biblioteki do kolorów i losowania
import random
import os
from termcolor import colored
import time

print("Zalecane jest aby nie podawać odstępu czasowego mniejszego niż 20")
print("______________________")

wys = int(input("Wpisz wysokość jednego poziomu choinki: "))
poz = int(input("Wpisz ilość poziomów choinki: "))
odstęp = int(input("Wpisz odstęp czasowy między animowaniem choinki: (w milisekundach) "))

os.system('cls' if os.name == 'nt' else 'clear')

#wymierzamy maksymalną szerokość
max_szer = 2 * wys * poz - 1
kolory = ['red', 'yellow', 'blue', 'magenta', 'cyan']

#funkcja do rysowania choinki

while True:
    for j in range(poz):
        for i in range(wys - 1 + j):
            bombka = list(bombka)
            bombka = '@' * (2 * i + 1)
            for b in range(len(bombka)):
                if random.randint(0, 3) == 0:  # Używamy funkcji random aby wylosować kolorowy kawałek choinki
                    bombka[b] = colored(bombka[b], random.choice(kolory))
                else:
                    bombka[b] = colored(bombka[b], 'green')
            bombka = ''.join(bombka)
            print(' ' * ((max_szer - (2 * i + 1)) // 2) + bombka)
    #Dodajemy pień
    if poz > 3:
      for i in range(3):
          print(colored(' ' * ((max_szer - 3) // 2) + '#' * 3, 'yellow'))
      time.sleep(odstęp/100)  #Tu mamy odstęp czasowy
      os.system('cls' if os.name == 'nt' else 'clear')  #Tutaj czyścimy ekran konsoli 
    else:
      for i in range(2):
        print(colored(' ' * ((max_szer - 3) // 2) + '#' * 3, 'yellow'))
        
        
      time.sleep(odstęp/100)  #Tu mamy odstęp czasowy
      
      os.system('cls' if os.name == 'nt' else 'clear')  #Tutaj czyścimy ekran konsoli 
