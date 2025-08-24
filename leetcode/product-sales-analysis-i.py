import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    d1 = sales.join(product.set_index('product_id'), on='product_id')
    return d1.loc[:, ['product_name', 'year', 'price']]