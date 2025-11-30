import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby("customer_number").size().reset_index(name="count").sort_values(by="count", ascending=False)
    # df.loc[]
    return df.loc[:, ["customer_number"]].head(1)