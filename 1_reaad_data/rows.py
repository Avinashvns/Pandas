
import pandas as pd

df=pd.read_json(r"D:\D\ML-DL-AI\Pandas\1_reaad_data\sample_Data.json")

print("Display 5 rows of First")
print(df.head(5))

print("Display 5 rpws of Last")
print(df.tail(5))