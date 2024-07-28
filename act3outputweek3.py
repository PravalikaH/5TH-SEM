import pandas as pd
import numpy as np

# Create the initial dataframe
marks = {
    'Chemistry': [67, 90, 66, 32],
    'Physics': [45, 92, 72, 40],
    'Mathematics': [50, 87, 81, 12],
    'English': [19, 90, 72, 68]
}
marks_df = pd.DataFrame(marks, index=['Subodh', 'Ram', 'Abdul',
                                      'John'])
print("Initial dataframe:")
print(marks_df)
print()

# Create a new column 'Total'
marks_df['Total'] = marks_df.sum(axis=1)
print("Dataframe with Total column:")
print(marks_df)
print()

# Drop the Total column
marks_df = marks_df.drop(columns='Total')
print("Dataframe after dropping Total column:")
print(marks_df)
print()

# Add 5 bonus marks to all students
marks_df_bonus = marks_df + 5
print("Dataframe after adding 5 bonus marks:")
print(marks_df_bonus)
print()

# Increase marks as specified
increase = pd.Series({'Chemistry': 5, 'Physics': 10, 'Mathematics': 10, 'English': 2})
marks_df_increased = marks_df + increase
print("Dataframe after increasing marks:")
print(marks_df_increased)
print()

# Get total marks scored in each subject
subject_totals = marks_df.sum()
print("Total marks scored in each subject:")
print(subject_totals)
print()

# Get total marks scored by each student
student_totals = marks_df.sum(axis=1)
print("Total marks scored by each student:")
print(student_totals)
print()

# Hide marks less than 35 and display 'Fail'
marks_df_fail = marks_df.mask(marks_df < 35, 'Fail')
print("Dataframe with 'Fail' for marks less than 35:")
print(marks_df_fail)
