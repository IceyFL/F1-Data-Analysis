import matplotlib.pyplot as plt
import numpy as np

def create_graph(drivers, driver_laps):
    # Compute minimum lap time for each driver
    mins = [np.min(laps) for laps in driver_laps]

    # Sort by minimum lap time (fastest first)
    sorted_indices = np.argsort(mins)
    drivers = [drivers[i] for i in sorted_indices]
    driver_laps = [driver_laps[i] for i in sorted_indices]

    plt.figure(figsize=(14, 6))

    # Create the boxplot with whiskers at min/max
    bp = plt.boxplot(driver_laps, patch_artist=True, whis=[0, 100])

    # Add distinct colors for each box
    colors = plt.cm.tab20(np.linspace(0, 1, len(driver_laps)))
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # Label x-axis with driver numbers
    plt.xticks(
        ticks=range(1, len(drivers) + 1),
        labels=[str(d) for d in drivers],
        rotation=45,
        ha='right'
    )

    plt.ylabel("Lap Time (seconds)")
    plt.xlabel("Driver Number")
    plt.title("Lap Time Distribution by Driver (Sorted by Fastest Lap)")

    plt.tight_layout()
    plt.show()
