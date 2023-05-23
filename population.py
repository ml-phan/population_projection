import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def data_loader(path):
    """
    :param path: relative path to data file.
    :return: a dictionary of dataframe, each dataframe contains one variation of the population projection.
    """
    df = pd.read_excel("data/12421-0003.xlsx")
    df = df.rename(columns={df.columns[0]: "States"})
    df.columns = [col[:4] if "States" not in col else "States" for col in df.columns]

    df_list = {}
    for index, value in enumerate(df["States"]):
        if "BEV" in value:
            df_list[value[-7:-1]] = df[index + 1:index + 17]
            df_list[value[-7:-1]].set_index("States", inplace=True)

    return df_list


def overview_plot(df, var):
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 6))
    for index, dataframe in enumerate(df.values()):
        axe = axes[index]
        dataframe.T.plot(ax=axe, linewidth=3)
        plt.legend(loc=(1.04, 0))
        plt.grid()
        plt.title(f"Population Projection with variation {var}")
        plt.xlabel("Years")
        plt.ylabel("Population in thousands")
        text_box_display(axes[index], var)
        plt.tight_layout()
        plt.show()


def growth_percentage(df, var):
    sns.set(style="ticks")
    sns.set_style("darkgrid")
    fig, axe = plt.subplots(figsize=(12, 6))
    df["Growth"] = (df["2070"] / df["2022"] * 100).round(2)
    growth = sns.barplot(x=df["Growth"], y=df.index,
                         order=df.sort_values("Growth", ascending=False).index,
                         )
    growth.set_title("Projected population growth in the period 2022-2070")
    growth.set_xlabel("Growth in percentage")
    growth.set_xticks(range(0, 120, 10))
    growth.bar_label(growth.containers[0], fmt='%.1f', padding=-35)
    text_box_display(growth, var)
    plt.tight_layout()
    plt.show()


def text_box_display(axe, var):
    birth_rate = ""
    life_expectancy = ""
    immigration = ""
    if "G1" in var:
        birth_rate = "Birth rate 1.44 children per woman"
    elif "G2" in var:
        birth_rate = "Birth rate 1.55 children per woman"
    elif "G3" in var:
        birth_rate = "Birth rate 1.7 children per woman"
    if "L1" in var:
        life_expectancy = "Life expectancy in 2070: 82.6 for men and 86.1 for women"
    elif "L2" in var:
        life_expectancy = "Life expectancy in 2070: 84.6 for men and 88.2 for women"
    elif "L3" in var:
        life_expectancy = "Life expectancy in 2070: 86.4 for men and 90.1 for women"
    if "W1" in var:
        immigration = "Decrease from 1.1 million in 2022 to 150000 in 2033, constant thereafter"
    elif "W2" in var:
        immigration = "Decrease from 1.3 million in 2022 to 250000 in 2033, constant thereafter"
    elif "W3" in var:
        immigration = "Decrease from 1.5 million in 2022 to 350000 in 2033, constant thereafter"
    text_box = "\n".join([birth_rate, life_expectancy, immigration])
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    axe.text(0, -0.2, text_box, transform=axe.transAxes, fontsize=14,
             verticalalignment='top', bbox=props)


if __name__ == '__main__':
    data_path = r"data\12421-0003.xlsx"
    projections = data_loader(data_path)
    variation = "G2L2W1"
    test_df = projections[variation]
    overview_plot(projections, variation)
    # growth_percentage(test_df, variation)
    # print(test_df)
