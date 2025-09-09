
import pandas as pd

# read data from CSV fil into a dataframe

# df=pd.read_csv(r"D:\D\ML-DL-AI\Pandas\1_reaad_data\sales_data_sample.csv" , encoding="latin1")


# df = pd.read_excel(r"D:\D\ML-DL-AI\Pandas\1_reaad_data\SampleSuperstore.xlsx")

df = pd.read_json(r"D:\D\ML-DL-AI\Pandas\1_reaad_data\sample_Data.json")
print(df)