import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = users.join(transactions.set_index('account'), on='account', how='left')
    df2 = df.groupby(['account', 'name'])['amount'].sum().reset_index()
    return df2.loc[df2['amount'] > 10000, ['name', 'amount']].rename(columns={
        'name' : 'NAME', 
        'amount' : 'BALANCE'
    })