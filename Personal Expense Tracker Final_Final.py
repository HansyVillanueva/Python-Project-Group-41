Income_list = []
Income = 0
Income_Total = 0
Storage_Income = []
Spending_list = []
Spending = 0
Spending_Total = 0
Storage_Spending = []
Desc_Spending = []
Others_list = []
Others = 0
Others_Total = 0
Storage_Others = []
def main():
    print("Welcome to the Personal Expense Tracker! Below are some commands you can choose")
    print("1. Income Management")
    print("2. Spending Management")
    print("3. Others(Saving Management, Investment and Charity Allocation)")
    print("4. Income from last year")
    print("5. Top 3 Spendings in the past 30 days")
    print("6. Our suggested function")
    while True:
        try:
            Option = int(input("Please input the number of assoicated command to proceed: "))
        except ValueError:
            print("Don't understand")
            continue
        if Option != 1 and Option != 2 and Option != 3 and Option != 4 and Option != 5 and Option != 6:
            print("Please reinput")
            continue
        else:
            break
    if Option == 1:
        Income_Mangement()
    elif Option == 2:
        Spending_Management()
    elif Option == 3:
        Others()
    elif Option == 4:
        Total_Income_Last_Year()
    elif Option == 5:
        Top_3_Spendings_In_Past_30_Days()
    elif Option == 6:
        Our_Suggested_Function()
    else:
        print("Not in command")


def Income_Mangement():
    global Income_list
    global Income
    global Income_Total
    print("Welcome to Income Management")
    Income_Input = int(input("Please input your daily incomes: "))
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
    global Spending_list
    global Spending
    global Spending_Total
    print("Welcome to Spending Management")
    Spending_Input = int(input("Please input your daily spendings: "))
    Spending_list.append(Spending_Input)
    while True:
        while True:
            try:
                Spending_Input = int(input("Please input your daily spendings, type -1 to stop the process: "))
            except ValueError:
                print("Please enter an integer")
                continue
            else:
                break

        if Spending_Input == -1:
            break
        Spending_list.append(Spending_Input)
    Spending_list = list(map(int, Spending_list))
    Spending_list = list(map(str, Spending_list))
    print("Below is the sequence of inputs/spendings input")
    print(Spending_list)

    while True:
        try:
            Option_Stay_Spending = int(input("Would you like to stay in Spending Management? Type 1 for Yes Type 2 for No: "))
        except ValueError:
            print("Please enter 1 or 2 only")
            continue
        if Option_Stay_Spending != 1 and Option_Stay_Spending != 2:
            print("Input 1 or 2 only")
            continue
        else:
            break

    if Option_Stay_Spending == 1:
        print("1. Store Spending")
        print("2. Update Spending")
        print("3. Retrieve Spending")
        while True:
            try:
                Choice_Spending = int(input("Above is the commands, type the number associated with the command: "))
            except ValueError:
                print("Please enter an integer only")
                continue
            if Choice_Spending != 1 and Choice_Spending != 2 and Choice_Spending != 3:
                print("Please enter 1, 2 or 3 only")
                continue
            else:
                break

        if Choice_Spending == 1:
            Store_Spending()
        elif Choice_Spending == 2:
            Update_Spending()
        elif Choice_Spending == 3:
            Retrieve_Spending()


    elif Option_Stay_Spending == 2:
        main()
    else:
        print("Not part of commands")


