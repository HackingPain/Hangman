# Set up the game variables
import random

wordList = ['apple', 'banana', 'orange', 'grape']
word = random.choice(wordList)
guessWord = ['_' for i in range(len(word))]
remainingGuesses = 6

# Check if the player's guess is correct
def checkGuess(guess):
  correct = False
  for i in range(len(word)):
    if word[i] == guess:
      guessWord[i] = guess
      correct = True
  if not correct:
    global remainingGuesses
    remainingGuesses -= 1
  return correct

# Check if the player has won the game
def checkWin():
  for i in range(len(guessWord)):
    if guessWord[i] == '_':
      return False
  return True

# Main game loop
while remainingGuesses > 0:
  # Get the player's guess
  guess = input('Guess a letter:')
  if checkGuess(guess):
    print('Correct!')
  else:
    print('Incorrect!')
  if checkWin():
    print('You win!')
    print(word)
    break

if remainingGuesses == 0:
  print('You lose!')
