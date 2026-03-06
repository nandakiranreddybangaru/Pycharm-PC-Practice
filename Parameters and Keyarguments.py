# 1. THE MACHINE (The Logic)
def calculate_weekly_revenue(daily_revenues):
    total = 0

    # A. The loop goes inside the machine! It processes whatever list is handed to it.
    for day_revenue in daily_revenues:
        total = total + day_revenue

    # B. The return is outside the loop, but inside the function.
    # It hands back the final calculated number.
    return total


# 2. THE RAW DATA (From the clinics)
clinic_hyd_data = [1500, 2000, 1800, 2200, 900, 3000, 2500]
clinic_blr_data = [800, 1200, 1000, 1500, 900, 1100, 1300]

# 3. RUNNING THE PIPELINE
print("--- One Ayush Platform Weekly Report ---")

# C. We call the machine, pour the Hyderabad data in, and catch the returned number
hyd_total = calculate_weekly_revenue(clinic_hyd_data)

# D. We pour the Bangalore data into the exact same machine, and catch the answer
blr_total = calculate_weekly_revenue(clinic_blr_data)

# E. Now we print the clean, finalized numbers!
print(f"Hyderabad Clinic Total: ₹{hyd_total}")
print(f"Bangalore Clinic Total: ₹{blr_total}")