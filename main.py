import mysql.connector
import pandas as pd

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",port=3306,
        password="Sivaa@2004",
        database="adv"
    )

    print("✅ MySQL Connected Successfully!")

    cursor = conn.cursor()

    # SQL Query
    query = "SELECT * FROM emp"
    cursor.execute(query)

    # Fetch Data
    rows = cursor.fetchall()

    # Get Column Names
    columns = [i[0] for i in cursor.description]

    # Create DataFrame
    df = pd.DataFrame(rows, columns=columns)

    # Save Excel File
    df.to_excel("Employee_Report.xlsx", index=False)

    print("✅ Excel File Created Successfully!")

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print("❌ Error:", err)
