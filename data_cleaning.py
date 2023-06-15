import pandas as pd
    
def clean_demographic(df):
    # drop columns
    df = df.drop(columns="default")
    # DOB
    df = df.rename(columns={"DOB": "date_of_birth"})
    # 'gender'
    df['gender'] = df['gender'].str.replace('Female','F')
    df['gender'] = df['gender'].str.replace('Femal','F')
    df['gender'] = df['gender'].str.replace('Male','M')
    df['gender'] = df['gender'].str.replace('F','Female')
    df['gender'] = df['gender'].str.replace('M','Male')
    # 'deceased_indicator'
    df['deceased_indicator'] = df['deceased_indicator'].str.replace('N','No')
    df['deceased_indicator'] = df['deceased_indicator'].str.replace('Y','Yes')
    return df

def clean_address(df):
    df['state'] = df['state'].str.replace('Victoria','VIC')
    df['state'] = df['state'].str.replace('New South Wales','NSW')
    return df

def clean_transactions(df):
    #delete rows with null (555 rows)
    df = df.dropna()
    return df




