print("Hello Calculator")

def get_number (num) :
    while True:
        operand = input("Number " + str(num) + " :")
        try:
            return float(operand)
        except: 
            print("enter a valid number")
            

            
result = 0

operand = get_number(1)
operand2 = get_number(2)


while True: 
    sign = input("Sign (+, -, * , /) : ")
    if sign in ["+", "-", "*", "/"]:
        break
    print("enter a valid sign")  
    
    
if sign == "+":
    result = operand + operand2

elif sign == "-":
    result = operand - operand2 

elif sign == "*":
    result = operand * operand2

elif sign == "/":
    if operand2 != 0 :
        result = operand / operand2
    else :
        print("Division by zero")    

    
    
print(result)           
            
 
        