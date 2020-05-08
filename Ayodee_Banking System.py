print ('''*******************************************************************************
                    Python User Data Validation
                    AYO OMOLADE
                    Slack username : Ayodee
                    Email Address : omoladee11@gmail.com
******************************************************************************''')

import random
import os
from datetime import datetime

with open('staff.txt','r') as staff:
    data = staff.read().splitlines()
 
session = 'sessions.txt'

def saveInfo(session, Username, Password, Date):
    with open(session, 'w', encoding='utf-8') as f:
        f.write('{}\n'.format(Username))
        f.write('{}\n'.format(Password))
        f.write('{}\n'.format(Date))

def loadInfo(session):
    with open(session, 'r', encoding='utf-8') as f:
        Username = f.readline().rstrip()
        Password = f.readline()
    return Username, Password

Login = True
while Login:

    #Get User Option
    print("\n=====================================")
    print("    ----Welcome to My Bank----       ")
    print("*************************************")
    print("=<<        1. Staff Login         >>=")
    print("=<<        2. Close App           >>=")
    print("*************************************")
    
    UserChoice = input("\nSelect your option from the menu above (1/2) : ")
    if UserChoice == "1":
        Username = str(input("Enter your Username : "))
        Password = str(input("Enter your Password : "))
        if Username and Password in data:
            print("*************************************")
            print("           Login Successful          ")
            print("*************************************")
            Date = str(datetime.now())
            saveInfo(session, Username, Password, Date)
            
            New = True
            while New:
                print("\n=====================================")
                print("        ----Staff Homepage----       ")
                print("*************************************")
                print("=<<  1. Create new bank account   >>=")
                print("=<<  2. Check Account Details     >>=")
                print("=<<           3. Logout           >>=")
                print("*************************************")

                
            
                StaffChoice = input("\nSelect your option from the menu above (1 - 3) : ")
                if StaffChoice == "1":
                    AC_name = str(input("1. Account name : "))
                    O_Bal = float(input("2. Opening Balance : "))
                    AC_type = str(input("3. Account Type : "))
                    AC_email = str(input("4. Account email : "))
                    AC_number = random.randrange(1101110000, 1101120000)
                    print("\n*******Account Successfully Created*********")
                    print("\nYour Account Number is : ", AC_number)
                    
                    customer_text=open('customer.txt', "w+")
                    customer_text.write("Account Name: %s \n" % AC_name )
                    customer_text.write("Opening Balance: %s \n" % O_Bal)
                    customer_text.write("Account Type: %s \n" % AC_type)
                    customer_text.write("Account Email: %s \n" % AC_email)
                    customer_text.close()
                    

                    while True:
                        Print = str(input("\nWould you like to view you Account details? If Yes(Y) if No(N) : "))
                        if Print.lower() == "y":
                            print("\nAccount name ---------- ",AC_name)
                            print("Opening Balance ------- ",'{:,.2f}'.format(O_Bal))
                            print("Account Type ---------- ",AC_type)
                            print("Account email --------- ",AC_email)
                            break
                        elif Print.lower() == "n":
                            break
                            New = True

                elif StaffChoice == "2":
                    AC_No = int(input("\nPlease enter Account number : "))
                    if AC_No == AC_number:
                        Cust = open('customer.txt','r')
                        print(Cust.read())
                        Cust.close()
                elif StaffChoice =="3":
                    os.remove('sessions.txt')
                    New = False
                    Login = True               
                 
        else:
            print("Invalid login!! Please Try again.")

    elif UserChoice == "2":
        print("\n=====================================")
        print(" ---Thank you for banking with us--- ")
        print("*************************************")
        Login = False

