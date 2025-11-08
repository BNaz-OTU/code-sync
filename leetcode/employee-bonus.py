import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df = employee.join(bonus.set_index('empId'), on='empId', how='left')
    return df.loc[(df['bonus'].isnull()) | (df['bonus'] < 1000), ['name', 'bonus']]