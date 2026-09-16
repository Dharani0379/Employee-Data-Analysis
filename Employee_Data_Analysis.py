import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# EMPLOYEE DATA ANALYSIS
# ============================================================

# ============================================================
# 1. LOAD DATASET
# ============================================================

file_path = r"C:\Users\DHARANIDHARAN\Downloads\Employee_Data_Analysis\employee_pay_equity_messy.csv"

df = pd.read_csv(file_path)

print("\n" + "=" * 60)
print("EMPLOYEE DATA ANALYSIS")
print("=" * 60)

print("\nOriginal Dataset Shape:")
print(df.shape)

print("\nOriginal Duplicate Rows:")
print(df.duplicated().sum())


# ============================================================
# 2. CREATE CLEAN DATASET
# ============================================================

clean_df = df.copy()

print("\nClean dataset created successfully!")


# ============================================================
# 3. CLEAN TEXT COLUMNS
# ============================================================

text_columns = [
    'gender',
    'ethnicity',
    'education_level',
    'department',
    'job_title',
    'country',
    'remote_status',
    'performance_rating',
    'currency',
    'pay_band'
]

for col in text_columns:
    clean_df[col] = (
        clean_df[col]
        .astype('string')
        .str.strip()
    )


# ============================================================
# 4. STANDARDIZE GENDER
# ============================================================

clean_df['gender'] = (
    clean_df['gender']
    .astype('string')
    .str.strip()
    .str.lower()
)

gender_mapping = {
    'm': 'Male',
    'male': 'Male',
    'man': 'Male',

    'f': 'Female',
    'female': 'Female',
    'woman': 'Female',

    'nb': 'Non-binary',
    'non-binary': 'Non-binary',

    'other': 'Other',
    'prefer not to say': 'Prefer not to say'
}

clean_df['gender'] = clean_df['gender'].replace(
    gender_mapping
)


# ============================================================
# 5. STANDARDIZE DEPARTMENT
# ============================================================

clean_df['department'] = (
    clean_df['department']
    .astype('string')
    .str.strip()
    .str.lower()
)

department_mapping = {
    'hr': 'HR',
    'it': 'IT',
    'operations': 'Operations',
    'finance': 'Finance',
    'marketing': 'Marketing',
    'customer support': 'Customer Support',
    'design': 'Design',
    'engineering': 'Engineering',
    'sales': 'Sales',
    'legal': 'Legal',
    'product': 'Product',
    'data science': 'Data Science'
}

clean_df['department'] = clean_df['department'].replace(
    department_mapping
)


# ============================================================
# 6. STANDARDIZE JOB TITLE
# ============================================================

clean_df['job_title'] = (
    clean_df['job_title']
    .astype('string')
    .str.strip()
    .str.replace(r'\s+', ' ', regex=True)
    .str.title()
)

job_title_mapping = {
    'It Manager': 'IT Manager',
    'It Support Specialist': 'IT Support Specialist',
    'Vp Design': 'VP Design',
    'Vp Product': 'VP Product',
    'Vp People': 'VP People',
    'Ux Designer': 'UX Designer',
    'Hr Business Partner': 'HR Business Partner',
    'Cmo': 'CMO',
    'Cfo': 'CFO',
    'Coo': 'COO'
}

clean_df['job_title'] = clean_df['job_title'].replace(
    job_title_mapping
)


# ============================================================
# 7. STANDARDIZE REMOTE STATUS
# ============================================================

clean_df['remote_status'] = (
    clean_df['remote_status']
    .astype('string')
    .str.strip()
    .str.lower()
)

remote_mapping = {
    'onsite': 'Onsite',
    'on-site': 'Onsite',
    'on site': 'Onsite',
    'remote': 'Remote',
    'hybrid': 'Hybrid'
}

clean_df['remote_status'] = clean_df['remote_status'].replace(
    remote_mapping
)


# ============================================================
# 8. STANDARDIZE EDUCATION LEVEL
# ============================================================

clean_df['education_level'] = (
    clean_df['education_level']
    .astype('string')
    .str.strip()
    .str.lower()
)

