import pandas as pd
from sqlalchemy import create_engine
import pymysql 

#Load the cleaned CSV file

csv_file = "cleaned_crypto_data.csv"
df = pd.read_csv(csv_file)
print(f"Loaded {len(df)} rows from {csv_file}")

#Define your MySQL Server connection details

user = 'root'
password = 'bd1998'
host = 'localhost'              # or your MySQL server IP/hostname
port = 3306                     # default MySQL port
database = 'crypto_analysis'

# #Create the connection string

# connection_string = urllib.parse.quote_plus(
#     f"DRIVER={{ODBC Driver 17 for SQL Server}};"
#     f"SERVER={server};"
#     f"DATABASE={database};"
#     f"UID={username};"
#     f"PWD={password}"
# )

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

#Load data into SQL Server table
try:
    df.to_sql('crypto_data', con=engine, if_exists='append', index=False)
    print("Data loaded successfully into MySQL table 'crypto_data'")
except Exception as e:
    print(f"Error loading data: {e}")