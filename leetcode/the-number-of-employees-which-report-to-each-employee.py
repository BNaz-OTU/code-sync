import pandas as pd

def round2(num):
    if (num % 1 >= 0.5):
        return math.ceil(num)
    else:
        return math.floor(num)

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.join(employees.set_index("employee_id"), on="reports_to", how="inner", rsuffix="_o")
    df2 = df.groupby(["reports_to", "name_o"]).agg(
        reports_count = ("employee_id", "size"),
        average_age = ("age", "mean")
    ).reset_index()

    df2["average_age"] = df2["average_age"].apply(round2)

    return df2.rename(columns={"reports_to" : "employee_id", "name_o" : "name"}).sort_values("employee_id")