import random
def guess(x):
    random_number = random.randint(1,x)
    trial = 0
    while (trial != random_number):
        trial = int(input("Enter your guess: "))
        if(trial < random_number):
            print("Too low. Enter a higher number")
        elif(trial > random_number):
            print("Too high. Enter a lower number")
    print(f"You got it right! the guess is {random_number}")    

def comp_guess (x): 
    my_guess = 25
    low =1
    high=x
    guess= 0
   
    feedback = ""
    while (feedback != "c"):
        
        if (low!= high):
            guess= random.randint(low,high)
        else:
            guess = low
        feedback = input((f"Is {guess} higher(h) or lower(l) or correct(c): "))
        if (feedback == "h"):
            high = guess-1
        elif(feedback == "l" ):
            low = guess +1
    print(f"the correct answer is {guess}")
comp_guess(5)










print("hello world")


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while (guess != random_number):
        guess = int(input("Enter your guess: "))
        if (guess > random_number):
            print("number is too high.Guess again please.")
        elif (guess < random_number):
            print("number is too low.Guess again please.")

    print(f"You guessed it right. the correct answer is {random_number}")


def comp_guess(x):
   
    low = 1
    high = x
    feedback = ""
    while (feedback != "c"):
        if (low != high):
            guess = random.randint(low, high)
            
        elif(low ==high):
            guess = low
       
        feedback = input(
            f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if (feedback == "h"):
            print(guess)
            high = guess - 1
        elif(feedback == "l"):
            print(guess)
            low = guess + 1
    print(f"You guessed it right, the answer is:{guess}")




def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(
            f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')

#computer_guess(10)


