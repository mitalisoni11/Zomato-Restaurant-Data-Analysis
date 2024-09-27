# Zomato Bengaluru Restaurant Data Analysis
Using Pandas, Numpy, Matplotlib and Seaborn packages in Python I analyzed a dataset of Zomato Bengaluru restaurants to determine the optimal location, service offerings, and pricing strategy for opening a new restaurant. The analysis focuses on identifying underserved locations, popular services, and pricing benchmarks to maximize the restaurant's success.

# Data Cleaning
- Cleaned the rate column by replacing non-numeric and null values with the mean rating.
- Dropped rows with null values in location, rest_type, cuisines, and approx_cost columns as the missing records count was below 1,000.
- Removed the redundant listed_in(city) column due to similarity with the location column.
- Converted the Cost2people column to a float for accurate analysis.
- Clustered categories in rest_type, location, and cuisine with low occurrences into an "others" category for better clarity in visualization.

# Data Visualization
- **Location Analysis** : A countplot revealed that BTM has the highest concentration of restaurants, signaling potential market saturation. Less saturated areas, like St. Marks Road and Commercial Street, could be viable locations. However, factors like rent and population density need further consideration.

![location_countplot](https://github.com/user-attachments/assets/3defb806-713f-42e1-b9fe-4f7896602e24)

- **Online Ordering**: Most restaurants offer online ordering, making it a popular service. A boxplot comparing customer ratings for restaurants with and without this service showed that those offering online orders had a higher maximum rating and positive skew. Thus, offering online orders could improve customer satisfaction and increase competitiveness.

![online_order_countplot](https://github.com/user-attachments/assets/facf80ba-5eb5-4c96-83e1-3254fd72c23d)

![online_order_vs_rate_boxplot](https://github.com/user-attachments/assets/a65ee0a7-44b7-441e-ad7d-3db2884edbcc)

- **Table Booking**: We created a countplot to compare the number of restaurants offering vs. not offering the book table service. The results showed that the majority of restaurants do not provide this service, suggesting it might not be essential. However, further analysis using a boxplot revealed that restaurants offering the book table feature had a significantly higher median rating, while those without it had a wider IQR and lower maximum rating. Based on these insights, offering the book table service could potentially enhance customer satisfaction and boost overall performance.

![book_table_countplot](https://github.com/user-attachments/assets/b11bf754-cde5-4fa7-b238-fcc05c3640a3)

![book_table_vs_rate_boxplot](https://github.com/user-attachments/assets/d03ed01f-6640-4415-8f1b-af69109b261e)

- **Service Trends by Location**: Visualizing the online ordering and table booking services across different locations provided insights into customer preferences. In areas where online orders dominate, a focus on delivery infrastructure is essential. Conversely, areas with high dine-in preference may require more investment in on-site dining facilities.

![online_order_vs_location](https://github.com/user-attachments/assets/133f05d3-b169-4f09-acda-4fdef9174fbf)

![book_table_vs_location](https://github.com/user-attachments/assets/f9a90178-8f7a-4d14-a828-9f141a71e010)

- **Restaurant Type vs. Rating**: Casual dining and casual dining with bars consistently performed well in ratings, indicating their popularity. Dessert parlors and cafes also showed promising results, suggesting these types of establishments may be well-received.

![rest_type_vs_rate_boxplot](https://github.com/user-attachments/assets/44298ba2-3b49-4560-ae7b-8a42412b1955)

- Cuisine Performance: Analyzing cuisines and their success rates across different locations helped identify which cuisines to include in the new restaurant. Cuisines like North Indian, South Indian and Chinese seem to be really popular. Offering popular cuisines tailored to the location could increase the restaurant's appeal and success rate.

![top_cuisines_bar](https://github.com/user-attachments/assets/3faedaf2-c1da-471d-b8ad-4b125ef90f17)

