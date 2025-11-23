import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class').size().reset_index(name='class_size')
    return df.loc[df['class_size'] >= 5, ['class']]