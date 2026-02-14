import matplotlib.pyplot as plt

categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
monthly_sales = [200, 250, 300, 350, 400]

plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.subplot(1, 2, 2)
plt.plot(months, monthly_sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")


plt.tight_layout()


plt.show()
