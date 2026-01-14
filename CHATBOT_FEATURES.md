# 🤖 AI Chatbot - Feature Overview

## What You Can Do

### 📊 Portfolio Analysis
```
✓ Get total portfolio values
✓ View breakdown by category
✓ Compare different time periods
✓ Track growth over time
✓ Identify top performing categories
```

### 📅 Time-Based Queries
```
✓ Query specific months/years
✓ Find latest snapshot
✓ Compare historical data
✓ Analyze trends over time
✓ Find date ranges
```

### 🏷️ Category Insights
```
✓ List all categories
✓ Find highest/lowest investments
✓ Compare category values
✓ Search by category name
✓ Get category statistics
```

### 🔢 Calculations & Aggregations
```
✓ Sum total values
✓ Calculate averages
✓ Find min/max values
✓ Count records
✓ Compute growth rates
```

### 🎯 Natural Language Understanding

The chatbot understands questions like:

**Simple Questions:**
- "What is my total portfolio value?"
- "Show me all categories"
- "List my investments"

**Time References:**
- "What was my portfolio last month?"
- "Show data for December 2024"
- "How much did I have in Q1 2024?"

**Comparisons:**
- "Compare January and February"
- "Which month was better?"
- "Show me the trend"

**Complex Queries:**
- "What's the average portfolio value over the last 6 months?"
- "Which category grew the most from January to March?"
- "Show me all categories with values above ₹100,000"

## How It Works

```
┌─────────────────┐
│  You ask a      │
│  question in    │──┐
│  natural        │  │
│  language       │  │
└─────────────────┘  │
                     │
                     ▼
         ┌───────────────────────┐
         │  AI Agent processes   │
         │  and understands      │
         │  your intent          │
         └───────────┬───────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │  Generates SQL query  │
         │  to get the data      │
         └───────────┬───────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │  Queries your MySQL   │
         │  portfolio database   │
         └───────────┬───────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │  Formats and returns  │
         │  the answer in        │
         │  natural language     │
         └───────────┬───────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │  You get a clear,     │
         │  helpful response!    │
         └───────────────────────┘
```

## User Interface

### Main Features

1. **Suggested Questions Panel**
   - Pre-built queries to get started
   - Click to instantly execute
   - Learn by example

2. **Chat Interface**
   - Clean, modern design
   - Message history preserved
   - User and assistant messages clearly distinguished

3. **Chat Input**
   - Type any question
   - Auto-submit on Enter
   - Placeholder with examples

4. **Settings Sidebar**
   - OpenAI API key input
   - Clear chat history button
   - Configuration options

5. **Help Section**
   - Usage tips
   - Database schema info
   - Example questions

### Visual Design

**Color Coding:**
- 🔵 **Blue Messages**: Your questions
- 🟢 **Green Messages**: AI responses
- 🟡 **Yellow Alerts**: Warnings
- 🔴 **Red Alerts**: Errors

**Interactive Elements:**
- Suggested question buttons
- Expandable help sections
- Loading spinners
- Error details expanders

## Technical Highlights

### AI Model
- **GPT-4o-mini**: Fast and cost-effective
- **Temperature 0**: Consistent, deterministic responses
- **Streaming**: See responses as they're generated

### Agent Type
- **OpenAI Functions**: Optimized for tool use
- **SQL Toolkit**: Built-in database query capabilities
- **Error Handling**: Automatic retry and recovery

### Security
- **API Key Protection**: Never logged or stored
- **Read-Only Access**: Can't modify your data
- **Environment Variables**: Secure configuration
- **Password Input**: Keys hidden in UI

### Performance
- **Agent Caching**: Initialized once per session
- **Connection Pooling**: Efficient database access
- **Optimized Queries**: Smart SQL generation

## Example Conversations

### Conversation 1: Getting Started
```
You: What is my total portfolio value?

AI: Based on your latest portfolio snapshot, your total 
portfolio value is ₹5,42,000. This includes investments 
across 6 categories: Stocks (₹2,50,000), Crypto (₹1,50,000), 
Bonds (₹75,000), Gold (₹40,000), Real Estate (₹20,000), 
and Cash (₹7,000).

You: Which category is the largest?

AI: Your Stocks category has the highest investment value 
at ₹2,50,000, representing 46% of your total portfolio.
```

