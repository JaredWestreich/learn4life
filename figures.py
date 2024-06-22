from matplotlib import pyplot as plt
from L4L_gui import calculate_revenue
import numpy as np

price_changes = np.arange(-30, 131, 1)

# # figure 1 - Finding the optimal fee increase with and without considering class size thresholds.
# base_price = 250
# total_students = 7800 / 0.7
# price_elasticity = 0.5
# mean_students = 17
# std_students = 7
# threshold = 15
#
# revenues_threshold_15 = [calculate_revenue(base_price, total_students, price_elasticity, mean_students, std_students, threshold, pc)
#             for pc in price_changes]
#
# plt.figure(1)
# plt.plot(price_changes, revenues_threshold_15, label="15 Students Threshold")
#
# threshold = 0
# revenues_threshold_0 = [calculate_revenue(base_price, total_students, price_elasticity, mean_students, std_students, threshold, pc)
#             for pc in price_changes]
#
# plt.plot(price_changes, revenues_threshold_0, label="No Threshold")
# plt.xlabel("Price Change (%)")
# plt.ylabel("Total Revenue ($)")
# plt.title("Optimizing Revenue with and without Class Size Thresholds")
# plt.grid(True)
# plt.legend()
# plt.ticklabel_format(style='plain', axis='y')
# plt.show()


# figure 2 - revenue projections at various price elasticities
plt.figure(2)

base_price = 250
total_students = 7800 / 0.7
mean_students = 17
std_students = 7
threshold = 15

price_elasticities = [0.5, 0.75, 1.0]
for pe in price_elasticities:
    revenues = [calculate_revenue(base_price, total_students, pe, mean_students, std_students, threshold, pc)
                for pc in price_changes]
    plt.plot(price_changes, revenues, label=f"Price Elasticity = {pe}")

plt.xlabel("Price Change (%)")
plt.ylabel("Total Revenue ($)")
# plt.title("Optimizing Revenue with and without Class Size Thresholds")
plt.title("Revenue Projections at Various Price Elasticities")
plt.grid(True)
plt.legend()
plt.ticklabel_format(style='plain', axis='y')
plt.show()