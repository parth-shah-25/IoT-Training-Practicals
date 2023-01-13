import os

s = "This is a String\n"
with open("FileOperations/Test2.txt","w") as file2:
    # file2.write(s)
    # file2.write("\n")
    # data = file2.read(1)
    file2.writelines("Line 1 \nLine 2\n")
    ans = file2.writable()

    # Get Current working Directory----------------
    print(os.getcwd())
    
    # Lists all sub directories
    print(os.listdir())
    print(ans)
