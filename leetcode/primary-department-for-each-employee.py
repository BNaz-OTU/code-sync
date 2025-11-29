import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    # Has multiple departments
    df1 = employee.loc[employee["primary_flag"] == "Y", ["employee_id", "department_id"]]
    
    # Only work 1 department
    df2 = employee.groupby("employee_id").size().reset_index(name="count")
    df3 = employee.join(df2.set_index("employee_id"), on="employee_id", how="inner")
    df4 = df3.loc[df3["count"] == 1, ["employee_id", "department_id"]]

    return pd.concat([df1, df4])