def Others():
    print("Welcome to Saving, Investment and Charity Mangement")
    global Others_list
    global Others
    global Others_Total
    Others_Input = int(input("Please input your daily Other money allocations: "))
    Others_list.append(Others_Input)
    while True:
        while True:
            try:
                Others_Input = int(input("Please input your dailt Other money allocations, type -1 to stop the process: "))
            except ValueError:
                print("Please enter an integer")
                continue
            else:
                break

        if Others_Input == -1:
            break
        Others_list.append(Others_Input)
    Others_list = list(map(int, Others_list))
    # for i in range(0, len(Income_list)):
    # Income_Total = Income_Total + Income_list[i]
    Others_list = list(map(str, Others_list))
    print("Below is the sequence of inputs of Other money allocations input")
    print(Others_list)

    while True:
        try:
            Option_Stay = int(input("Would you like to stay in Others Management? Type 1 for Yes Type 2 for No: "))
        except ValueError:
            print("Please enter 1 or 2 only")
            continue
        if Option_Stay != 1 and Option_Stay != 2:
            print("Input 1 or 2 only")
            continue
        else:
            break

    if Option_Stay == 1:
        print("1. Store Others")
        print("2. Update Others")
        print("3. Retrieve Others")
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
            Store_Others()
        elif Choice == 2:
            Update_Others()
        elif Choice == 3:
            Retrieve_Others()


    elif Option_Stay == 2:
        main()
    else:
        print("Not part of commands")



def Total_Income_Last_Year():
    print("Welcome to Total Income Last Year") #Is it this year or last year? If this year just add the list Income List
    print(Income_list)


def Top_3_Spendings_In_Past_30_Days():
    global Spending_list
    print("Welcome to Top 3 Spendings in Past 30 days")
    print("Below is your list of Spending: ")
    print(Spending_list)
    print("Below is your list in descending order ")
    Spending_list.sort(reverse=True)
    print(Spending_list)
    print("Below is the top 3 spendings ") #need to find out how to do the 30 days thing
    print(Spending_list[0])
    print(Spending_list[1])
    print(Spending_list[2])


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
    print("Below is your current input list: ")
    print(Income_list)
    print("1. Add Income ")
    print("2. Remove Income ")
    while True:
        try:
            Update_Income_Input = int(input("Please enter 1 to add Income, 2 to delete Income "))
        except ValueError:
            print("Please enter an integer only")
            continue
        if Update_Income_Input != 1 and Update_Income_Input != 2 :
            print("Please enter 1 or 2 ")
            continue
        else:
            break
    if Update_Income_Input == 1:
        Update_Income_Add_Income()
    elif Update_Income_Input == 2:
        Update_Income_Remove_Income()
    else:
        print("Not part of commands")


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

def Update_Income_Add_Income():
    global Income_list
    print("Welcome to Updating Income for adding Income: ")
    print("Below is your most updated list of Incomes: ")
    print(Income_list)
    Update_Income_Add_Income_Add_Income = int(input("Please input an integer to add to the end of the list: "))
    Income_list.append(Update_Income_Add_Income_Add_Income)
    while True:
        while True:
            try:
                Update_Income_Add_Income_Add_Income = int(input("Please input an integer to add to the end of the list, -1 to stop: "))
            except ValueError:
                print("Please enter an intger: ")
                continue
            else:
                break

        if Update_Income_Add_Income_Add_Income == -1:
            break
        Income_list.append(Update_Income_Add_Income_Add_Income)
    Income_list = list(map(int, Income_list))
    Income_list = list(map(str, Income_list))
    print("The new list is below: ")
    print(Income_list)
    while True:
        try:
            Choice_Stay_Update_Income = int(input("Please enter 1 to Stay in Income Management, 2 to exit Update Income: "))
        except ValueError:
            print("Please enter an integer only")
            continue
        if Choice_Stay_Update_Income != 1 and Choice_Stay_Update_Income != 2:
            print("Please enter 1 or 2 only")
            continue
        else:
            break
    if Choice_Stay_Update_Income == 1:
        Income_Mangement()
    elif Choice_Stay_Update_Income == 2:
        main()
    else:
        print("Not part of commands")

def Update_Income_Remove_Income():  #I need help in the remove function for all objects, not sure why not outputting the list and updating
    global Income_list
    print("Welcome to Update Income, Removing Income ")
    print("Below is your most updated list")
    print(Income_list)
    Update_Income_Remove_Income_Index = int(input("Please input the index of wanted removed number: "))
    Income_list.pop(Update_Income_Remove_Income_Index)
    while True:
        while True:
            try:
                Update_Income_Add_Income_Add_Income = int(input("Please input the index of wanted removed number: "))
            except ValueError:
                print("Please enter an intger: ")
                continue
            else:
                break

        if Update_Income_Add_Income_Add_Income == -1:
            break

