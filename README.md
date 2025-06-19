#  Expense Tracker – Python CLI App

A simple and powerful command-line app for tracking personal expenses, generating summaries, and visualizing spending via pie charts.

---

##  Features

- ✅ Add expenses with category, amount, and optional notes
- 📄 View all expenses in a readable format
- 📊 Summary by category (Food, Transport, etc.)
- 🧾 Delete an expense by number
- 🥧 Pie chart visualization using matplotlib
- 💾 Data stored in a local `expenses.json` file

---

##  Tech Stack

- Python 3
- `matplotlib`
- JSON (for persistence)
- CLI interface

---

##  Project Structure

expense-tracker/
├── tracker.py # Main CLI logic
├── utils.py # Expense model and load/save helpers
├── charts.py # Pie chart generation
├── expenses.json # Local data store
├── requirements.txt # Dependencies
└── README.md

---

##  How to Run

```bash
git clone https://github.com/Pkamana31/Expense-Tracker.git
cd Expense-Tracker

python -m venv venv
venv\Scripts\activate      # or source venv/bin/activate (Mac/Linux)

pip install -r requirements.txt
python tracker.py

## 📸 Screenshots

> _Example CLI output or pie chart here_  
> (You can add screenshots later by uploading in GitHub or dragging into the README editor.)

## 🧪 Example Usage

Select an option (1–6): 1
Enter amount (₹): 250
Enter category (e.g., Food, Transport): Food
Optional note: Lunch at cafe
✅ Expense added successfully.

## 🧠 Author

**Pranitha K**  
🔗 [LinkedIn](https://www.linkedin.com/in/pranitha-k)  
📫 GitHub: [@Pkamana31](https://github.com/Pkamana31)

## 📄 License

This project is licensed under the [MIT License](LICENSE).
