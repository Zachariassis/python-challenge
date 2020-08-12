import os
import csv

csvpath=os.path.join('C:/Users/Zacha/Documents','python-challenge','PyBank','budget_data.csv')
#print(csvpath)
sum=0
nummonths=0
greatest_increase=0
greatest_decrease=0

with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        nummonths=nummonths+1

        if int(row[1])>greatest_increase:
            greatest_increase=int(row[1])
            greatest_increase_year=row[0]
        if int(row[1])<greatest_decrease:
            greatest_decrease=int(row[1])
            greatest_decrease_year=row[0]
        
        if nummonths ==1:
            diff_val=0
        else:
            diff=int(row[1])-old_val
            diff_val=diff_val+diff
        
        old_val=int(row[1])
        sum=sum+int(row[1])
        #print(row)
        #print(type(row))

diff_avg=round(diff_val/nummonths)

print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {nummonths}")
print(f"Total: ${sum}")
print(f"Average Change: ${diff_avg}")
print(f"Greatest Increase in Profits: {greatest_increase_year} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_year} (${greatest_decrease})")

output_path = os.path.join('C:/Users/Zacha/Documents','python-challenge','PyBank','totals_output.csv')

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['Total Months',nummonths])
    csvwriter.writerow(['Total','$'+str(sum)])
    csvwriter.writerow(['Average Change', '$'+str(diff_avg)])
    csvwriter.writerow(['Greatest Increase in Profits',greatest_increase_year,'$'+str(greatest_increase)])
    csvwriter.writerow(['Greatest Increase in Profits',greatest_decrease_year,'$'+str(greatest_decrease)])