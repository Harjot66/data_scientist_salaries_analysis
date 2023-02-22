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
