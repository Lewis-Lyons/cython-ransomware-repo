# libraries
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.25

# set height of bar
encrypt_means = [0.1, 0.1, 0.3, 2.8, 22.6, 58.4, 45.7 ,49.0]
read_means = [0.3, 0.2, 0.2, 0.4, 2.0, 5.9, 36.3, 33.4,]
write_means = [0.0, 0.0, 2.9, 3.6, 5.8, 11.3, 14.2, 15.0]
cumulative_means = [0.4, 0.3, 3.4, 6.8, 30.4, 78.1, 96.2, 97.4]

# Set position of bar on X axis
r1 = np.arange(len(encrypt_means))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
#r4 = [x + barWidth for x in r3]

# Make the plot
fig, ax = plt.subplots()
rects1 = plt.bar(r1, encrypt_means, color='#7f6d5f', width=barWidth, edgecolor='white', label="{method 'encrypt' of '_AES' objects}")
rects2 = plt.bar(r2, read_means, color='#557f2d', width=barWidth, edgecolor='white', label="{method 'read' of '_io.BufferedReader' objects}")
rects3 = plt.bar(r3, write_means, color='#2d7f5e', width=barWidth, edgecolor='white', label="{method 'write' of '_io.BufferedWriter' objects}")
#plt.bar(r4, cumulative_means, color='#ff0000', width=barWidth, edgecolor='white', label="{cumulative time for above 3 functions}")

rects1
rects2
rects3

# Add xticks on the middle of the group bars
ax.set_title('Effect Of CryPy Encryption On Runtime Speed VS File Size For Key Profiled Functions')
plt.xlabel('File Size Encrypted In Bytes', fontweight='bold')
plt.ylabel('Percentage of Total Runtime', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(encrypt_means))], ['1*10^4', '1*10^5', '1*10^6', '1*10^7', '1*10^8', '1*10^9', '1*10^10', '1*10^11'])



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
autolabel(rects2)
autolabel(rects3)

fig.tight_layout()


# Create legend & Show graphic
plt.legend()
plt.show()
