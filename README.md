# Introduction

In this data analysis I will be analyzing data scientist job salaries (USD) by the proportion of remote work they do, the company size as well as by their experience level in the work year of 2022 for full-time employees. I will be comparing these 3 factors and checking which one correlates with average salary most, and then visualize these results. My hypothesis is that the experience level and company size will positively correlate with salary, and the proportion of remote work done will not correlate with salary. I will make use of Python, Python Pandas, and MySQL.

This dataset has been retrieved from https://www.kaggle.com/datasets/niyalthakkar/data-science-jobs-analysis.

Note: The columns in the dataset for company_size (values being S, M, and L) and experience_level (values being ES, EX, MI, and SE) were converted to numrical values for the purposes of calculating correlation with salary as follows:

```
S = 0
M = 0.5
L = 1

EN = 0
EX = 0
MI = 0.5
SE = 1
```

# Results

The results that were found through this analysis are:

```
The correlation between salary and proportion of remote work is 0.15.
The correlation between salary and company size is -0.02.
The correlation between salary and experience level is 0.62.
```

Data visualizations are in files.

# Discussion

Correlation is a number between -1 and 1 where it measures how correlated 2 variables are, -1 means that the variables are completely negatively correlated, 0 means that the variables are completely uncorrelated and 1 means the variables are completely positively correlated. For example, if the correlation were to be 1, that means as one variable goes up in value, the other variable is going up the same amount.

In this data analysis I found that salary and experience level were significantly positively correlated at 0.62, meaning that generally, as experience level goes up, the salary goes up as well. This can be seen in the data visualization titled "average_salary_vs_experience_level.png," where average salary consistantly increases when going from entry level to more senior roles. Salary and company size were almost completely uncorrelated, as this was at-0.02, meaning that pay does not change much between different company sizes. This can actually be seen in the data visualization named "average_salary_vs_company_size.png," where we can see that the large sized companies have a slightly lower average pay than medium sized companies. Salary and proportion of remote work done were insignificantly positively correlated at 0.15, meaning that there is a slight correlation with more remote working paying higher. This can be seen using the data visualization named "average_salary_vs_remote_work.png," where it is evident that remote workers (100%) had the highest average salaries, and in-person workers (0%) were a close second. Hybrid workers (50%) had the lowest average salary, however there is a weak correlation with average salary as the remote workers did earn more than the in-person workers.

The visualized differences of correlations to salary by variable can be seen in "correlation_with_salary_vs_variables.png."

# Conclusion

My hypothesis of experience level being positively correlated with salary was confirmed to be correct. However, my other hypotheses were incorrect as proportion of remote work done did very slightly correlate positively with salary and the company size was uncorrelated with salary. From this analysis we can conclude that experience level has a significant correlation with increased salary, a greater proportion of remote work has a very slight correlation with increased salary, and company size has no correlation with salary.

# How to run this program

Prior to running program you must have unix terminal, pandas, git and python installed.

In the terminal enter:
```
cd desktop
git clone https://github.com/Harjot66/data_scientist_salaries_analysis.git
```
then you must drag the "cleaned_data.csv" file out of the repository file and place it in your desktop,
after this you must enter the following in the terminal:
```
python3 data_scientist_salaries_analysis
```
