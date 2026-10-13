import pandas as pd  # type: ignore[import-not-found]
import matplotlib.pyplot as plt  # type: ignore[import-not-found]

# Dataset
data = {
    "Statistic": [
        "Points Per Game",
        "Rebounds Per Game",
        "Assists Per Game",
        "Field Goal %"
    ],
    "Value": [
        30.1,
        6.2,
        5.3,
        49.7
    ]
}

df = pd.DataFrame(data)

# Grafico a barre
plt.figure(figsize=(10, 6))
plt.bar(
    df["Statistic"],
    df["Value"],
    color=["red", "blue", "green", "orange"]
)

plt.title("Michael Jordan Career Statistics")
plt.ylabel("Value")
plt.xlabel("Statistic")
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, value in enumerate(df["Value"]):
    plt.text(i, value + 0.5, str(value), ha="center")

plt.tight_layout()
plt.show()