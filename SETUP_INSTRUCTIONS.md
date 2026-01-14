# 🚀 Quick Setup Instructions for AI Chatbot

Follow these simple steps to get the AI chatbot working in your Portfolio Management App.

## Step 1: Update Your .env File

Open your `.env` file (or create it from `env_sample.txt`) and add your OpenAI API key:

```env
# Existing database configuration
DB_HOST=localhost
DB_PORT=3306
DB_NAME=portfolio
DB_USER=root
DB_PASSWORD=your_password

# NEW: Add your OpenAI API key
OPENAI_API_KEY=sk-your-openai-api-key-here
```

**How to get your OpenAI API key:**
1. Go to https://platform.openai.com/api-keys
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)
5. Paste it in your `.env` file

## Step 2: Verify Requirements

The chatbot uses packages already in your `requirements.txt`:
- langchain
- langchain-community
- langchain-openai
- openai
- SQLAlchemy
- mysql-connector-python

These should already be installed, but if not:

```bash
pip install -r requirements.txt
```

## Step 3: Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at http://localhost:8501

## Step 4: Use the Chatbot

1. Click on the **"🤖 AI Chatbot"** tab
2. If you didn't add the API key to `.env`, enter it in the sidebar
3. Click any suggested question or type your own
4. Start chatting with your portfolio data!

## Example Questions to Try

Start with these:
```
What is my total portfolio value?
Show me all investment categories
What was my portfolio in December 2024?
Which category has the highest investment?
```

## Files Added

Your portfolio app now includes these new files:

```
myPortfolio/
├── chat_agent.py                    # NEW: AI agent logic
├── CHATBOT_GUIDE.md                 # NEW: Complete user guide
├── CHATBOT_QUICK_REFERENCE.md      # NEW: Quick reference
├── IMPLEMENTATION_NOTES.md          # NEW: Technical details
├── SETUP_INSTRUCTIONS.md            # NEW: This file
├── app.py                           # MODIFIED: Added chatbot tab
├── env_sample.txt                   # MODIFIED: Added OPENAI_API_KEY
└── README.md                        # MODIFIED: Updated with chatbot info
```

## Troubleshooting

### Problem: "Chat agent not initialized"
**Solution:** Check that:
- Your OpenAI API key is correct
- Your MySQL database is running
- Your `.env` file has the correct credentials

### Problem: "Module not found" errors
**Solution:** Install/reinstall requirements:
```bash
pip install -r requirements.txt --upgrade
```

### Problem: Slow responses
**Solution:** 
- GPT-4o-mini is fast, but complex queries take time
- Check your internet connection
- OpenAI API might be experiencing high load

### Problem: Wrong or empty responses
**Solution:**
- Make sure you have data in your portfolio database
- Be more specific in your questions
- Check that your database has the expected tables

## Cost Information

**Model Used:** GPT-4o-mini
- **Very affordable**: ~$0.15 per 1 million tokens
- **Per query**: Usually a few cents
- **100 queries**: Less than $1

Monitor your usage at: https://platform.openai.com/usage

## Security Reminders

🔒 **Important:**
- Never commit your `.env` file to git
- Don't share your API key with anyone
- Keep your `.gitignore` updated
- The `.env` file should already be in `.gitignore`

## Need Help?

1. **User Guide**: See [CHATBOT_GUIDE.md](CHATBOT_GUIDE.md) for detailed documentation
2. **Quick Reference**: See [CHATBOT_QUICK_REFERENCE.md](CHATBOT_QUICK_REFERENCE.md) for common questions
3. **Technical Details**: See [IMPLEMENTATION_NOTES.md](IMPLEMENTATION_NOTES.md) for implementation details

## What's Next?

Once your chatbot is working:

1. **Try different questions** to explore your portfolio data
2. **Use suggested questions** as templates
3. **Share feedback** on what works well
4. **Explore the database** to understand what data is available

---

**That's it! You're ready to chat with your portfolio data using AI! 🎉**

Need help? Check the troubleshooting section above or the detailed guides.

