# --------------
# Importing header files

import numpy as np

# Path of the file has been stored in variable called 'path'
path
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
#data_file='path'
data=np.genfromtxt(path, delimiter=",", skip_header=1)
print("\n Data: \n\n", data)
print("\n Type of Data: \n\n", type(data))
census=np.concatenate((data,new_record), axis=0)
print(census)


# --------------
#Code starts here
import numpy as np 
age = census[:,0]
print(age)

max_age = max(age)
min_age = min(age)
print(max_age)
print(min_age)
age_mean = np.mean(age)
age_std = np.std(age)
print("The mean age of dataset is:",age_mean)
print("The standard deviation of age of dataset is:",age_std)


# --------------
#Code starts here
import numpy as np 
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

#Storing the different race lengths with appropriate indexes
race_list_count = [len_0,len_1,len_2,len_3,len_4]
print(race_list_count)

#Storing the race with minimum length into a variable 
minority_race = race_list_count.index(min(race_list_count))
print("The minority race is:",minority_race)


# --------------
#Code starts here

senior_citizens=census[census[:,0]>60]
working_hours_sum=senior_citizens.sum(axis=0)[6]
senior_citizens_len=len(senior_citizens)
avg_working_hours=(working_hours_sum/senior_citizens_len)
print(avg_working_hours)


# --------------
#Code starts here
import numpy as np 
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
len(high)
len(low)
avg_pay_high=high[:,7].mean()
avg_pay_low=low[:,7].mean()
print(avg_pay_high)
print(avg_pay_low)


