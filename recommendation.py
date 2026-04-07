import pandas as pd

# Read sentiment results
df = pd.read_csv("sentiment_results.csv")

# Count sentiments
positive = len(df[df["Sentiment"] == "Positive"])
negative = len(df[df["Sentiment"] == "Negative"])
neutral = len(df[df["Sentiment"] == "Neutral"])

print("Positive Reviews:", positive)
print("Negative Reviews:", negative)
print("Neutral Reviews:", neutral)

# Calculate total reviews
total = positive + negative + neutral

# Calculate percentages
positive_percent = (positive / total) * 100
negative_percent = (negative / total) * 100
neutral_percent = (neutral / total) * 100

print("\nSentiment Percentage:")
print("Positive:", round(positive_percent,2), "%")
print("Negative:", round(negative_percent,2), "%")
print("Neutral:", round(neutral_percent,2), "%")

# Recommendation logic
print("\nProduct Recommendation:")

if positive > negative:
    print("BUY THIS PRODUCT")
elif negative > positive:
    print("DO NOT BUY THIS PRODUCT")
else:
    print("PRODUCT HAS MIXED REVIEWS")

# Confidence score
confidence = abs(positive - negative) / total * 100

print("\nConfidence Score:", round(confidence,2), "%")