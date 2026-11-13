import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("data - data.csv")

df = data[data["scenario"] == "05_AdVsRevenue"]

df["study_hours"] = pd.to_numeric(df["study_hours"])
df["exam_score"] = pd.to_numeric(df["exam_score"])

sns.regplot(
    data=df,
    x="study_hours",
    y="exam_score",
    scatter_kws={"color": "darkgreen", "marker": "+"}
)

plt.title("Impact of Advertising Spend on Total Revenue")
plt.xlabel("Ad Spend ($)")
plt.ylabel("Revenue ($)")

plt.grid(True)

plt.show()