import datetime

def writeFromFile(x,y):
    '''
    Function for writing user inputs into files
    :param x: File name
    :param y: data object to append into files
    :return:
    '''
    f1 = open(x,"a+")
    if(len(y)>2): #If statement differentiates different reporting states as some tools have more/less user data
        f1.write(str(y[0])+" "+str(y[1])+" "+str(y[2])+"\n")
    else:
        f1.write(str(y[0])+" "+str(y[1])+"\n")
    f1.close()

def finacialRep():
    '''
    Functions which handles user input flow for income reporting
    :return:
    '''
    print("-------------------------------------------------\nWelcome to Personal Finance Management!\n-------------------------------------------------\n")
    print("1 for Income Input\n2 for Income Retrieval\ns,S,stop,Stop to end program\n")
    print("Latest Income is "+str(retrieveLatestIncome())+"\n")
    ret = "FinData"
    move = input("Action: ")
    while(move != "1" and move !="2" and move !="s" and move !="Stop" and move !="S" and move !="stop"): #User input validation, alongside checking whether the user wishes to leave the function.
        move = input("Invalid Input - Action: ")

    while(move !="s" and move !="Stop" and move !="S"and move !="stop"):
        if(move=="1"):
            finacialRepAdd()
        elif(move=="2"):
            finacialRepRet(ret)
        print("\n1 for Income Input\n2 for Income Retrieval\ns,S,stop,Stop to end program\n")
        move = input("Action: ")

def finacialRepAdd():
    '''
    Function which handle user inputs for income reporting, includes input validation and file handling
    :return:
    '''
    finData = "FinData"
    print("Welcome to Finance Addition - Input s,stop,S to leave\nInput Format: amount date\nExample: 5000 15/2/2022\n")
    money = input("How much are you making?: ").split()
    while(money[0] != "s" and money[0] != "stop" and money[0]!="S"and money!="stop"): #User input validation, alongside checking whether the user wishes to leave the function.
        while(len(money)!=2):
            money = input("Incorrect length - Only 2 values allowed - How much are you making?: ").split()
        while(type(money[0]) != type(1)):
            try:
                money[0]=int(money[0])
            except ValueError:
                money[0] = input("Incorrect input type - Only numerical values allowed - How much are you making?: ")
        x=""
        while(not x):
            try:
                dates=money[1].split('/')
                x = datetime.datetime(int(dates[2]),int(dates[1]),int(dates[0]))
            except (ValueError,IndexError) as error:
                money[1] = input("Incorrect input type - Only date values allowed - what date was it (D/M/Y): ")
        money[1]=x
        writeFromFile(finData,money)
        money = input("How much are you making?: ").split()

def retrieveLatestIncome():
    '''
    Function to retrieve the latest added Income, serves to depict latest input
    :return:
    '''
    try:
        f1 = open("FinData", "r+")
        values = [x[:-1] for x in f1.readlines()]
        values.reverse()
        return (values[0].split())[0] #returns latest income input
    except (FileNotFoundError,IndexError)as error:
        f2 = open("FinData", "w+")
        return "N/A"


def spendingRep():
    '''
    Functions which handles user input flow for spending reporting
    :return:
    '''
    print("-------------------------------------------------\nWelcome to Personal Spending Management!\n-------------------------------------------------\n")
    print("1 for Spending Input\n2 for Spending Retrieval\ns,S,stop,Stop to end program\n")
    ret = "spenData"
    move = input("Action: ")
    while(move != "1" and move !="2" and move !="s" and move !="Stop" and move !="S"and move !="stop"): #User input validation, alongside checking whether the user wishes to leave the function.
        move = input("Invalid Input - Action: ")
    while(move !="s" and move !="Stop" and move !="S"and move !="stop"):
        if(move=="1"):
            spendingRepAdd()
        elif(move=="2"):
            finacialRepRet(ret)
        print("\n1 for Spending Input\n2 for Spending Retrieval\ns,S,stop,Stop to end program\n")
        move = input("Action: ")

