import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('iacs_metrics_cleaned.csv')

# Plot holder growth
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Unique Holders (Cumulative)'], color='blue')
plt.title('$IACS Unique Holders Over Time')
plt.xlabel('Date')
plt.ylabel('Unique Holders')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
