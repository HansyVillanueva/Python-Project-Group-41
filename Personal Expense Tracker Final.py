Income_list = []
Income = 0
Income_Total = 0
Storage_Income = []

def main():
    print("Welcome to the Personal Expense Tracker! Below are some commands you can choose")
    print("1. Income Management")
    print("2. Spending Management")
    print("3. Saving Management")
    print("4. Investment Management")
    print("5. Charity Management")
    print("6. Income from last year")
    print("7. Top 3 Spendings in the past 30 days")
    print("8. Our suggested function")
    while True:
        try:
            Option = int(input("Please input the number of assoicated command to proceed: "))
        except ValueError:
            print("Don't understand")
            continue
        if Option != 1 and Option != 2 and Option != 3 and Option != 4 and Option != 5 and Option != 6 and Option != 7 and Option != 8:
            print("Please reinput")
            continue
        else:
            break
    if Option == 1:
        Income_Mangement()
    elif Option == 2:
        Spending_Management()
    elif Option == 3:
        Saving_Management()
    elif Option == 4:
        Investment_Management()
    elif Option == 5:
        Charity_Management()
    elif Option == 6:
        Total_Income_Last_Year()
    elif Option == 7:
        Top_3_Spendings_In_Past_30_Days()
    elif Option == 8:
        Our_Suggested_Function()
    else:
        print("Not in command")


def Income_Mangement():
    global Income_list
    global Income
    global Income_Total
    print("Welcome to Income Management")
    Income_Input = int(input("Please input your daily incomes, type stop to stop the process: "))
    Income_list.append(Income_Input)
    while True:
        while True:
            try:
                Income_Input = int(input("Please input your daily incomes, type -1 to stop the process: "))
            except ValueError:
                print("Please enter an intger")
                continue
            else:
                break

        if Income_Input == -1:
            break
        Income_list.append(Income_Input)
    Income_list = list(map(int, Income_list))
    #for i in range(0, len(Income_list)):
        #Income_Total = Income_Total + Income_list[i]
    Income_list = list(map(str, Income_list))
    print("Below is the sequence of inputs/incomes input")
    print(Income_list)
    #print("Below is your total Income from inputs: ")
    #print(Income_Total)

    while True:
        try:
            Option_Stay = int(input("Would you like to stay in Income Management? Type 1 for Yes Type 2 for No: "))
        except ValueError:
            print("Please enter 1 or 2 only")
            continue
        if Option_Stay != 1 and Option_Stay != 2:
            print("Input 1 or 2 only")
            continue
        else:
            break

    if Option_Stay == 1:
        print("1. Store Income")
        print("2. Update Income")
        print("3. Retrieve Income")
        while True:
            try:
                Choice = int(input("Above is the commands, type the number associated with the command: "))
            except ValueError:
                print("Please enter an integer only")
                continue
            if Choice != 1 and Choice != 2 and Choice != 3:
                print("Please enter 1, 2 or 3 only")
                continue
            else:
                break

        if Choice == 1:
            Store_Income()
        elif Choice == 2:
            Update_Income()
        elif Choice == 3:
            Retrieve_Income()





    elif Option_Stay == 2:
        print("No")
    else:
        print("Not part of commands")




def Spending_Management():
    global Income_list
    print("Welcome to Spending Management")
    print(Income_list)


def Saving_Management():
    print("Welcome to Saving Mangement")

def Investment_Management():
    print("Welcome to Investment Management")

def Charity_Management():
    print("Welcome to Charity Management")

def Total_Income_Last_Year():
    print("Welcome to Total Income Last Year")

def Top_3_Spendings_In_Past_30_Days():
    print("Welcome to Top 3 Spendings in Past 30 days")

def Our_Suggested_Function():
    print("Welcome to our suggested function")

def Store_Income():
    global Storage_Income
    global Income_list
    print("Welcome to Store Income")
    for element in Income_list:
        Storage_Income.append(element)
    print("Below is the stored income inputs in sequence: ")
    print(Storage_Income)
    while True:
        try:
            Choice_Stay_Store_Income = int(input("Please enter 1 to Stay in Income Management, 2 to exit Store Income"))
        except ValueError:
            print("Please enter an integer only")
            continue
        if Choice_Stay_Store_Income != 1 and Choice_Stay_Store_Income != 2:
            print("Please enter 1 or 2 only")
            continue
        else:
            break
    if Choice_Stay_Store_Income == 1:
        Income_Mangement()
    elif Choice_Stay_Store_Income == 2:
        main()
    else:
        print("Not part of commands")

def Update_Income():
    print("Welcome to Update ")

def Retrieve_Income():
    global Income_list
    global Income_Total
    print("Welcome to Retrieve Income")
    print("Below is your income after inputs sequentially")
    print(Income_list)
    #print("Below is the total of your income")
    #print(Income_Total)
    while True:
        try:
            Choice_Stay_Retrieve_Income = int(input("Please enter 1 to Stay in Income Management, 2 to exit Retrieve Income"))
        except ValueError:
            print("Please enter an integer only")
            continue
        if Choice_Stay_Retrieve_Income != 1 and Choice_Stay_Retrieve_Income != 2:
            print("Please enter 1 or 2 only")
            continue
        else:
            break
    if Choice_Stay_Retrieve_Income == 1:
        Income_Mangement()
    elif Choice_Stay_Retrieve_Income == 2:
        main()
    else:
        print("Not part of commands")



main()