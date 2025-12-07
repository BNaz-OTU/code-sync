import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    df = users.join(rides.set_index("user_id"), on="id", how="left", rsuffix="_o").fillna(0)
    df2 = df.groupby(["id", "name"])["distance"].sum().reset_index(name="travelled_distance")
    return df2.loc[:, ["name", "travelled_distance"]].sort_values(by=["travelled_distance", "name"], ascending=[False, True])