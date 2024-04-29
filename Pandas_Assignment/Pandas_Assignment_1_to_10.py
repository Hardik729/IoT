import pandas as pd
import numpy as np

#Q.1
df1 = pd.DataFrame([1,2,3,4,5],columns=["No.s"],index=["n1","n2","n3","n4","n5"])
print(df1)

#Q.2
df2 = pd.Series([1,2,3,4,5])
print(df2.tolist())

#Q.3
df3 = pd.Series([1,2,3,4,5])
df4 = pd.Series([6,7,8,9,10])
print(f"Add:-")
print(df4+df3)
print(f"Subtract:-")
print(df4-df3)
print(f"Multiply:-")
print(df4*df3)
print(f"Divide:-")
print(df4/df3)

#Q.4
data1 = {"Name": ["Hardik","Parimal","Sandesh","Pranav"]}
s1 = pd.Series(data1)
print(s1)

#Q.5
data2 = np.array([1,2,3,4,5])
s2 = pd.Series(data2,index=["n1","n2","n3","n4","n5"])
print(s2)

#Q.6
data3 = pd.Series([1,2,3,4,5])
print(list(data3))

#Q.7
data4 = pd.Series([1,2,3,4,5])
print(data4.to_numpy())

#Q.8
data5 = {"Name": ["Hardik","Sandesh","Parimal","Pranav"], "Age": [25,24,24,23]}
df2 = pd.DataFrame(data5,index=[1,2,3,4])
print(df2)

#Q.9
n1 = [1,2,3,4,5,6,7,8,9,10]
n2 = ["Vishal","Sumit","Mayur","Swapnil","Arun","Chirag","Hemanshu","Radhika","Ashish","Hitul"]
s1 = pd.Series(n1,name="emp_id")
s2 = pd.Series(n2,name="names")
df3 = pd.concat([s1,s2],axis=1)
print(df3)
print("")
print(df3.head(5))
print("")
print(df3.tail(5))
print("")
print(df3.head(2))
print("")
print(df3.tail(2))
print("")
print(f"Name of the 5th employpee: {df3.iloc[4]['names']}")
print("")
print("Record of the 4th employpee:")
print(df3.iloc[3])

df3.to_csv('MyRecord.csv')

#Q.10
df4 = pd.read_csv('MyRecord.csv')
df4['Salary'] = [25000,35000,31000,85000,36000,63000,52000,50000,91000,40000]
df4.to_csv('MyRecord.csv')
