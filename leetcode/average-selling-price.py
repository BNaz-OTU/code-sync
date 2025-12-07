import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = prices.join(units_sold.set_index("product_id"), on="product_id", how="inner")
    df2 = df.loc[(df["start_date"] <= df["purchase_date"]) & (df["purchase_date"] <= df["end_date"])]
    df2["revenue"] = df2["price"] * df2["units"]
    df3 = df2.groupby("product_id").agg(
        total_units = ("units", "sum"),
        total_revenue = ("revenue", "sum")
    ).reset_index()

    df3["average_price"] = round(df3["total_revenue"] / df3["total_units"], 2)

    df4 = prices.join(df3.set_index("product_id"), on="product_id", how="left").fillna(0)
    return df4[["product_id", "average_price"]].drop_duplicates()