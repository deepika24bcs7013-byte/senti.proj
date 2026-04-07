import subprocess

print("STEP 1: Using existing reviews dataset")

print("\nSTEP 2: Cleaning the data...")
subprocess.run(["python", "data_cleaning.py"])

print("\nSTEP 3: Performing sentiment analysis...")
subprocess.run(["python", "sentiment_analysis.py"])

print("\nSTEP 4: Generating sentiment graph...")
subprocess.run(["python", "visualisation.py"])

print("\nSTEP 5: Product recommendation...")
subprocess.run(["python", "recommendation.py"])

print("\nSTEP 6: Word analysis...")
subprocess.run(["python", "word_analysis.py"])

print("\nSTEP 7: Fake review detection...")
subprocess.run(["python", "fake_review_detector.py"])

print("\nALL ANALYSIS COMPLETED SUCCESSFULLY")