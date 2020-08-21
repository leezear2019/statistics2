x = [1, 2, 3, 5, 10, 100, 1000]
y1 = [1, 0.822, 0.763, 0.715, 0.680, 0.648, 0.645]
y2 = [1, 0.859, 0.812, 0.774, 0.746, 0.721, 0.718]

import matplotlib.pyplot as plt
from matplotlib.transforms import BlendedGenericTransform

# mode 01 from one case
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
line1, = ax1.plot(x, y1, label='mode 01')
# mode 01 from other case
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
line2, = ax2.plot(x, y2, label='mode 01')

# Create new figure and two subplots, sharing both axes
fig3, (ax3, ax4) = plt.subplots(1, 2, sharey=True, sharex=True, figsize=(10, 5))

# Plot data from fig1 and fig2
line3, = ax3.plot(line1.get_data()[0], line1.get_data()[1])
line4, = ax4.plot(line2.get_data()[0], line2.get_data()[1])
# If possible (easy access to plotting data) use
# ax3.plot(x, y1)
# ax4.lpot(x, y2)

ax3.set_ylabel('y-axis')
ax3.grid(True)
ax4.grid(True)

# Add legend
fig3.legend((line3, line4),
            ('label 3', 'label 4'),
            loc='upper center',
            bbox_to_anchor=[0.5, -0.05],
            bbox_transform=BlendedGenericTransform(fig3.transFigure, ax3.transAxes))
# Make space for the legend beneath the subplots
plt.subplots_adjust(bottom=0.2)
# Show only fig3
fig3.show()
