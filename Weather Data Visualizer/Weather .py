# =================================================
#  Name = Parth Singh
#  Roll no = 2501730144
#  Course = B.tech CSE (AI/ML)
#  Section = D
# **********Weather Data Visualizer***********
# =================================================


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

filename = "weather.csv"

# -------------------------------
# ✅ STEP 1: CHECK FILE EXISTENCE
# -------------------------------

if not os.path.exists(filename):
    print("⚠️ weather.csv not found!")
    print("✅ Creating a sample weather.csv automatically...")

    sample = {
        "Date": ["2025-01-01","2025-01-02","2025-01-03","2025-01-04"],
        "Temperature": [25, 27, 26, 28],
        "Rainfall": [5, 0, 10, 2],
        "Humidity": [70, 65, 80, 75]
    }

    df = pd.DataFrame(sample)
    df.to_csv(filename, index=False)
    print("✅ Sample weather.csv created!")

# -------------------------------
# ✅ STEP 2: CHECK IF FILE EMPTY
# -------------------------------

if os.path.getsize(filename) == 0:
    print("❌ CSV file is EMPTY!")
    print("✅ Add data or delete file and run again to generate sample")
    exit()

# -------------------------------
# ✅ STEP 3: LOAD THE DATA
# -------------------------------

data = pd.read_csv(filename)
print("✅ Data Loaded Successfully!")
print(data.head())

# -------------------------------
# ✅ STEP 4: DATA CLEANING
# -------------------------------

data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
data = data.dropna()
data = data[["Date", "Temperature", "Rainfall", "Humidity"]]

print("✅ Data Cleaned!")

# -------------------------------
# ✅ STEP 5: STATISTICS
# -------------------------------

mean_temp = np.mean(data["Temperature"])
max_temp = np.max(data["Temperature"])
min_temp = np.min(data["Temperature"])
std_temp = np.std(data["Temperature"])

print("\n🌡 Temperature Summary:")
print("Average:", mean_temp)
print("Max:", max_temp)
print("Min:", min_temp)
print("Std Dev:", std_temp)

# -------------------------------
# ✅ STEP 6: VISUALIZATION
# -------------------------------

# Line Chart
plt.figure()
plt.plot(data["Date"], data["Temperature"])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.savefig("temperature_trend.png")
plt.show()

# Bar Chart
monthly_rain = data.groupby(data["Date"].dt.month)["Rainfall"].sum()
plt.figure()
monthly_rain.plot(kind="bar")
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.savefig("monthly_rainfall.png")
plt.show()

# Scatter Plot
plt.figure()
plt.scatter(data["Temperature"], data["Humidity"])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.savefig("humidity_vs_temperature.png")
plt.show()

# -------------------------------
# ✅ STEP 7: GROUPING
# -------------------------------

monthly_stats = data.groupby(data["Date"].dt.month).agg({
    "Temperature": ["mean", "max", "min"],
    "Rainfall": "sum"
})

print("\n📊 Monthly Summary:\n", monthly_stats)

# -------------------------------
# ✅ STEP 8: EXPORT
# -------------------------------

data.to_csv("cleaned_weather.csv", index=False)

with open("summary.txt", "w") as f:
    f.write("Weather Data Summary\n")
    f.write(f"Average Temp: {mean_temp}\n")
    f.write(f"Max Temp: {max_temp}\n")
    f.write(f"Min Temp: {min_temp}\n")

print("\n✅ All Done!")
print("✅ Cleaned CSV Saved")
print("✅ Plots Saved")
print("✅ Summary Created")
