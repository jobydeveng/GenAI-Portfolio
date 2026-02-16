# Troubleshooting Guide

## Common Issues and Solutions

### 1. Duplicate Key Error on Portfolio Value Insert

**Error Message:**
```
Error saving portfolio value: duplicate key value violates unique constraint "portfolio_value_pkey"
DETAIL: Key (value_id)=(13) already exists.
```

**Cause:**
This error occurs when the PostgreSQL sequence for `value_id` gets out of sync with the actual data in the table. This can happen when:
- Data was manually inserted into the database
- Database was migrated from another system
- Sequence was not properly updated after bulk operations

**Solution:**
Run the sequence fix utility:

```bash
python fix_sequence.py
```

This script will:
1. Check the current sequence status
2. Find the maximum `value_id` in the table
3. Reset the sequence to the correct value
4. Verify the fix

**Expected Output:**
```
============================================================
PostgreSQL Sequence Fix Utility
============================================================

Step 1: Checking current sequence status...
[INFO] Verification:
   - Sequence last_value: 24
   - Maximum value_id in table: 36
   [WARNING] Sequence needs adjustment

Step 2: Fixing sequence...
[INFO] Current maximum value_id: 36
[SUCCESS] Sequence reset successfully! Next value_id will be: 37

Step 3: Verifying fix...
[INFO] Verification:
   - Sequence last_value: 37
   - Maximum value_id in table: 36
   [SUCCESS] Sequence is correct! Next ID will be: 37

============================================================
[SUCCESS] All done! You can now use the app without errors.
============================================================
```

After running this script, you should be able to add portfolio values without errors.

---

### 2. Database Connection Error

**Error Message:**
```
Error connecting to PostgreSQL (Neon): ...
```

**Possible Causes:**
- Incorrect database credentials in `.env` file
- Database server is down
- Network connectivity issues
- SSL/TLS configuration issues

**Solution:**
1. Check your `.env` file has correct credentials:
   ```
   DB_HOST=your-neon-host.neon.tech
   DB_PORT=5432
   DB_NAME=your_database_name
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_SSLMODE=require
   ```

2. Verify your database is accessible:
   - Log into your Neon dashboard
   - Check if the database is active
   - Verify connection string is correct

3. Test connection manually:
   ```bash
   python -c "from db_config import get_db_connection; conn = get_db_connection(); print('Connected!' if conn else 'Failed')"
   ```

---

### 3. Missing Categories Error

**Error Message:**
```
No categories available. Please add categories first in 'Manage Categories' tab.
```

**Cause:**
No investment categories have been created yet.

**Solution:**
1. Go to the **"Manage Categories"** tab
2. Add at least one category (e.g., "Stocks", "Crypto", "Mutual Funds")
3. Then you can add portfolio data

---

### 4. OpenAI API Key Error (Chatbot)

**Error Message:**
```
OpenAI API key not found!
```

**Cause:**
The `OPENAI_API_KEY` environment variable is not set.

**Solution:**
1. Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Add it to your `.env` file:
   ```
   OPENAI_API_KEY=sk-your-key-here
   ```
3. Restart the Streamlit app

---

### 5. Import Errors

**Error Message:**
```
ModuleNotFoundError: No module named 'streamlit'
```

**Cause:**
Required Python packages are not installed.

**Solution:**
Install all dependencies:
```bash
pip install -r requirements.txt
```

---

### 6. Data Not Showing in Dashboard

**Possible Causes:**
- No data has been added yet
- Wrong year/month selected
- Database connection issues

**Solution:**
1. Verify you've added categories first
2. Add portfolio data for at least one month
3. Select the correct year and month in the dashboard
4. Check database connection

---

### 7. Streamlit Deprecation Warnings

**Warning Message:**
```
Please replace `use_container_width` with `width`.
`use_container_width` will be removed after 2025-12-31.
```

**Cause:**
Using deprecated Streamlit API.

**Impact:**
This is just a warning and doesn't affect functionality. The app will continue to work.

**Solution:**
This will be fixed in a future update. You can safely ignore these warnings for now.

---

## Database Maintenance

### Reset Sequences for All Tables

If you encounter sequence issues with other tables, you can manually reset them:

```sql
-- For investment_category
SELECT setval('investment_category_category_id_seq', 
    (SELECT MAX(category_id) FROM investment_category) + 1, false);

-- For portfolio_month
SELECT setval('portfolio_month_month_id_seq', 
    (SELECT MAX(month_id) FROM portfolio_month) + 1, false);

-- For portfolio_value
SELECT setval('portfolio_value_value_id_seq', 
    (SELECT MAX(value_id) FROM portfolio_value) + 1, false);
```

### Check All Sequences

```sql
-- Check all sequences in the database
SELECT 
    schemaname,
    sequencename,
    last_value
FROM pg_sequences
WHERE schemaname = 'public';
```

---

## Getting Help

If you encounter issues not covered in this guide:

1. Check the error message carefully
2. Look at the terminal/console output for detailed error information
3. Verify your `.env` configuration
4. Check database connectivity
5. Ensure all dependencies are installed

For PostgreSQL-specific issues, refer to the [PostgreSQL Documentation](https://www.postgresql.org/docs/).

For Streamlit issues, refer to the [Streamlit Documentation](https://docs.streamlit.io/).
