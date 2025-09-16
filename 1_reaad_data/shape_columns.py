
import pandas as pd

data={
    "Name" : ["Avi", "Ravi" , "Kavi" , "Ram" , "Shyam" , "Mala"],
    "Age" : [10,20,30,40,50,60],
    "Salary" : [2000,3000,4000,5000,6000,10000]
}

df=pd.DataFrame(data)
print(df)

# print shape of the Data Frame
print(f'Shapes : {df.shape}')

# print Column Name of th Data Frame
print(f'Column Name : {df.columns}')