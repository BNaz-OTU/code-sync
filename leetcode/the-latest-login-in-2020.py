import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    df = logins.loc[(logins['time_stamp'] >= '2020-01-01 00:00:00') & (logins['time_stamp'] <= '2020-12-31 23:59:59')]

    return df.groupby('user_id')['time_stamp'].max().reset_index(name='last_stamp')