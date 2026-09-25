import pandas as pd


def clean_data(data):

    # Convert scraped list into DataFrame
    df = pd.DataFrame(data)

    # Convert rating words into numbers
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    df["rating"] = df["rating"].map(rating_map)

    # Clean price
    df["price"] = (
        df["price"]
        .str.replace("Â£", "", regex=False)
        .str.replace("£", "", regex=False)
        .astype(float)
    )

    return df