import streamlit as st
import pandas as pd
import subprocess
from collections import Counter
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

st.title("Product Review Sentiment Analyzer")

product_link = st.text_input("Paste Product Link")

if st.button("Analyze Reviews"):

    st.write("Running analysis...")

    # Run the full pipeline
    subprocess.run(["python", "main.py"])

    # Load sentiment results
    df = pd.read_csv("sentiment_results.csv")

    sentiment_counts = df["Sentiment"].value_counts()

    st.subheader("Sentiment Distribution")

    st.bar_chart(sentiment_counts)

    positive = sentiment_counts.get("Positive", 0)
    negative = sentiment_counts.get("Negative", 0)
    neutral = sentiment_counts.get("Neutral", 0)

    total = positive + negative + neutral

    st.subheader("Sentiment Percentages")

    st.write("Positive:", round((positive/total)*100,2), "%")
    st.write("Negative:", round((negative/total)*100,2), "%")
    st.write("Neutral:", round((neutral/total)*100,2), "%")

    st.subheader("Product Recommendation")

    if positive > negative:
        st.success("BUY THIS PRODUCT")
    elif negative > positive:
        st.error("DO NOT BUY THIS PRODUCT")
    else:
        st.warning("PRODUCT HAS MIXED REVIEWS")

    confidence = abs(positive - negative) / total * 100

    st.write("Confidence Score:", round(confidence,2), "%")

    # Aspect analysis
    positive_reviews = df[df["Sentiment"] == "Positive"]["Clean_Review"]
    negative_reviews = df[df["Sentiment"] == "Negative"]["Clean_Review"]

    pos_words = " ".join(positive_reviews).lower().split()
    pos_words = [word for word in pos_words if word not in stop_words]

    neg_words = " ".join(negative_reviews).lower().split()
    neg_words = [word for word in neg_words if word not in stop_words]

    pos_count = Counter(pos_words)
    neg_count = Counter(neg_words)

    st.subheader("Positive Aspects Customers Like")

    for word, count in pos_count.most_common(5):
        st.write(word, ":", count)

    st.subheader("Negative Aspects Customers Dislike")

    for word, count in neg_count.most_common(5):
        st.write(word, ":", count)

    # Fake review detection
    clean_df = pd.read_csv("clean_reviews.csv")

    fake_count = 0

    for review in clean_df["Clean_Review"]:
        if len(review.split()) < 3:
            fake_count += 1

    st.subheader("Fake Review Detection")

    st.write("Possible Fake Reviews:", fake_count)