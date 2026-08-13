# ============================================================
# PANDAS COMPLETE REVISION - 100+ LINES
# ============================================================

import pandas as pd
import numpy as np

# ============================================================
# 1. CREATE A DATAFRAME
# ============================================================

df = pd.DataFrame({
    "ID": [101, 102, 103, 104, 105],
    "Name": ["  Alice  ", "Bob", "Charlie", "David", "Eva"],
    "Age": [22, 25, 30, 28, 24],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 45000, 70000, 60000, 48000],
    "Marks": [85, 72, 90, 65, 78],
    "City": ["Bangalore", "Mumbai", "Delhi", "Pune", "Bangalore"]
})

print("\n========== ORIGINAL DATA ==========")
print(df)


# ============================================================
# 2. BASIC DATAFRAME INFORMATION
# ============================================================

print("\n========== HEAD ==========")
print(df.head())

print("\n========== TAIL ==========")
print(df.tail())

print("\n========== SHAPE ==========")
print(df.shape)

print("\n========== COLUMNS ==========")
print(df.columns)

print("\n========== INDEX ==========")
print(df.index)

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== INFO ==========")
df.info()

print("\n========== STATISTICS ==========")
print(df.describe())


# ============================================================
# 3. SELECTING COLUMNS
# ============================================================

print("\n========== SINGLE COLUMN ==========")
print(df["Name"])

print("\n========== MULTIPLE COLUMNS ==========")
print(df[["Name", "Age", "Salary"]])


# ============================================================
# 4. SELECTING ROWS WITH iloc
# ============================================================

print("\n========== FIRST ROW ==========")
print(df.iloc[0])

print("\n========== FIRST THREE ROWS ==========")
print(df.iloc[0:3])

print("\n========== FIRST TWO COLUMNS ==========")
print(df.iloc[:, 0:2])

print("\n========== ROW 1, COLUMN 2 ==========")
print(df.iloc[1, 2])


# ============================================================
# 5. SELECTING DATA WITH loc
# ============================================================

print("\n========== LOC ==========")
print(df.loc[0])

print("\n========== LOC ROWS + COLUMNS ==========")
print(df.loc[0:2, ["Name", "Age"]])


# ============================================================
# 6. BOOLEAN INDEXING / FILTERING
# ============================================================

print("\n========== AGE > 25 ==========")
print(df[df["Age"] > 25])

print("\n========== SALARY >= 50000 ==========")
print(df[df["Salary"] >= 50000])

print("\n========== MARKS < 70 ==========")
print(df[df["Marks"] < 70])


# ============================================================
# 7. MULTIPLE CONDITIONS
# ============================================================

print("\n========== AGE > 25 AND SALARY > 50000 ==========")
print(df[(df["Age"] > 25) & (df["Salary"] > 50000)])

print("\n========== IT OR HR ==========")
print(df[
    (df["Department"] == "IT") |
    (df["Department"] == "HR")
])

print("\n========== NOT IT ==========")
print(df[df["Department"] != "IT"])


# ============================================================
# 8. query()
# ============================================================

print("\n========== QUERY ==========")
print(df.query("Age > 25"))

print("\n========== QUERY WITH MULTIPLE CONDITIONS ==========")
print(df.query("Age > 25 and Salary >= 50000"))


# ============================================================
# 9. isin()
# ============================================================

print("\n========== ISIN ==========")
print(df[df["Department"].isin(["IT", "HR"])])

print("\n========== CITY ISIN ==========")
print(df[df["City"].isin(["Bangalore", "Delhi"])])


# ============================================================
# 10. between()
# ============================================================

print("\n========== AGE BETWEEN 23 AND 28 ==========")
print(df[df["Age"].between(23, 28)])

print("\n========== MARKS BETWEEN 70 AND 90 ==========")
print(df[df["Marks"].between(70, 90)])


# ============================================================
# 11. STRING OPERATIONS - .str
# ============================================================

