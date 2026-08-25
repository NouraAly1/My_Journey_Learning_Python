# My Journey Learning Python

Python programs I am building while preparing for software engineering internships.

This repository is a practice log, not a single app. Each file is a small program I wrote to learn a concept, run it, and be able to explain it: inputs, logic, and output.

## Why this repo exists

I want recruiters and interviewers to see how I learn. The early files cover language fundamentals. Later files move into lists, functions, error handling, pandas, Excel, and matplotlib.

As I add projects, this README stays the index: what each program does, which Python ideas it uses, and how to run it.

## Skills demonstrated

- Variables, operators, and user input
- Conditionals and loops (`if` / `elif` / `else`, `for`, `while`)
- Functions and reusable logic
- Lists, sorting, and simple summaries (min, max, count)
- String handling (slicing, `.strip()`, `.lower()`)
- Input validation with `try` / `except`
- pandas for reading Excel and working with DataFrames
- matplotlib for charts (line, bar, scatter, pie)

## Project index

### Fundamentals and control flow

| File | What it does |
| --- | --- |
| [for_loop_examples.py](for_loop_examples.py) | Practice with `for` loops |
| [while_loop_examples.py](while_loop_examples.py) | Practice with `while` loops |
| [function_practice.py](function_practice.py) | Defining and calling functions |
| [number_comparison.py](number_comparison.py) | Compare numbers with conditionals |
| [divisibility_checker.py](divisibility_checker.py) | Check whether a number is divisible by another |
| [weather_recommendation.py](weather_recommendation.py) | Suggest clothing based on a weather string |
| [grade_calculator.py](grade_calculator.py) | Convert a numeric score (0-100) to a letter grade, with invalid-input handling |
| [grade_converter.py](grade_converter.py) | Convert between grade formats |

### Calculators and applied logic

| File | What it does |
| --- | --- |
| [basic_calculator.py](basic_calculator.py) | Add, subtract, multiply, or divide two numbers; guards against division by zero |
| [age_calculator.py](age_calculator.py) | Calculate age from user input |
| [weight_converter.py](weight_converter.py) | Convert weight between units |
| [pay_calculator.py](pay_calculator.py) | Calculate pay from hours and rate |
| [salary_cal.py](salary_cal.py) | Salary calculation practice |
| [order_cost_calculator.py](order_cost_calculator.py) | Compute order cost |
| [shopping_calculator.py](shopping_calculator.py) | Shopping total practice |
| [money_distribution_calculator.py](money_distribution_calculator.py) | Split or distribute an amount of money |
| [power_function.py](power_function.py) | Practice with exponentiation |

### Lists, strings, and small tools

| File | What it does |
| --- | --- |
| [fruit_inventory_manager.py](fruit_inventory_manager.py) | Collect fruit names until `done`, skip empty input, then print a sorted summary |
| [basketball_score_tracker.py](basketball_score_tracker.py) | Track game scores until `done`, reject invalid or negative values, then show lowest, highest, and game count |
| [grocery_price_tracker.py](grocery_price_tracker.py) | Track grocery prices in a list |
| [temperature_tracker.py](temperature_tracker.py) | Track temperature readings |
| [username_proj.py](username_proj.py) | Username / string practice |
| [employee_credentials_generator.py](employee_credentials_generator.py) | Build an employee ID from name and date of birth, and rewrite an email domain |

### Data analysis

| File | What it does |
| --- | --- |
| [employee.xlsx](employee.xlsx) | Sample employee spreadsheet used by the pandas and chart files |
| [pandas_dataframe_practice.py](pandas_dataframe_practice.py) | Read Excel into a DataFrame; practice `loc`, `iloc`, filtering, and cell access |
| [pandas_data_manipulation.py](pandas_data_manipulation.py) | More pandas DataFrame manipulation |
| [visualization_matplot.py](visualization_matplot.py) | Chart employee data with matplotlib (line, bar, scatter, pie) |

## How to run a program

Most files are standalone console scripts:

```bash
python3 grade_calculator.py
```

The pandas and matplotlib files need those libraries and the Excel file in the same folder:

```bash
pip install pandas matplotlib openpyxl
python3 pandas_dataframe_practice.py
python3 visualization_matplot.py
```

## How I want this repo to be read

1. Start here for the project list.
2. Open a `.py` file. Comments at the top describe the goal.
3. Run it locally and change the inputs.

I keep each program small enough to read in one sitting so I can walk through the logic in an interview the same way I wrote it.

## About me

I am applying for internships and using this repository to show consistent practice in Python. If you are reviewing my application, the latest files are the best picture of where I am right now.

*This README will grow as I upload more advanced work.*
