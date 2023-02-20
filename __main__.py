#importing the pandas library and reading csv file into a pandas dataframe

import pandas as pd
dscsvfile = pd.read_csv("cleaned_data.csv")

#calculating the correlation between the salary_in_usd column and the remote_ratio column

correlation_prop_remote_work = dscsvfile['salary_in_usd'].corr(dscsvfile['remote_ratio'])
print('\n', 'The correlation between salary and proportion of remote work is ' + str(round(correlation_prop_remote_work, 2)) + '.')

#converting the company_size column into categories and calculating the correlation between the salary_in_usd column and
#the company_size column

dscsvfile['company_size'] = dscsvfile['company_size'].astype('category').cat.codes
correlation_prop_remote_work = dscsvfile['salary_in_usd'].corr(dscsvfile['company_size'])
print('\n', 'The correlation between salary and company size is ' + str(round(correlation_prop_remote_work, 2)) + '.')

#converting the experience_level column into categories and calculating the correlation between the salary_in_usd column and
#the experience_level column

dscsvfile['experience_level'] = dscsvfile['experience_level'].astype('category').cat.codes
correlation_prop_remote_work = dscsvfile['salary_in_usd'].corr(dscsvfile['experience_level'])
print('\n', 'The correlation between salary and experience level is ' + str(round(correlation_prop_remote_work, 2)) + '.\n')
