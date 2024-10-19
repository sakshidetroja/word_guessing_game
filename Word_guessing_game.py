import random #choose for random word : importing library of random
import re
#class contain information abot game:
class wordGame:
    def __init__(self,wordlist):
        self.wordlist = wordlist #pick a random word from list of words
        self.guessword_attempt = 6 #number of attempts to guess a word 
        self.current_word = '' #showing which is current word
        self.chosen_word = ''#showing which word is choosen from list
        self.gussed_letter = []
    def choose_word(self):

        with open(self.wordlist) as file:  # use open to open the file
            words = file.read().split() # read is use for read the words from wordlist one by one
        word_count = len(words) # length of the woords 
        self.chosen_word  = words[random.randrange(0,word_count)] # randrange is used to provide the range of any word 
        self.word_status = ['-' for i in range(len(self.chosen_word)) ]#staus is show the total length of word or initilize of word in for of list
    # Randomly choose a word from the wordlist
    def fill_word_status(self):

        fw = random.randrange(0,5) #choose a few letter from word
        filled_positions = set() #keep track of the filled positions
        for i in range(fw):
            pos = random.randrange(0,len(self.chosen_word)) # position
            while pos in filled_positions:
                pos = random.randrange(0,len(self.chosen_word))
            #print(self.chosen_word)
            self.word_status[pos] = self.chosen_word[pos]#put letters for position in word
            filled_positions.add(pos)
    def guess_letter(self):

        letter = input("Guess the letter : ")
        if letter in self.gussed_letter:
            print("you have already guessed that letter . your guessed letter is : {} ".format(''.join(self.gussed_letter)))
            return 
        
        self.gussed_letter.append(letter)
        occurrence = []
        matches = re.finditer(letter,self.chosen_word)# Occurrence is used in re for find out all possible match  
        #finditers if find where the matches is happening in word
        for m in matches :
            occurrence.append(m.start())

        if len(occurrence)==0:
            self.guessword_attempt -= 1
            print("you're guessing wrong letter , Attemps remaining is {}".format(self.guessword_attempt)) # it shows how much attmpets is left 
        else:
            for pos in occurrence:
                self.word_status[pos] = self.chosen_word[pos]
            print("one letter found")

    def get_word_status(self):
        print("current status {}\n".format(''.join(self.word_status)))