def spendingRepAdd():
    '''
    Function which handle user inputs for spending reporting, includes input validation and file handling
    :return:
    '''
    spenData = "spenData"
    print("Welcome to Spending Reporting - Input s,stop,S to leave\nInput Format: amount date\nExample: 5000 15/2/2022\n")
    money = input("How much are you spending?: ").split()
    while(money[0] != "s" and money[0] != "stop" and money[0] != "S"and money !="stop"): #User input validation, alongside checking whether the user wishes to leave the function.
        while (len(money) != 2):
            money = input("Incorrect length - Only 2 values allowed - How much are you making?: ").split()
        while (type(money[0]) != type(1)):
            try:
                money[0] = int(money[0])
            except ValueError:
                money[0] = input("Incorrect input type - Only numerical values allowed - How much are you spending?: ")
        x = ""
        while (not x):
            try:
                dates = money[1].split('/')
                x = datetime.datetime(int(dates[2]), int(dates[1]), int(dates[0])) #datetime input validation, to ensure it is in the proper format with acceptable values
            except (ValueError, IndexError) as error:
                money[1] = input("Incorrect input type - Only date values allowed - what date was it (D/M/Y): ")
        money[1] = x
        writeFromFile(spenData, money)
        money = input("How much are you spending?: ").split()

def finacialRepRet(y):
    '''
    Function to retrieve user inputs from files, utilized in most analysis functions and for data retreival and updates
    :param y: name string for the files
    :return:
    '''
    try:
        f1 = open(y,"r+")
        print("Previous incomes:")
        print([x[:-1] for x in f1.readlines()]) #returns user inputs for a specific file
    except FileNotFoundError:
        print("Function not avaliable, please input values")

def financeInfo():
    '''
    Functions which handles user input flow for the financial info section of the program
    :return:
    '''
    print(
        "-------------------------------------------------\nWelcome to Finance Info!\n-------------------------------------------------\n")
    print("1 for Income information from last year\n2 for Spending information from last month\ns,S,stop,Stop to end program\n")
    move = input("Action: ")
    while (move != "1" and move != "2" and move != "s" and move != "Stop" and move != "S"and move != "stop"):#User input validation, alongside checking whether the user wishes to leave the function.
        move = input("Invalid Input - Action: ")

    while (move != "s" and move != "Stop" and move != "S"and move !="stop"):
        if (move == "1"):
            print()
            topIncomeLastYear()
        elif (move == "2"):
            print()
            topSpendingLastMonth()
        print("\n1 for Income information from last year\n2 for Spending information from last month\ns,S,stop,Stop to end program\n")
        move = input("Action: ")

def topIncomeLastYear():
    '''
    Function which calculates the top income from last year according to user inputs. (utilizing timedata library)
    :return:
    '''
    try:
        year_now = datetime.datetime.now().year-1
        f1 = open("FinData", "r")
        comparision_values=[]
        for row in f1.readlines():
            row_date_info=(row.split())[1].split("-")
            if(int(row_date_info[0])==year_now):
                comparision_values.append(int(row.split()[0]))
        comparision_values.sort(reverse=True)
        if(not comparision_values):
            print("No income earned last year")
        else:
            print("Largest income earned last year: "+ str(comparision_values[0]))
    except FileNotFoundError:
        print("Function not avaliable, please input values")

def topSpendingLastMonth():
    '''
    Function which calculates the top 3 spendings of the user from the last 30 days. (utilizing timedata library)
    :return:
    '''
    try:
        day_now = datetime.datetime.now()
        diff = day_now - datetime.timedelta(days=30)
        f1 = open("spenData", "r")
        comparision_values = []
        for row in f1.readlines():
            row_date_info = ((row.split())[1]).split("-")
            comp_date = datetime.datetime(day=int(row_date_info[2]),month=int(row_date_info[1]),year=int(row_date_info[0]))
            if (comp_date>=diff and comp_date<=datetime.datetime.now()):
                comparision_values.append(int(row.split()[0]))
        comparision_values.sort(reverse=True)
        print("Top 3 spendings of the last 30 days:",comparision_values[:3])
    except FileNotFoundError:
        print("Function not avaliable, please input values")