print("\n========== LOWERCASE ==========")
print(df["Name"].str.lower())

print("\n========== UPPERCASE ==========")
print(df["Name"].str.upper())

print("\n========== TITLE ==========")
print(df["Name"].str.title())

print("\n========== STRIP SPACES ==========")
print(df["Name"].str.strip())

print("\n========== STRING LENGTH ==========")
print(df["Name"].str.len())

print("\n========== STARTS WITH A ==========")
print(df[df["Name"].str.strip().str.startswith("A")])

print("\n========== CONTAINS A ==========")
print(df[df["Name"].str.contains("a", case=False, na=False)])

print("\n========== REPLACE TEXT ==========")
print(df["City"].str.replace("Bangalore", "Bengaluru"))


# ============================================================
# 12. ADD A NEW COLUMN
# ============================================================

df["Bonus"] = df["Salary"] * 0.10

print("\n========== NEW COLUMN ==========")
print(df)


# ============================================================
# 13. ADD COLUMN USING A CONDITION
# ============================================================

df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print("\n========== RESULT COLUMN ==========")
print(df)


# ============================================================
# 14. ADD COLUMN USING EXISTING COLUMNS
# ============================================================

df["Salary_After_Bonus"] = df["Salary"] + df["Bonus"]

print("\n========== CALCULATED COLUMN ==========")
print(df)


# ============================================================
# 15. INSERT COLUMN AT A SPECIFIC POSITION
# ============================================================

df.insert(2, "Country", "India")

print("\n========== INSERTED COLUMN ==========")
print(df)


# ============================================================
# 16. ADD ONE NEW ROW
# ============================================================

df.loc[len(df)] = [
    106,
    "India",
    "Frank",
    26,
    "IT",
    55000,
    82,
    "Hyderabad",
    5500,
    "Pass",
    60500
]

print("\n========== AFTER ADDING ONE ROW ==========")
print(df)


# ============================================================
# 17. REMOVE A COLUMN
# ============================================================

df = df.drop("Country", axis=1)

print("\n========== COUNTRY REMOVED ==========")
print(df)


# ============================================================
# 18. SORTING
# ============================================================

print("\n========== SORT BY AGE ==========")
print(df.sort_values("Age"))

print("\n========== SORT BY SALARY DESCENDING ==========")
print(df.sort_values("Salary", ascending=False))

print("\n========== SORT BY DEPARTMENT AND SALARY ==========")
print(df.sort_values(["Department", "Salary"]))


# ============================================================
# 19. UNIQUE VALUES AND COUNTS
# ============================================================

print("\n========== UNIQUE DEPARTMENTS ==========")
print(df["Department"].unique())

print("\n========== NUMBER OF UNIQUE DEPARTMENTS ==========")
print(df["Department"].nunique())

print("\n========== DEPARTMENT COUNTS ==========")
print(df["Department"].value_counts())

print("\n========== DEPARTMENT PERCENTAGE ==========")
print(df["Department"].value_counts(normalize=True))


# ============================================================
# 20. STATISTICAL FUNCTIONS
# ============================================================

print("\n========== MEAN SALARY ==========")
print(df["Salary"].mean())

print("\n========== MEDIAN SALARY ==========")
print(df["Salary"].median())

print("\n========== MIN SALARY ==========")
print(df["Salary"].min())

print("\n========== MAX SALARY ==========")
print(df["Salary"].max())

print("\n========== TOTAL SALARY ==========")
print(df["Salary"].sum())

print("\n========== STANDARD DEVIATION ==========")
print(df["Salary"].std())


# ============================================================
# 21. GROUPBY
# ============================================================

print("\n========== AVERAGE SALARY BY DEPARTMENT ==========")
print(
    df.groupby("Department")["Salary"].mean()
)

print("\n========== AVERAGE MARKS BY DEPARTMENT ==========")
print(
    df.groupby("Department")["Marks"].mean()
)

