import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def perform_eda(df):
    """
    Performs EDA including descriptive statistics, outlier detection,
    and correlation analysis.

    Parameters:
    df (DataFrame): A DataFrame containing data for EDA.
    """
    statistics = df.describe().style.format()
    outliner = sns.boxplot(data=df, orient='h', log_scale=True, width=.5, fliersize=3)
    plt.title("Boxplot")
    plt.show()
    plt.close()

    matrix = df.corr()
    sns.heatmap(matrix, annot=True, cmap='coolwarm')
    plt.title("Heatmap")
    plt.show()
    plt.close()

    return statistics, outliner, matrix


# Example data
df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50) * 10,
    'C': np.random.rand(50) * 100
})
perform_eda(df)
