import matplotlib.pyplot as plt
import numpy as np
import collections


def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.
    """
    counts = collections.Counter(data)

    fig = plt.figure()
    plt.bar(range(len(counts)), list(counts.values()), tick_label=list(counts.keys()))
    plt.xlabel('Category')
    plt.ylabel('Frequency')
    plt.title('Counts of classes')
    plt.close()
    return fig


# Example data
data = np.random.choice(['A', 'B', 'C'], size=100)
plot_distribution(data)
