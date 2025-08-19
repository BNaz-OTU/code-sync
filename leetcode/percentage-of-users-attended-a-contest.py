import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    df1 = register.groupby('contest_id').size().reset_index(name='percentage')
    df1['percentage'] = round(df1['percentage'] / len(users) * 100, 2)
    return df1.sort_values(by=['percentage', 'contest_id'], ascending=[False, True])