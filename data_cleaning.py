import pandas as pd

# Load the manually created clean reviews
df = pd.read_csv("clean_reviews.csv")

# Remove empty rows
df = df.dropna()

# Save again to ensure clean format
df.to_csv("clean_reviews.csv", index=False)

print("Data cleaning completed. Using manual reviews dataset.")