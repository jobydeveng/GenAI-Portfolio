"""
Database operations for portfolio management
"""
from db_config import get_db_connection, close_connection
from datetime import date
from typing import List, Dict, Optional, Tuple

def get_all_categories() -> List[Dict]:
    """
    Fetch all active investment categories
    """
    connection = get_db_connection()
    if not connection:
        return []
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT category_id, category_name, description, is_active, created_at
            FROM investment_category
            WHERE is_active = TRUE
            ORDER BY category_name
        """
        cursor.execute(query)
        categories = cursor.fetchall()
        return categories
    except Exception as e:
        print(f"Error fetching categories: {e}")
        return []
    finally:
        cursor.close()
        close_connection(connection)

def add_category(category_name: str, description: str = "") -> Tuple[bool, str]:
    """
    Add a new investment category
    Returns: (success: bool, message: str)
    """
    connection = get_db_connection()
    if not connection:
        return False, "Database connection failed"
    
    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO investment_category (category_name, description)
            VALUES (%s, %s)
        """
        cursor.execute(query, (category_name, description))
        connection.commit()
        return True, "Category added successfully"
    except Exception as e:
        connection.rollback()
        if "Duplicate entry" in str(e):
            return False, f"Category '{category_name}' already exists"
        return False, f"Error adding category: {e}"
    finally:
        cursor.close()
        close_connection(connection)

def get_or_create_month(year: int, month: int, snapshot_date: date) -> Optional[int]:
    """
    Get existing month_id or create new portfolio_month entry
    Returns: month_id or None
    """
    connection = get_db_connection()
    if not connection:
        return None
    
    try:
        cursor = connection.cursor()
        
        # Check if month already exists
        check_query = """
            SELECT month_id FROM portfolio_month
            WHERE year = %s AND month = %s
        """
        cursor.execute(check_query, (year, month))
        result = cursor.fetchone()
        
        if result:
            return result[0]
        
        # Create new month entry
        insert_query = """
            INSERT INTO portfolio_month (year, month, snapshot_date)
            VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (year, month, snapshot_date))
        connection.commit()
        return cursor.lastrowid
        
    except Exception as e:
        connection.rollback()
        print(f"Error getting/creating month: {e}")
        return None
    finally:
        cursor.close()
        close_connection(connection)

def save_portfolio_value(month_id: int, category_id: int, amount: float) -> Tuple[bool, str]:
    """
    Save or update portfolio value for a specific month and category
    Returns: (success: bool, message: str)
    """
    connection = get_db_connection()
    if not connection:
        return False, "Database connection failed"
    
    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO portfolio_value (month_id, category_id, amount)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE amount = %s, updated_at = CURRENT_TIMESTAMP
        """
        cursor.execute(query, (month_id, category_id, amount, amount))
        connection.commit()
        return True, "Portfolio value saved successfully"
    except Exception as e:
        connection.rollback()
        return False, f"Error saving portfolio value: {e}"
    finally:
        cursor.close()
        close_connection(connection)

def get_portfolio_data(year: Optional[int] = None, month: Optional[int] = None) -> List[Dict]:
    """
    Fetch portfolio data with optional year/month filter
    """
    connection = get_db_connection()
    if not connection:
        return []
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT 
                pm.year,
                pm.month,
                pm.snapshot_date,
                ic.category_name,
                pv.amount,
                pv.updated_at
            FROM portfolio_value pv
            JOIN portfolio_month pm ON pv.month_id = pm.month_id
            JOIN investment_category ic ON pv.category_id = ic.category_id
            WHERE 1=1
        """
        params = []
        
        if year:
            query += " AND pm.year = %s"
            params.append(year)
        
        if month:
            query += " AND pm.month = %s"
            params.append(month)
        
        query += " ORDER BY pm.year DESC, pm.month DESC, ic.category_name"
        
        cursor.execute(query, params)
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(f"Error fetching portfolio data: {e}")
        return []
    finally:
        cursor.close()
        close_connection(connection)

def get_all_months() -> List[Dict]:
    """
    Fetch all available months/years
    """
    connection = get_db_connection()
    if not connection:
        return []
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT month_id, year, month, snapshot_date
            FROM portfolio_month
            ORDER BY year DESC, month DESC
        """
        cursor.execute(query)
        months = cursor.fetchall()
        return months
    except Exception as e:
        print(f"Error fetching months: {e}")
        return []
    finally:
        cursor.close()
        close_connection(connection)

def get_monthly_summary(year: int, month: int) -> Dict:
    """
    Get total portfolio value for a specific month
    """
    connection = get_db_connection()
    if not connection:
        return {}
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT 
                pm.year,
                pm.month,
                pm.snapshot_date,
                COUNT(pv.value_id) as category_count,
                SUM(pv.amount) as total_value
            FROM portfolio_month pm
            LEFT JOIN portfolio_value pv ON pm.month_id = pv.month_id
            WHERE pm.year = %s AND pm.month = %s
            GROUP BY pm.month_id, pm.year, pm.month, pm.snapshot_date
        """
        cursor.execute(query, (year, month))
        result = cursor.fetchone()
        return result if result else {}
    except Exception as e:
        print(f"Error fetching monthly summary: {e}")
        return {}
    finally:
        cursor.close()
        close_connection(connection)

def delete_category(category_id: int) -> Tuple[bool, str]:
    """
    Soft delete a category (set is_active to FALSE)
    """
    connection = get_db_connection()
    if not connection:
        return False, "Database connection failed"
    
    try:
        cursor = connection.cursor()
        query = """
            UPDATE investment_category
            SET is_active = FALSE
            WHERE category_id = %s
        """
        cursor.execute(query, (category_id,))
        connection.commit()
        return True, "Category deleted successfully"
    except Exception as e:
        connection.rollback()
        return False, f"Error deleting category: {e}"
    finally:
        cursor.close()
        close_connection(connection)

