#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
#bhujun, 2021-Feb-14, Modified script to add inner data for dictionary, load existing data and delete an entry
#------------------------------------------#

# Declare variable

strChoice = '' # User input
lstTbl = []# list of dictionary to hold data
# TODO replace list of lists with list of dicts
dicRow1 = {'id':3, 'Artist':'Pink Floyd','Title':'ABC'}

lstTbl.append(dicRow1)

strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    elif strChoice == 'l':
        # TODO Add the functionality of loading existing data
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            rowlst = row.strip().split(',')
            dicRow1 = {'id':rowlst[0], 'Artist':rowlst[1], 'Title':rowlst[2]}
            lstTbl.append(dicRow1)

        objFile.close()
        print(lstTbl)
        
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow1 = {'id': intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow1)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(row['id'], row['Title'], row['Artist'], sep=', ')
        print()
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        strID = input('Enter an ID: ')
        intID = int(strID)
        for row in lstTbl:
            if row['id']==intID:
                lstTbl.remove(row)
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = "{},{},{}".format(row['id'], row['Title'], row['Artist']) + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Invalid command: ',strChoice)
        print('Please choose either l, a, i, d, s or x!')

