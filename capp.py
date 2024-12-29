import streamlit as st
from nltk.chat.util import Chat, reflections


pairs = [
    [
        r"hi|hello|hey",
        ["Hello! I'm your finance assistant. How can I help you today?", "Hi there! Ready to manage your finances?"]
    ],
    [
        r"(.*) budget",
        ["To create a budget, start by listing all your income and expenses.", 
         "A good rule of thumb is the 50/30/20 rule: 50% needs, 30% wants, 20% savings."]
    ],
    [
        r"(.*) save money",
        ["Track your expenses, avoid unnecessary purchases, and aim to save at least 20% of your income.", 
         "Automating your savings can be very effective."]
    ],
    [
        r"(.*) investment options",
        ["You can explore options like stocks, bonds, mutual funds, or real estate. Always assess the risk involved.",
         "For beginners, index funds and ETFs are good low-risk options."]
    ],
    [
        r"(.*) track expenses",
        ["You can use apps like Mint, YNAB, or even Excel to track your expenses effectively.",
         "Start by categorizing your spending into essentials, non-essentials, and savings."]
    ],
    [
        r"(.*) retirement planning",
        ["It's never too early to start. Consider contributing to retirement accounts like a 401(k) or IRA.",
         "Aim to save at least 15% of your income for retirement."]
    ],
    [
        r"(.*) debt management",
        ["Focus on paying off high-interest debt first, then move to low-interest debt.",
         "Consider using the snowball or avalanche method for tackling debt."]
    ],
    [
        r"(.*) emergency fund",
        ["An emergency fund should cover 3-6 months of living expenses.", 
         "Start small and aim to build it up gradually."]
    ],
    [
        r"quit|bye",
        ["Goodbye! Remember to stay financially smart.", "Bye! Reach out if you need more financial advice."]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand that. Could you elaborate?", "Can you please clarify your query?"]
    ]
]

# Create a chatbot instance
finance_chatbot = Chat(pairs, reflections)

# Streamlit app interface
st.title("Finance Management Chatbot 🤖💰")
st.subheader("Ask me anything about budgeting, saving, investments, and more!")

# Input box for user query
user_input = st.text_input("Type your question here and press Enter:", "")

if user_input:
    if user_input.lower() in ["quit", "bye"]:
        st.write("Goodbye! Remember to stay financially smart.")
    else:
        response = finance_chatbot.respond(user_input)
        st.write(f"💬 Chatbot: {response}")

st.markdown("---")
st.markdown("**Tip:** Type 'quit' or 'bye' to end the chat.")

