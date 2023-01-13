import csv

file = open('FileOperations/Info.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Name','Salary'])

count = int(input("Enter the count: \n"))

with open('FileOperations/Info.csv', 'a') as file:
    

    for i in range(1,count+1):

        col1 = input("Data {} Column 1: ".format(i))
        col2 = input("Data {} Column 2: ".format(i))
        writer.writerow([col1,col2])
