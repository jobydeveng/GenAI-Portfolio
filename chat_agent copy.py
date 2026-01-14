"""
AI Chatbot Agent for Portfolio Database
Allows natural language queries on portfolio data
"""
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

class PortfolioChatAgent:
    """
    Chat agent for interacting with portfolio database using natural language
    """
    
    def __init__(self, openai_api_key: str):
        """
        Initialize the chat agent with OpenAI API key
        
        Args:
            openai_api_key: OpenAI API key for LLM
        """
        self.api_key = openai_api_key
        self.llm = None
        self.agent = None
        self.db = None
        
    def initialize(self) -> bool:
        """
        Initialize database connection and create SQL agent
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Get database credentials from environment
            db_host = os.getenv('DB_HOST', 'localhost')
            db_port = os.getenv('DB_PORT', '3306')
            db_name = os.getenv('DB_NAME', 'portfolio')
            db_user = os.getenv('DB_USER', 'root')
            db_password = os.getenv('DB_PASSWORD', '')
            
            # Create database connection string
            connection_string = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
            
            # Create SQLAlchemy engine
            engine = create_engine(connection_string)
            
            # Create SQLDatabase instance
            self.db = SQLDatabase(engine)
            
            # Initialize LLM with OpenAI GPT-4o-mini (fast and cost-effective)
            self.llm = ChatOpenAI(
                api_key=self.api_key,
                model="gpt-4o-mini",
                temperature=0,  # Deterministic responses for database queries
                streaming=True
            )
            
            # Create SQL toolkit
            toolkit = SQLDatabaseToolkit(db=self.db, llm=self.llm)
            
            # Create SQL agent with optimal configuration
            self.agent = create_sql_agent(
                llm=self.llm,
                toolkit=toolkit,
                agent_type="openai-functions",  # Fast and reliable
                verbose=True,
                handle_parsing_errors=True,
                max_iterations=10,
                agent_executor_kwargs={
                    "return_intermediate_steps": True
                }
            )
            
            return True
            
        except Exception as e:
            print(f"Error initializing chat agent: {e}")
            return False
    
    def query(self, user_question: str) -> dict:
        """
        Process user question and return response
        
        Args:
            user_question: Natural language question from user
            
        Returns:
            dict: Response containing output and any errors
        """
        if not self.agent:
            return {
                "success": False,
                "output": "Chat agent not initialized. Please check your API key and database connection.",
                "error": "Agent not initialized"
            }
        
        try:
            # Enhance the question with portfolio context
            enhanced_question = f"""
            You are querying a portfolio management database with these tables:
            - investment_category: stores investment categories (category_id, category_name, description, is_active)
            - portfolio_month: stores month snapshots (month_id, year, month, snapshot_date)
            - portfolio_value: stores portfolio values (value_id, month_id, category_id, amount, updated_at)
            
            User question: {user_question}
            
            Please provide a clear, concise answer with relevant data.
            """
            
            # Execute query through agent
            response = self.agent.invoke({"input": enhanced_question})
            
            # Extract output
            output = response.get("output", str(response))
            
            return {
                "success": True,
                "output": output,
                "error": None
            }
            
        except Exception as e:
            error_msg = f"Error processing query: {str(e)}"
            return {
                "success": False,
                "output": "Sorry, I encountered an error processing your question. Please try rephrasing or ask something else.",
                "error": error_msg
            }
    
    def get_suggested_questions(self) -> list:
        """
        Get a list of suggested questions for users
        
        Returns:
            list: Suggested questions
        """
        return [
            "What is my total portfolio value for the latest month?",
            "Show me all investment categories",
            "What was my portfolio value in December 2024?",
            "Which category has the highest investment?",
            "Show me the trend of my portfolio over the last 6 months",
            "What is the average portfolio value per month?",
            "List all months where I have portfolio data",
            "Compare my portfolio values between different months",
            "What are my active investment categories?",
            "Show me the growth rate of my portfolio"
        ]

