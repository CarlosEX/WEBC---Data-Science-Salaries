import pandas as pd

def transform_dataframe(df) -> pd.DataFrame:
    df = df.drop('id',axis=1)

    df.rename(columns={'work_year': 'Work year', 'experience_level': 'Experience level', 'employment_type': 'Employment type', 'job_title': 'Job title', 'salary_in_usd': 'Salary usd', 'employee_residence': 'Employee residence', 'remote_ratio': 'Remote ratio', 'company_location': 'Company location', 'company_size': 'Company size'}, inplace=True)

    df.replace({'Employment type': {
        'FT': 'Full Time',
        'PT': 'Part Time',
        'CT': 'Contract',
        'FL': 'Freelance'
    }}, inplace=True)

    df.replace({'Company size': {
        'L': 'Large',
        'S': 'Small',
        'M': 'Medium'
    }}, inplace=True)

    df.replace({'Experience level': {
        'MI': 'Mid-level',
        'SE': 'Senior',
        'EN': 'Entry Level',
        'EX': 'Experienced'
    }}, inplace=True)
    
    return df