### Conversation 2: Time Comparison
```
You: Compare my portfolio between January and March 2024

AI: Here's the comparison between January and March 2024:

January 2024: ₹4,80,000
March 2024: ₹5,42,000
Increase: ₹62,000 (12.9% growth)

The growth was primarily driven by increases in your 
Stocks (+₹40,000) and Crypto (+₹25,000) categories.

You: That's great! What was the trend month by month?

AI: Here's your monthly portfolio trend:
- January 2024: ₹4,80,000
- February 2024: ₹5,10,000 (+6.25%)
- March 2024: ₹5,42,000 (+6.27%)

You had steady growth of around 6% each month!
```

### Conversation 3: Category Analysis
```
You: Show me all my cryptocurrency investments

AI: Here are your cryptocurrency investments over time:

December 2023: ₹1,20,000
January 2024: ₹1,25,000
February 2024: ₹1,40,000
March 2024: ₹1,50,000

Your crypto portfolio has grown by 25% over this period!

You: Which month had the biggest gain?

AI: February 2024 had the biggest gain with an increase 
of ₹15,000 (12% growth) compared to January 2024.
```

## Best Practices

### For Accurate Results

1. **Use Exact Category Names**
   - ✅ "Show me my Stocks category"
   - ❌ "Show me my stock investments" (if category is "Stocks")

2. **Specify Time Periods Clearly**
   - ✅ "What was my portfolio in January 2024?"
   - ❌ "Show me last month" (unless context is clear)

3. **One Question at a Time**
   - ✅ "What is my total value?" then "Which category is highest?"
   - ❌ "What is my total value and which category is highest?"

4. **Check Your Data First**
   - Verify data exists in your database
   - Use the Dashboard/History tabs to explore
   - Then ask specific questions

### For Better Performance

1. **Start Simple**: Begin with basic queries to understand capabilities
2. **Use Suggested Questions**: They're optimized and tested
3. **Be Patient**: Complex queries may take a few seconds
4. **Clear History**: Use "Clear Chat History" to start fresh

## Limitations

**What the Chatbot CANNOT Do:**

❌ Add or modify data (read-only)
❌ Delete categories or records
❌ Predict future values
❌ Access data outside your database
❌ Perform calculations beyond SQL capabilities
❌ Generate visualizations (yet!)

**What You Should NOT Ask:**

❌ "What will my portfolio be next month?"
❌ "Should I invest more in stocks?"
❌ "Update my crypto value to ₹2,00,000"
❌ "Delete my December data"
❌ "Show me stock market prices"

## Advanced Usage

### Complex Queries

**Multi-condition Filtering:**
```
Show me all categories with values greater than ₹50,000 
in months where my total portfolio exceeded ₹500,000
```

**Aggregations with Grouping:**
```
What is the average value of each category across all months?
```

**Ranking:**
```
Show me the top 3 months by total portfolio value
```

**Date Range Queries:**
```
What was my total portfolio growth between January 2024 
and March 2024?
```

### Combining with Other Tabs

1. **Use Dashboard** to see overall stats
2. **Use Chatbot** to dig deeper into specifics
3. **Use History** to verify chatbot responses
4. **Use Add Data** to input new values
5. **Return to Chatbot** to analyze updated data

## FAQ

**Q: How much does it cost per query?**
A: About $0.0001 (1/100th of a cent) per typical query

**Q: Is my data safe?**
A: Yes, queries are processed securely via OpenAI API and only you can access

**Q: Can I use it offline?**
A: No, requires internet connection for OpenAI API

**Q: How accurate are the responses?**
A: Very accurate for data in your database, but always verify important figures

**Q: Can I export chat history?**
A: Not yet, but this feature is planned for future updates

**Q: Does it learn from my questions?**
A: Each session is independent, but you can see chat history within a session

**Q: What if I get an error?**
A: Try rephrasing your question, check error details, or verify your data

---

**Ready to explore your portfolio data with AI? Head to the 🤖 AI Chatbot tab!**

