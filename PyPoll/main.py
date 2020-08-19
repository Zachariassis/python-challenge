import os
import csv

csvpath=os.path.join('election_data.csv')
Candidates=["empty"]
Results=[10]
Percent=[]
num=0

with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        num=num+1
        test=row[2] in Candidates
        if test == True:
            Results[Candidates.index(row[2])]=Results[Candidates.index(row[2])]+1
        else:
            Candidates.append(row[2])
            Results.append(1)
            if "empty" in Candidates:
                Candidates.remove("empty")
                Results.remove(10)

max=0
for i in range(len(Candidates)):
    Percent.append(0)
    Percent[i]="{:.3%}".format(Results[i]/num)
    if Results[i]>max:
        max=Results[i]
        Winner=Candidates[i]

print("Election Results")
print("---------------------")
print(f"Total Votes: {num}")
print("---------------------")
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {Percent[i]} {Results[i]}")
print("---------------------")
print(f"Winner: {Winner}")
print("---------------------")

output_path = os.path.join('Election_Results.txt')

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['Total Votes', num])
    for i in range(len(Candidates)):
        csvwriter.writerow([Candidates[i],Percent[i],Results[i]])
    csvwriter.writerow(['Winner',Winner])