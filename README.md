#  Expense Tracker – Python CLI App

<p align="center">
  <img src="./Thumbnail.png" width="720" alt="Expense Tracker Project Preview"/>
</p>


A command-line Python app to manage and analyze your expenses.  
Track spending, view summaries, export data, and visualize your budget with pie & bar charts — all from the terminal!

---

##  Features

- ✅ Add new expenses (amount, category, note)
- 📄 View all recorded expenses
- 📊 View summary by category
- 🧾 Delete individual expenses
- 📅 Filter expenses by month (e.g., 2024-06)
- 📤 Export expenses to CSV (`expenses_export.csv`)
- 🥧 Pie chart of category-wise spending
- 📊 Bar chart comparing total spent per category
- 💾 Data saved to `expenses.json`

---

##  Tech Stack

- Python 3
- `matplotlib`, `json`, `csv`
- Command-line interface

---

##  How to Run

```bash
# Clone the repo
git clone https://github.com/Pkamana31/Expense-Tracker.git
cd Expense-Tracker

# Set up a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
python tracker.py

🧪 Menu Options
1. Add new expense
2. View all expenses
3. View summary by category
4. Show pie chart
5. Show bar chart
6. Delete an expense
7. Filter expenses by month
8. Export expenses to CSV
9. Exit

📁 Project Structure
Expense-Tracker/
├── tracker.py            # CLI logic
├── utils.py              # Load/save/export helpers
├── charts.py             # Pie & bar chart visualization
├── expenses.json         # Local data storage
├── requirements.txt
└── README.md


🪪 License
This project is licensed under the MIT License
