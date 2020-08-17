# libraries
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.25

# set height of bar
runtime_means_100 = [1.8518, 1.9868, 1.9754, 2.1284, 2.8798, 12.0734, 138.0020, 1286.2614]

# Set position of bar on X axis
r1 = np.arange(len(runtime_means_100))

# Make the plot
fig, ax = plt.subplots()
rects1 = plt.bar(r1, runtime_means_100, color='#38EC4F', width=barWidth, edgecolor='white', label="total program runtime")

rects1

# Add xticks on the middle of the group bars
ax.set_title('Average Runtime Of Ransomware Sample VS File Size (For 100 Files)')
plt.xlabel('Total Data Encrypted (bytes)', fontweight='bold')
plt.ylabel('Average Runtime (seconds)', fontweight='bold')
plt.yscale('log')
plt.xticks(r1, ['1*10^4', '1*10^5', '1*10^6', '1*10^7', '1*10^8', '1*10^9', '1*10^10', '1*10^11'])



def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)

fig.tight_layout()


# Create legend & Show graphic
plt.legend()
plt.show()
