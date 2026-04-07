import pandas as pd
from collections import Counter

df = pd.read_csv("clean_reviews.csv")

# Combine all reviews
all_text = " ".join(df["Clean_Review"].astype(str))

# Split words
words = all_text.split()

# Count frequency
word_counts = Counter(words)

print("\nTop 10 Words Used In Reviews:")

for word, count in word_counts.most_common(10):
    print(word, ":", count)