education_mapping = {
    'high school': 'High School',
    'highschool': 'High School',

    'bachelor': "Bachelor's",
    "bachelor's": "Bachelor's",
    'bachelors': "Bachelor's",

    'master': "Master's",
    "master's": "Master's",
    'masters': "Master's",

    'phd': 'PhD',
    'doctorate': 'PhD'
}

clean_df['education_level'] = clean_df[
    'education_level'
].replace(education_mapping)


# ============================================================
# 9. CONVERT NUMERIC COLUMNS
# ============================================================

numeric_columns = [
    'age',
    'years_experience',
    'tenure_years',
    'performance_review_score'
]

for col in numeric_columns:
    clean_df[col] = pd.to_numeric(
        clean_df[col],
        errors='coerce'
    )


# ============================================================
# 10. CONVERT HIRE DATE
# ============================================================

clean_df['hire_date'] = pd.to_datetime(
    clean_df['hire_date'],
    errors='coerce'
)


# ============================================================
# 11. CREATE NUMERIC SALARY
# ============================================================

clean_df['salary_numeric'] = (
    clean_df['salary_raw']
    .astype('string')
    .str.replace(',', '', regex=False)
    .str.extract(r'(\d+(?:\.\d+)?)')[0]
)

clean_df['salary_numeric'] = pd.to_numeric(
    clean_df['salary_numeric'],
    errors='coerce'
)


# ============================================================
# 12. HANDLE MISSING VALUES
# ============================================================

# Numeric columns

clean_df['age'] = clean_df['age'].fillna(
    clean_df['age'].median()
)

clean_df['years_experience'] = clean_df[
    'years_experience'
].fillna(
    clean_df['years_experience'].median()
)

clean_df['tenure_years'] = clean_df[
    'tenure_years'
].fillna(
    clean_df['tenure_years'].median()
)

clean_df['performance_review_score'] = clean_df[
    'performance_review_score'
].fillna(
    clean_df['performance_review_score'].median()
)

clean_df['salary_numeric'] = clean_df[
    'salary_numeric'
].fillna(
    clean_df['salary_numeric'].median()
)


# Categorical columns

categorical_columns = [
    'gender',
    'ethnicity',
    'education_level',
    'remote_status'
]

for col in categorical_columns:
    clean_df[col] = clean_df[col].fillna('Unknown')


# Performance rating

clean_df['performance_rating'] = clean_df[
    'performance_rating'
].fillna('Not Rated')


# ============================================================
# 13. CREATE EXPERIENCE LEVEL
# ============================================================

clean_df['experience_level'] = pd.cut(
    clean_df['years_experience'],
    bins=[-1, 2, 5, 10, 20, float('inf')],
    labels=[
        'Entry Level',
        'Junior',
        'Mid Level',
        'Senior',
        'Expert'
    ]
)


# ============================================================
# 14. CREATE TENURE GROUP
# ============================================================

clean_df['tenure_group'] = pd.cut(
    clean_df['tenure_years'],
    bins=[-1, 2, 5, 10, 20, float('inf')],
    labels=[
        '0-2 Years',
        '3-5 Years',
        '6-10 Years',
        '11-20 Years',
        '20+ Years'
    ]
)


# ============================================================
# 15. FINAL CLEANING CHECK
# ============================================================

print("\n" + "=" * 60)
print("CLEANING CHECK")
print("=" * 60)

print("\nClean Dataset Shape:")
print(clean_df.shape)

print("\nDuplicate Rows:")
print(clean_df.duplicated().sum())

print("\nTotal Missing Values:")
print(clean_df.isnull().sum().sum())


# ============================================================
# 16. WORKFORCE CHARACTERISTICS
# ============================================================

print("\n" + "=" * 60)
print("WORKFORCE CHARACTERISTICS")
print("=" * 60)

print("\nTotal Employees:")
print(len(clean_df))

print("\nGender Distribution:")
print(clean_df['gender'].value_counts())

print("\nEmployees by Department:")
print(clean_df['department'].value_counts())

print("\nWork Location Distribution:")
print(clean_df['remote_status'].value_counts())

