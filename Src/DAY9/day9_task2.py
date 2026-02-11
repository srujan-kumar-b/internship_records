import pandas as pd

grades = pd.Series([85, None, 92, 45, None, 78, 55])

print("Original Grades:")
print(grades)

print("\nMissing Values:")
print(grades.isnull())

filled = grades.fillna(0)

print("\nAfter Filling Missing Values:")
print(filled)

print("\nScores Greater Than 60:")
print(filled[filled > 60])
