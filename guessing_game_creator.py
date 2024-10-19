import Word_guessing_game

game = Word_guessing_game.wordGame('wordlist.txt')
game.choose_word()
game.fill_word_status()
while True:
   game.get_word_status()
   game.guess_letter()

   if(game.guessword_attempt == 0):
      print("out of attempts. The word was {}. Game over!".format(game.chosen_word))
      break
   elif game.chosen_word == game.fill_word_status():
      print("Congratulations! You guessed the word correctly. The word was {}.".format(game.chosen_word))
      break