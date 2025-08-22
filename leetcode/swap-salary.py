import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    
    swap = lambda x: 'm' if x == 'f' else 'f'
    salary['sex'] = salary.sex.apply(swap)

    return salary