print("\nAverage Employee Age:")
print(round(clean_df['age'].mean(), 2))

print("\nAverage Years of Experience:")
print(round(clean_df['years_experience'].mean(), 2))

print("\nAverage Employee Tenure:")
print(round(clean_df['tenure_years'].mean(), 2))


# ============================================================
# CHART 1 - GENDER DISTRIBUTION
# ============================================================

gender_count = clean_df['gender'].value_counts()

plt.figure(figsize=(8, 6))
gender_count.plot(kind='bar')

plt.title('Employee Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(
    'Output/employee_gender_distribution.png'
)
plt.show()


# ============================================================
# CHART 2 - DEPARTMENT DISTRIBUTION
# ============================================================

department_count = clean_df['department'].value_counts()

plt.figure(figsize=(10, 6))
department_count.plot(kind='bar')

plt.title('Employee Count by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.savefig(
    'Output/employee_department_distribution.png'
)
plt.show()


# ============================================================
# CHART 3 - WORK LOCATION
# ============================================================

remote_count = clean_df['remote_status'].value_counts()

plt.figure(figsize=(8, 6))
remote_count.plot(kind='bar')

plt.title('Employee Count by Work Location')
plt.xlabel('Work Location')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(
    'Output/employee_work_location.png'
)
plt.show()


# ============================================================
# CHART 4 - EDUCATION DISTRIBUTION
# ============================================================

education_count = clean_df['education_level'].value_counts()

plt.figure(figsize=(8, 6))
education_count.plot(kind='bar')

plt.title('Employee Count by Education Level')
plt.xlabel('Education Level')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(
    'Output/employee_education_distribution.png'
)
plt.show()


# ============================================================
# CHART 5 - AGE DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

clean_df['age'].plot(
    kind='hist',
    bins=15
)

plt.title('Employee Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Employees')

plt.tight_layout()
plt.savefig(
    'Output/employee_age_distribution.png'
)
plt.show()


# ============================================================
# SALARY ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("SALARY ANALYSIS")
print("=" * 60)

print("\nSalary Statistics by Currency:")

salary_by_currency = (
    clean_df
    .groupby('currency')['salary_numeric']
    .agg([
        'count',
        'mean',
        'median',
        'min',
        'max'
    ])
    .round(2)
)

print(salary_by_currency)


# ============================================================
# CHART 6 - SALARY RANGE DISTRIBUTION
# ============================================================

salary_range = pd.cut(
    clean_df['salary_numeric'],
    bins=[
        0,
        30000,
        50000,
        75000,
        100000,
        150000,
        float('inf')
    ],
    labels=[
        '0-30K',
        '30K-50K',
        '50K-75K',
        '75K-100K',
        '100K-150K',
        '150K+'
    ]
)

salary_range_count = (
    salary_range
    .value_counts()
    .sort_index()
)

print("\nEmployees by Salary Range:")
print(salary_range_count)

plt.figure(figsize=(10, 6))

salary_range_count.plot(kind='bar')

plt.title('Employee Distribution by Salary Range')
plt.xlabel('Salary Range')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(
    'Output/salary_range_distribution.png'
)
plt.show()


# ============================================================
# EXPERIENCE ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("EXPERIENCE ANALYSIS")
print("=" * 60)

print("\nAverage Years of Experience:")
print(round(clean_df['years_experience'].mean(), 2))

print("\nMinimum Years of Experience:")
print(clean_df['years_experience'].min())

print("\nMaximum Years of Experience:")
print(clean_df['years_experience'].max())

print("\nMedian Years of Experience:")
print(clean_df['years_experience'].median())

print("\nEmployees by Experience Level:")
print(
    clean_df['experience_level']
    .value_counts()
    .sort_index()
)


# ============================================================
# CHART 7 - EXPERIENCE LEVEL
# ============================================================

experience_count = (
    clean_df['experience_level']
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(9, 6))

experience_count.plot(kind='bar')

plt.title('Employee Distribution by Experience Level')
plt.xlabel('Experience Level')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(
    'Output/employee_experience_level.png'
)
plt.show()


