
from nltk.chat.util import Chat, reflections
import time

# Enhanced pairs with more natural language variations
pairs = [
    [
        r"hi|hello|hey|hey there|good morning|good afternoon",
        ["Hello! I'm your Finance Assistant. How can I help you manage your money today? 💬", 
         "Hi there! Ready to take control of your finances? I'm here to help! 💰", 
         "Hey! Welcome back. How can I assist you with your financial goals today? 🌟"]
    ],
    [
        r"(.*) budget(.*)",
        ["To create a solid budget, start by tracking your monthly income and all expenses—both fixed and variable.",
         "Try the 50/30/20 rule: 50% needs, 30% wants, and 20% savings or debt repayment. Want help applying it?",
         "Budgeting apps like YNAB or Mint can automate the process. Would you like tips on setting one up?"]
    ],
    [
        r"(.*) save money|save|saving|savings",
        ["Start by cutting recurring subscriptions you don’t use and automating transfers to a savings account.",
         "A great strategy is 'pay yourself first'—set aside savings before spending on anything else.",
         "Consider using a high-yield savings account to grow your emergency fund faster."]
    ],
    [
        r"(.*) investment|investing|invest|stocks|bonds|mutual funds|etf",
        ["For beginners, low-cost index funds and ETFs offer diversification and steady growth over time.",
         "Your risk tolerance and timeline matter. Younger investors often lean toward stocks; those near retirement may prefer bonds.",
         "Consider tax-advantaged accounts like IRAs or 401(k)s for long-term investing."]
    ],
    [
        r"(.*) track expenses|spending|spend|where did my money go",
        ["Use apps like Mint, YNAB, or PocketGuard to automatically sync and categorize your transactions.",
         "Manually tracking for one week can reveal surprising spending habits. A simple spreadsheet works too!",
         "Categorize spending into Needs, Wants, and Savings to gain clarity."]
    ],
    [
        r"(.*) retirement|retirement planning|retire",
        ["Start early! Even small contributions grow significantly with compound interest.",
         "Aim to save 10–15% of your income annually. If your employer offers a 401(k) match, take full advantage.",
         "Roth IRAs are great for tax-free growth in retirement. Want help estimating your retirement needs?"]
    ],
    [
        r"(.*) debt|debt management|pay off debt|credit card debt",
        ["Use the avalanche method (pay highest interest first) to save money, or the snowball method (smallest balance first) for motivation.",
         "Consolidating high-interest debt with a lower-interest personal loan can help reduce

