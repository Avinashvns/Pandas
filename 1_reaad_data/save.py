
import pandas as pd

data={
    "Name" : ["Avinash","Shyam","Ram"],
    "Age" : [10,20,30],
    "City": ["Nagpur", "Varanasi","Ayodhya"]

}

# Creating a new Data Frame
df=pd.DataFrame(data)
print(df)

# df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx" , index=False)