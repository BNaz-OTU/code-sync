import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.join(employee.set_index('id'), on='managerId', how='inner', lsuffix="_emp", rsuffix="_mgr")
    return df.loc[(df['salary_emp'] > df['salary_mgr']), ['name_emp']].rename(columns={'name_emp' : 'Employee'})