print("\n========== MULTIPLE AGGREGATIONS ==========")
print(
    df.groupby("Department")["Salary"].agg(
        ["mean", "min", "max", "count"]
    )
)


# ============================================================
# 22. APPLY()
# ============================================================

df["Age_Next_Year"] = df["Age"].apply(
    lambda x: x + 1
)

print("\n========== APPLY ==========")
print(df[["Name", "Age", "Age_Next_Year"]])


# ============================================================
# 23. DUPLICATES
# ============================================================

print("\n========== DUPLICATES ==========")
print(df.duplicated())

print("\n========== REMOVE DUPLICATES ==========")
df = df.drop_duplicates()


# ============================================================
# 24. MISSING VALUES
# ============================================================

print("\n========== CHECK MISSING VALUES ==========")
print(df.isna())

print("\n========== MISSING VALUE COUNT ==========")
print(df.isna().sum())

print("\n========== NON-MISSING VALUES ==========")
print(df.notna())


# ============================================================
# 25. CREATE MISSING DATA
# ============================================================

df.loc[0, "Salary"] = np.nan

print("\n========== DATA WITH MISSING SALARY ==========")
print(df)


# ============================================================
# 26. fillna()
# ============================================================

df["Salary"] = df["Salary"].fillna(
    df["Salary"].mean()
)

print("\n========== AFTER fillna() ==========")
print(df)


# ============================================================
# 27. dropna()
# ============================================================

temp_df = df.copy()

temp_df.loc[1, "Marks"] = np.nan

print("\n========== BEFORE dropna ==========")
print(temp_df)

temp_df = temp_df.dropna()

print("\n========== AFTER dropna ==========")
print(temp_df)


# ============================================================
# 28. RENAME COLUMNS
# ============================================================

df = df.rename(
    columns={
        "Name": "Student_Name",
        "Marks": "Exam_Marks"
    }
)

print("\n========== RENAMED COLUMNS ==========")
print(df)


# ============================================================
# 29. RESET INDEX
# ============================================================

df = df.reset_index(drop=True)

print("\n========== RESET INDEX ==========")
print(df)


# ============================================================
# 30. SET INDEX
# ============================================================

indexed_df = df.set_index("ID")

print("\n========== SET ID AS INDEX ==========")
print(indexed_df)


# ============================================================
# 31. CREATE SECOND DATAFRAME FOR JOINING
# ============================================================

orders = pd.DataFrame({
    "ID": [101, 102, 106, 110],
    "Order_Amount": [500, 700, 900, 300],
    "Product": ["Laptop", "Phone", "Tablet", "Monitor"]
})

print("\n========== ORDERS DATAFRAME ==========")
print(orders)


# ============================================================
# 32. INNER JOIN
# ============================================================

inner_join = pd.merge(
    df,
    orders,
    on="ID",
    how="inner"
)

print("\n========== INNER JOIN ==========")
print(inner_join)


# ============================================================
# 33. LEFT JOIN
# ============================================================

left_join = pd.merge(
    df,
    orders,
    on="ID",
    how="left"
)

print("\n========== LEFT JOIN ==========")
print(left_join)


# ============================================================
# 34. RIGHT JOIN
# ============================================================

right_join = pd.merge(
    df,
    orders,
    on="ID",
    how="right"
)

print("\n========== RIGHT JOIN ==========")
print(right_join)


# ============================================================
# 35. OUTER JOIN
# ============================================================

outer_join = pd.merge(
    df,
    orders,
    on="ID",
    how="outer"
)

print("\n========== OUTER JOIN ==========")
print(outer_join)


# ============================================================
# 36. JOIN USING DIFFERENT COLUMN NAMES
# ============================================================

orders_2 = orders.rename(
    columns={"ID": "Customer_ID"}
)

different_key_join = pd.merge(
    df,
    orders_2,
    left_on="ID",
    right_on="Customer_ID",
    how="inner"
)

