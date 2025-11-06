import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    df1 = employees.join(salaries.set_index('employee_id'), on='employee_id', how='left')
    df2 = employees.join(salaries.set_index('employee_id'), on='employee_id', how='right')
    combine = [df1, df2]
    update_df = pd.concat(combine)
    return update_df.loc[
        (update_df['name'].isnull() | update_df['salary'].isnull()), ['employee_id']
        ].sort_values('employee_id')