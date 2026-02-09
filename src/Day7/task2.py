import csv
with open("C:\\DS_AI_Internship\\src\\Day7\\Students.csv","r")as file:
    reader=csv.DictReader(file)
    
    print("Students who Passed:")
    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])
   