print("\n========== DIFFERENT COLUMN NAME JOIN ==========")
print(different_key_join)


# ============================================================
# 37. CONCAT - ADD ROWS
# ============================================================

new_students = pd.DataFrame({
    "ID": [107, 108],
    "Student_Name": ["George", "Helen"],
    "Age": [27, 23],
    "Department": ["IT", "HR"],
    "Salary": [58000, 47000],
    "Exam_Marks": [88, 76],
    "City": ["Pune", "Mumbai"]
})

rows_added = pd.concat(
    [df, new_students],
    ignore_index=True
)

print("\n========== CONCAT ROWS ==========")
print(rows_added)


# ============================================================
# 38. CONCAT - ADD COLUMNS
# ============================================================

extra_columns = pd.DataFrame({
    "Experience": [1, 2, 5, 4, 2, 3, 4],
    "Status": ["Active"] * 7
})

columns_added = pd.concat(
    [df.reset_index(drop=True),
     extra_columns],
    axis=1
)

print("\n========== CONCAT COLUMNS ==========")
print(columns_added)


# ============================================================
# 39. SAMPLE
# ============================================================

print("\n========== RANDOM SAMPLE ==========")
print(df.sample(3))


# ============================================================
# 40. VALUE REPLACEMENT
# ============================================================

df["Department"] = df["Department"].replace(
    "IT",
    "Information Technology"
)

print("\n========== REPLACED VALUE ==========")
print(df)


# ============================================================
# 41. WHERE
# ============================================================

print("\n========== WHERE ==========")
print(
    df["Exam_Marks"].where(
        df["Exam_Marks"] >= 70,
        0
    )
)


# ============================================================
# 42. MASK
# ============================================================

print("\n========== MASK ==========")
print(
    df["Exam_Marks"].mask(
        df["Exam_Marks"] < 70,
        0
    )
)


# ============================================================
# 43. DATE/TIME OPERATIONS
# ============================================================

df["Joining_Date"] = pd.to_datetime([
    "2024-01-10",
    "2023-05-20",
    "2022-03-15",
    "2024-06-01",
    "2023-09-10",
    "2024-02-20"
])

print("\n========== DATE COLUMN ==========")
print(df["Joining_Date"])

print("\n========== YEAR ==========")
print(df["Joining_Date"].dt.year)

print("\n========== MONTH ==========")
print(df["Joining_Date"].dt.month)

print("\n========== DAY ==========")
print(df["Joining_Date"].dt.day)

print("\n========== DAY NAME ==========")
print(df["Joining_Date"].dt.day_name())


# ============================================================
# 44. STRING SPLIT
# ============================================================

print("\n========== STRING SPLIT ==========")
print(
    df["Student_Name"].str.split()
)


# ============================================================
# 45. STRING LENGTH
# ============================================================

print("\n========== NAME LENGTH ==========")
print(
    df["Student_Name"].str.len()
)


# ============================================================
# 46. FILTER USING STRING
# ============================================================

print("\n========== NAMES CONTAINING 'a' ==========")
print(
    df[
        df["Student_Name"].str.contains(
            "a",
            case=False,
            na=False
        )
    ]
)


# ============================================================
# 47. FINAL DATAFRAME INFORMATION
# ============================================================

print("\n========== FINAL SHAPE ==========")
print(df.shape)

print("\n========== FINAL COLUMNS ==========")
print(df.columns)

print("\n========== FINAL DATA TYPES ==========")
print(df.dtypes)

print("\n========== FINAL DATA ==========")
print(df)


# ============================================================
# 48. SAVE DATA
# ============================================================

# Save as CSV
df.to_csv(
    "pandas_revision_output.csv",
    index=False
)

# Save as Excel
# df.to_excel("pandas_revision_output.xlsx", index=False)


# ============================================================
# END OF PANDAS REVISION
# ============================================================