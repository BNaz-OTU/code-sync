import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = product.join(sales.set_index('product_id'), on='product_id', how='inner')
    return df.loc[:, ['product_name', 'year', 'price']]