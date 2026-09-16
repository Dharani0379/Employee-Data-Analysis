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
- Average age
- Average experience
- Average tenure

### Salary Analysis

Analyzed:

- Salary statistics by currency
- Salary ranges
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

### Tenure Analysis

Employees were grouped into:

- 0–2 Years
- 3–5 Years
- 6–10 Years
- 11–20 Years
- 20+ Years

## Visualizations

The project generates 12 visualizations covering:

1. Employee Gender Distribution
2. Employee Count by Department
3. Employee Count by Work Location
4. Employee Count by Education Level
5. Employee Age Distribution
6. Employee Distribution by Salary Range
7. Employee Distribution by Experience Level
8. Employee Performance Rating Distribution
9. Average Performance Score by Experience Level
10. Average Performance Score by Department
11. Employee Distribution by Tenure
12. Average Salary by Experience Level

## Attrition Analysis

The dataset does not contain a dedicated employee attrition, termination, or exit-status field. Therefore, a direct employee attrition rate was not calculated.

Employee tenure was analyzed instead to provide workforce retention-related context.

## Project Outcome

This project demonstrates the use of Python-based data cleaning, exploratory data analysis, statistical summaries, and data visualization to understand employee workforce patterns and support data-driven insights.

## Author

DHARANIDHARAN G
