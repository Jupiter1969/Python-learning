#Author WenyuZheng

'''
age_of_oldboy = 56
for count in range(3):
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("Correct!")
        break
    elif guess_age > age_of_oldboy:
        print("Guess smaller.")
    else:
        print("Guess bigger.")
else:
    print("GAME OVER!")



for i in range(0,10,3):
    print("Loop ",i)
'''

for i in range(0,10,1):
    if i < 5:
        print("Loop ",i)
    else:
        continue
