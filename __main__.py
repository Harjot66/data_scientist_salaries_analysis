#importing the pandas library and reading csv file into a pandas dataframe

import pandas as pd
dscsvfile = pd.read_csv("cleaned_data.csv")

#creating new dataframes for charts and making them variables

remote_ratio_df = dscsvfile.groupby('remote_ratio').salary_in_usd.mean()
company_size_df = dscsvfile.groupby('company_size').salary_in_usd.mean()
experience_level_df = dscsvfile.groupby('experience_level').salary_in_usd.mean()

#creating visualization for remote_ratio vs salary_in_usd

remote_ratio_df.plot.bar(x = 'remote_ratio', y = '', title = 'average salary (USD) vs. remote work ratio', xlabel = 'remote work ratio', ylabel = 'average salary (USD)')

#creating visualization for company_size vs salary_in_usd

company_size_df.plot.bar(x = 'company_size', y = '', title = 'average salary (USD) vs. company size', xlabel = 'company size', ylabel = 'average salary (USD)')

#creating visualization for experience_level vs salary_in_usd

experience_level_df.plot.bar(x = 'experience_level', y = '', title = 'average salary (USD) vs. experience level', xlabel = 'experience level', ylabel = 'average salary (USD)')

#calculating the correlation between the salary_in_usd column and the remote_ratio column

correlation_prop_remote_work = dscsvfile['salary_in_usd'].corr(dscsvfile['remote_ratio'])
print('\n', 'The correlation between salary and proportion of remote work is ' + str(round(correlation_prop_remote_work, 2)) + '.')

#converting the company_size column into numerical values and calculating the correlation
#between the salary_in_usd column and the company_size column

company_size_converted = []

for value in dscsvfile['company_size']:
    if value == 'S':
        company_size_converted.append(0)
    elif value == 'M':
        company_size_converted.append(0.5)
    else:
        company_size_converted.append(1)

dscsvfile['company_size_converted'] = company_size_converted

correlation_company_size = dscsvfile['salary_in_usd'].corr(dscsvfile['company_size_converted'])
print('\n', 'The correlation between salary and company size is ' + str(round(correlation_company_size, 2)) + '.')

#converting the experience_level column into numerical values and calculating the correlation
#between the salary_in_usd column and the experience_level column
#EN/EX = Entry level, #MI = Mid level, #SE = Senior level

experience_level_converted = []

for value in dscsvfile['experience_level']:
    if value == 'EN' or value == 'EX':
        experience_level_converted.append(0)
    elif value == 'MI':
        experience_level_converted.append(0.5)
    else:
        experience_level_converted.append(1)

dscsvfile['experience_level_converted'] = experience_level_converted

correlation_experience_level = dscsvfile['salary_in_usd'].corr(dscsvfile['experience_level_converted'])
print('\n', 'The correlation between salary and experience level is ' + str(round(correlation_experience_level, 2)) + '.')

#creating a bar chart to compare the 3 correlations

corr_df_input = [['remote work', correlation_prop_remote_work], ['company size ', correlation_company_size], ['experience level', correlation_experience_level]]
corr_df = pd.DataFrame(corr_df_input, columns = ['variable', 'correlation with salary'])
corr_df.plot.bar(x = 'variable', ylabel ='correlation coefficient with salary (r)', title = 'correlation coefficient with salary (r)')
