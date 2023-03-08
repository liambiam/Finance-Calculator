import math

while True:
    # Use \n to show options on different lines.
    user_choice = input("investment - to calculate the amount of interest you'll earn on your investment \nbond - to calculate the amount you'll have to pay on a home loan \n\nEnter either 'investment' or 'bond' from the menu above to proceed: ")
    # Convert string to lowercase, making it easier to check for correct input.
    user_choice = user_choice.lower()
    # Use 'while' to re-ask for input if variable user_choice is entered incorrectly.  
    if user_choice == "investment":
        # Use 'while' to re-ask for input if any of the below user inputs are entered incorrectly.
        while True:
            # Use 'try & except' to re-ask for input if the user enters a non float value which would return an error (a little experimental!).
            try:
                deposit = float(input("How much money are you depositing? £"))
                if type(deposit) == float:
                    break
            except: ValueError
            print("Please enter a numerical value only") 
        while True:
            try:
                interest_rate = float(input("What is the interest rate? %"))
                if type(interest_rate) == float:
                    break
            except: ValueError
            print("Please enter a numerical value only") 
        while True:
            try:
                years = int(input("How many years are you planning to invest for? "))
                if type(years) == int:
                    break
            except:
                print("Please enter a numerical value only")    #this requires an indent, but previous didn't??    
        while True: 
            interest_type = input("Enter either 'simple' or 'compound' for your preferred interest type: ")
            interest_type = interest_type.lower()
            # Calculate and return result for each type of interest.
            if interest_type == "simple":
                total = deposit * (1 + (interest_rate * years / 100))
                print(f"The total amount of your investment after {years} years will be £{total:.2f}")
                break
            elif interest_type == "compound":
                total = deposit * math.pow((1 + (interest_rate / 100)),years)
                total = round(total, 2)
                print(f"The total amount of your investment after {years} years will be £{total:.2f}")
                break
            else:
                print("You have entered an incorrect value, please try again")
        break
    elif user_choice == "bond":
        # User inputs here, I've included all of the while/try/except too to prevent errors.
        while True:
            try:
                house_value = float(input("How much is the current value of the house? £"))
                if type(house_value) == float:
                    break
            except: ValueError
            print("Please enter a numerical value only")
        while True:
            try:
                interest_rate = float(input("What is the interest rate? %"))
                if type(interest_rate) == float:
                    break
            except: ValueError
            print("Please enter a numerical value only")
        while True:
            try:
                months = float(input("How many months do you plan to repay the bond? "))
                if type(months) == float:
                    break
            except: ValueError
            print("Please enter a numerical value only")        
        # Calculations, round to 2dp, and print.
        repayment = (interest_rate * house_value / 100) / (1 - (1 + (interest_rate / 100))**(-months)) 
        print(f"You will need to repay £{repayment:.2f} each month")
        break
    else:
        print("You have entered an incorrect choice, please try again")

#notes: re. while/try/except statements to re-ask for input if the user entered e.g. deposit/interest_rate/years incorrectly - is there a simpler/shorter way to do this??
# experimenting with try/else. Qs why is print() on the same indent? no need for else?