# 🤖 AI Portfolio Chatbot Guide

## Overview

The AI Portfolio Chatbot is an intelligent assistant that allows you to query your portfolio database using natural language. Powered by OpenAI's GPT-4o-mini and LangChain, it can understand complex questions and provide insights about your investment data.

## Features

✨ **Natural Language Queries**: Ask questions in plain English
📊 **Data Analysis**: Get instant insights from your portfolio
🔍 **Smart Search**: Find specific data across all your investments
📈 **Trend Analysis**: Compare values across different time periods
💡 **Suggested Questions**: Pre-built queries to get you started

## Setup

### 1. Install Requirements

The chatbot uses the following packages (already in `requirements.txt`):
- `langchain`
- `langchain-community`
- `langchain-openai`
- `openai`
- `SQLAlchemy`
- `mysql-connector-python`

If you haven't installed them yet:
```bash
pip install -r requirements.txt
```

### 2. Get OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Navigate to API Keys section
4. Click "Create new secret key"
5. Copy your API key

### 3. Configure Environment

Add your OpenAI API key to your `.env` file:

```env
# OpenAI API Key
OPENAI_API_KEY=sk-your-api-key-here
```

Alternatively, you can enter it directly in the chatbot sidebar when running the app.

## How to Use

### Accessing the Chatbot

1. Run the portfolio management app:
   ```bash
   streamlit run app.py
   ```

2. Navigate to the **🤖 AI Chatbot** tab

3. Enter your OpenAI API key in the sidebar (if not in .env)

4. Start asking questions!

### Example Questions

#### Basic Queries
- "What is my total portfolio value?"
- "Show me all investment categories"
- "List all months where I have portfolio data"

#### Time-Based Queries
- "What was my portfolio value in December 2024?"
- "Show me my portfolio for January 2025"
- "What were my investments in the last quarter?"

#### Comparative Analysis
- "Compare my portfolio values between January and March 2024"
- "Which month had the highest portfolio value?"
- "Show me the trend of my portfolio over the last 6 months"

#### Category Analysis
- "Which category has the highest investment?"
- "Show me all values for my 'Stocks' category"
- "What is the total invested in cryptocurrency?"

#### Advanced Queries
- "What is my average monthly portfolio value?"
- "Calculate the growth rate of my portfolio year over year"
- "Show me categories with values greater than ₹50,000"

### Suggested Questions

The chatbot provides suggested questions to help you get started:
- Click any suggested question button
- The chatbot will automatically answer it
- Use these as templates for your own questions

## Database Schema

The chatbot has access to three main tables:

### 1. investment_category
- `category_id`: Unique identifier
- `category_name`: Name of the investment category
- `description`: Description of the category
- `is_active`: Whether the category is active

### 2. portfolio_month
- `month_id`: Unique identifier
- `year`: Year of the snapshot
- `month`: Month number (1-12)
- `snapshot_date`: Date when snapshot was taken

### 3. portfolio_value
- `value_id`: Unique identifier
- `month_id`: Reference to portfolio_month
- `category_id`: Reference to investment_category
- `amount`: Portfolio value amount
- `updated_at`: Last update timestamp

## Tips for Better Results

### ✅ Do's

1. **Be Specific**: Instead of "show data", ask "show portfolio values for December 2024"

2. **Use Time References**: Mention specific months, years, or date ranges

3. **Ask One Thing at a Time**: Break complex questions into simpler ones

4. **Use Natural Language**: Write as if talking to a colleague

5. **Refer to Categories**: Use your actual category names in questions

### ❌ Don'ts

1. **Avoid Vague Questions**: "Give me information" won't work well

2. **Don't Request Non-existent Data**: The chatbot can only query data in your database

3. **Avoid Multiple Questions**: Don't combine unrelated questions

4. **Don't Expect Predictions**: The chatbot analyzes existing data, not future projections

## Troubleshooting

### Issue: "Chat agent not initialized"
**Solution**: Check your OpenAI API key and database connection in the .env file

### Issue: "Error processing query"
**Solution**: 
- Rephrase your question more clearly
- Check if the data you're asking about exists in your database
- Look at the error details in the expander

### Issue: Slow responses
**Solution**: 
- GPT-4o-mini is fast, but complex queries may take time
- Try breaking down complex questions
- Check your internet connection

### Issue: Incorrect results
**Solution**:
- Verify the data in your database is correct
- Be more specific in your question
- Use exact category names and date formats

## Model Information

**Model**: GPT-4o-mini
- Fast response times
- Cost-effective
- Optimized for structured data queries
- Temperature set to 0 for deterministic results

**Agent Type**: OpenAI Functions
- Reliable SQL query generation
- Better error handling
- Automatic query optimization

## Security Notes

🔒 **Important Security Considerations**:

1. **Never share your OpenAI API key** with others
2. **Don't commit .env file** to version control
3. **Rotate API keys** regularly
4. **Monitor API usage** to avoid unexpected costs
5. **Use environment variables** instead of hardcoding keys

## Cost Considerations

- GPT-4o-mini is very cost-effective (~$0.15 per 1M input tokens)
- Each question costs a few cents at most
- Monitor usage at [OpenAI Usage Dashboard](https://platform.openai.com/usage)
- Set spending limits in your OpenAI account

## Limitations

1. **Read-Only**: The chatbot can only query data, not modify it
2. **Database Scope**: Only accesses portfolio-related tables
3. **No Predictions**: Cannot forecast future values
4. **Token Limits**: Very long queries may be truncated
5. **Rate Limits**: Subject to OpenAI API rate limits

## Advanced Features

### Custom Prompts

The chatbot automatically enhances your questions with portfolio context for better results.

### Chat History

- All conversations are preserved in your session
- Use the "Clear Chat History" button to start fresh
- History is lost when you refresh the page

### Intermediate Steps

The chatbot logs all SQL queries and intermediate steps for debugging (visible in verbose mode).

## Future Enhancements

🚀 Potential future features:
- Export chat conversations
- Save favorite questions
- Multi-language support
- Voice input
- Data visualization generation
- Scheduled reports via chatbot

## Support

For issues or questions:
1. Check this guide first
2. Review the troubleshooting section
3. Ensure all requirements are installed
4. Verify your .env configuration

## Additional Resources

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

---

**Enjoy your AI-powered portfolio assistant! 🎉**

