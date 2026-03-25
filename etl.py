import pandas as pd

# -------------------------------
# EXTRACT (Read CSV file)
# -------------------------------
file_path = "data/sales.csv"

try:
    df = pd.read_csv(file_path)
    print("Data Loaded Successfully!\n")
    print(df.head())
except Exception as e:
    print("Error loading file:", e)
    exit()

# -------------------------------
# TRANSFORM (Clean Data)
# -------------------------------

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values with 0
df = df.fillna(0)

# Convert column names to lowercase
df.columns = df.columns.str.lower()

print("\nData Cleaned Successfully!\n")

# -------------------------------
# LOAD (Save Clean Data)
# -------------------------------
output_file = "cleaned_data.csv"

try:
    df.to_csv(output_file, index=False)
    print("Cleaned data saved as:", output_file)
except Exception as e:
    print("Error saving file:", e)