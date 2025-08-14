import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    dp1 = employee.groupby('employee_id').size().reset_index(name='count')
    dp1 = employee.join(dp1.set_index('employee_id'), on='employee_id', how='inner')
    dp1 = dp1.loc[dp1['count'] == 1, ['employee_id', 'department_id']]
    
    flagged = employee.loc[employee['primary_flag'] == 'Y', ['employee_id', 'department_id']]

    return pd.concat([dp1, flagged])