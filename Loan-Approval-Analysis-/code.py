# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
path
bank=pd.read_csv(path)



# code starts here

categorical_var=bank.select_dtypes(include='object')
print(categorical_var)
numerical_var=bank.select_dtypes(include='number')
print(numerical_var)


# code ends here


# --------------
# code starts here
banks = bank.drop(columns='Loan_ID')
print(banks.isnull().sum())

bank_mode = banks.mode().iloc[0]
#print('Bank mode is : \n', bank_mode)

banks.fillna(bank_mode, inplace=True)

print(banks.isnull().sum())


# --------------
# Code starts here

import numpy as np
import pandas  as pd


avg_loan_amount=banks.pivot_table(values='LoanAmount', index=['Gender','Married','Self_Employed'], aggfunc=np.mean)
print(avg_loan_amount)

# code ends here



# --------------
loan_approved_se = len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status']== 'Y')])

loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])

percentage_se = (loan_approved_se * 100)/614
percentage_nse = (loan_approved_nse * 100)/614


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x: (x/12))

big_loan_term = len(loan_term[loan_term >= 25])



# code ends here


# --------------
# code starts here


loan_groupby= banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']

mean_values = loan_groupby.mean()
print(mean_values)

# code ends here


