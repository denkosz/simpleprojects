
import random
x = random.randint(1, 101)
print(x)

guesses = 0
gameover = True
while gameover:
    guess = int(input("1 to 100: "))
    if guess < 1 or guess > 100:
        print("out of bounds")
    elif guess == x:
        gameover = False
        break

    if abs(x-guess) <= 2:
        print("warmer")
    elif abs(x-guess) <= 10:
        print("warm")
    elif abs(x-guess) <= 20:
        print("cold")
    else:
        print("colder")
    guesses += 1

print(f"Congrats, you guessed it on only {guesses} guesses")


