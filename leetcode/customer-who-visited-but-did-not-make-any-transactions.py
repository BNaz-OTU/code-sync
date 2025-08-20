import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df1 = visits.join(transactions.set_index('visit_id'), on='visit_id', how='left')
    df2 = df1.loc[df1['transaction_id'].isnull(), ['customer_id', 'transaction_id']]
    return df2.groupby('customer_id').size().reset_index(name='count_no_trans')