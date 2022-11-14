#------------------------------------------#
# Title: CDInventory.py
# Desc: Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# fabiosacca, 2022-Nov-13, Modified script to use dictionaries
#------------------------------------------#

# Declare variables
strChoice = '' # User input
lstTbl = []  # list of dicts to hold data
lstRow = []  # list of data row
dicRow = {}  # dictionary
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    # @fabiosacca: Capitalized each row for consistency
    print('\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory') 
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit')
    print()
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input

    if strChoice == 'x':
        # 1. Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        # @fabiosacca: Added functionality and Structured Error Handling in case there is no file to load
        # 2. Load existing data
        try: 
            lstTbl = []
            objFile = open(strFileName, 'r')
            for row in objFile:
                lstRow = row.strip().split(',')
                lstRow[0] = int(lstRow[0]) # converted ID to integer
                dicRow = {'id': lstRow[0], 'Title': lstRow[1], 'Artist': lstRow[2]}
                lstTbl.append(dicRow)
            objFile.close()
        except: 
            print('\nAn error occurred. No Inventory file found. \n')

    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 3. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        lstRow = [intID, strTitle, strArtist]
        dicRow = {'id': lstRow[0], 'Title': lstRow[1], 'Artist': lstRow[2]}
        lstTbl.append(dicRow)
        # @fabiosacca: corrected starter script to ensure row is a dictionary
        
    elif strChoice == 'i':
        # 4. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
            # @fabiosacca: corrected to print only the values from dictionary
            
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        # @fabiosacca: added functionality. Need to add error handling logic (invalid entries, entry not in table) 
        # 5. Delete an entry from current data
        delRow = int(input('Enter the ID you want to delete: '))
        for row in lstTbl:
                for value in row.values():
                    if value == delRow:
                        lstTbl.remove(row)
                    
    elif strChoice == 's':
        # 6. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for value in row.values():
                strRow += str(value) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        
    else:
        print('Please choose either l, a, i, d, s or x!\n') # @fabiosacca: Added \n to improve formatting

