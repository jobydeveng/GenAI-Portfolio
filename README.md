# Portfolio Management App

A Streamlit-based portfolio management application to track your investments across different categories on a monthly basis.

## Features

- **Dashboard**: View your portfolio summary and distribution for any month
- **Add Data**: Enter portfolio values for multiple categories for a specific month
- **Manage Categories**: Add, view, and delete investment categories
- **View History**: Browse historical portfolio data with filters
- **🤖 AI Chatbot**: Query your portfolio using natural language powered by OpenAI (NEW!)

## Database Schema

The app uses three main tables:

1. **investment_category**: Stores investment categories (e.g., coin, upstock, kite, DCX, etc.)
2. **portfolio_month**: Tracks unique year/month combinations with snapshot dates
3. **portfolio_value**: Stores the actual portfolio amounts for each category per month

## Setup Instructions

### 1. Database Setup

First, make sure you have MySQL installed and running. Then execute the following SQL commands:

```sql
CREATE DATABASE portfolio;
USE portfolio;

CREATE TABLE investment_category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    description VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE portfolio_month (
    month_id INT AUTO_INCREMENT PRIMARY KEY,
    year SMALLINT NOT NULL,
    month TINYINT NOT NULL,
    snapshot_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_year_month UNIQUE (year, month),
    CONSTRAINT chk_month CHECK (month BETWEEN 1 AND 12)
);

CREATE TABLE portfolio_value (
    value_id INT AUTO_INCREMENT PRIMARY KEY,
    month_id INT NOT NULL,
    category_id INT NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_month
        FOREIGN KEY (month_id) REFERENCES portfolio_month(month_id),
    CONSTRAINT fk_category
        FOREIGN KEY (category_id) REFERENCES investment_category(category_id),
    UNIQUE (month_id, category_id)
);
```

### 2. Python Environment Setup

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

1. Copy `env_sample.txt` to `.env`:
   ```bash
   copy env_sample.txt .env
   ```

2. Edit `.env` and update with your MySQL credentials and OpenAI API key:
   ```
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=portfolio
   DB_USER=root
   DB_PASSWORD=your_actual_password
   
   # For AI Chatbot feature (optional, can also enter in app)
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)

### 4. Run the Application

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## Usage Guide

### Adding Categories

1. Go to the **"Manage Categories"** tab
2. Enter a category name (e.g., "coin", "upstock", "kite")
3. Optionally add a description
4. Click "Add Category"

### Adding Portfolio Data

1. Go to the **"Add Data"** tab
2. Select the year, month, and snapshot date
3. Enter the amount for each category
4. Click "Save All Values" to save all non-zero amounts

### Viewing Dashboard

1. Go to the **"Dashboard"** tab
2. Select a year and month from the dropdowns
3. View the total portfolio value, category breakdown, and distribution chart

### Viewing History

1. Go to the **"View History"** tab
2. Choose a filter option (All Data, Specific Year, or Specific Month)
3. View all historical records with summary statistics

### Using AI Chatbot 🤖

1. Go to the **"AI Chatbot"** tab
2. Enter your OpenAI API key in the sidebar (if not in .env)
3. Ask questions in natural language like:
   - "What is my total portfolio value?"
   - "Show me my portfolio for December 2024"
   - "Which category has the highest investment?"
   - "Compare my portfolio between January and March"
4. Use suggested questions for quick insights
5. View detailed guide in [CHATBOT_GUIDE.md](CHATBOT_GUIDE.md)

## File Structure

```
myPortfolio/
├── app.py                 # Main Streamlit application
├── db_config.py          # Database connection configuration
├── db_operations.py      # Database CRUD operations
├── chat_agent.py         # AI Chatbot agent (NEW)
├── requirements.txt      # Python dependencies
├── env_sample.txt        # Example environment variables
├── .env                  # Your actual environment variables (create this)
├── README.md             # This file
├── CHATBOT_GUIDE.md      # Detailed chatbot guide (NEW)
└── QUICKSTART.md         # Quick start guide
```

## Notes

- The app uses soft delete for categories (sets `is_active` to FALSE)
- Portfolio values are automatically updated if you enter data for the same month/category twice
- Only non-zero values are saved when adding portfolio data
- The unique constraint on (year, month) ensures one snapshot per month
- The unique constraint on (month_id, category_id) ensures one value per category per month

## Troubleshooting

**Database Connection Error**: 
- Verify your MySQL server is running
- Check your `.env` file has correct credentials
- Ensure the `portfolio` database exists

**Import Errors**:
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Ensure you're using Python 3.8 or higher

**Data Not Showing**:
- Make sure you've added categories first
- Verify data was saved successfully (check for success message)
- Check the database directly if needed

## Future Enhancements

- Export data to CSV/Excel
- Enhanced data visualization
- Backup and restore functionality
- AI chatbot conversation export
- Voice input for chatbot
- Automated portfolio reports
- Multi-user support with authentication

## Technologies Used

- **Frontend**: Streamlit
- **Database**: MySQL
- **AI/ML**: OpenAI GPT-4o-mini, LangChain
- **Data Processing**: Pandas, SQLAlchemy
- **Environment Management**: python-dotenv

## Learn More

- [Quick Start Guide](QUICKSTART.md) - Get started quickly
- [Chatbot Guide](CHATBOT_GUIDE.md) - Detailed AI chatbot documentation
- [Streamlit Documentation](https://docs.streamlit.io/)
- [LangChain Documentation](https://python.langchain.com/)

