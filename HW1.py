"""Uses seaborn.violinplot for a visual that shows the distribution shape of income data across education levels.

Demonstrates clear economic modeling application (education vs. income).

Can be modified for real-world datasets, e.g., from pandas-datareader or public sources like OECD.

"""


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data: Income distributions by education level
data = {
    "Income": [35, 40, 45, 38, 50, 55, 52, 49, 60, 65, 62, 61, 70, 68, 75, 72],
    "Education": [
        "High School", "High School", "High School", "High School",
        "Bachelor", "Bachelor", "Bachelor", "Bachelor",
        "Master", "Master", "Master", "Master",
        "PhD", "PhD", "PhD", "PhD"
    ]
}

df = pd.DataFrame(data)

# Create the violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x="Education", y="Income", data=df, palette="muted")

plt.title("Income Distribution by Education Level")
plt.ylabel("Annual Income (in $1000s)")
plt.xlabel("Education Level")
plt.grid(True)
plt.tight_layout()
plt.show()