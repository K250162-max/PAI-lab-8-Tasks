import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("data - data.csv")

df = data[data["scenario"] == "03_SalaryDiff"]

sns.boxplot(
    data=df,
    x="prep_course",
    y="exam_score",
    order=["Entry", "Mid", "Senior"],
    palette="Set2"
)

plt.title("Salary Spread Across Experience Levels")
plt.xlabel("Experience Level")
plt.ylabel("Salary ($)")

plt.show()