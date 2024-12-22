import pandas as pd
df=pd.read_csv('ds_salaries.csv')
print(df)
# Aggregation functions
# (mean,median,mode,std,max,min,sum)

# Average salaries
avg_salaries=df['salary_in_usd'].mean()
print(f"average salary in usd is ${round(avg_salaries)}")

# max salary
max_salary=df['salary_in_usd'].max
print(f'max salary in usd is ${max_salary}')

# Filter the DataFrame to return the row(s) with the highest salary in USD
highest_salary_row=df[df['salary_in_usd']==df['salary_in_usd'].max()]
print(highest_salary_row)

# Task
# how to get the job title who gets the max salary??
max_salary_row=df[df['salary_in_usd']==df['salary_in_usd'].max()]

# Extract job title from the max salary row
job_title_max_salary=max_salary_row['job_title'].values[0]
# Extract the first value from the 'job_title' column of the filtered row
print(f"The job title with the highest salary is: {job_title_max_salary}")

# Filter the DataFrame to include only rows where the year is 2020
print(df[df['work_year']==2020])

# describe:Generate summary statistics of the numerical columns in the DataFrame
print(df.describe())
# note
"""
# 25%: The first quartile, where 25% of the data points are below or equal to this value
# 50%: The median (second quartile), which divides the data into two equal halves
# 70%: The 70th percentile, where 70% of the data points are below or equal to this value
"""
# write a code to describe only salary and remote_ratio
print(df[['salary','remote_ratio']].describe())