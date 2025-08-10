import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    df = users.join(rides.set_index('user_id'), on='id', how='left', lsuffix='_c')
    df2 = df.groupby('id_c')['distance'].sum().reset_index(name='travelled_distance')
    df3 = df2.join(users.set_index('id'), on='id_c')
    return df3[['name', 'travelled_distance']].sort_values(by=['travelled_distance', 'name'], ascending=[False, True])