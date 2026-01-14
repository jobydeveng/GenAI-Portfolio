"""
Sample script to populate initial categories based on the spreadsheet
Run this after setting up the database to quickly add all categories
"""
from db_operations import add_category

# Categories from your spreadsheet
categories = [
    ("coin", "Cryptocurrency investments"),
    ("upstock", "Upstox stock portfolio"),
    ("kite", "Zerodha Kite trading account"),
    ("DCX", "DCX Exchange"),
    ("vest", "Vest investment platform"),
    ("f1", "Fund 1"),
    ("rd", "Recurring Deposit"),
    ("f2", "Fund 2"),
    ("f3", "Fund 3"),
    ("bin", "Binary/Binance"),
    ("pf", "Provident Fund"),
    ("nps", "National Pension Scheme")
]

def populate_categories():
    """Add all sample categories to database"""
    print("Starting to add categories...\n")
    
    success_count = 0
    error_count = 0
    
    for category_name, description in categories:
        success, message = add_category(category_name, description)
        if success:
            print(f"✓ {message}: {category_name}")
            success_count += 1
        else:
            print(f"✗ {message}: {category_name}")
            error_count += 1
    
    print(f"\n{'='*50}")
    print(f"Summary:")
    print(f"  Successfully added: {success_count}")
    print(f"  Errors: {error_count}")
    print(f"{'='*50}")

if __name__ == "__main__":
    print("="*50)
    print("Portfolio Categories Setup")
    print("="*50)
    print("\nThis script will add initial categories to your database.")
    print("Make sure your .env file is configured with correct DB credentials.\n")
    
    response = input("Continue? (y/n): ")
    if response.lower() == 'y':
        populate_categories()
        print("\nYou can now run the Streamlit app: streamlit run app.py")
    else:
        print("Cancelled.")

