cat > README.md << 'EOF'
# Week 7 Python Assignment — Shopping List Manager

Three small Python programs that practise working with lists: index access, `.append()`, `.remove()`, membership checks with `in`, and looping to summarise what's inside.

## Files

- `list_warmup.py` — creates a list of four fruits, prints the first and last by index, appends a fifth, removes one, and prints the count with `len()`.
- `shopping_list.py` — an interactive menu (add / remove / show / done) that manages a shopping list. Uses `in` to check before removing so it never crashes.
- `list_report.py` — loops through a fixed list to print it numbered, counts items with more than 4 letters, and finds the longest item name using a loop comparison.

## Program output

- `screenshots/list_warmup_output.txt`
- `screenshots/shopping_list_output.txt`
- `screenshots/list_report_output.txt`

Note: this project was developed on a headless Ubuntu 24.04 session without a graphical desktop, so terminal output files are included instead of screenshots.

## Why it is safer to check `in` before calling `.remove()`

Calling `.remove(x)` on a list that doesn't contain `x` raises a `ValueError` and crashes the program. Before removing, we check `if x in shopping:` — the `in` operator returns `True` or `False` without raising anything, so we can print a friendly "That item is not on your list." message instead of letting the program stop. Checking first also keeps the interaction predictable for the user — they always get a clear response, never a crash.

## How to run

    python3 list_warmup.py
    python3 shopping_list.py
    python3 list_report.py

## Expected output

`list_warmup.py`:

    First fruit: apple
    Last fruit: mango
    After append: ['apple', 'banana', 'cherry', 'mango', 'orange']
    After remove: ['apple', 'cherry', 'mango', 'orange']
    Number of fruits: 4

`list_report.py`:

    Numbered list:
      1. bread
      2. avocado
      3. milk
      4. sweet potatoes
      5. tea

    Items with more than 4 letters: 3
    Longest item name: sweet potatoes

## Concepts used

- Creating lists and reading items by index
- Growing and shrinking lists with `.append()` and `.remove()`
- Membership test with `in`
- Counting with `len()`
- Looping with `for`
- Conditionals inside loops
- `break` to leave a `while True` loop

## Author

Zakariye Ali Mursal
PLP 2026
EOF