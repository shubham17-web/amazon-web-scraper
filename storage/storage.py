import pandas as pd


def save_products(df):
    """
    Save the latest scraped dataset.
    """

    file_path = "data/products_data.csv"

    df.to_csv(
        file_path,
        index=False
    )

    print("\nDataset saved successfully!")

    return file_path