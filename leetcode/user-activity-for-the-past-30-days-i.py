import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby('activity_date')['user_id'].nunique().reset_index()
    return df.loc[
        (df['activity_date'] <= '2019-07-27') & 
        (df['activity_date'] >= '2019-06-28'), 
        ['activity_date', 'user_id']].rename(columns={'activity_date' : 'day', 'user_id' : 'active_users'})