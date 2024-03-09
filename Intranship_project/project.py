import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Function to generate random dates within a specified range
def random_dates(start_date, end_date, n=100000):
    date_range = (end_date - start_date).days
    random_dates = [start_date + timedelta(days=np.random.randint(date_range)) for _ in range(n)]
    return sorted(random_dates)

# Function to simulate complex retail sales data with seasonality and trends
def generate_complex_retail_data(start_date, end_date, products=['smartphones', 'laptops', 'headphones','Smartwatches','Televisions ','Tablets']):
    dates = random_dates(start_date, end_date, n=1098)  # Simulate data for one year

    data = []
    for product in products:
        base_sales = np.random.randint(50000, 150000)
        trend = np.linspace(0, 20000, len(dates)) + np.random.normal(0, 50000, len(dates))
        seasonality = 10 * np.sin(np.arange(len(dates)) * (2 * np.pi / 1098))
        random_noise = np.random.normal(0, 4000, len(dates))
        sales = base_sales + trend + seasonality + random_noise

        product_data = {'Date': dates, 'ProductName': [product] * len(dates), 'MonthlySales': sales,}
        data.append(pd.DataFrame(product_data))

    return pd.concat(data, ignore_index=True)

# Define the date range for the dataset
start_date = datetime(2019, 1, 1)
end_date = datetime(2023, 12, 31)

# List of products to simulate
product_list = [ 'smartphones', 'laptops', 'headphones','Smartwatches','Televisions ','Tablets',]

# Generate a complex retail dataset for multiple products
complex_retail_dataset = generate_complex_retail_data(start_date, end_date, products=product_list)

# Save the dataset to a CSV file
complex_retail_dataset.to_csv('complex_retail_demand_forecast_dataset.csv', index=False)