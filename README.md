# Zomato Bengaluru Restaurant Data Analysis
Using Pandas, Numpy, Matplotlib and Seaborn packages in Python I analyzed a dataset of Zomato Bengaluru restaurants to determine the optimal location, service offerings, and pricing strategy for opening a new restaurant. The analysis focuses on identifying underserved locations, popular services, and pricing benchmarks to maximize the restaurant's success.

# Data Cleaning
- Cleaned the rate column by replacing non-numeric and null values with the mean rating.
- Dropped rows with null values in location, rest_type, cuisines, and approx_cost columns as the missing records count was below 1,000.
- Removed the redundant listed_in(city) column due to similarity with the location column.
- Converted the Cost2people column to a float for accurate analysis.
- Clustered categories in rest_type, location, and cuisine with low occurrences into an "others" category for better clarity in visualization.

# Data Visualization
