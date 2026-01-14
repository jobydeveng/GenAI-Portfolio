# Quick Start Guide - Portfolio Management App

## Prerequisites
- MySQL Server installed and running
- Python 3.8 or higher

## Step 1: Setup Database
Open MySQL and run:
```sql
CREATE DATABASE portfolio;
USE portfolio;

-- Copy and paste all table creation scripts from README.md
```

## Step 2: Configure Environment
1. Navigate to myPortfolio folder
2. Copy `.env.example` to `.env`
3. Edit `.env` with your MySQL credentials

Example `.env`:
```
DB_HOST=localhost
DB_PORT=3306
DB_NAME=portfolio
DB_USER=root
DB_PASSWORD=yourpassword
```

## Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## Step 4: Run the App
```bash
streamlit run app.py
```

## First Time Usage

### 1. Add Categories
- Go to "Manage Categories" tab
- Add categories like: coin, upstock, kite, DCX, vest, f1, rd, f2, f3, bin, pf, nps
- Click "Add Category" for each

### 2. Add Your First Data
- Go to "Add Data" tab
- Select Year: 2025, Month: January
- Choose snapshot date
- Enter amounts for each category
- Click "Save All Values"

### 3. View Dashboard
- Go to "Dashboard" tab
- Select the month you just added
- See your portfolio summary and charts!

## Tips
- You can update values by entering data for the same month again
- Only non-zero values are saved
- Use the History tab to see all your data
- Categories can be deleted but won't affect existing data

## Troubleshooting

**"Database connection failed"**
- Check MySQL is running
- Verify `.env` credentials are correct
- Ensure `portfolio` database exists

**"No categories available"**
- Add categories in "Manage Categories" tab first

**App won't start**
- Make sure all requirements are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)

