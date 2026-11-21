# Name: Prathana Kumari
# Admission No: 26B15410286
# email: prathana.26b15410286
# github repository:https://github.com/prathana23052007/Prathana_HCL_Project/edit/main/Travel-and-tourism.py

import os
import numpy as np
import pandas as pd

# ============================================================
# CREATE OUTPUT FOLDER
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE_DIR, "output")

if os.path.exists(OUT_DIR) and not os.path.isdir(OUT_DIR):
    os.remove(OUT_DIR)

os.makedirs(OUT_DIR, exist_ok=True)

# ============================================================
# HEADING FUNCTION
# ============================================================

def heading(text):
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60)

# ============================================================
# TASK 1 : LOAD DATASET
# ============================================================

heading("TASK 1 : LOAD AND INSPECT DATASET")

df = pd.read_csv("29_travel_bookings.csv")

print("Shape :", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Records:")
print(df.head())

# ============================================================
# TASK 2 : MISSING VALUES AND DUPLICATES
# ============================================================

heading("TASK 2 : MISSING VALUES AND DUPLICATES")

print("Missing Values:")

print(df.isnull().sum()[df.isnull().sum() > 0])

duplicate_count = df["Booking_ID"].duplicated().sum()

print("\nDuplicate Booking IDs:", duplicate_count)

print(
    df[df["Booking_ID"].duplicated(keep=False)]
    [["Booking_ID", "Destination", "Booking_Amount"]]
    .head(10)
)

# Remove duplicate bookings

df = df.drop_duplicates(
    subset="Booking_ID",
    keep="first"
).reset_index(drop=True)

print("\nRows After Removing Duplicates:", len(df))

# ============================================================
# TASK 3 : HANDLE MISSING VALUES
# ============================================================

heading("TASK 3 : HANDLE MISSING VALUES")

# Fill duration using median package duration

df["Trip_Duration_Days"] = df["Trip_Duration_Days"].fillna(
    df.groupby("Package_Type")["Trip_Duration_Days"]
      .transform("median")
)

# Fill booking amount using destination + package median

df["Booking_Amount"] = df["Booking_Amount"].fillna(
    df.groupby(
        ["Destination", "Package_Type"]
    )["Booking_Amount"]
    .transform("median")
)

# Remaining amount values

df["Booking_Amount"] = df["Booking_Amount"].fillna(
    df["Booking_Amount"].median()
)

df["Trip_Duration_Days"] = (
    df["Trip_Duration_Days"]
    .round()
    .astype(int)
)

print("Missing Trip_Duration_Days:",
      df["Trip_Duration_Days"].isnull().sum())

print("Missing Booking_Amount:",
      df["Booking_Amount"].isnull().sum())

# ============================================================
# TASK 4 : DATE CONVERSION
# ============================================================

heading("TASK 4 : BOOKING DATE CONVERSION")

df["Booking_Date"] = pd.to_datetime(
    df["Booking_Date"],
    dayfirst=True
)

df["Month_Num"] = df["Booking_Date"].dt.month

df["Month"] = df["Booking_Date"].dt.month_name()

df["Weekday"] = df["Booking_Date"].dt.day_name()

print(
    df[
        ["Booking_Date",
         "Month",
         "Weekday"]
    ].head()
)

# ============================================================
# TASK 5 : TOTALS
# ============================================================

heading("TASK 5 : TOTAL BOOKINGS")

total_bookings = len(df)

total_travelers = df["Num_Travelers"].sum()

total_revenue = df["Booking_Amount"].sum()

print("Total Bookings:", total_bookings)
print("Total Travelers:", total_travelers)
print(f"Total Revenue: Rs {total_revenue:,.0f}")

# ============================================================
# TASK 6 : AVERAGES
# ============================================================

heading("TASK 6 : AVERAGES")

print(
    f"Average Booking Amount: Rs {df['Booking_Amount'].mean():,.0f}"
)

print(
    f"Average Trip Duration: {df['Trip_Duration_Days'].mean():.2f} Days"
)

# ============================================================
# TASK 7 : DESTINATION RANKING
# ============================================================

heading("TASK 7 : DESTINATION RANKING")

destination_summary = (
    df.groupby("Destination")
      .agg(
        Booking_Count=("Booking_ID", "count"),
        Total_Revenue=("Booking_Amount", "sum"),
        Average_Value=("Booking_Amount", "mean")
      )
      .reset_index()
)

destination_summary = destination_summary.sort_values(
    by="Booking_Count",
    ascending=False
)

print(destination_summary)

destination_summary.to_csv(
    os.path.join(
        OUT_DIR,
        "destination_ranking.csv"
    ),
    index=False
)

# ============================================================
# TASK 8 : PACKAGE ANALYSIS
# ============================================================

heading("TASK 8 : PACKAGE TYPE ANALYSIS")

package_summary = (
    df.groupby("Package_Type")
      .agg(
        Avg_Duration=("Trip_Duration_Days", "mean"),
        Avg_Amount=("Booking_Amount", "mean"),
        Avg_Rating=("Customer_Rating", "mean")
      )
      .round(2)
)

print(package_summary)

# ============================================================
# TASK 9 : AGE GROUP ANALYSIS
# ============================================================

heading("TASK 9 : AGE GROUP ANALYSIS")

df["Age_Group"] = pd.cut(
    df["Customer_Age"],
    bins=[17, 25, 35, 45, 55, 100],
    labels=[
        "18-25",
        "26-35",
        "36-45",
        "46-55",
        "56+"
    ]
)

age_summary = (
    df.groupby("Age_Group")
      .agg(
        Bookings=("Booking_ID", "count"),
        Avg_Amount=("Booking_Amount", "mean"),
        Avg_Duration=("Trip_Duration_Days", "mean")
      )
      .round(2)
)

print(age_summary)

# ============================================================
# TASK 10 : TOP 5 MONTHS
# ============================================================

heading("TASK 10 : TOP 5 MONTHS")

top_months = (
    df["Month"]
      .value_counts()
      .head(5)
)

print(top_months)

# ============================================================
# TASK 11 : LIST TUPLE SET
# ============================================================

heading("TASK 11 : LIST TUPLE SET")

popular_destinations = (
    destination_summary["Destination"]
    .head(5)
    .tolist()
)

package_types = (
    "Budget",
    "Standard",
    "Premium",
    "Luxury"
)

unique_destinations = set(
    df["Destination"]
)

print("Popular Destinations:")
print(popular_destinations)

print("\nPackage Types:")
print(package_types)

print("\nUnique Destinations:")
print(unique_destinations)

# ============================================================
# TASK 12 : DICTIONARY AND FUNCTION
# ============================================================

heading("TASK 12 : DICTIONARY AND FUNCTION")

destination_counts = (
    df["Destination"]
    .value_counts()
    .to_dict()
)

for place, count in destination_counts.items():
    print(f"{place:<15} {count}")

def average_booking_value(destination):

    data = df[
        df["Destination"]
        .str.lower()
        ==
        destination.lower()
    ]

    if data.empty:
        return None

    return data["Booking_Amount"].mean()

print("\nGoa:",
      average_booking_value("Goa"))

print("Dubai:",
      average_booking_value("Dubai"))

# ============================================================
# TASK 13 : NUMPY STATISTICS
# ============================================================

heading("TASK 13 : NUMPY STATISTICS")

amounts = df["Booking_Amount"].to_numpy()

print("Mean:",
      round(np.mean(amounts), 2))

print("Median:",
      round(np.median(amounts), 2))

print("Standard Deviation:",
      round(np.std(amounts), 2))

# ============================================================
# TASK 14 : IQR OUTLIERS
# ============================================================

heading("TASK 14 : IQR OUTLIERS")

Q1 = np.percentile(amounts, 25)
Q3 = np.percentile(amounts, 75)

IQR = Q3 - Q1

Upper = Q3 + 1.5 * IQR

outliers = df[
    df["Booking_Amount"] > Upper
]

print("\nOutlier Count:",
      len(outliers))

print(
    outliers[
        [
            "Booking_ID",
            "Destination",
            "Booking_Amount"
        ]
    ].head(10)
)

def duration_band(days):

    if days <= 4:
        return "Short"

    elif days <= 7:
        return "Medium"

    return "Long"

df["Duration_Band"] = (
    df["Trip_Duration_Days"]
      .apply(duration_band)
)

print(
    df["Duration_Band"]
      .value_counts()
)

# ============================================================
# TASK 15 : CLASS
# ============================================================

heading("TASK 15 : CLASS")

class TravelBooking:

    def __init__(
        self,
        booking_id,
        destination,
        amount
    ):
        self.booking_id = booking_id
        self.destination = destination
        self.amount = amount

    def show(self):
        print(
            f"Booking {self.booking_id} | "
            f"{self.destination} | "
            f"Rs {self.amount:,.0f}"
        )

for _, row in df.head(3).iterrows():

    booking = TravelBooking(
        row["Booking_ID"],
        row["Destination"],
        row["Booking_Amount"]
    )

    booking.show()

# ============================================================
# SAVE FILES
# ============================================================

df.to_csv(
    os.path.join(
        OUT_DIR,
        "travel_bookings_cleaned.csv"
    ),
    index=False
)

df.to_excel(
    os.path.join(
        OUT_DIR,
        "travel_bookings_cleaned.xlsx"
    ),
    index=False
)
