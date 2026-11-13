import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("data - data.csv")

df = data[data["scenario"] == "04_CustAgeDist"]

sns.histplot(
    data=df,
    x="study_hours",
    bins=5,
    hue="prep_course",
    kde=True
)

plt.title("Customer Age Distribution by Gender")
plt.xlabel("Age")
plt.ylabel("Customer Count")

plt.show()