print(Income_list)


def Store_Spending():
    print("Welcome to Store Spending ")
    global Storage_Spending
    global Spending_list
    print("Welcome to Store Spending")
    for element in Spending_list:
        Storage_Spending.append(element)
    print("Below is the stored spending inputs in sequence: ")
    print(Storage_Spending)
    while True:
        try:
            Choice_Stay_Store_Spending = int(input("Please enter 1 to Stay in Spending Management, 2 to exit Store Income"))
        except ValueError:
            print("Please enter an integer only")
            continue
        if Choice_Stay_Store_Spending != 1 and Choice_Stay_Store_Spending != 2:
            print("Please enter 1 or 2 only")
            continue
        else:
            break
    if Choice_Stay_Store_Spending == 1:
        Spending_Management()
    elif Choice_Stay_Store_Spending == 2:
        main()
    else:
        print("Not part of commands")

def Update_Spending_Add_Spending():
    global Spending_list
    print("Welcome to Updating Spending for adding Spending: ")
    print("Below is your most updated list of Spending: ")
    print(Spending_list)
    Update_Spending_Add_Spending_Add_Spending = int(input("Please input an integer to add to the end of the list "))
    Spending_list.append(Update_Spending_Add_Spending_Add_Spending)
    while True:
        while True:
            try:
                Update_Spending_Add_Spending_Add_Spending = int(input("Please input an integer to add to the end of the list, -1 to stop: "))
            except ValueError:
                print("Please enter an integer: ")
                continue
            else:
                break

        if Update_Spending_Add_Spending_Add_Spending == -1:
            break
        Spending_list.append(Update_Spending_Add_Spending_Add_Spending)
    Spending_list = list(map(int, Spending_list))
    Spending_list = list(map(str, Spending_list))
    print("The new list is below: ")
    print(Spending_list)
    while True:
        try:
            Choice_Stay_Update_Spending = int(input("Please enter 1 to Stay in Spending Management, 2 to exit Update Spending: "))
        except ValueError:
            print("Please enter an integer only")
            continue
        if Choice_Stay_Update_Spending != 1 and Choice_Stay_Update_Spending != 2:
            print("Please enter 1 or 2 only")
            continue
        else:
            break
    if Choice_Stay_Update_Spending == 1:
        Spending_Management()
    elif Choice_Stay_Update_Spending == 2:
        main()
    else:
        print("Not part of commands")

def Update_Spending_Remove_Spending():
    print("shy") #need help in removal of elementts within list

def Update_Spending():
    print("Welcome to Update Spending ")
    print("Below is your current input list: ")
    print(Spending_list)
    print("1. Add Spending ")
    print("2. Remove Spending ")
    while True:
        try:
            Update_Spending_Input = int(input("Please enter 1 to add Spending, 2 to delete Spending "))
        except ValueError:
            print("Please enter an integer only")
            continue
        if Update_Spending_Input != 1 and Update_Spending_Input != 2:
            print("Please enter 1 or 2")
            continue
        else:
            break
    if Update_Spending_Input == 1:
        Update_Spending_Add_Spending()
    elif Update_Spending_Input == 2:
        Update_Spending_Remove_Spending()
    else:
        print("Not part of commands")

def Retrieve_Spending():
    global Spending_list
    global Spending_Total
    print("Welcome to Retrieve Spending")
    print("Below is your Spending after inputs sequentially")
    print(Spending_list)
    while True:
        try:
            Choice_Stay_Retrieve_Spending = int(input("Please enter 1 to Stay in Spending Management, 2 to exit Retrieve Spending"))
        except ValueError:
            print("Please enter an integer only")
            continue
        if Choice_Stay_Retrieve_Spending != 1 and Choice_Stay_Retrieve_Spending != 2:
            print("Please enter 1 or 2 only")
            continue
        else:
            break
    if Choice_Stay_Retrieve_Spending == 1:
        Spending_Management()
    elif Choice_Stay_Retrieve_Spending == 2:
        main()
    else:
        print("Not part of commands")


