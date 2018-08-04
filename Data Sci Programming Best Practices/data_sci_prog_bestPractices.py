# -*- coding: utf-8 -*-
"""
Recreated from Dataquest "Programming Best Practices for Data Science" article
https://www.dataquest.io/blog/programming-best-practices-for-data-science/
"""

-----------------------------
#Prototyping phase:
"""
In general, code in the prototyping mindset should focus on:

Understandability
Markdown cells to describe our observations and assumptions
Small pieces of code for the actual logic
Lots of visualizations and counts
Minimal abstractions
Most code shouldn't be in functions (should feel more object-oriented)
"""

#####set working directory
import os
os.chdir('D:\Python Projects')


import pandas as pd

##### read in data
#set skiprows=1 to ignore first row which has notes rather than headers
#set low_memory=False to improve type inferencing in Pandas
loans_2007 = pd.read_csv('LoanStats3a.csv', skiprows=1, low_memory=False)
loans_2007.head(2)

#####drop unnecessary columns
#desc and url seem useless
loans_2007 = loans_2007.drop(['desc', 'url'], axis=1)

#drop any columns w/ more than 50% missing rows
#this shows the proportion of null values within each column
loans_2007.isnull().sum()/len(loans_2007)

#this removes columns w/ more than half missing values
#axis=1 removes columns (instead of rows)
#thresh sets the threshold for removal
half_count = len(loans_2007)/2
loans_2007 = loans_2007.dropna(thresh=half_count, axis=1)


-----------------------------------------------
#Production phase:
"""
In production mindset, we want to focus on code that will generalize to
more situations. 
In this case the code should work for any of the data sets from
Lending Club. 
Best way to do this is to create a data pipeline, where data is modified
within functions, then passed between functions. 
"""

import pandas as pd

#this uses a single function to hold data cleaning code
def import_clean(file_list):
    frames = []
    for file in file_list:
        loans = pd.read_csv(file, skiprows=1, low_memory=False)
        loans = loans.drop(['desc', 'url'], axis=1)
        half_count = len(loans)/2
        loans = loans.dropna(thresh=half_count, axis=1)
        loans = loans.drop_duplicates()
        # Drop first group of features
        loans = loans.drop(["funded_amnt", "funded_amnt_inv", "grade", "sub_grade", "emp_title", "issue_d"], axis=1)
        # Drop second group of features
        loans = loans.drop(["zip_code", "out_prncp", "out_prncp_inv", "total_pymnt", "total_pymnt_inv", "total_rec_prncp"], axis=1)
        # Drop third group of features
        loans = loans.drop(["total_rec_int", "total_rec_late_fee", "recoveries", "collection_recovery_fee", "last_pymnt_d", "last_pymnt_amnt"], axis=1)
        frames.append(loans)
    return frames

frames = import_clean(['LoanStats3a.csv'])

"""
In general, the production mindset should focus on:

Healthy abstractions
Code should generalize to be compatible with similar data sources
Code shouldn't be so general that it becomes cumbersome to understand
pipeline stability
Reliability should match how frequently its run (daily? weekly? monthly?)
"""
