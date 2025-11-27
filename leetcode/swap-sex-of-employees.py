import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    swap = lambda x: "f" if x == "m" else "m"
    salary["sex"] = salary.sex.apply(swap)
    return salary