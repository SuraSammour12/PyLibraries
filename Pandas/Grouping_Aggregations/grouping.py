import pandas as pd
df=pd.read_csv('ds_salaries.csv')
print(df)
print(df['job_title'])
# method 1
avg_salary_by_job=df.groupby('job_title')['salary_in_usd'].mean()
print(avg_salary_by_job)
# method 2
average_salary_by_job=df.groupby('job_title').agg({'salary_in_usd':'mean'})

# Find the total salary paid for each combination of experience_level and employment_type.
total_salary=df.groupby(['experience_level','employment_type'])['salary_in_usd'].sum()
print(total_salary)

median_salary=df.groupby(['company_location','company_size'])['salary_in_usd'].median()
print(median_salary)
print(median_salary.reset_index())

# Count the number of employees in each country (employee_residence)
employee_count_by_residence=df.groupby('employee_residence').size()
print(employee_count_by_residence)