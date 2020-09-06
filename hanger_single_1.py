#Varitables
from nltk.corpus import words
import random
dif = None
word_list = words.words()
al = "qwertyuiopasdfghjklzxcvbnm"
n_a = 0
m = -1
alphabet = list(al)
hanger_man=["   |", "   O", "  /||", "   A", "  /|"]
hanger = [""]*5
mistakes = 0
#Defining the word
wordy = random.choice(word_list)
word = wordy.lower()
letters = list(word)
for i in range(26):
    n_a+=word.count(alphabet[i])
out_letters = ["-"]*n_a
#Introduction
ans = input("""Welcome to the "Hanger" game!
Would you like to start?
(Yes/No)\n""")
if ans == "Yes" or ans == "yes" or ans == "YES":
    print("Great! Let's start!")
else:
    print("Well, we're going to play anyways.")            
#Choosing difficulty
dif = input("""What level of difficulty do you choose?:
Easy/Medium/Hard\n""")
while dif != "Easy" and dif != "easy" and dif != "Medium" and dif != "medium" and dif != "Hard" and dif != "hard":
    dif = input("Level's not clear. Please write it down again.\n")
if dif == "Easy" or dif == "easy":
    n_c = 20
else:
    if dif == "Medium" or dif == "medium":
        n_c = 12
    else:
        n_c = 8
#Active game
print("\nTry to guess one letter from the ", n_a, "-letter word.\n", "You can make ", n_c, " mistakes.", sep="")
n_d = n_a + n_c
n_b = n_c
used_letters = [""]*n_d
for i in range(n_a):
    while (n_c !=0) and "-" in out_letters:
        your_letter = input("Your guess:")
        while your_letter in used_letters:
            your_letter = input("You've already used that letter. Please try another guess.\n")
        n_d -= 1
        m += 1
        used_letters[m] = your_letter
        for i in range(n_a):
            if your_letter == letters[i]:
                    out_letters[i] = your_letter
        if your_letter in out_letters:
            print("'", your_letter, "' is correct!", sep="")
        else:
            mistakes += 1
            n_c -= 1
            for j in range(5):
                if mistakes/n_b >= 0.2*(j+1):
                    hanger[j] = hanger_man[j]
            print("'", your_letter, "' is incorrect.", sep="")
        print("Your hanger man:")
        for i in range(5):
            print(hanger[i])
        print("__________________________\n", "You can still make", n_c, "mistakes.")
        print(*out_letters, "\n", "Used letters:", *used_letters)
if "-" in out_letters:
    print("You lose(. The word was '", word, "'. To try again press 'play'.", sep="")
else:
    print("Hooray! You win! Well done!")
    print("+", n_c, " points!", sep="")