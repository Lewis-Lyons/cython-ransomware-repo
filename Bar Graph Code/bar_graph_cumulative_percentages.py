# libraries
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.25

# set height of bar
cumulative_means = [0.4, 0.3, 3.4, 6.8, 30.4, 78.1, 96.2, 97.4]

# Set position of bar on X axis
r1 = np.arange(len(cumulative_means))

# Make the plot
fig, ax = plt.subplots()
rects1 = plt.bar(r1, cumulative_means, color='#ff0000', width=barWidth, edgecolor='white', label="{cumulative runtime for key profiled functions}")

rects1

# Add xticks on the middle of the group bars
ax.set_title('Cumulative Effect Of CryPy Encryption On Runtime Speed VS File Size For Key Profiled Functions')
plt.xlabel('File Size Encrypted In Bytes', fontweight='bold')
plt.ylabel('Percentage of Total Runtime', fontweight='bold')
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
