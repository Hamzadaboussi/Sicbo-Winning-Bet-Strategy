import pandas as pd
import numpy as np

# Set the random seed for reproducibility


# Function to generate random data
def generate_random_data(num_rows):
    data = {'time': pd.date_range(start="2023-03-10 22:32:00", periods=num_rows, freq='T'),
            'dice11': np.random.randint(1, 7, size=num_rows),
            'dice12': np.random.randint(1, 7, size=num_rows),
            'dice13': np.random.randint(1, 7, size=num_rows)}

    # Convert the data dictionary to a pandas DataFrame
    df = pd.DataFrame(data)

    # Calculate total1
    df['total1'] = df['dice11'] + df['dice12'] + df['dice13']

    # Shift the 'total1' column and fill NaN values with 0
    df['result'] = df['total1'].shift().fillna(0).astype(int)

    # Set the first row of 'result' column to 0
    df.at[0, 'result'] = 0

    # Calculate totalwinners
    df['totalwinners'] = np.random.randint(140, 280, size=num_rows)

    # Rearrange columns
    columns_order = ['time', 'totalwinners', 'dice11', 'dice12', 'dice13', 'total1', 'result']
    df = df[columns_order]

    return df

# Generate random data with 60000 rows
num_rows = 1000000
random_data = generate_random_data(num_rows)
random_data['time'] = random_data['time'].dt.strftime('%Y-%m-%d %H:%M:%S')
# Save the DataFrame to an Excel file
excel_file_path = r'C:\Users\daboussi\Desktop\Data\very_big_Random_data.xlsx'
random_data.to_excel(excel_file_path, index=False)

# Display the first few rows of the generated data
print(random_data.head())
