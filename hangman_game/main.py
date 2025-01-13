import random
import os
from .hangman_art import hangmanpics

class Game:
    def __init__(self):
        self.hangmanpics = hangmanpics
        self.state = 0
        self.maxState = len(hangmanpics)
        self.currentTurn = 0

        wordlist = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
        
        chosen_idx = random.randint(0,len(wordlist))
        wordstr = wordlist[chosen_idx].upper()
        self.word = []
        self.discoveredLetters = []
        self.testedLetters = []
        for letter in wordstr:
            self.word.append(letter)
        self.startGame()

    def __str__(self):
        return f"Hangman game object"
    
    def startGame(self):
        os.system('cls')
        won = False
        while self.state < self.maxState - 1 and won == False:
            self.printGameState()
            letter = input("Entrez une lettre...\n\n").upper()
            if len(letter) != 1:
                input("Vous n'avez pas entré une lettre ! Appuyez sur entrer pour ré-essayer\n")
            else:
                if letter in self.word:
                    print(len(self.discoveredLetters))
                    print(len(self.word))
                    input("La lettre est dans le mot, bravo !")
                    for _ in range(self.countLetterInWord(letter, self.word)):
                        self.discoveredLetters.append(letter)
                    
                    if(len(self.discoveredLetters) == len(self.word)):
                        won = True
                else:
                    input("La lettre n'est pas dans le mot ! Appuyez sur entrer pour ré-essayer\n")
                    self.testedLetters.append(letter)
                    self.state += 1
            
            os.system('cls')
        
        os.system('cls')
        if won:
            print("Word:\n")
            self.printWord()
            print("\n")
            input("Vous avez gagné ! Appuyez sur entrer pour relancer une partie !")
        else:
            print("Vous avez perdu !\n")
            self.printHangman(len(self.hangmanpics)-1)
            input("\n\nAppuyez sur entrer pour relancer le jeu !")

        newgame = Game()

    
    def printGameState(self):
        print(self.word)
        print("Word:\n")
        self.printWord()
        print("\n\nCurrent State:")
        self.printHangman(self.state)
        print("\n\nTested letters:")
        self.printTestedLetters()
        print("\n")

    def countLetterInWord(self, letter, word):
        counter = 0
        for i in range(len(word)):
            if letter == word[i]:
                counter += 1

        return counter

    def printWord(self):
        for letter in self.word:
            if letter in self.discoveredLetters:
                print(f"{letter}", end=" ")
            else:
                print("_", end=" ")

    def printHangman(self, n: int):
        print(self.hangmanpics[n])

    def printTestedLetters(self):
        if len(self.testedLetters) >= 1:
            for letter in self.testedLetters:
                print(letter, end=" ")
        else:
            print("No wrong letters yet !")
        