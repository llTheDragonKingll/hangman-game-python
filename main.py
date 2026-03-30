import random
words = [
    "book",     # commonly used object
    "car",      # everyday means of transport
    "dog",      # familiar animal
    "house",    # place where people live
    "school",   # place of learning
    "apple",    # simple fruit
    "pen",      # common writing tool
    "chair",    # everyday furniture
    "water",    # essential for life (uncountable)
    "table"     # household item
]
choosen_word=random.choice(words)
length=len(choosen_word)
guessing_word=""
blanks=""
lives=5
for i in range(1,length+1):
    blanks+="_"
print(blanks)
guessed_letters=[]
while guessing_word != choosen_word and lives>=1:
    guessing_word=""
    guess=input("Guess a letter: ").lower()
    for letter in choosen_word:
       if guess==letter:
           guessing_word+=guess
           guessed_letters.append(guess)
       elif letter in guessed_letters:
           guessing_word+=letter          
       else:
           guessing_word+="_"
    if guess not in choosen_word:
        lives=lives-1
    print(guessing_word) 
    print(f"lives remaining: ",lives)
    if lives==0:
        print(f"You lost!! The word was", choosen_word)  
        print('''
          ------
          |    |
          O    |
         /|\   |
         / \   |
               |
        =========
         ''')     
    if lives==4:
        print('''
          ------
          |    |
               |
               |
               |
               |
        =========
         ''')
    if lives==3:
        print('''
          ------
          |    |
          O    |
               |
               |
               |
        =========
         ''')
    if lives==2:
        print('''
          ------
          |    |
          O    |
          |    |
               |
               |
        =========
         ''')    
    if lives==1:
        print('''
          ------
          |    |
          O    |
         /|\   |
               |
               |
        =========
         ''')
if guessing_word == choosen_word:
    print("You Win!!!!")        