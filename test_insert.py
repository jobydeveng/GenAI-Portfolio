"""
Test script to verify the sequence fix is working
"""

from db_operations import save_portfolio_value, get_or_create_month
from datetime import date

def test_insert():
    """
    Test inserting a portfolio value to verify the sequence fix
    """
    print("=" * 60)
    print("Testing Portfolio Value Insert")
    print("=" * 60)
    print()
    
    # Test data
    year = 2026
    month = 2
    snapshot_date = date(2026, 2, 16)
    category_id = 1  # Assuming category 1 exists
    test_amount = 10000.00
    
    print(f"Test Parameters:")
    print(f"  - Year: {year}")
    print(f"  - Month: {month}")
    print(f"  - Snapshot Date: {snapshot_date}")
    print(f"  - Category ID: {category_id}")
    print(f"  - Amount: {test_amount}")
    print()
    
    # Get or create month
    print("Step 1: Getting/creating month entry...")
    month_id = get_or_create_month(year, month, snapshot_date)
    
    if not month_id:
        print("[ERROR] Failed to get/create month entry")
        return False
    
    print(f"[SUCCESS] Month ID: {month_id}")
    print()
    
    # Try to save portfolio value
    print("Step 2: Saving portfolio value...")
    success, message = save_portfolio_value(month_id, category_id, test_amount)
    
    if success:
        print(f"[SUCCESS] {message}")
        print()
        print("=" * 60)
        print("[SUCCESS] Test completed successfully!")
        print("The sequence fix is working correctly.")
        print("=" * 60)
        return True
    else:
        print(f"[ERROR] {message}")
        print()
        print("=" * 60)
        print("[ERROR] Test failed!")
        print("There may still be issues with the database.")
        print("=" * 60)
        return False

if __name__ == "__main__":
    test_insert()
