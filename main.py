import random

def get_stage():
    return [
    """
       O
      """,

    """
    
       O
       |
       """
    ,"""
       O
      /|
      """,

"""
       O
      /|\\
       
      """
    ,

    """
       O
      /|\\
      / 
      """
    ,
"""
       O
      ____
      /|\\
      / \\
    """,

]

words = ["CAT", "DOG", "APPLE", "BANANA", "DONKEY"]

def play_game():
    word = random.choice(words)
    # print(word)
    gusses = ''
    turns = 6
    stage = get_stage()
    while turns > 0:
        faild = 0
        for char in word:
            if char in gusses:
                print(char,end='')
            else:
                print('_',end='')
                faild += 1
        print()
        if faild == 0:
            print(word,"exllent")
            break

        gusse = input("enter litter: ").upper()
        if gusse in gusses:
            print("you enter this word before this")
            continue

        gusses += gusse

        if gusse not in word:
            turns -= 1

            print(f"false you have just {turns} turns")
            print(stage[ 5 - turns])

        if turns == 0:
            print(f"you are loss , the word is :{word}")
def main():
    while True:
        play_game()
        again = input("Would you like to play again? (y/n):").lower()
        if again != 'y':
            print("Thank you for playing")
            break

main()