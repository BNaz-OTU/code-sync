import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.join(employee.set_index('id'), on='managerId', how='left', lsuffix='_c')
    return df.loc[df['salary_c'] > df['salary'], ['name_c']].rename(columns={'name_c' : 'Employee'})