# ============================================================
# PERFORMANCE ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("PERFORMANCE ANALYSIS")
print("=" * 60)

print("\nPerformance Rating Distribution:")
print(
    clean_df['performance_rating']
    .value_counts()
)

print("\nAverage Performance Review Score:")
print(
    round(
        clean_df['performance_review_score'].mean(),
        2
    )
)

performance_by_department = (
    clean_df
    .groupby('department')['performance_review_score']
    .agg([
        'count',
        'mean',
        'median'
    ])
    .round(2)
    .sort_values(
        'mean',
        ascending=False
    )
)

print("\nPerformance Statistics by Department:")
print(performance_by_department)


# ============================================================
# CHART 8 - PERFORMANCE RATING
# ============================================================

rating_count = (
    clean_df['performance_rating']
    .value_counts()
)

plt.figure(figsize=(9, 6))

rating_count.plot(kind='bar')

plt.title(
    'Employee Performance Rating Distribution'
)
plt.xlabel('Performance Rating')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.savefig(
    'Output/performance_rating_distribution.png'
)
plt.show()


# ============================================================
# CHART 9 - PERFORMANCE BY EXPERIENCE
# ============================================================

performance_experience = (
    clean_df
    .groupby(
        'experience_level',
        observed=True
    )['performance_review_score']
    .mean()
    .round(2)
)

print("\nAverage Performance Score by Experience Level:")
print(performance_experience)

plt.figure(figsize=(9, 6))

performance_experience.plot(kind='bar')

plt.title(
    'Average Performance Score by Experience Level'
)
plt.xlabel('Experience Level')
plt.ylabel('Average Performance Score')
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(
    'Output/performance_by_experience_level.png'
)
plt.show()


# ============================================================
# CHART 10 - DEPARTMENT PERFORMANCE
# ============================================================

