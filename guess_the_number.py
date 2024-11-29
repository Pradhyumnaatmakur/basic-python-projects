import random


print("welcome to number guessing game!")

game = input("Play computer mode or user mode (C/U): ").lower()


if game == "c":
    
    print("The computer will guess your the number")
    
    def computer_mode(x):
        
        low = 1
        high = x
        feedback = ""
        
        while feedback != "c":
            
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low
            
            feedback = input(f"Is the {guess} too high or too low: ").lower()
            
            if feedback == "h":
                high = guess - 1
                
            elif feedback == "l":
                low = guess - 1       
        
        print(f"I Guessed the number {guess} right i won!")  
          
    computer_mode(100)        
                    
       
        
if game == "u":
    print("You will guess the number the computer number")    
    def user_mode(x):
        low = 1
        high = x
        guess = 0
        
        random_number = random.randint(1, x)
        
        while guess != random_number:
            
            guess = int(input(f"Enter a number between {low} and {high}: "))
            
            if guess > random_number:
                print("Too High")
            elif guess < random_number:
                print("Too Low")    
        
        print(f"You guessed the number right! {random_number}, You won!")
    
    
    user_mode(100)        
    
    