import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = visits.join(transactions.set_index('visit_id'), on='visit_id', how='left')
    no_visit_df = df.loc[df['transaction_id'].isnull()]
    return no_visit_df.groupby('customer_id')['transaction_id'].size().reset_index(name="count_no_trans")