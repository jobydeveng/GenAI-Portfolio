"""
Portfolio Management Streamlit App
"""
import streamlit as st
import pandas as pd
from datetime import date, datetime
from db_operations import (
    get_all_categories,
    add_category,
    get_or_create_month,
    save_portfolio_value,
    get_portfolio_data,
    get_all_months,
    get_monthly_summary,
    delete_category
)
from chat_agent import PortfolioChatAgent
import os

# Page configuration
st.set_page_config(
    page_title="Portfolio Manager",
    page_icon="💰",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main content padding and background */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 50%, #1a202c 100%);
    }
    
    /* Overall page background */
    .stApp {
        background: linear-gradient(135deg, #0f1419 0%, #1a202c 100%);
    }
    
    /* Tab styling with better visibility */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%);
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
        border: 2px solid #4a5568;
    }
    .stTabs [data-baseweb="tab"] {
        height: 55px;
        white-space: pre-wrap;
        background: linear-gradient(135deg, #2d3748 0%, #374151 100%);
        border-radius: 8px;
        gap: 1px;
        padding: 12px 24px;
        font-weight: 500;
        border: 2px solid #4a5568;
        transition: all 0.3s ease;
        color: #e2e8f0 !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, #374151 0%, #4a5568 100%);
        border-color: #4CAF50;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%) !important;
        color: white !important;
        border-color: #45a049 !important;
        box-shadow: 0 2px 12px rgba(76, 175, 80, 0.5);
    }
    
    /* Section headers with better spacing */
    h1 {
        padding-bottom: 1rem;
        margin-bottom: 1.5rem;
        color: #e2e8f0 !important;
    }
    h2 {
        padding-top: 1rem;
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #4a5568;
        color: #e2e8f0 !important;
    }
    h3 {
        padding-top: 1.5rem;
        padding-bottom: 0.75rem;
        margin-bottom: 1rem;
        color: #cbd5e0 !important;
    }
    
    /* All text elements */
    p, span, div {
        color: #e2e8f0;
    }
    
    /* Metric cards with better visibility */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        color: #4CAF50 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #e2e8f0 !important;
        font-weight: 600 !important;
    }
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #2d3748 0%, #374151 100%);
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #4a5568;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    [data-testid="metric-container"]:hover {
        box-shadow: 0 6px 16px rgba(76, 175, 80, 0.3);
        border-color: #4CAF50;
        transform: translateY(-2px);
    }
    
    /* Form styling with better spacing */
    .stForm {
        background: linear-gradient(135deg, #2d3748 0%, #1a202c 100%);
        padding: 30px;
        border-radius: 12px;
        border: 2px solid #4a5568;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    
    /* Make labels visible with light color */
    .stNumberInput label,
    .stTextInput label,
    .stSelectbox label,
    .stDateInput label,
    .stRadio label,
    label[data-testid="stWidgetLabel"] {
        color: #e2e8f0 !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        margin-bottom: 8px !important;
    }
    
    /* Input fields with better visibility */
    .stNumberInput > div > div > input,
    .stTextInput > div > div > input,
    .stSelectbox > div > div,
    .stDateInput > div > div > input {
        border: 2px solid #4a5568 !important;
        border-radius: 6px !important;
        padding: 12px !important;
        font-size: 1rem !important;
        background-color: #2d3748 !important;
        color: #e2e8f0 !important;
    }
    .stNumberInput > div > div > input:focus,
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div:focus-within,
    .stDateInput > div > div > input:focus {
        border-color: #4CAF50 !important;
        box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.3) !important;
        background-color: #374151 !important;
    }
    
    /* Placeholder text visibility */
    .stNumberInput input::placeholder,
    .stTextInput input::placeholder {
        color: #a0aec0 !important;
    }
    
    /* Number input increment/decrement buttons */
    .stNumberInput button {
        background-color: #4a5568 !important;
        color: #e2e8f0 !important;
        border: 1px solid #4a5568 !important;
    }
    
    .stNumberInput button:hover {
        background-color: #4CAF50 !important;
        border-color: #4CAF50 !important;
    }
    
    /* Date input calendar icon */
    .stDateInput button {
        color: #e2e8f0 !important;
    }
    
    /* Button styling */
    .stButton > button {
        padding: 12px 28px;
        font-size: 1rem;
        font-weight: 600;
        border-radius: 8px;
        border: 2px solid #4a5568;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        background: linear-gradient(135deg, #2d3748 0%, #374151 100%);
        color: #e2e8f0 !important;
    }
    .stButton > button:hover {
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3);
        transform: translateY(-1px);
        border-color: #4CAF50;
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white !important;
        border-color: #45a049;
    }
    
    /* Delete button styling */
    .stButton > button:has-text("Delete"),
    .stButton > button:contains("🗑️") {
        background: linear-gradient(135deg, #e53e3e 0%, #c53030 100%);
        border-color: #c53030;
        color: white !important;
    }
    
    /* Dataframe styling */
    [data-testid="stDataFrame"] {
        border: 2px solid #4a5568;
        border-radius: 8px;
        padding: 10px;
        background-color: #2d3748;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }
    
    /* Dataframe text color */
    [data-testid="stDataFrame"] * {
        color: #e2e8f0 !important;
    }
    
    /* Alert boxes with better padding and dark theme */
    .stAlert {
        padding: 16px 20px !important;
        border-radius: 8px !important;
        margin: 16px 0 !important;
        border-width: 2px !important;
        font-weight: 500 !important;
    }
    
    /* Info box */
    [data-baseweb="notification"][kind="info"],
    .stAlert[kind="info"] {
        background-color: #2c5282 !important;
        border-color: #4299e1 !important;
        color: #e2e8f0 !important;
    }
    
    /* Success box */
    [data-baseweb="notification"][kind="success"],
    .stAlert[kind="success"] {
        background-color: #276749 !important;
        border-color: #48bb78 !important;
        color: #e2e8f0 !important;
    }
    
    /* Warning box */
    [data-baseweb="notification"][kind="warning"],
    .stAlert[kind="warning"] {
        background-color: #744210 !important;
        border-color: #ed8936 !important;
        color: #e2e8f0 !important;
    }
    
    /* Error box */
    [data-baseweb="notification"][kind="error"],
    .stAlert[kind="error"] {
        background-color: #742a2a !important;
        border-color: #fc8181 !important;
        color: #e2e8f0 !important;
    }
    
    /* Info, Warning, Success, Error boxes */
    [data-baseweb="notification"] {
        padding: 16px 20px;
        border-radius: 8px;
        margin: 12px 0;
        border-width: 2px;
    }
    
    /* Divider with better spacing */
    hr {
        margin: 2rem 0;
        border: none;
        border-top: 2px solid #4a5568;
        opacity: 0.6;
    }
    
    /* Selectbox dropdown options */
    [data-baseweb="popover"] {
        background-color: #2d3748 !important;
    }
    
    [data-baseweb="menu"] {
        background-color: #2d3748 !important;
    }
    
    [role="option"] {
        background-color: #2d3748 !important;
        color: #e2e8f0 !important;
    }
    
    [role="option"]:hover {
        background-color: #374151 !important;
    }
    
    /* Column spacing */
    [data-testid="column"] {
        padding: 0 12px;
    }
    
    /* Sidebar styling if used */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%);
    }
    
    /* Ensure all markdown text is visible */
    .stMarkdown {
        color: #e2e8f0;
    }
    
    /* Streamlit default text color override */
    .element-container {
        color: #e2e8f0;
    }
    
    /* Chart container */
    [data-testid="stArrowVegaLiteChart"] {
        background: linear-gradient(135deg, #2d3748 0%, #374151 100%);
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #4a5568;
        margin: 20px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }
    
    /* Custom boxes */
    .success-box {
        padding: 16px 20px;
        border-radius: 8px;
        background-color: #276749;
        border: 2px solid #48bb78;
        color: #e2e8f0;
        margin: 12px 0;
        font-weight: 500;
    }
    .error-box {
        padding: 16px 20px;
        border-radius: 8px;
        background-color: #742a2a;
        border: 2px solid #fc8181;
        color: #e2e8f0;
        margin: 12px 0;
        font-weight: 500;
    }
    
    /* Radio buttons */
    [data-testid="stRadio"] > div {
        padding: 12px;
        background: linear-gradient(135deg, #2d3748 0%, #374151 100%);
        border-radius: 8px;
        border: 2px solid #4a5568;
    }
    
    /* Radio button labels and options */
    [data-testid="stRadio"] label,
    [data-testid="stRadio"] div[role="radiogroup"] label {
        color: #e2e8f0 !important;
    }
    
    /* Form submit button */
    .stForm [data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white !important;
        padding: 14px 32px;
        font-size: 1.1rem;
        font-weight: 700;
        margin-top: 20px;
        border: none;
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.4);
    }
    
    .stForm [data-testid="stFormSubmitButton"] > button:hover {
        box-shadow: 0 6px 16px rgba(76, 175, 80, 0.6);
    }
    
    /* Form helper text and descriptions */
    .stForm p, .stForm span, .stForm div {
        color: #cbd5e0 !important;
    }
    
    /* Chatbot styling */
    .chat-message {
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
        border: 2px solid #4a5568;
        background: linear-gradient(135deg, #2d3748 0%, #374151 100%);
    }
    .chat-message.user {
        background: linear-gradient(135deg, #2c5282 0%, #2b6cb0 100%);
        border-color: #4299e1;
    }
    .chat-message.assistant {
        background: linear-gradient(135deg, #276749 0%, #2f855a 100%);
        border-color: #48bb78;
    }
    .chat-message .message {
        color: #e2e8f0;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* Chat input */
    .stChatInput > div > div > input {
        background-color: #2d3748 !important;
        color: #e2e8f0 !important;
        border: 2px solid #4a5568 !important;
        border-radius: 8px !important;
        padding: 12px !important;
        font-size: 1rem !important;
    }
    
    /* Suggested questions styling */
    .suggested-question {
        background: linear-gradient(135deg, #2d3748 0%, #374151 100%);
        padding: 12px 16px;
        border-radius: 8px;
        border: 2px solid #4a5568;
        margin: 8px 0;
        cursor: pointer;
        transition: all 0.3s ease;
        color: #e2e8f0;
    }
    .suggested-question:hover {
        border-color: #4CAF50;
        background: linear-gradient(135deg, #374151 0%, #4a5568 100%);
        transform: translateX(5px);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'refresh' not in st.session_state:
    st.session_state.refresh = 0

def main():
    st.title("💰 Portfolio Management System")
    st.markdown("---")
    
    # Create tabs
    tabs = st.tabs(["📊 Dashboard", "➕ Add Data", "🏷️ Manage Categories", "📈 View History", "🤖 AI Chatbot"])
    
    # Tab 1: Dashboard
    with tabs[0]:
        show_dashboard()
    
    # Tab 2: Add Data
    with tabs[1]:
        show_add_data()
    
    # Tab 3: Manage Categories
    with tabs[2]:
        show_manage_categories()
    
    # Tab 4: View History
    with tabs[3]:
        show_history()
    
    # Tab 5: AI Chatbot
    with tabs[4]:
        show_chatbot()

def show_dashboard():
    """Display portfolio dashboard with summary"""
    st.header("Portfolio Dashboard")
    
    # Get all months
    months = get_all_months()
    
    if not months:
        st.info("📝 No portfolio data yet. Start by adding categories and data!")
        return
    
    # Select month for dashboard
    col1, col2 = st.columns(2)
    
    with col1:
        years = sorted(list(set([m['year'] for m in months])), reverse=True)
        selected_year = st.selectbox("Select Year", years, key="dash_year")
    
    with col2:
        available_months = [m['month'] for m in months if m['year'] == selected_year]
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month_options = {i: month_names[i-1] for i in available_months}
        
        if month_options:
            selected_month = st.selectbox(
                "Select Month",
                options=list(month_options.keys()),
                format_func=lambda x: month_options[x],
                key="dash_month"
            )
        else:
            st.warning("No data for selected year")
            return
    
    # Get summary
    summary = get_monthly_summary(selected_year, selected_month)
    
    if summary:
        st.markdown("### 📊 Summary")
        st.markdown("")  # Add spacing
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Portfolio Value", f"₹{summary.get('total_value', 0):,.2f}")
        
        with col2:
            st.metric("Categories", summary.get('category_count', 0))
        
        with col3:
            snapshot = summary.get('snapshot_date')
            if snapshot:
                st.metric("Snapshot Date", snapshot.strftime('%d %b %Y'))
        
        st.markdown("")  # Add spacing
        
        # Get detailed data
        data = get_portfolio_data(selected_year, selected_month)
        
        if data:
            st.markdown("---")
            st.markdown("### 💼 Category Breakdown")
            st.markdown("")  # Add spacing
            df = pd.DataFrame(data)
            df['amount'] = df['amount'].apply(lambda x: f"₹{x:,.2f}")
            df = df[['category_name', 'amount']]
            df.columns = ['Category', 'Amount']
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            # Show chart
            chart_data = pd.DataFrame(data)
            if not chart_data.empty:
                st.markdown("")  # Add spacing
                st.markdown("### 📊 Portfolio Distribution")
                st.markdown("")  # Add spacing
                st.bar_chart(chart_data.set_index('category_name')['amount'])

def show_add_data():
    """Add portfolio data for a specific month"""
    st.header("Add Portfolio Data")
    st.markdown("")  # Add spacing
    
    # Get categories
    categories = get_all_categories()
    
    if not categories:
        st.warning("⚠️ No categories available. Please add categories first in 'Manage Categories' tab.")
        return
    
    st.markdown("### 📅 Select Date")
    st.markdown("")  # Add spacing
    col1, col2, col3 = st.columns(3)
    
    with col1:
        year = st.number_input("Year", min_value=2000, max_value=2100, value=datetime.now().year)
    
    with col2:
        month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December']
        month = st.selectbox("Month", range(1, 13), format_func=lambda x: month_names[x-1])
    
    with col3:
        snapshot_date = st.date_input("Snapshot Date", value=date.today())
    
    st.markdown("---")
    st.markdown("### 💰 Enter Portfolio Values")
    st.markdown("")  # Add spacing
    
    # Create a form for entering values
    with st.form("portfolio_form"):
        values = {}
        
        st.markdown("Enter the current value for each category:")
        st.markdown("")  # Add spacing
        
        # Create two columns for better layout
        num_cols = 2
        cols = st.columns(num_cols)
        
        for idx, category in enumerate(categories):
            col_idx = idx % num_cols
            with cols[col_idx]:
                values[category['category_id']] = st.number_input(
                    f"{category['category_name']}",
                    min_value=0.0,
                    value=0.0,
                    step=100.0,
                    format="%.2f",
                    key=f"cat_{category['category_id']}"
                )
        
        submitted = st.form_submit_button("💾 Save All Values", use_container_width=True)
        
        if submitted:
            # Get or create month
            month_id = get_or_create_month(year, month, snapshot_date)
            
            if not month_id:
                st.error("❌ Error creating month entry in database")
                return
            
            success_count = 0
            error_count = 0
            
            # Save each value
            for category_id, amount in values.items():
                if amount > 0:  # Only save non-zero values
                    success, message = save_portfolio_value(month_id, category_id, amount)
                    if success:
                        success_count += 1
                    else:
                        error_count += 1
                        st.error(f"❌ {message}")
            
            if success_count > 0:
                st.success(f"✅ Successfully saved {success_count} portfolio value(s)!")
                st.balloons()
            
            if error_count > 0:
                st.warning(f"⚠️ {error_count} value(s) failed to save")

def show_manage_categories():
    """Manage investment categories"""
    st.header("Manage Categories")
    st.markdown("")  # Add spacing
    
    # Add new category section
    st.markdown("### ➕ Add New Category")
    st.markdown("")  # Add spacing
    with st.form("add_category_form"):
        col1, col2 = st.columns([2, 3])
        
        with col1:
            new_category_name = st.text_input("Category Name*", placeholder="e.g., coin, upstock, kite")
        
        with col2:
            new_category_desc = st.text_input("Description (Optional)", placeholder="e.g., Cryptocurrency investments")
        
        submit_button = st.form_submit_button("➕ Add Category", use_container_width=True)
        
        if submit_button:
            if not new_category_name.strip():
                st.error("❌ Category name is required")
            else:
                success, message = add_category(new_category_name.strip(), new_category_desc.strip())
                if success:
                    st.success(f"✅ {message}")
                    st.session_state.refresh += 1
                    st.rerun()
                else:
                    st.error(f"❌ {message}")
    
    st.markdown("---")
    st.markdown("### 📋 Existing Categories")
    st.markdown("")  # Add spacing
    
    # Display existing categories
    categories = get_all_categories()
    
    if not categories:
        st.info("📝 No categories yet. Add your first category above!")
        return
    
    # Create a dataframe for display
    df_data = []
    for cat in categories:
        df_data.append({
            "Category Name": cat['category_name'],
            "Description": cat['description'] or "-",
            "Created At": cat['created_at'].strftime('%d %b %Y') if cat['created_at'] else "-",
            "ID": cat['category_id']
        })
    
    df = pd.DataFrame(df_data)
    
    # Display as table
    st.dataframe(df[['Category Name', 'Description', 'Created At']], use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### 🗑️ Delete Category")
    st.markdown("")  # Add spacing
    st.warning("⚠️ Note: Deleting a category will not remove existing portfolio data, but the category will no longer be available for new entries.")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        category_to_delete = st.selectbox(
            "Select category to delete",
            options=[cat['category_id'] for cat in categories],
            format_func=lambda x: next(cat['category_name'] for cat in categories if cat['category_id'] == x)
        )
    
    with col2:
        if st.button("🗑️ Delete", use_container_width=True):
            success, message = delete_category(category_to_delete)
            if success:
                st.success(f"✅ {message}")
                st.rerun()
            else:
                st.error(f"❌ {message}")

def show_history():
    """View portfolio history"""
    st.header("Portfolio History")
    st.markdown("")  # Add spacing
    
    st.markdown("### 🔍 Filters")
    st.markdown("")  # Add spacing
    
    # Filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        filter_option = st.radio("Filter by:", ["All Data", "Specific Year", "Specific Month"])
    
    year_filter = None
    month_filter = None
    
    if filter_option == "Specific Year":
        with col2:
            year_filter = st.number_input("Year", min_value=2000, max_value=2100, value=datetime.now().year)
    
    elif filter_option == "Specific Month":
        with col2:
            year_filter = st.number_input("Year", min_value=2000, max_value=2100, value=datetime.now().year)
        with col3:
            month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                          'July', 'August', 'September', 'October', 'November', 'December']
            month_filter = st.selectbox("Month", range(1, 13), format_func=lambda x: month_names[x-1])
    
    # Get data
    data = get_portfolio_data(year_filter, month_filter)
    
    if not data:
        st.info("📝 No portfolio history found for the selected filters.")
        return
    
    st.markdown("---")
    st.markdown("### 📊 Historical Data")
    st.markdown("")  # Add spacing
    
    # Display data
    df = pd.DataFrame(data)
    
    # Format the dataframe
    df['snapshot_date'] = pd.to_datetime(df['snapshot_date']).dt.strftime('%d %b %Y')
    df['month_name'] = df['month'].apply(lambda x: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                                     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][x-1])
    df['amount'] = df['amount'].apply(lambda x: f"₹{x:,.2f}")
    
    # Select and rename columns
    display_df = df[['year', 'month_name', 'snapshot_date', 'category_name', 'amount']]
    display_df.columns = ['Year', 'Month', 'Snapshot Date', 'Category', 'Amount']
    
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    # Summary statistics
    st.markdown("---")
    st.markdown("### 📈 Summary Statistics")
    st.markdown("")  # Add spacing
    
    col1, col2, col3 = st.columns(3)
    
    numeric_df = pd.DataFrame(data)
    
    with col1:
        total_records = len(numeric_df)
        st.metric("Total Records", total_records)
    
    with col2:
        unique_months = numeric_df[['year', 'month']].drop_duplicates()
        st.metric("Unique Months", len(unique_months))
    
    with col3:
        total_value = numeric_df['amount'].sum()
        st.metric("Total Value (All)", f"₹{total_value:,.2f}")

def show_chatbot():
    """AI Chatbot for natural language database queries"""
    st.header("🤖 AI Portfolio Assistant")
    st.markdown("Ask questions about your portfolio data in natural language!")
    st.markdown("")  # Add spacing
    
    # Get API key from environment variable
    openai_api_key = os.getenv('OPENAI_API_KEY', '')
    
    # Clear chat button in sidebar
    with st.sidebar:
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.chat_messages = []
            st.session_state.chat_agent = None
            st.rerun()
    
    if not openai_api_key:
        st.error("❌ OpenAI API key not found!")
        st.info("Please add your OpenAI API key to the `.env` file:\n\n```\nOPENAI_API_KEY=sk-your-key-here\n```")
        return
    
    # Initialize chat agent
    if 'chat_agent' not in st.session_state or st.session_state.chat_agent is None:
        with st.spinner("🔄 Initializing AI agent..."):
            agent = PortfolioChatAgent(openai_api_key)
            if agent.initialize():
                st.session_state.chat_agent = agent
                st.success("✅ AI agent initialized successfully!")
            else:
                st.error("❌ Failed to initialize AI agent. Please check your database connection and API key.")
                return
    
    # Initialize chat history
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = [
            {
                "role": "assistant",
                "content": "👋 Hello! I'm your AI Portfolio Assistant. I can help you analyze your portfolio data using natural language. Ask me anything about your investments, categories, or portfolio history!"
            }
        ]
    
    # Suggested questions section
    st.markdown("### 💡 Suggested Questions")
    st.markdown("")  # Add spacing
    
    suggested_questions = st.session_state.chat_agent.get_suggested_questions()
    
    # Display suggested questions in a nice grid
    cols = st.columns(2)
    for idx, question in enumerate(suggested_questions[:6]):  # Show first 6 questions
        col_idx = idx % 2
        with cols[col_idx]:
            if st.button(f"💬 {question}", key=f"suggest_{idx}", use_container_width=True):
                # Add question to chat
                st.session_state.chat_messages.append({
                    "role": "user",
                    "content": question
                })
                # Process the question
                with st.spinner("🤔 Thinking..."):
                    response = st.session_state.chat_agent.query(question)
                    st.session_state.chat_messages.append({
                        "role": "assistant",
                        "content": response['output']
                    })
                st.rerun()
    
    st.markdown("---")
    st.markdown("### 💬 Chat")
    st.markdown("")  # Add spacing
    
    # Display chat messages
    for message in st.session_state.chat_messages:
        role = message["role"]
        content = message["content"]
        
        with st.chat_message(role):
            st.markdown(content)
    
    # Chat input
    user_question = st.chat_input(
        placeholder="Ask me anything about your portfolio... (e.g., 'What's my total portfolio value?')"
    )
    
    if user_question:
        # Add user message to chat
        st.session_state.chat_messages.append({
            "role": "user",
            "content": user_question
        })
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_question)
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("🤔 Analyzing your portfolio data..."):
                response = st.session_state.chat_agent.query(user_question)
                
                if response['success']:
                    st.markdown(response['output'])
                    st.session_state.chat_messages.append({
                        "role": "assistant",
                        "content": response['output']
                    })
                else:
                    error_msg = "❌ Sorry, I encountered an error. Please try rephrasing your question."
                    st.error(error_msg)
                    if response['error']:
                        with st.expander("🔍 Error Details"):
                            st.code(response['error'])
                    st.session_state.chat_messages.append({
                        "role": "assistant",
                        "content": error_msg
                    })
    
    # Help section
    with st.expander("ℹ️ How to use the AI Chatbot"):
        st.markdown("""
        ### Tips for asking questions:
        
        1. **Be specific**: "What was my portfolio value in December 2024?" works better than "Show me data"
        
        2. **Ask about trends**: "Compare my portfolio values between January and March 2024"
        
        3. **Request analysis**: "Which investment category has grown the most?"
        
        4. **Simple queries**: "Show me all my investment categories"
        
        5. **Aggregations**: "What is my average monthly portfolio value?"
        
        ### What the chatbot can do:
        - Query your portfolio data using natural language
        - Perform calculations and aggregations
        - Compare values across different time periods
        - List categories and portfolio entries
        - Generate insights from your portfolio data
        
        ### Database Schema:
        - **investment_category**: Your investment categories
        - **portfolio_month**: Monthly snapshots
        - **portfolio_value**: Portfolio values by category and month
        """)

if __name__ == "__main__":
    main()

