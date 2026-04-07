import pandas as pd
import matplotlib.pyplot as plt

# Read sentiment results
df = pd.read_csv("sentiment_results.csv")

# Count sentiments
sentiment_counts = df["Sentiment"].value_counts()

print("\nSentiment Distribution:")
print(sentiment_counts)

# Plot graph
sentiment_counts.plot(kind="bar")

plt.title("Sentiment Analysis of Product Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

plt.show()