department_performance = (
    clean_df
    .groupby('department')['performance_review_score']
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

print("\nAverage Performance Score by Department:")
print(department_performance)

plt.figure(figsize=(10, 6))

department_performance.plot(kind='bar')

plt.title(
    'Average Performance Score by Department'
)
plt.xlabel('Department')
plt.ylabel('Average Performance Score')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.savefig(
    'Output/department_performance.png'
)
plt.show()


# ============================================================
# TENURE ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("EMPLOYEE TENURE ANALYSIS")
print("=" * 60)

print("\nAverage Employee Tenure:")
print(
    round(
        clean_df['tenure_years'].mean(),
        2
    )
)

print("\nMinimum Employee Tenure:")
print(clean_df['tenure_years'].min())

print("\nMaximum Employee Tenure:")
print(clean_df['tenure_years'].max())

print("\nMedian Employee Tenure:")
print(clean_df['tenure_years'].median())

tenure_count = (
    clean_df['tenure_group']
    .value_counts()
    .sort_index()
)

print("\nEmployees by Tenure Group:")
print(tenure_count)


# ============================================================
# CHART 11 - TENURE DISTRIBUTION
# ============================================================

plt.figure(figsize=(9, 6))

tenure_count.plot(kind='bar')

plt.title('Employee Distribution by Tenure')
plt.xlabel('Tenure Group')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(
    'Output/employee_tenure_distribution.png'
)
plt.show()


# ============================================================
# CHART 12 - SALARY BY EXPERIENCE LEVEL
# ============================================================

salary_experience = (
    clean_df
    .groupby(
        'experience_level',
        observed=True
    )['salary_numeric']
    .mean()
    .round(2)
)

print("\n" + "=" * 60)
print("AVERAGE SALARY BY EXPERIENCE LEVEL")
print("=" * 60)

print("\nAverage Salary by Experience Level:")
print(salary_experience)

plt.figure(figsize=(9, 6))

salary_experience.plot(kind='bar')

plt.title(
    'Average Salary by Experience Level'
)
plt.xlabel('Experience Level')
plt.ylabel('Average Salary')
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(
    'Output/average_salary_by_experience.png'
)
plt.show()


# ============================================================
# TURNOVER / ATTRITION ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("TURNOVER / ATTRITION ANALYSIS")
print("=" * 60)

turnover_columns = [
    col for col in clean_df.columns
    if any(
        word in col.lower()
        for word in [
            'attrition',
            'turnover',
            'termination',
            'terminated',
            'exit',
            'employment_status'
        ]
    )
]

print("\nPossible Turnover / Attrition Columns:")
print(turnover_columns)

if len(turnover_columns) == 0:
    print(
        "\nDirect attrition analysis is not available "
        "because the dataset does not contain a "
        "dedicated attrition or termination column."
    )


# ============================================================
# FINAL DATA QUALITY CHECK
# ============================================================

print("\n" + "=" * 60)
print("FINAL DATA QUALITY CHECK")
print("=" * 60)

print("\nFinal Dataset Shape:")
print(clean_df.shape)

print("\nDuplicate Rows:")
print(clean_df.duplicated().sum())

print("\nTotal Missing Values:")
print(clean_df.isnull().sum().sum())

print("\nMissing Values by Column:")
print(clean_df.isnull().sum())

print("\nFinal Columns:")
print(clean_df.columns.tolist())

print("\n" + "=" * 60)
print("EMPLOYEE DATA ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)


# ============================================================
# FINAL PROJECT SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("FINAL PROJECT SUMMARY")
print("=" * 60)

print("\nProject: Employee Data Analysis")

print("\nObjectives:")
print("1. Analyze workforce characteristics")
print("2. Examine salary distribution")
print("3. Compare department performance")
print("4. Analyze employee experience levels")
print("5. Examine employee tenure")
print("6. Analyze employee performance ratings")

print("\nTools Used:")
print("Python")
print("Pandas")
print("NumPy")
print("Matplotlib")

print("\nDataset Information:")
print("Total Employees:", len(clean_df))
print("Total Columns:", len(clean_df.columns))

print("\nKey Metrics:")
print("Average Age:", round(clean_df['age'].mean(), 2))
print(
    "Average Experience:",
    round(clean_df['years_experience'].mean(), 2),
    "years"
)
print(
    "Average Tenure:",
    round(clean_df['tenure_years'].mean(), 2),
    "years"
)
print(
    "Average Performance Score:",
    round(
        clean_df['performance_review_score'].mean(),
        2
    )
)

print("\nAnalysis completed successfully!")



# ============================================================
# PROJECT INSIGHTS
# ============================================================

print("\n" + "=" * 60)
print("PROJECT INSIGHTS")
print("=" * 60)

print("\n1. Workforce:")
print(
    "The dataset contains",
    len(clean_df),
    "employees across multiple departments."
)

print(
    "The average employee age is",
    round(clean_df['age'].mean(), 2),
    "years."
)

print(
    "The average years of experience is",
    round(clean_df['years_experience'].mean(), 2),
    "years."
)

print(
    "The average employee tenure is",
    round(clean_df['tenure_years'].mean(), 2),
    "years."
)


print("\n2. Department:")
print(
    "Employee counts were analyzed across",
    clean_df['department'].nunique(),
    "standardized departments."
)


print("\n3. Work Location:")
print(
    "Employee distribution was analyzed across",
    clean_df['remote_status'].nunique(),
    "work-location categories."
)


print("\n4. Performance:")
print(
    "The overall average performance review score is",
    round(
        clean_df['performance_review_score'].mean(),
        2
    ),
    "."
)


print("\n5. Experience:")
print(
    "Employees were grouped into five experience levels:"
)

print(
    "Entry Level, Junior, Mid Level, Senior, and Expert."
)


print("\n6. Tenure:")
print(
    "Employee tenure was grouped into five categories "
    "to understand workforce retention patterns."
)


print("\n7. Salary:")
print(
    "Salary distributions were examined using salary ranges "
    "and salary statistics by currency."
)


print("\n8. Attrition:")
print(
    "A direct attrition rate was not calculated because "
    "the dataset does not contain a dedicated attrition "
    "or termination field."
)

print("\n" + "=" * 60)
print("PROJECT ANALYSIS COMPLETED")
print("=" * 60)
