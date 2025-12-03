import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    return followers.groupby("user_id").size().reset_index(name="followers_count").sort_values(by="user_id")