import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = product.join(sales.set_index("product_id"), on="product_id", how="inner")
    df2 = df.groupby(["product_id", "product_name"]).agg(
        min_date = ("sale_date", "min"),
        max_date = ("sale_date", "max")
    ).reset_index()

    b_qtr = pd.Timestamp(2019, 1, 1)
    e_qtr = pd.Timestamp(2019, 3, 31)

    return df2.loc[(b_qtr <= df2["min_date"]) & (df2["max_date"] <= e_qtr), ["product_id", "product_name"]]