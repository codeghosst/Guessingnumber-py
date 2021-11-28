import random
toguess= int(random. randint(0,99))
print(toguess)
attempts=0
while True:
    attempts = attempts+1
    gtm = int(input("Guess the number given by the system:"))
    if(toguess>gtm):
        print("Wrong!!! \n Clue: Your guess is less than the number. ")
    elif(toguess<gtm):
        print("Wrong!!! \n Clue: Your guess is greater than the number.")
    else:
        print(f"Congratulations !!! You got it right in {attempts}  attempts..." )
        break
