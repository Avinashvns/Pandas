import pandas as pd

df=pd.read_json(r"D:\D\ML-DL-AI\Pandas\1_reaad_data\sample_Data.json")

print("Display the info of Dataset")
print(df.info())