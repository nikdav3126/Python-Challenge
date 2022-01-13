import os
import csv

csv_path = os.path.join('Resources','budget_data.csv')
csv_path2 = os.path.join('Resources','election_data.csv')

#Create List to store data
DateList = []
ProfitList = []
CandidateList = []

#set variable types 
Month = 0
Votes = 0

#Open and read CSV
with open(csv_path) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        Date = str(row[0])
        Profits = int(row[1])

        #Find total number of inputs
        Month = Month + 1
        DateList.append (row[0])

        #Find total profit 
        ProfitList.append (row[1])
        TotalProfits = Profits + 0

        #Find Average
        FinancialAverage = TotalProfits / Month
        FinalAverage = round(FinancialAverage, 2)

        #Find greatest profit
        MaxProfit = max(ProfitList)
        MinProfit = min(ProfitList)

            # Print out the Financial Analysis
    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months:  {str(Month)}")
    print(f"Total Profits: ${str(TotalProfits)}")
    print(f"Average Change: ${FinalAverage}")
    print(f"Greatest Increase in Profits: ${MaxProfit}")
    print(f"Greatest Decrease in Profits: ${MinProfit}")

output_file = os.path.join("FinancialAnalysis.csv")