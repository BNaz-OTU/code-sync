import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    total_df = employees.groupby(['emp_id', 'event_day']).agg(
        total_in = ('in_time', 'sum'),
        total_out = ('out_time', 'sum')
    ).reset_index()

    total_df['total_time'] = total_df['total_out'] - total_df['total_in']

    return total_df.loc[:, ['event_day', 'emp_id', 'total_time']].rename(columns={'event_day' : 'day'})