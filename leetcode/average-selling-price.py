import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = prices.join(units_sold.set_index("product_id"), on="product_id", how="left")

    # Filter for products sold in the given purchase window
    df2 = df.loc[(df['start_date'] <= df['purchase_date']) & (df['purchase_date'] <= df['end_date'])]
    
    # Calculations to get average price
    df2["curr_price"] = df2["price"] * df2["units"]
    df3 = df2.groupby("product_id").agg(
        total_units = ("units", "sum"),
        total_price = ("curr_price", "sum")
    ).reset_index()
    df3["average_price"] = round(df3["total_price"] / df3["total_units"], 2)

    # This step ensures that if there was a product that sold no units, we would set its values to be "0"
    final_df = prices.join(df3.set_index("product_id"), on="product_id", how="left").fillna(0)

    # Removes duplicates because did a "Left Join" on the previous step that would lead to duplications
    return final_df[["product_id", "average_price"]].drop_duplicates()