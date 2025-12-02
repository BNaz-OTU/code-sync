import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    df = users.join(rides.set_index("user_id"), on="id", how="left", lsuffix="_c", rsuffix="_o")
    df.fillna(0, inplace=True)
    df2 = df.groupby(["id_c", "name"])["distance"].sum().reset_index(name="travelled_distance")
    return df2.loc[:, 
        ["name", "travelled_distance"]
    ].sort_values(by=["travelled_distance", "name"], ascending=[False, True])