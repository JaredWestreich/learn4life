import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np


def calculate_revenue(base_price, total_students, price_elasticity, mean_students, std_students, threshold,
                      price_change, marketing_boost=0.0):
    # Calculate adjusted enrollment based on price change and random distribution
    enrollment_adjustment = (1 - (price_elasticity * price_change) / 100) * (1 + marketing_boost)
    adjusted_enrollment = total_students * enrollment_adjustment

    if adjusted_enrollment <= 0:
        return 0
    elif base_price <= 0:
        return 0
    else:
        # Generate random distribution of students per class
        num_classes = int(total_students / mean_students)
        adjusted_mean_students = mean_students * enrollment_adjustment
        num_students_per_class = np.random.normal(adjusted_mean_students, std_students, num_classes * 100)

        # Calculate revenue considering class cancellation
        revenue = 0
        for students_in_class in num_students_per_class:
            if students_in_class >= threshold:
                revenue += students_in_class * base_price * ((100 + price_change) / 100)

        return revenue / 100



def plot_graph(price_changes, revenues):
    plt.plot(price_changes, revenues)
    plt.xlabel("Price Change (%)")
    plt.ylabel("Total Revenue ($)")
    plt.title("Price Adjustment for Maximum Revenue")
    plt.grid(True)
    plt.show()

def calculate_and_plot():
    base_price = float(entry_base_price.get())
    total_students = int(entry_total_students.get())
    mean_students = float(entry_mean_students.get())
    std_students = float(entry_std_students.get())
    threshold = int(entry_threshold.get())
    price_elasticity = float(entry_price_sensitivity.get())
    marketing_boost = float(entry_marketing_boost.get())

    price_changes = np.arange(-30, 131, 1)
    revenues = [calculate_revenue(base_price, total_students, price_elasticity, mean_students, std_students, threshold, pc, marketing_boost) for pc in price_changes]

    plot_graph(price_changes, revenues)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Learn4Life Revenue Projection")

    # Add input fields for each parameter
    # Base Hourly Price
    label_base_price = tk.Label(root, text="Average Class Price:")
    label_base_price.pack()
    entry_base_price = tk.Entry(root)
    entry_base_price.pack()

    # Total Students
    label_total_students = tk.Label(root, text="Total Students (Last Year):")
    label_total_students.pack()
    entry_total_students = tk.Entry(root)
    entry_total_students.pack()

    # Percent Decrease
    label_price_elasticity = tk.Label(root, text="Price Elasticity:")
    label_price_elasticity.pack()
    entry_price_sensitivity = tk.Entry(root)
    entry_price_sensitivity.pack()

    # Mean Students per Class
    label_mean_students = tk.Label(root, text="Mean Students per Class (2023-2024):")
    label_mean_students.pack()
    entry_mean_students = tk.Entry(root)
    entry_mean_students.pack()

    # Standard Deviation of Students per Class
    label_std_students = tk.Label(root, text="Standard Deviation of Students per Class:")
    label_std_students.pack()
    entry_std_students = tk.Entry(root)
    entry_std_students.pack()

    # Class Threshold
    label_threshold = tk.Label(root, text="Class Threshold (Minimum Students for Class to Run):")
    label_threshold.pack()
    entry_threshold = tk.Entry(root)
    entry_threshold.pack()

    # Marketing Enrollment Boost
    label_marketing_boost = tk.Label(root, text="Marketing enrollment boost:")
    label_marketing_boost.pack()
    entry_marketing_boost = tk.Entry(root)
    entry_marketing_boost.pack()

    # Calculate and Plot Button
    btn_calculate = tk.Button(root, text="Calculate and Plot", command=calculate_and_plot)
    btn_calculate.pack()

    root.mainloop()