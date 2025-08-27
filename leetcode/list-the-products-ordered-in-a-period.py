import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = products.join(orders.set_index('product_id'), on='product_id', how='inner')
    df1 = df.loc[(df['order_date'] >= '2020-02-01') & (df['order_date'] <= '2020-02-29')]
    df2 = df1.groupby(['product_id', 'product_name'])['unit'].sum().reset_index()
    return df2.loc[df2['unit'] >= 100, ['product_name', 'unit']]