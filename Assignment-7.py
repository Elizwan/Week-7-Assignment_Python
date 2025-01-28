#!/usr/bin/env python
# coding: utf-8

# # PYTHON ASSIGNMENT-WEEK 7 

# # Task 1

# In[1]:


import pandas as pd

# Step 2:Load dataset
file_path = "D:\chrome\Titanic-Dataset.csv" 
data = pd.read_csv(file_path)


# In[2]:


# Step 3: Display the first few rows
print("First 5 rows of the dataset:")
print(data.head())


# In[3]:


# Step 4: Explore the structure of the dataset
print("\nDataset info:")
print(data.info())

print("\nChecking for missing values:")
print(data.isnull().sum())


# In[4]:


# Step 5: Clean the dataset (fill or drop missing values)
if data.isnull().sum().sum() > 0:
    data.fillna(data.mean(numeric_only=True), inplace=True)
    print("\nMissing values handled by filling with column mean.")
else:
    print("\nNo missing values found.")

# Verify cleaning
print("\nDataset after cleaning:")
print(data.head())


# # Task 2

# In[5]:


# Basic statistics of numerical columns
print(data.describe())


# In[6]:


# Group by 'Pclass' and calculate the mean of 'Age'
grouped_by_class = data.groupby('Pclass')['Age'].mean()
print(grouped_by_class)


# In[7]:


#Interesting fact
# Calculate the survival rate by Sex
survival_rate_by_sex = data.groupby('Sex')['Survived'].mean()

# Display the result
print(survival_rate_by_sex)


# # Task 3

# # Data Visualization

# In[8]:


import matplotlib.pyplot as plt

#Creating a bar chart
# Bar chart of survivors by gender
gender_survival = data.groupby(['Sex', 'Survived']).size().unstack()
gender_survival.plot(kind='bar', stacked=True, color=['red', 'green'])
plt.title('Survival Count by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()


# In[9]:


# Creating Histogram
# Histogram of Age distribution
data['Age'].dropna().plot(kind='hist', bins=30, color='skyblue', edgecolor='black')
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[10]:


import seaborn as sns
# Drawing Box plot
# Box plot of Fare by Passenger Class
sns.boxplot(x='Pclass', y='Fare', data=data)
plt.title('Fare Distribution by Passenger Class')
plt.show()


# In[11]:


# Drawing a Scatter Plot
# Scatter plot of Age vs Fare
plt.scatter(data['Age'], data['Fare'], alpha=0.5, color='blue')
plt.title('Age vs Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()


# In[12]:


#Handling missing values
# Fill missing 'Age' with mean value
data['Age'].fillna(data['Age'].mean(), inplace=True)


# In[ ]:




