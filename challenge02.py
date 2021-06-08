import random

icecream= ["flavors", "salty"] 
tlgclass= ["Brian","Clint","Damian","Dan","David","Jelani","Jerad","Jon","Jun","Mark","Max"]

icecream.append(99)

inputNumber =int(input("Enter a number from 0 - 10 inclusive\n>"))

#outputing this <99> <flavors>, and <student name> chooses to be <salty>.
print(f"99 {icecream[0]} and {tlgclass[inputNumber]} chose to be {icecream[1]}")

#random generated students
randomInt = random.randint(0,10)
print(f"99 {icecream[0]} and {tlgclass[randomInt]} chose to be {icecream[1]}")


