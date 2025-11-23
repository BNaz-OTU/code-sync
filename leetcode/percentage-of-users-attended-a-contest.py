import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    total_contestants = users['user_id'].count()

    df = register.groupby('contest_id')['user_id'].size().reset_index(name="participants")
    df['percentage'] = round((df['participants'] / total_contestants) * 100, 2)
    return df.loc[:, 
        ["contest_id", "percentage"]
    ].sort_values(by=["percentage", "contest_id"], ascending=[False, True])