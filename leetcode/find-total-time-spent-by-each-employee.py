import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.groupby(["emp_id", "event_day"]).agg(
        total_in_time = ('in_time', 'sum'),
        total_out_time = ('out_time', 'sum')
    ).reset_index()

    df['total_time'] = df['total_out_time'] - df['total_in_time']

    return df[['event_day', 'emp_id', 'total_time']].rename(columns={'event_day' : 'day'})