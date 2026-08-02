import mysql.connector
import pandas as pd

try:
    # -----------------------------
    # MySQL Connection
    # -----------------------------
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Sivaa@2004",
        database="adv"
    )

    print("✅ MySQL Connected Successfully!")

    cursor = conn.cursor()

    # -----------------------------
    # SQL Query
    # Fetch employees whose first name starts with D
    # and salary is greater than 5000
    # -----------------------------
    query = """
    SELECT *
    FROM emp
    WHERE first_name LIKE 'D%'
      AND salary > 5000;
    """

    cursor.execute(query)

    # -----------------------------
    # Fetch Data
    # -----------------------------
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("⚠️ No records found.")
    else:
        # Get Column Names
        columns = [column[0] for column in cursor.description]

        # Create DataFrame
        df = pd.DataFrame(rows, columns=columns)

        # Display Data
        print(df)

        # Save to Excel
        file_name = "Employee_Report.xlsx"
        df.to_excel(file_name, index=False)

        print(f"\n✅ Excel File '{file_name}' Created Successfully!")

    # -----------------------------
    # Close Connection
    # -----------------------------
    cursor.close()
    conn.close()

    print("✅ Database Connection Closed!")

except mysql.connector.Error as err:
    print("❌ Database Error:", err)

except Exception as e:
    print("❌ Error:", e)