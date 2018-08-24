#Author WenyuZheng

age_of_oldboy = 56
count = 0
while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("Correct!")
        break
    elif guess_age > age_of_oldboy:
        print("Guess smaller.")
    else:
        print("Guess bigger.")
    count += 1
    if count == 3:
        continue_confirm = input("Do you want to continue(y/n)?")
        if continue_confirm != 'n':
            count = 0
else:
    print("GAME OVER!")