def Store_Others():
    global Storage_Others
    global Others_list
    print("Welcome to Store Others")
    for element in Others_list:
        Storage_Others.append(element)
    print("Below is the stored Other money allocations inputs in sequence: ")
    print(Storage_Others)
    while True:
        try:
            Choice_Stay_Store_Others = int(input("Please enter 1 to Stay in Others Management, 2 to exit Store Others: "))
        except ValueError:
            print("Please enter an integer only")
            continue
        if Choice_Stay_Store_Others != 1 and Choice_Stay_Store_Others != 2:
            print("Please enter 1 or 2 only")
            continue
        else:
            break
    if Choice_Stay_Store_Others == 1:
        Others()
    elif Choice_Stay_Store_Others == 2:
        main()
    else:
        print("Not part of commands")

def Update_Others_Add_Others():
    global Others_list
    print("Welcome to Updating Others for adding Others: ")
    print("Below is your most updated list of Others: ")
    print(Others_list)
    Update_Others_Add_Others_Add_Others = int(input("Please input an integer to add to the end of the list "))
    Others_list.append(Update_Others_Add_Others_Add_Others)
    while True:
        while True:
            try:
                Update_Others_Add_Others_Add_Others = int(input("Please input an integer to add to the end of the list, -1 to stop: "))
            except ValueError:
                print("Please enter an integer: ")
                continue
            else:
                break

        if Update_Others_Add_Others_Add_Others == -1:
            break
        Others_list.append(Update_Others_Add_Others_Add_Others)
    Others_list = list(map(int, Others_list))
    Others_list = list(map(str, Others_list))
    print("The new list is below: ")
    print(Others_list)
    while True:
        try:
            Choice_Stay_Update_Others = int(input("Please enter 1 to Stay in Others Management, 2 to exit Update Others: "))
        except ValueError:
            print("Please enter an integer only")
            continue
        if Choice_Stay_Update_Others != 1 and Choice_Stay_Update_Others != 2:
            print("Please enter 1 or 2 only")
            continue
        else:
            break
    if Choice_Stay_Update_Others == 1:
        Others()
    elif Choice_Stay_Update_Others == 2:
        main()
    else:
        print("Not part of commands")

def Update_Others_Remove_Others():
    pass

def Update_Others():
    print("Welcome to Update Others ")
    print("Below is your current input list: ")
    print(Others_list)
    print("1. Add Others ")
    print("2. Remove Others ")
    while True:
        try:
            Update_Others_Input = int(input("Please enter 1 to add others, 2 to delete others "))
        except ValueError:
            print("Please enter an integer only")
            continue
        if Update_Others_Input != 1 and Update_Others_Input != 2:
            print("Please enter 1 or 2")
            continue
        else:
            break
    if Update_Others_Input == 1:
        Update_Others_Add_Others()
    elif Update_Others_Input == 2:
        pass
    else:
        print("Not part of commands")

def Retrieve_Others():
    global Others_list
    global Others_Total
    print("Welcome to Retrieve Others")
    print("Below is your Others(other money allocations) after inputs sequentially")
    print(Others_list)
    while True:
        try:
            Choice_Stay_Retrieve_Others = int(input("Please enter 1 to Stay in Others Management, 2 to exit Others Spending"))
        except ValueError:
            print("Please enter an integer only")
            continue
        if Choice_Stay_Retrieve_Others != 1 and Choice_Stay_Retrieve_Others != 2:
            print("Please enter 1 or 2 only")
            continue
        else:
            break
    if Choice_Stay_Retrieve_Others == 1:
        Others()
    elif Choice_Stay_Retrieve_Others == 2:
        main()
    else:
        print("Not part of commands")


main()