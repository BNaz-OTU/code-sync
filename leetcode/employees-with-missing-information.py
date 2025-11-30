import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    # Get NULL values to show in DataFrame's
    df_names = employees.join(salaries.set_index("employee_id"), on="employee_id", how="left")
    df_salary = employees.join(salaries.set_index("employee_id"), on="employee_id", how="right")

    # Combine the tables together
    df_final = pd.concat([df_names, df_salary])

    # Filter for the specific tables
    return df_final.loc[
        (df_final["name"].isnull()) | (df_final["salary"].isnull()), ['employee_id']
    ].sort_values(by="employee_id")