print("Welcome to mindy skills calculator .")
operator = input("Enter the operator : ")
first_number = int(input("Enter the first number : "))
sec_number = int(input("Enter the second number : "))

if operator == "+" :
    print(first_number + sec_number)
    
elif operator == "-" :
    print(first_number - sec_number)
    
elif operator == "*" :
    print(first_number * sec_number)
    
elif operator == "/" :
    print(first_number / sec_number)
    
else :
    print("ERROR !!!")