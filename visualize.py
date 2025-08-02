from analyze_sales import region_sales
import matplotlib.pyplot as plt

plt.bar(region_sales["Region"], region_sales["TotalSales"], color='orange')
plt.title("Real-Time Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.show()
