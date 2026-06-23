# Expense Tracker Script

An interactive command-line interface (CLI) application that allows users to log expense amounts, calculates the total spent, and displays a summary report.

This project demonstrates core backend programming concepts, specifically **input validation**, **loops**, and **accumulators**.

## Key Programming Skill: Accumulators

The core logic of this program revolves around an **accumulator**. An accumulator is a variable used to gather or accumulate data step-by-step. 

In this script, the running total is accumulated using the following logic:
```python
total = total + new_expense
```
Or in its shorthand form:
```python
total += new_expense
```

---

## File Structure

- [expense_tracker.py](file:///C:/Users/intel/.gemini/antigravity/scratch/expense_tracker/expense_tracker.py) - The main script containing the interactive logic and calculations.

---

## How to Run

1. Open your terminal or command prompt.
2. Run the script using Python:
   ```bash
   python expense_tracker.py
   ```

---

## Features

- **Interactive Inputs**: Keep typing expense values one after another.
- **Robust Error Handling**: Handles non-numeric inputs gracefully without crashing.
- **Negative Value Check**: Ensures negative amounts are flagged to maintain accurate spending stats.
- **Exit Command**: Type `q`, `quit`, or `exit` to finalize your logging session and view your summary report.
