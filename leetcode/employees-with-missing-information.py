import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(employees, salaries, on='employee_id', how='outer')

    miss_data = merged_df[merged_df.isna().any(axis=1)]

    return miss_data[['employee_id']].sort_values('employee_id')