from random import choice
valid_letters = "q w e r t y u i o p a s d f g h j k l z x c v b n m"
valid_letters_list = valid_letters.split()
word_list = []
with open("words.txt") as word_file:
    for row in word_file:
        word_list.append(row[:-1])
print(word_list)
word_string = choice(word_list)
word = list(word_string)
print(word)
word_guessed = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
word_guessed = word_guessed[0:len(word)]
score = 0
print("Score: " + str(score))
while True:
    user_guess = input("Enter a letter: ")
    if len(user_guess) > 1:
        print("Guess should only be one character!")
    if not user_guess.islower():
        print("Guess should only be lowercase")
    if len(user_guess) == 1 and user_guess.islower():
        if user_guess in word:
            print("Your guess is in the word.")
            for i in range(len(word)):
                if word[i] == user_guess:
                    word_guessed[i] = user_guess
            print(word_guessed)
            score += 1
            print("Score: " + str(score))
        else:
            print("Your guess is not in the word.")
            score -= 1
            print("Score: " + str(score))
        if word_guessed == word:
            print("You win!")
            input('Hit your ENTER key as hard as you can to exit.')
            break
        if score <= -5:
            print("Beep. You lost!")
            input('Break your keyboard with a hit to the ENTER key to exit.')
            break