
import pandas as pd
import func as f

def load_data():
    path = r"/Users/oksana_kaledina/Documents/5_PORTFOLIO/KPMG/data.xlsx"
    df_transactions = pd.read_excel(path, sheet_name=1)
    df_new_cust_list = pd.read_excel(path, sheet_name=2,parse_dates=['DOB'], date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d'))
    df_demographic = pd.read_excel(path,sheet_name=3,parse_dates=['DOB'], date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d'))
    df_address = pd.read_excel(path, sheet_name=4)

    dff = [df_transactions,df_new_cust_list,df_demographic,df_address]
    dff = f.change_index(dff)
    return dff

    