def donationRep():
    '''
    Functions which handles user input flow for donation reporting
    :return:
    '''
    print("-------------------------------------------------\nWelcome to Donation Management!\n-------------------------------------------------\n")
    print("1 for Donation Input\n2 for Donation Retrieval\n3 for Donation info\ns,S,stop,Stop to end program\n")
    ret = "donData"
    move = input("Action: ")
    while(move != "1" and move !="2"and move !="3" and move !="s" and move !="Stop" and move !="S"and move !="stop"):#User input validation, alongside checking whether the user wishes to leave the function.
        move = input("Invalid Input - Action: ")
    while(move !="s" and move !="Stop" and move !="S"and move !="stop"):
        if(move=="1"):
            donationRepAdd()
        elif(move=="2"):
            finacialRepRet(ret)
        elif (move == "3"):
            donationInfo()
        print("\n1 for Donation Input\n2 for Donation Retrieval\n3 for Donation info\ns,S,stop,Stop to end program\n")
        move = input("Action: ")

def donationRepAdd():
    '''
    Function which handle user inputs for donation reporting, includes input validation and file handling
    :return:
    '''
    donData = "donData"
    print("Welcome to Donation Addition - Input s,stop,S to leave\nInput Format: amount date charity\nExample: 5000 15/2/2022 RedCross\n")#User input validation, alongside checking whether the user wishes to leave the function.
    money = input("How much are you donating?: ").split()
    while(money[0] != "s" and money[0] != "stop" and money[0] != "S"and money !="stop"):
        while (len(money) != 3):
            money = input("Incorrect length - Only 2 values allowed - How much are you making?: ").split()
        while (type(money[0]) != type(1)):
            try:
                money[0] = int(money[0])
            except ValueError:
                money[0] = input("Incorrect input type - Only numerical values allowed - How much are you donating?: ")
        x = ""
        while (not x):
            try:
                dates = money[1].split('/')
                x = datetime.datetime(int(dates[2]), int(dates[1]), int(dates[0]))
            except (ValueError, IndexError) as error:
                money[1] = input("Incorrect input type - Only date values allowed - what date was it (D/M/Y): ")
        money[1] = x
        writeFromFile(donData, money)
        money = input("How much are you donating?: ").split()

def donationInfo():
    '''
    Function which does some analysis on user inputs for the donation function, and presents them. Ex. how much money donated.
    :return:
    '''
    print()
    try:
        f1 = open("donData", "r")
        values = [x[:-1] for x in f1.readlines()]
        unique_charities=[]
        total_money=0
        for row in values:
           if(not(row.split()[3] in unique_charities)):
                unique_charities.append(row.split()[3])
           total_money+=int(row.split()[0])

        print(len(values),"Donations logged.")
        print(len(unique_charities),"Unique charities donated too.")
        print(str(total_money)+"$"+" donated to charities.")
    except FileNotFoundError:
        print("Function not avaliable, please input values")

def intializeFiles():
    '''
    Function that intializes the files for data storage
    :return:
    '''
    f1 = open("FinData", "a+")
    f1 = open("spenData", "a+")
    f1 = open("donData", "a+")

def startProgram():
    '''
    Main function which controls user program flow.
    :return:
    '''
    intializeFiles()
    move = ""
    while(move != "s" and move != "S" and move!="stop" and move != "Stop"):
        print("-------------------------------------------------\nHey Welcome to your Personalised Finance Program!\n-------------------------------------------------\n")
        print("1 for Income Management\n2 for Spending Management\n3 for Finance Info\n4 for Donation Management\ns,S,stop,Stop to end program\n")
        move = input("Action: ")
        while(move != "1" and move !="2" and move!="3" and move != "s" and move != "S" and move!="stop" and move != "Stop"and move != "4"):
            move = input("Invalid Action - Action: ")
        if(move=="1"):
            finacialRep()
        elif(move=="2"):
            spendingRep()
        elif(move=="3"):
            financeInfo()
        elif(move=="4"):
            donationRep()

if __name__ == "__main__":
    startProgram()
