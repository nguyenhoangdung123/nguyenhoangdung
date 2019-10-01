import random
word = "champion"
shuffled = list(word)
random.shuffle(shuffled)
shuffled = ''.join(shuffled)
print(shuffled.upper())
print("the jumble is:")
guess = raw_input("your guess:")
guess = guess.lower()
while True:
    if guess == correct:
        print("chinh xac")
        break
    else:
        print("chua chinh xac")    
