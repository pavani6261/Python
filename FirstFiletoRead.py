# open and append text to the file
def Fileopen(filename):
    # with open(filename, "a") as f1:    #open the file with name f1 and close the file after executing given lines in it
    #     f1.write("\nHi all\n")     #write() used to write the content into the file
    temp = open(filename)
    print(temp.read())  #read()- this function used to read the content in the file
    temp.close()
Fileopen('FirstFile.txt')

def FileCount(filename):
    temp = open(filename)  #open the file
    for i, l in enumerate(temp):
        pass
    return i+1
    temp.close()  #to close the file
print("number of lines in the file are:",FileCount('FirstFile.txt'))
