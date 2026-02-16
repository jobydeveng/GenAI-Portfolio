"""
Fix PostgreSQL sequence for portfolio_value table

This script resets the sequence for value_id to the correct value
to prevent duplicate key errors.
"""

from db_config import get_db_connection, close_connection


def fix_portfolio_value_sequence():
    """
    Reset the sequence for portfolio_value.value_id to prevent duplicate key errors.
    
    This happens when:
    - Data was manually inserted
    - Database was migrated
    - Sequence got out of sync
    """
    connection = get_db_connection()
    if not connection:
        print("[ERROR] Failed to connect to database")
        return False
    
    cursor = None
    try:
        cursor = connection.cursor()
        
        # Get the current maximum value_id
        cursor.execute("SELECT MAX(value_id) FROM portfolio_value")
        result = cursor.fetchone()
        max_id = result[0] if result and result[0] else 0
        
        print(f"[INFO] Current maximum value_id: {max_id}")
        
        # Reset the sequence to max_id + 1
        next_id = max_id + 1
        cursor.execute(
            "SELECT setval('portfolio_value_value_id_seq', %s, false)",
            (next_id,)
        )
        
        connection.commit()
        print(f"[SUCCESS] Sequence reset successfully! Next value_id will be: {next_id}")
        return True
        
    except Exception as e:
        print(f"[ERROR] Error fixing sequence: {e}")
        connection.rollback()
        return False
        
    finally:
        if cursor:
            cursor.close()
        close_connection(connection)


def verify_sequence():
    """
    Verify that the sequence is working correctly
    """
    connection = get_db_connection()
    if not connection:
        print("[ERROR] Failed to connect to database")
        return False
    
    cursor = None
    try:
        cursor = connection.cursor()
        
        # Get current sequence value
        cursor.execute("SELECT last_value FROM portfolio_value_value_id_seq")
        seq_value = cursor.fetchone()[0]
        
        # Get max value_id from table
        cursor.execute("SELECT MAX(value_id) FROM portfolio_value")
        result = cursor.fetchone()
        max_id = result[0] if result and result[0] else 0
        
        print(f"\n[INFO] Verification:")
        print(f"   - Sequence last_value: {seq_value}")
        print(f"   - Maximum value_id in table: {max_id}")
        
        if seq_value > max_id:
            print(f"   [SUCCESS] Sequence is correct! Next ID will be: {seq_value}")
            return True
        else:
            print(f"   [WARNING] Sequence needs adjustment")
            return False
            
    except Exception as e:
        print(f"[ERROR] Error verifying sequence: {e}")
        return False
        
    finally:
        if cursor:
            cursor.close()
        close_connection(connection)


def main():
    """
    Main function to fix and verify the sequence
    """
    print("=" * 60)
    print("PostgreSQL Sequence Fix Utility")
    print("=" * 60)
    print()
    
    print("Step 1: Checking current sequence status...")
    verify_sequence()
    
    print("\nStep 2: Fixing sequence...")
    success = fix_portfolio_value_sequence()
    
    if success:
        print("\nStep 3: Verifying fix...")
        verify_sequence()
        print("\n" + "=" * 60)
        print("[SUCCESS] All done! You can now use the app without errors.")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("[ERROR] Failed to fix sequence. Please check the error messages above.")
        print("=" * 60)


if __name__ == "__main__":
    main()
