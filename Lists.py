employee_database = [
    ["Rahul", "HR", 500000],
    ["Priya", "IT", 85000],
    ["Amit", "Sales", 60000]
    ["Nanda Bangaru", "Finance", 200000]
    ["Raghu", "Automation Testing", 250000]
    ["Ravi", "Manual Testing", 150000]
    ["Rohit", "DevOps", 300000]
]

# The Outer Loop (Grabs one entire row at a time)
for row in employee_database:
    print("--- New Employee ---")

    # The Inner Loop (Grabs each specific item inside that row)
    for detail in row:
        print(detail)
