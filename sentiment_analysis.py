import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_csv("clean_reviews.csv")

analyzer = SentimentIntensityAnalyzer()

sentiments = []

for review in df["Clean_Review"]:
    
    score = analyzer.polarity_scores(str(review))
    
    if score["compound"] >= 0.05:
        sentiments.append("Positive")
    elif score["compound"] <= -0.05:
        sentiments.append("Negative")
    else:
        sentiments.append("Neutral")

df["Sentiment"] = sentiments

df.to_csv("sentiment_results.csv", index=False)

print("Sentiment analysis completed. Results saved to sentiment_results.csv")