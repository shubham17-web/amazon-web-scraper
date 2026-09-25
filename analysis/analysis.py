import pandas as pd


def basic_analysis(df):
    """
    Display basic statistics about the dataset.
    """

    print("\n================ TOTAL PRODUCTS ================")
    print(len(df))

    print("\n================ AVERAGE PRICE ================")
    print(round(df["price"].mean(), 2))

    print("\n================ MINIMUM PRICE ================")
    print(df["price"].min())

    print("\n================ MAXIMUM PRICE ================")
    print(df["price"].max())

    print("\n================ AVERAGE RATING ================")
    print(round(df["rating"].mean(), 2))

    print("\n================ RATING DISTRIBUTION ================")
    print(df["rating"].value_counts().sort_index())

    print("\n================ AVAILABILITY ================")
    print(df["availability"].value_counts())


def price_analysis(df):
    """
    Display the cheapest and most expensive products.
    """

    top_expensive = df.nlargest(10, "price")

    print("\n================ TOP 10 MOST EXPENSIVE ================")
    print(
        top_expensive[
            ["title", "price", "rating"]
        ]
    )

    top_cheap = df.nsmallest(10, "price")

    print("\n================ TOP 10 CHEAPEST ================")
    print(
        top_cheap[
            ["title", "price", "rating"]
        ]
    )


def track_price_history(df):
    """
    Store historical product prices.
    """

    historical_file = "data/price_history.csv"

    history_data = df[
        ["title", "price", "product_url", "scraped_date"]
    ].copy()

    try:
        old_history = pd.read_csv(historical_file)

        history = pd.concat(
            [old_history, history_data],
            ignore_index=True
        )

    except FileNotFoundError:

        history = history_data

    history = history.drop_duplicates(
        subset=["product_url", "scraped_date"],
        keep="last"
    )

    history.to_csv(
        historical_file,
        index=False
    )

    print("\nHistorical price data saved successfully!")

    return history


def detect_price_changes(history):
    """
    Detect product price increases and decreases.
    """

    history = history.sort_values(
        ["product_url", "scraped_date"]
    ).copy()

    history["previous_price"] = (
        history
        .groupby("product_url")["price"]
        .shift(1)
    )

    history["price_change"] = (
        history["price"] -
        history["previous_price"]
    )

    price_drops = history[
        history["price_change"] < 0
    ]

    price_increases = history[
        history["price_change"] > 0
    ]

    print("\n================ PRICE DROPS ================")

    print(
        price_drops[
            [
                "title",
                "previous_price",
                "price",
                "price_change",
                "scraped_date"
            ]
        ]
    )

    print("\n================ PRICE INCREASES ================")

    print(
        price_increases[
            [
                "title",
                "previous_price",
                "price",
                "price_change",
                "scraped_date"
            ]
        ]
    )

    return history, price_drops, price_increases


def final_summary(
    df,
    price_drops,
    price_increases
):
    """
    Display final project summary.
    """

    print("\n================ FINAL SUMMARY ================")

    print(
        "Total Products:",
        len(df)
    )

    print(
        "Average Price:",
        round(df["price"].mean(), 2)
    )

    print(
        "Minimum Price:",
        df["price"].min()
    )

    print(
        "Maximum Price:",
        df["price"].max()
    )

    print(
        "Average Rating:",
        round(df["rating"].mean(), 2)
    )

    print(
        "Price Drops:",
        len(price_drops)
    )

    print(
        "Price Increases:",
        len(price_increases)
    )

    most_expensive = df.loc[
        df["price"].idxmax()
    ]

    print("\nMost Expensive Product:")

    print(
        most_expensive[
            ["title", "price", "rating"]
        ]
    )

    cheapest = df.loc[
        df["price"].idxmin()
    ]

    print("\nCheapest Product:")

    print(
        cheapest[
            ["title", "price", "rating"]
        ]
    )