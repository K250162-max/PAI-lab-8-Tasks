import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("data - data.csv")

df = data[data["scenario"] == "01_StudyVsScore"]

sns.scatterplot(
    data=df,
    x="study_hours",
    y="exam_score",
    hue="prep_course",
    style="prep_course"
)

plt.title("Study Hours vs. Exam Score by Prep Course Status")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)

plt.show()