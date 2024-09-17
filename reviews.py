# Import packages
import pandas as pd
import pytest

# read in wine reviews data
wine_reviews_df = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

# Take a look at the data
print(wine_reviews_df.head())
columns = wine_reviews_df.columns.tolist()
# print(columns)

# Summary
summary = wine_reviews_df.groupby("country").agg(
    count=("title", "count"),
    points=("points", "mean")
).reset_index()

# Sort the summary by number of reviews
summary = summary.sort_values(by="count", ascending=False)

# Round the points column to 1 decimal point
summary["points"] = summary["points"].round(1)

# Print the new summary
print(summary)

# Write the summary data to a new file in the data folder
summary.to_csv("data/reviews-per-country.csv", index=False)