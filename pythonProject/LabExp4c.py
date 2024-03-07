import pandas as pd
import matplotlib.pyplot as plt
# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('students.csv')
# Define age groups
age_bins = [0, 12, 18, 25, 35, 50, 100]  # You can adjust the age groups as needed
age_labels = ['0-12', '13-18', '19-25', '26-35', '36-50', '51+']
# Categorize students into age groups
df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)
# Calculate the average grade for each age group
average_grade_by_age = df.groupby('AgeGroup')['Grade'].mean()
# Create a bar plot
plt.bar(average_grade_by_age.index, average_grade_by_age)
plt.xlabel('Age Groups')
plt.ylabel('Average Grade')
plt.title('Average Grade for Different Age Groups')
plt.show()
