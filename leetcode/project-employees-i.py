import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = project.join(employee.set_index('employee_id'), on='employee_id', how='left')
    df1 = df.groupby('project_id')['experience_years'].mean().round(2).reset_index(name='average_years')
    return df1
    # return df1['average_years'] = df1['average_years'].round(2)