import pandas as pd

data={
    "Name" : ["Avi", "Ravi" , "Kavi" , "Ram" , "Shyam" , "Mala"],
    "Age" : [10,20,30,40,50,60],
    "Salary" : [2000,3000,4000,5000,6000,10000]
}

df=pd.DataFrame(data)

print("Sample Data Fram")
print(df)

# Describe method
print("Descriptive Statistics")
print(df.describe())
