import pandas as pd

def clean_data(filename="ebay_tech_deals.csv"):
    # Load the CSV file with all columns as strings
    df = pd.read_csv(filename, dtype=str)

    # Clean the 'price' and 'original_price' columns by removing 'US $' and commas
    df['price'] = df['price'].replace({'US \$': '', ',': ''}, regex=True).str.strip()
    df['original_price'] = df['original_price'].replace({'US \$': '', ',': ''}, regex=True).str.strip()

    # If 'original_price' is missing or 'N/A', replace it with the corresponding 'price'
    df['original_price'] = df['original_price'].replace({'N/A': '', '': None})
    df['original_price'].fillna(df['price'], inplace=True)

    # Clean the 'shipping' column by replacing empty strings or 'N/A' with a default message
    # Clean the shipping column
    df["shipping"] = df["shipping"].apply(
        lambda shipping: "Shipping info unavailable" if pd.isna(
            shipping) or shipping.strip() == "" or shipping.strip() == "N/A" else shipping.strip()
    )


    # Convert 'price' and 'original_price' columns to numeric values (float)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['original_price'] = pd.to_numeric(df['original_price'], errors='coerce')

    # Create a new column 'discount_percentage' computed as:
    df['discount_percentage'] = ((df['original_price'] - df['price']) / df['original_price']) * 100
    df['discount_percentage'] = df['discount_percentage'].round(2)

    # Save the cleaned data to a new CSV file
    cleaned_filename = "cleaned_ebay_deals.csv"
    df.to_csv(cleaned_filename, index=False)

    print(f"Cleaned data saved to {cleaned_filename}")

if __name__ == "__main__":
    clean_data()
