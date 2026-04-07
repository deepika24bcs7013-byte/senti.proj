import pandas as pd

df = pd.read_csv("clean_reviews.csv")

fake_count = 0

for review in df["Clean_Review"]:
    
    if len(review.split()) < 3:
        fake_count += 1

print("Possible Fake Reviews:", fake_count)