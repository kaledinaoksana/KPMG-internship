import pandas as pd
import numpy as np
import lib.load as load
import data_cleaning as dc

df = load.load_data()
df_transactions = df[0]
df_new_cust_list = df[1]
df_demographic = df[2]
df_address = df[3]

try:
    df_demographic = dc.clean_demographic(df_demographic)
    df_address = dc.clean_address(df_address)
    df_transactions = dc.clean_transactions(df_transactions)
except Exception:
    print('This function has already used or you have ERROR.')

print(df_demographic)