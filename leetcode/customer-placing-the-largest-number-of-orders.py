import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby('customer_number').size().reset_index(name='count')
    df1 = df.sort_values('count', ascending=False)
    return df1.loc[:, ['customer_number']].head(1)