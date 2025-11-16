# Budget Tracker

## Overview
- This is a simple budget tracker program that allows users to add income and expenses, view all transactions, delete entries, and see summaries by category or overall balance.

## How to run it?
- This program is built using **python 3.13 (64-bit)**
- This code was made using vs-studio code
- The oldest version that this program can run on is python 3.6
### Tip 
- If the program does not work download Python 3.13
- If using Vs-Studio-Code your inputs can directly be entered in the terminal which is located down below

## Assumptions and Limitations
- **Assumption** that the program will store data till the program is running
- **Limitation** is that once the program is terminated the stored data is deleted aswell, no permenant storage

- **Assumption** that once the delete transaction option has been entered user has to delete a transactions
- **Limitation** there is no way to get out of the function untill user deletes a transaction

## Testing

### Task 2: Display Menu

| Test Case                          | Input                     | Expected Output                                      | Status |
|-----------------------------------|---------------------------|------------------------------------------------------|--------|
| Valid menu selection              | `1` to `7`                | Routes to correct function or exits                  | ✅     |
| Invalid menu selection            | `0`, `8`, `abc`           | Ignores the value and repeats the display options             |  ✅    |
| Continuous loop until exit        | Multiple valid inputs     | Keeps prompting until `7` is entered                 | ✅     |

### Task 3: Add Transaction

| Test Case                          | Input                     | Expected Output                                      | Status |
|-----------------------------------|---------------------------|------------------------------------------------------|--------|
| Valid income                      | `500`, `"Salary"`, `"Job"`| Transaction added successfully                       | ✅     |
| Valid expense                     | `50`, `"Lunch"`, `"Food"` | Transaction added successfully                       | ✅     |
| Negative amount                   | `-100`                    | Rejected with error message                          | ✅     |
| Non-numeric amount                | `"abc"`                   | Rejected with error message                          | ✅     |
| Empty description or category     | `""`                      | Accepted (stored as empty string)                    | ✅     |

### Task 4: List Transactions

| Test Case                          | Input                     | Expected Output                                      | Status |
|-----------------------------------|---------------------------|------------------------------------------------------|--------|
| No transactions                   | Empty list                | "No transaction found" message                       | ✅     |
| Multiple transactions             | 2–3 entries               | All displayed with correct formatting                | ✅     |

### Task 5: Delete Transaction

| Test Case                          | Input                     | Expected Output                                      | Status |
|-----------------------------------|---------------------------|------------------------------------------------------|--------|
| Valid index                       | `1`                       | Transaction removed                                  | ✅     |
| Invalid index                     | `0`, `999`, `abc`         | Error message shown                                  | ✅     |
| Empty list                        | No entries                | "List is empty" message                              | ✅     |

### Task 6: Summary Calculations

| Test Case                          | Input                     | Expected Output                                      | Status |
|-----------------------------------|---------------------------|------------------------------------------------------|--------|
| Only income                       | One income entry          | Expense = 0, Net Balance = Income                    | ✅     |
| Only expense                      | One expense entry         | Income = 0, Net Balance = -Expense                   | ✅     |
| Mixed transactions                | Multiple entries          | Correct totals and net balance                       | ✅     |
| Category summary with duplicates  | Two "Food" expenses       | Grouped correctly under "Food"                       | ✅     |
| Empty transaction list            | No entries                | Zero totals and empty category summary               | ✅     |

 
## Completion Report

| Task | Requirement Summary | Completed? | Notes |
|------|---------------------|------------|--------|
| **Task 1** | Docstrings and inline comments | ✅ Yes | All functions include clear docstrings with purpose, parameters, and return values.. |
| **Task 2** | Menu display and loop | ✅ Yes | `display_menu()` prints all 7 options. Main loop runs until user selects Exit. |
| **Task 3** | Add transaction with validation | ✅ Yes | `add_transaction()` handles income/expense, validates amount, and appends to `transactions` list. |
| **Task 4** | List transactions with formatting | ✅ Yes | `list_transactions()` prints indexed list or "No transactions found" if empty. |
| **Task 5** | Delete transaction by index | ✅ Yes | `delete_transaction()` validates input, handles empty list, and confirms deletion. |
| **Task 6** | Summary calculations using loops | ✅ Yes | `calculate_summary()`, `print_summary_by_category()`, `Print_Overall Summary` use loops and dictionaries (no `sum()` or `Counter`). |
| **Task 7** | README with overview, test plan, and report | ✅ Yes | README includes overview, run instructions, assumptions, test plan, and this completion table. |

