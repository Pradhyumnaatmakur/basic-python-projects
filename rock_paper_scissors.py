import random

computer_points = 0
user_points = 0

def play():
    
    global computer_points, user_points
        
    user_choice = input("Rock Paper Scissors (R/P/S): ").lower()
    
    if user_choice not in ["r", "p", "s"]:
        return "Enter a valid choice"
    
    computer_choice = random.choice(["r", "p", "s"])
    
    if user_choice == computer_choice:
        return "Its a tie"
    
    if winner(user_choice, computer_choice):
        user_points += 1            
        return "You Won"
    
    computer_points += 1
    return "You Lost"
    
def winner(p, o):
    #winning r> s, s > p, p > r
    return (p == "r" and o == "o") or \
           (p == "s" and o == "p") or \
           (p == "p" and o == "r")    

while True:
    print(f"Your Score : {user_points} and Computer Score: {computer_points}")
    print(play())