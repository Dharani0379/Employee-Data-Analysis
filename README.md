# Employee Data Analysis

## Project Overview

Employee Data Analysis is a Python-based data analysis project that examines employee workforce characteristics, salary patterns, experience levels, performance, and tenure.

The project uses Python, Pandas, NumPy, and Matplotlib to clean the dataset, perform analysis, and generate visualizations.

## Objectives

- Analyze workforce characteristics
- Examine employee salary distribution
- Analyze employee experience levels
- Evaluate performance patterns
- Analyze employee tenure
- Identify workforce distribution across departments and work locations
- Create meaningful data visualizations

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

## Dataset

The dataset contains 96,900 employee records with information including:

- Employee ID
- Employee Name
- Age
- Gender
- Ethnicity
- Education Level
- Years of Experience
- Tenure
- Department
- Job Title
- Country
- Remote Status
- Performance Rating
- Performance Review Score
- Hire Date
- Currency
- Salary
- Pay Band

## Data Cleaning

The following cleaning techniques were performed:

- Standardized gender categories
- Standardized department names
- Standardized remote work status
- Cleaned job titles
- Converted numeric columns to appropriate data types
- Converted hire dates to datetime format
- Extracted numeric salary values
- Handled missing numeric values using median values
- Handled missing categorical values using "Unknown"
- Handled missing performance ratings using "Not Rated"
- Created experience-level categories
- Created tenure groups
- Checked for duplicate records

## Analysis Performed

### Workforce Analysis

Analyzed:

- Total employee count
- Gender distribution
- Department distribution
- Work location distribution
- Education level distribution
- Age distribution
- Average age
- Average experience
- Average tenure

### Salary Analysis

Analyzed:

- Salary distribution
- Salary ranges
- Average salary by currency
- Average salary by department
- Average salary by experience level

### Experience Analysis

Employees were categorized into:

- Entry Level
- Junior
- Mid Level
- Senior
- Expert

### Performance Analysis

Analyzed:

- Performance rating distribution
- Average performance review score
- Performance by department
- Performance by experience level
- Relationship between experience and performance

### Tenure Analysis

Employees were grouped into:

- 0–2 Years
- 3–5 Years
- 6–10 Years
- 11–20 Years
- 20+ Years

## Visualizations

The project generates **18 visualizations** covering workforce, salary, experience, performance, gender, department, and tenure analysis:

1. Average Salary by Experience
2. Employee Tenure Distribution
3. Department Performance
4. Performance by Experience Level
5. Performance Rating Distribution
6. Employee Experience Level Distribution
7. Salary Range Distribution
8. Employee Age Distribution
9. Employee Education Distribution
10. Employee Work Location Distribution
11. Employee Department Distribution
12. Employee Gender Distribution
13. Average Salary by Department
14. Salary Distribution
15. Experience vs Performance
16. Average Salary by Currency
17. Gender Distribution
18. Employees by Department

All generated charts are stored in the `Output` folder.

## Attrition Analysis

The dataset does not contain a dedicated employee attrition, termination, or exit-status field. Therefore, a direct employee attrition rate was not calculated.

Employee tenure was analyzed instead to provide workforce retention-related context.

## Project Structure

```text
Employee-Data-Analysis/
│
├── Employee_Data_Analysis.py
├── employee_pay_equity_messy.csv
├── README.md
│
└── Output/
    ├── average_salary_by_experience.png
    ├── employee_tenure_distribution.png
    ├── department_performance.png
    ├── performance_by_experience_level.png
    ├── performance_rating_distribution.png
    ├── employee_experience_level.png
    ├── salary_range_distribution.png
    ├── employee_age_distribution.png
    ├── employee_education_distribution.png
    ├── employee_work_location.png
    ├── employee_department_distribution.png
    ├── employee_gender_distribution.png
    ├── average_salary_by_department.png
    ├── salary_distribution.png
    ├── experience_vs_performance.png
    ├── average_salary_by_currency.png
    ├── gender_distribution.png
    └── employees_by_department.png
