import pandas as pd

def custom_round(value):
    if (value % 1 >= 0.5):
        return math.ceil(value)
    else:
        return math.floor(value)

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.join(employees.set_index("reports_to"), on="employee_id", how="inner", rsuffix="_o")
    df2 = df.groupby(["employee_id", "name"]).agg(
        reports_count = ("employee_id_o", "size"),
        average_age = ("age_o", "mean")
    ).reset_index()

    df2["average_age"] = df2["average_age"].apply(custom_round)

    return df2.sort_values("employee_id")