# 🤖 AI Chatbot - Quick Reference

## Setup (3 steps)

1. **Install packages** (if not already done):
   ```bash
   pip install -r requirements.txt
   ```

2. **Get OpenAI API Key**:
   - Visit: https://platform.openai.com/api-keys
   - Create new key, copy it

3. **Add to .env file**:
   ```env
   OPENAI_API_KEY=sk-your-key-here
   ```

## How to Use

1. Run app: `streamlit run app.py`
2. Click **"🤖 AI Chatbot"** tab
3. Ask questions in natural language!

## Example Questions

### Quick Insights
```
What is my total portfolio value?
Show me all investment categories
List all months with data
```

### Time-Based Queries
```
What was my portfolio in December 2024?
Show my investments for January 2025
What were my values last month?
```

### Comparisons
```
Compare January and March 2024
Which month had highest value?
Show portfolio trend over last 6 months
```

### Category Analysis
```
Which category has highest investment?
Show all values for Stocks category
Total invested in cryptocurrency?
```

### Advanced
```
Average monthly portfolio value?
Calculate year-over-year growth
Categories with values > ₹50,000
```

## Tips

✅ **DO**
- Be specific with dates/categories
- Ask one question at a time
- Use natural language

❌ **DON'T**
- Ask vague questions
- Combine multiple questions
- Request non-existent data

## Cost

- Model: GPT-4o-mini
- Cost: ~$0.15 per 1M tokens
- Per question: Few cents

## Database Tables

- `investment_category` - Your investment types
- `portfolio_month` - Monthly snapshots
- `portfolio_value` - Actual values

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Agent not initialized" | Check API key & database connection |
| Slow responses | Complex queries take time, be patient |
| Wrong results | Be more specific, use exact names |
| Error messages | Check error details, rephrase question |

## Security

🔒 Never share your API key
🔒 Don't commit .env to git
🔒 Monitor usage on OpenAI dashboard

---

**Full Guide**: See [CHATBOT_GUIDE.md](CHATBOT_GUIDE.md) for complete documentation

