#import modules
import csv
#path
budget_path = "C:/Users/Marc Roca/Documents/Python-Challenge/PyBank/Resources/budget_data.csv"
budget_analysis = "C:/Users/Marc Roca/Documents/Python-Challenge/PyBank/analysis/PyBank_analysis.txt"

with open (budget_analysis,'w') as bwrite: 
    #open file
    with open(budget_path,'r') as read:
        csv_reader = csv.reader(read,delimiter=",")
        csv_header = next(csv_reader)
        
        #Set up Variable 
        Total_number_months =0 
        Total_profit_losses_amount = 0
        Profit_Loss_list = []
        Date_list = []
        
        #open file
        for row in csv_reader:
            Total_number_months = Total_number_months + 1
            Total_profit_losses_amount = Total_profit_losses_amount + int(row[1])
            Profit_Loss_list.append(int(row[1]))
            Date_list.append((row[0]))
        
        Difference_list = []
        Number_of_iterations = len(Profit_Loss_list) -1
        for values in Profit_Loss_list:
            x = Profit_Loss_list.index(values)
            if x+1 <= Number_of_iterations:
                difference = Profit_Loss_list[x+1] - Profit_Loss_list[x]
                Difference_list.append(difference)
        
        Sum_difference = 0
        Max_difference = 0
        Min_difference = 0

        Combined_list= zip(Date_list, Difference_list)
        
        Max_difference_date = ""
        Min_difference_date = ""

        for row in Combined_list:
            Sum_difference = Sum_difference + row[1]
            if Max_difference < row[1]:
                Max_difference = row[1]
                Max_difference_date = Date_list[(Difference_list.index(row[1]))+1]

            if Min_difference > row[1]:
                Min_difference = row[1]
                Min_difference_date = Date_list[(Difference_list.index(row[1]))+1]

        
        Average_difference = round(Sum_difference / (len(Difference_list)),2)
        
        ##Output
        print(f'Financial Analysis')
        print("--------------------------------")
        print(f'Total Months: {Total_number_months}')
        print(f'Total: ${Total_profit_losses_amount}')
        print(f'Average Change: ${Average_difference}')
        print(f'Greatest Increase in Profits: {Max_difference_date} (${Max_difference})')
        print(f'Greatest Decrease in Profits: {Min_difference_date} (${Min_difference})')

    #Output
    bwrite.write(f'Financial Analysis\n')
    bwrite.write("--------------------------------\n")
    bwrite.write(f'Total Months: {Total_number_months}\n')
    bwrite.write(f'Total: ${Total_profit_losses_amount}\n')
    bwrite.write(f'Average Change: ${Average_difference}\n')
    bwrite.write(f'Greatest Increase in Profits: {Max_difference_date} (${Max_difference})\n')
    bwrite.write(f'Greatest Decrease in Profits: {Min_difference_date} (${Min_difference})\n')