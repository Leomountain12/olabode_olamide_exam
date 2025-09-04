#question 1
def addition(a,b):
    return a + b

def sibtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b


def division(a,b):
    if a !=0 and b !=0:
        return a/b
    else:
        print("error dividing number by zero")

while True:
    calculation = int(input("kindly choose an option\n1.addition\n2.subtraction\n3.mupltiplication\n4.division\n5exit"))
    if calculation == 1 :
        num1=int(input("enter first number"))
        num2= int(input("enter second number")) 
        print("answer:",addition(num1,num2)) 
        

    elif calculation == 2 :
        num1=int(input("enter first number"))
        num2= int(input("enter second number")) 
        print("answer:",sibtraction(num1,num2))
    elif calculation == 3 :
        num1=int(input("enter first number"))
        num2= int(input("enter second number")) 
        print("answer:",multiplication(num1,num2))
    elif calculation==4 :
        num1=int(input("enter first number"))
        num2= int(input("enter second number")) 
        print("answer:",division(num1,num2))  
    elif calculation == 5 :
        print("existing calculator") 
        break           
    else:
        print("entwer number from 1_4")
    


# question 2


while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break        # break out of loop
    
    num = int(input("user_input:") )  # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")




#question 3    
while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == "exit":
        print("Goodbye!")
        break
    
    try:
        if int(age) >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input")    



    
