# snbank
The code is for a basic banking system
Login details for staff are stored in the 'staff.txt' file.
Username - Ayodamope/Tolu
Password - ayodee/toolzbae
Enter username and password for Staff login on initial page of the banking system.
Once logged in, select preference of options with the numbers 1-3
The cose stores the session for the staff ID logged in at the moment in a file: 'session.txt' that is created when staff logs in succeessfully. If staff should logout, session is deleted and 'session.txt' file is deleted.
After login, staff is presented with following options as landing page: 
1 Create new bank account
2 Check Account Details
3 Logout
If staff selects Create bank account, input is requested for the following:
- Account name
- Opening Balance
- Account Type
- Account email
The details are saved in the 'customer.txt file', 10 digit Account number is generated and displayed to user.
User is prompted to decide whether to view account details or not (Y/N).
If staff selects Check Account Details from landing page, the program requests for account number that was created.
The code fetches the details of the account from the 'customer.txt' file and displays it to the staff, then presents back the landing page.
