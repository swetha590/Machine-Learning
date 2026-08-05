import pandas as pd
col_list=["id","first","last","gender","Marks","selected"]
df = pd.read_csv("sample.csv",usecols=col_list)
print(df)

mean1 = df['Marks'].mean()
sum1 = df['Marks'].sum()
max1 = df['Marks'].max()
min1 = df['Marks'].min()
count1 = df['Marks'].count()
median1 = df['Marks'].median()
sd1 = df['Marks'].std()
var1 = df['Marks'].var() 

print('Mean Marks\n' + str(mean1))
print('Sum of the Marks\n' + str(sum1))
print('Maximum of the marks\n' + str(max1))
print('Minimum of the marks\n' + str(min1))
print('Count of the marks\n' + str(count1))
print('Standard deviation of the marks\n' + str(sd1))
print('Variance of the marks\n' + str(var1))
print('End of Summary \n\n\n')
