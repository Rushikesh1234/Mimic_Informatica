from src.utils.log import log_info, log_error
import pandas as pd


Transformations = {}

def register(name):
    def decorator(fn):
        Transformations[name] = fn
        return fn
    return decorator


@register("Filter Rows")
def filter_rows(df, * expression: str):
    return df.query(expression)

@register("Derived Column")
def derived_column(df, *, new_column: str, expression:str):
    df[new_column] = df.eval(expression)
    return df

@register("Aggregator")
def aggregator(df, *, group_by: list, aggregation: dict):
    return df.groupby(group_by, as_index=False).agg(aggregation)

@register("Sort Rows")
def sort_rows(df, *, by: list, ascending: bool = True):
    return df.sort_values(by=by, ascending=ascending)

@register("Sequence Generator")
def seq_generator(df, *, column_name: str = "sequence", start: int = 1):
    df[column_name] = range(start, start + len(df))
    return df

@register("Join with Lookup Table")
def join_with_lookup(df, *, lookup_data: pd.DataFrame, on:str, how: str ="left"):
    return df.merge(lookup_data, on=on, how=how)

@register("Drop Null values")
def drop_nulls(df, *, columns: list=None):
    return df.dropna(subset=columns) if columns else df.dropna()

@register("Fill Nulls")
def fill_nulls(df, *, fill_value: dict):
    return df.fillna(fill_value)

@register("String Operations")
def string_ops(df, *, column: str, operation: str):
    df[column] = getattr(df[column].str, operation)()
    return df

@register("Date Operation")
def date_ops(df, *, column: str, extract:str):
    col = pd.to_datetime(df[column])
    if extract == "year":
        df[column + "_year"] = col.dt.year
    elif extract == "month":
        df[column + "_month"] = col.dt.month
    elif extract == "day":
        df[column + "_day"] = col.dt.day
    elif extract == "weekday":
        df[column + "_weekday"] = col.dt.weekday
    return df

@register("Normalize Column")
def normalize_column(df, *, column: str):
    min_val = df[column].min()
    max_val = df[column].max()
    df[column + "_normalized"] = (df[column] - min_val) / (max_val - min_val)
    return df

@register("Standardize Column")
def standardize_column(df, *, column: str):
    df[column + "_standardize"] = (df[column] - df[column].mean()) / df[column].std()
    return df


'''
def clean_data(df):
    """Perform Data Cleaning"""
    try:
        df.columns = df.columns.str.strip()
        log_info(f"Data cleaned: whitespaces removed from column names")

        df.columns = df.columns.str.lower()
        log_info(f"Data cleaned: Convert column values to lower case")

        df.fillna(0, inplace=True)
        log_info(f"Data cleaned: Fill empty columns values with 0")

        return df
    except Exception as e:
        log_error(f"Error cleaning data: {e}")
        return None
    
def normalize_column(df, column):
    """Normalize column min-max scaling"""
    try:
        if column in df.columns:
            min_val = df[column].min()
            max_val = df[column].max()

            df[column + '_normalized'] = (df[column] - min_val) / (max_val - min_val)
            log_info(f"Data normalize with min-max scaling for columns")
        return df
    except Exception as e:
        log_error(f"Error cleaning data: {e}")
        return None

def remove_outliers(df, column, threshold=3):
    """Remove rows where column has outliers based on z-score"""
    try:
        if column in df.columns:
            mean = df[column].mean()
            std = df[column].std()

            df = df[(df[column] - mean).abs() / std < threshold]
            log_info(f"Remove outliers for Data columns")
        return df
    except Exception as e:
        log_error(f"Error cleaning data: {e}")
        return None

def standardize_column(df, column):
    """Standardize column using z-score"""
    try:
        if column in df.columns:
            df[column + '_zscore'] = (df[column] - df[column].mean()) / df[column].std()
            log_info(f"Data standardize for column")
        return df
    except Exception as e:
        log_error(f"Error cleaning data: {e}")
        return None
'''