import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    df = followers.groupby('user_id')['follower_id'].size().reset_index()
    df1 = df.rename(columns={'follower_id' : 'followers_count'})
    return df1.sort_values('user_id')