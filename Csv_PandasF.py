import pandas as pd  #importing pandas. pd=pandas here.
# Pandas is a popular data science library in Python for data manipulation and analysis.

# data = pd.read_csv("FirstCsvFile.csv")  #reading csv file with read_csv() of pandas and storing in data variable
# print(data)  #printing the data

## To write to a CSV file, we need to call the to_csv() function of a DataFrame
# df = pd.DataFrame([[1,'Rav',23],[2,'Esa',32],[3,'Dev',33]], columns=['sno','name','age'])
# df.to_csv('PdCsvFile.csv')  #writing data frame to csv file

# data1 = pd.read_csv('PdCsvFile.csv',index_col='sno')  # adding index value
# print(data1)

# df = pd.read_csv('PdCsvFile.csv',header=0,names=['Id','SName','Age']) #replacing heading with another names
# print(df)
##-------------------------
