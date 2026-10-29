import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee.csv")

print(df[["Name", "Department", "Salary"]])

avg_salary = df.groupby("Department")["Salary"].mean()

print("Average Salary by Department:")
print(avg_salary)

avg_salary.plot(kind="bar")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()