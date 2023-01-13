# Opens and closes a file automatically
# BEST PRACTICE--------

with open("FileOperations/test.txt","r") as file1:
    file1_Data = file1.read()
    print(file1_Data)