# Travel Booking & Tourist Preference Analysis

**Project 29** | Individual Assignment | Python, pandas, NumPy

A Python script that cleans a travel bookings dataset and analyses it to answer business questions: which destinations are most popular, which months are busiest, which packages customers prefer, and which bookings are unusually expensive.

---

## Problem Statement

A travel agency stores hundreds of bookings in a spreadsheet. The raw data has duplicate bookings, missing values and unformatted dates, so it cannot give reliable answers. This project cleans the data first and then produces clear summary tables that support decisions on destinations, pricing, marketing and seasonal planning.

---

## Features

- Loads the Excel dataset and shows its shape, columns, data types and sample rows
- Detects and removes duplicate `Booking_ID` records
- Fills missing `Trip_Duration_Days` and `Booking_Amount` using group medians
- Converts `Booking_Date` and extracts month and weekday
- Calculates total bookings, travelers and revenue, plus average amount and duration
- Ranks destinations by booking count and revenue
- Compares Budget, Standard, Premium and Luxury packages
- Analyses preferences by age group
- Finds the top 5 busiest months
- Detects unusually expensive bookings using the IQR method
- Groups trips into Short, Medium and Long bands
- Demonstrates list, tuple, set, dictionary, function and class in Python
- Saves the cleaned data and summary tables to an `output` folder

---

## Project Structure

```
HCL Project/
├── Travel-and-tourism.py        # Main script
├── 29_travel_bookings.xlsx      # Input dataset (sheet: Travel_Bookings)
├── README.md                    # This file
└── output/                      # Created automatically when you run the script
    ├── destination_ranking.csv
    ├── package_comparison.csv
    ├── monthly_trend.csv
    ├── expensive_bookings.csv
    ├── travel_bookings_cleaned.csv
    └── travel_bookings_cleaned.xlsx
```

---

## Requirements

- Python 3.x
- pandas
- NumPy
- openpyxl (needed by pandas to read and write `.xlsx` files)

The `os` module is built into Python and needs no installation. Matplotlib is **not** used.

---

## Installation

Open the terminal in VS Code (`` Ctrl + ` ``) inside the project folder and run:

```
python -m pip install pandas numpy openpyxl
```

Check that everything imports:

```
python -c "import pandas, numpy, openpyxl; print('All OK')"
```

---

## How to Run

1. Put `Travel-and-tourism.py` and `29_travel_bookings.xlsx` in the **same folder**.
2. Open the folder in VS Code.
3. Select the Python interpreter where you installed the libraries (`Ctrl+Shift+P` > **Python: Select Interpreter**).
4. Run in the terminal:

```
python Travel-and-tourism.py
```

Or click the play button at the top right of the editor.

The results print in the terminal under 15 numbered task headings, and the files are saved in the `output` folder.

---

## Input Data

Sheet name: `Travel_Bookings`

| Column | Description |
|---|---|
| Booking_ID | Unique identifier of a booking |
| Destination | Place the customer is travelling to |
| Package_Type | Budget, Standard, Premium or Luxury |
| Booking_Amount | Amount paid (Rs) |
| Trip_Duration_Days | Length of the trip in days |
| Booking_Date | Date the booking was made |
| Num_Travelers | Number of people in the booking |
| Customer_Age | Age of the customer |
| Customer_Rating | Customer rating (may be missing) |

---

## Data Cleaning Rules

| Issue | Rule |
|---|---|
| Duplicate `Booking_ID` | Keep the first record, remove the rest |
| Missing `Trip_Duration_Days` | Median of the same `Package_Type`, rounded to whole days |
| Missing `Booking_Amount` | Median of the same `Destination` + `Package_Type`; overall median if the group is empty |
| Missing `Customer_Rating` | Left as is (averages ignore missing values) |

Medians are used instead of means because booking amounts contain high outliers.

---

## Tasks Covered

| Task | Description |
|---|---|
| 1 | Load and inspect the dataset |
| 2 | Check missing values and duplicates |
| 3 | Handle missing values |
| 4 | Date conversion, month and weekday |
| 5 | Totals: bookings, travelers, revenue |
| 6 | Averages: booking amount, trip duration |
| 7 | Destination ranking |
| 8 | Trip duration by package type |
| 9 | Preferences by age group |
| 10 | Top 5 months by bookings |
| 11 | List, tuple and set |
| 12 | Dictionary and function |
| 13 | NumPy statistics (mean, median, standard deviation) |
| 14 | IQR outliers and trip-duration bands |
| 15 | `TravelBooking` class |

---

## Output Files

| File | Content |
|---|---|
| `destination_ranking.csv` | Bookings, revenue, average value and ranks per destination |
| `package_comparison.csv` | Bookings, average duration, amount and rating per package type |
| `monthly_trend.csv` | Number of bookings per month |
| `expensive_bookings.csv` | Bookings above Q3 + 1.5 x IQR |
| `travel_bookings_cleaned.csv` | Full cleaned dataset (CSV) |
| `travel_bookings_cleaned.xlsx` | Full cleaned dataset (Excel) |

---

## Troubleshooting

**`File not found: ...29_travel_bookings.xlsx`**
Place the Excel file in the same folder as the script.

**`ModuleNotFoundError: No module named 'openpyxl'` (or pandas / numpy)**
Run `python -m pip install pandas numpy openpyxl`. If the error continues, VS Code is using a different Python. Fix it with **Python: Select Interpreter**.

**`ImportError: DLL load failed ... An Application Control policy has blocked this file`**
Windows security is blocking pandas' compiled files, so reinstalling will not help. Options:
- Install Python 3.12 or 3.13 from python.org and run with `py -3.13 Travel-and-tourism.py`
- Run the script in Google Colab (change `BASE_DIR` to `"."` because `__file__` does not exist in notebooks)
- On a college or company laptop, ask IT to allow Python packages

**`IndentationError: unexpected indent`**
Remove any space before the first character of a line, and run the whole file instead of a selected part.

**`import ...` shows "not recognized" in the terminal**
Python code goes in the `.py` file, not in the PowerShell terminal. The terminal is only for commands like `python Travel-and-tourism.py`.

---

## Limitations

- No charts are produced (matplotlib is not used)
- Filled values are estimates, not the true values
- Outliers are flagged, not removed
- The input file name and sheet name are fixed in the code

## Future Scope

- Add charts for destinations and monthly trends
- Build an interactive dashboard
- Predict demand from the monthly trend
- Let the user choose the input file at run time
