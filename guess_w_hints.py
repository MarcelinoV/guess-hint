# Guessing Game with Hints
# Modules used
import random 

word_bank = [{ # nested dictionary within a list
'queen': 'She runs the game',
'rook': "home sweet home",
'knight': 'Shining armor',
'king': "Doesn't do much like modern ones",
'bishop':'Religious zealot',
'pawn':'Another cog in the system'}]

bank_keys = [] # To be appended list
guess = "" # empty string
guess_count = 0 # # of guesses user has made
guess_limit = 3 # # of guesses user can make
out_of_guesses = False # initial condition, User hasn't guessed yet

for dict in word_bank: # access dict inside word_bank which is a list
    for key in word_bank[0].keys(): # dict is index 0 in list, method returns keys of dict
        bank_keys.append(key) # append keys to list
       
secret_word = random.choice(bank_keys) # uses function to randomly choose word
hint = word_bank[0][secret_word] # ensures correct hint is assigned to secret word


# and or & not are logical operators used to set conditions
# not is used to say that the condition has to be false
# for code to run, for example:

print ("Guess which chess piece this is!\n") # Welcome/Prompt Message

while guess != secret_word and not(out_of_guesses): # conditions that need to be met for game to end

# initial variable values are disregarded in logical statements
# while & if assume everything after IS TRUE
    print(hint) # prints hint
    
    if guess_count < guess_limit: # While user hasn't surpassed guess limit
        guess = input("Enter guess: ") # input value for guess variable
        guess_count += 1 # increment of guess count per guess
    else:
        out_of_guesses = True # becomes true if if clause above becomes untrue

if out_of_guesses: 
    print("Out of guesses, you LOSE!") # Losing message

else:
    print("Nice guess, you WIN!\n") # Winning message

print(secret_word)
