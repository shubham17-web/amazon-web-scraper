# ============================================================
# Amazon-Style Web Scraper
# Main Program
# ============================================================

from scraper.scraper import scrape_products
from scraper.cleaner import clean_data

from analysis.analysis import (
    basic_analysis,
    price_analysis,
    track_price_history,
    detect_price_changes,
    final_summary
)

from storage.storage import save_products


def main():

    # ========================================================
    # 1. SCRAPE DATA
    # ========================================================

    print("\nStarting scraper...")

    data = scrape_products()


    # ========================================================
    # 2. CLEAN DATA
    # ========================================================

    df = clean_data(data)


    # ========================================================
    # 3. SAVE LATEST DATASET
    # ========================================================

    save_products(df)


    # ========================================================
    # 4. BASIC ANALYSIS
    # ========================================================

    basic_analysis(df)


    # ========================================================
    # 5. PRICE ANALYSIS
    # ========================================================

    price_analysis(df)


    # ========================================================
    # 6. HISTORICAL PRICE TRACKING
    # ========================================================

    history = track_price_history(df)


    # ========================================================
    # 7. PRICE CHANGE DETECTION
    # ========================================================

    (
        history,
        price_drops,
        price_increases
    ) = detect_price_changes(history)


    # ========================================================
    # 8. FINAL SUMMARY
    # ========================================================

    final_summary(
        df,
        price_drops,
        price_increases
    )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main() #If I'm running this file directly, start the program from main()