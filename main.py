import pandas as pd
import numpy as np
import lib.load as load
import data_cleaning as dc

# MERGE
def merge_df(d_d,d_t,d_a):
    # address + demographic
    df = d_d.merge(d_a, how = 'outer', on = 'customer_id') 
    df = df.loc[df['first_name'].notnull()].reset_index().drop(columns=['index']) 
    # address + demographic + transactions
    df = df.merge(d_t, how = 'outer', on = 'customer_id') 
    # CLEANING MERGED DF
    df = df.drop(df[df['transaction_id'].isnull()].index)
    # df = df.drop(df[df['first_name'].isnull()].index)
    # df = df.drop(df[df['address'].isnull()].index)
    # df = df.drop(df[df['DOB'].isnull()].index)
    return df

def revenue(df):
    return (df['list_price'].sum()-df['standard_cost'].sum())
    
def percentage(x,y):
    return 100*(x-y)/x


df = load.load_data()
df_transactions = df[0]
df_new_cust_list = df[1]
df_demographic = df[2]
df_address = df[3]


try:
    df_demographic = dc.clean_demographic(df_demographic).reset_index(drop=True)
    df_address = dc.clean_address(df_address).reset_index(drop=True)
    df_transactions = dc.clean_transactions(df_transactions).reset_index(drop=True)
except Exception:
    print('ERROR.')

dff = merge_df(df_demographic,df_transactions,df_address)

per_revenue = percentage(revenue(df[0]),revenue(dff))
per_len = percentage(len(df[0]), len(dff))

print('% revenue = ',per_revenue.round(2),', % len = ',per_len)
