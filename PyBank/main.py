#import modules
import os
import csv

#set path for csv file needed
bank_path=os.path.join('Resources','budget_data.csv')

#create list names to store the two columns of data
#b_date is for budget date (date column)
#b_amount is for budget amount (profit/loss column)
#change is for the profit/loss change calculation result
b_date=[]
b_amount=[]
change=[]


#open the CSV file
with open(bank_path,'r') as csvfile:
    bankdata = csv.reader(csvfile,delimiter=',')
    
    #store header rows
    header=next(bankdata)

    #define variable outside for loop to store previous row data for use in profit/loss change calculations
    last_change=0

    for row in bankdata:
        #add date to b_date list
        b_date.append(row[0])

        #save amount on current row for ease of use in multiple places below
        amount=int(row[1])
        #add profit/loss amount to b_amount list as integer instead of string
        b_amount.append(amount)
        
        #Calculate changes in profit/loss 
        #compare each month to the previous and store that number as the change for the 'current' month
        #example, for change in Aug, do Aug minus July
        change.append(amount-last_change)
        last_change=amount
    
    #rezip the lists into a dictionary so that later the months can be matched with the right values
    data_dict=dict(zip(b_date,change))
    print(data_dict)

    #Count the months in the dataset
    #number of months in the set should be equal to the number of non-header rows
    #count the non-header rows in the csv and store that number
    months=len(b_date)
    print(months)

    #Calculate net total amount of Profits/Losses over the entire period
    #sum entire profit/loss column using sum function
    total_profits=sum(b_amount)    
    print(total_profits)

    #Calculate average profit/loss in dataset
    average=sum(change[1:86])/(months-1)
    average=round(average,2)
    print(average)

    #find greatest increase in profits over entire period
    #return month and amount
    increase=max(change)
    print(increase)

    #create a variable to determine if we've found the right entry in the dictionary
    found=False

     

    #find greatest decrease in profits over entire period
    #return month and amount
    decrease=min(change)
    print(decrease)

    #print all results
    #write all results to a new file
