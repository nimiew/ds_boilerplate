from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
colors = ['#008fd5', 'red', 'yellow', 'green', 'orange']
explode = [0, 0, 0, 0.1, 0] # python slice will be more pronounced

plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})
# shadow=True, startangle=90, autopct='%1.1f%%'

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f