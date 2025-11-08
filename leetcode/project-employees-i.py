import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = project.join(employee.set_index('employee_id'), on='employee_id', how='inner')
    df2 = df.groupby('project_id')['experience_years'].mean().round(2).reset_index()
    return df2.rename(columns={'experience_years' : 'average_years'})