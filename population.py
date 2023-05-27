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


def overall_trend(df: dict[str, pd.DataFrame]):
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(30, 20), dpi=40)
    for index, (var, dataframe) in enumerate(df.items()):
        ax = axes.flat[index]
        dataframe.T.plot(ax=ax, linewidth=3)
        ax.legend(loc=(1.04, 0))
        ax.grid(axis="y")
        ax.set_title(f"Population Projection with variation {var}")
        ax.set_xlabel("Years")
        ax.set_ylabel("Population in thousands")
        text_box_display(ax, var)
    axes.flat[5].axis("off")
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    answer_1 = "Question 1: How does the variation in birthrate, life expectancy and\n" \
               "immigration across different German states influence \ntheir respective" \
               "projected population growth?\n\n" \
               "    As the graph shows, except for the most optimistic scenarios, with high\n" \
               "birth rate and immigration rate, most German states will have a negative\n" \
               "population growth in the next five decades"
    axes.flat[5].text(0.1, 0.2, answer_1,
                      # transform=axes.flat[5].transAxes,
                      fontsize=20,
                      # verticalalignment='top',
                      bbox=props,
                      wrap=True)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig("01_overall_trend.png", dpi=80)
    plt.show()


def growth_percentage(df):
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(30, 20), dpi=40)
    for index, (variation, dataframe) in enumerate(df.items()):
        ax = axes.flat[index]
        dataframe["Growth"] = (dataframe["2070"] / dataframe["2022"] * 100).round(2)
        sns.barplot(x=dataframe["Growth"],
                    y=dataframe.index,
                    order=dataframe.sort_values("Growth", ascending=False).index,
                    ax=ax
                    )
        ax.grid(axis="x")
        ax.set_title(f"Projected population growth in the period 2022-2070 with variation {variation}",
                     fontsize=20)
        ax.set_xlabel("Population ratio of the year 2070 / the year 2022 in percentage", fontsize=15)
        ax.set_xticks(range(0, round(max(dataframe["Growth"] + 10)), 10), fontsize=15)
        ax.tick_params(axis='both', which='major', labelsize=15)
        ax.tick_params(axis='both', which='minor', labelsize=8)
        ax.bar_label(ax.containers[0], fmt='%.1f', padding=-35)
        text_box_display(ax, variation)
    axes.flat[5].axis("off")
    answer_2 = "Question 2: Are there specific states that have consistently shown higher growth in\n" \
               "projected population figures?\n\n" \
               "The graph clearly illustrate that Berlin stands alone as the only state projected\n" \
               "to experience positive population growth across all scenarios, ranging from 100-130%.\n" \
               "Hamburg ranks as the second-strongest performer, only projecting negative growth in\n" \
               "the most pessimistic of scenarios.\n\n" \
               "Question 3: Conversely, are there specific states that have shown a consistent decline\n" \
               "or stagnation in their projected population figures?\n\n" \
               "Sachsen-Anhalt exhibits the most concerning performance among the states, with a\n" \
               "projected population contraction of 20 to 30%, regardless of scenarios. Thüringen, while\n" \
               "marginally outperforming Sachsen-Anhalt, is expected to see a decline that is roughly \n" \
               "2-3% less severe.\n\n" \
               "States positioned in the median range, such as Niedersachsen, Rheinland-Pfalz,Schleswig-\n" \
               "Holstein, and Nordrhein-Westfalen, are anticipated to main a relatively stable population,\n" \
               "hovering around 90-110% depending on the scenarios.\n" \
               "These graphs indicate that the range of population change are very different between all\n" \
               "German states."
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    axes.flat[5].text(0, -0.3, answer_2,
                      # transform=axes.flat[5].transAxes,
                      fontsize=20,
                      # verticalalignment='top',
                      bbox=props,
                      wrap=True)
    axes.flat[5].text(0, -0.4,
                      "*A value of 90 means that the population in 2070 is 90% that in 2022,"
                      "in other words a 10% decline in 50 years.",
                      fontsize=15,
                      style='italic')
    fig.tight_layout(rect=[0, 0, 0.97, 0.98])
    plt.show()
    fig.savefig("02_growth_percentage.png", dpi=160)


def text_box_display(axe, var, pos=(0, -0.15)):
    birth_rate = ""
    life_expectancy = ""
    immigration = ""
    if "G1" in var:
        birth_rate = "G1: " + "Birth rate 1.44 children per woman."
    elif "G2" in var:
        birth_rate = "G2: " + "Birth rate 1.55 children per woman."
    elif "G3" in var:
        birth_rate = "G3: " + "Birth rate 1.7 children per woman."
    if "L1" in var:
        life_expectancy = "L1: " + "Life expectancy in 2070: 82.6 for men and 86.1 for women."
    elif "L2" in var:
        life_expectancy = "L2: " + "Life expectancy in 2070: 84.6 for men and 88.2 for women."
    elif "L3" in var:
        life_expectancy = "L3: " + "Life expectancy in 2070: 86.4 for men and 90.1 for women."
    if "W1" in var:
        immigration = "W1: " + " Immigration decreases from 1.1 million in 2022 to 150000 in 2033, constant thereafter."
    elif "W2" in var:
        immigration = "W2: " + "Immigration decreases from 1.3 million in 2022 to 250000 in 2033, constant thereafter."
    elif "W3" in var:
        immigration = "W3: " + "Immigration decreases from 1.5 million in 2022 to 350000 in 2033, constant thereafter."
    text_box = "\n".join([birth_rate, life_expectancy, immigration])
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    axe.text(*pos, text_box, transform=axe.transAxes, fontsize=14,
             verticalalignment='top', bbox=props)


def biggest_smallest(df: dict[str, pd.DataFrame]):
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(30, 20), dpi=40)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    for index, (variation, dataframe) in enumerate(df.items()):
        ax = axes.flat[index]
        dataframe = dataframe.loc[["Nordrhein-Westfalen", "Bremen"], ["2022", "2070"]]
        dataframe.T.plot(ax=ax, linewidth=3, kind="bar")
        ax.legend(loc=(1.04, 0), fontsize=16)
        ax.set_title(f"Comparison of population between Nordrhein-Westfalen and Bremen {variation}", fontsize=20)
        ax.set_xlabel("Years", fontsize=15)
        ax.set_ylabel("Population in thousands", fontsize=15)
        ax.tick_params(axis='both', which='major', labelsize=15)
        ax.tick_params(axis='both', which='minor', labelsize=15)
        ax.bar_label(ax.containers[0], fmt='%.1f', padding=0)
        ax.bar_label(ax.containers[1], fmt='%.1f', padding=0)
        nw_growth = dataframe.loc["Nordrhein-Westfalen", "2070"] / dataframe.loc["Nordrhein-Westfalen", "2022"]
        br_growth = dataframe.loc["Bremen", "2070"] / dataframe.loc["Bremen", "2022"]
        text = f"Growth:\n" \
               f"Nordrhein-Westfalen : {round(100 * nw_growth - 100, 2)} %\n" \
               f"Bremen: {round(100 * br_growth - 100, 2)} %"
        ax.text(1.05, 0.35, text, transform=ax.transAxes, fontsize=14,
                verticalalignment='top', bbox=props)
    answer_4 = "Question 4: How will the dynamic between the most and least populous states\n" \
               "change over the next five decades?\n\n" \
               "In a comprehensive overview, Nordrhein-Westfalen seems to face a more adverse\n" \
               "impact on its population compared to Bremen. Under pessimistic scenarios,\n" \
               "the population decline in Nordrhein-Westfalen substantially surpasses that\n" \
               "of Bremen, exhibiting a contraction range of 12.39 to 13.73%, whereas Bremen's\n" \
               "population reduction is relatively contained within a span of 6.42 to 7.58%.\n\n" \
               "Contrastingly, under optimistic circumstances, Bremen exhibits a swifter pace\n" \
               "of population growth than Nordrhein-Westfalen. While the growth rate in Nordrhein-\n" \
               "Westfalen hovers between a modest 2.41 to 3.84%, Bremen outperforms significantly,\n" \
               "with a robust growth estimate ranging from 15.89 to 17.32%.\n\n" \
               "A noteworthy deviation is observed in the G2L2W2 scenario, wherein Nordrhein-\n" \
               "Westfalen's population undergoes a contraction of 4.51%, while, intriguingly,\n" \
               "Bremen's population escalates by 5.44%. This highlights the stark contrast in\n" \
               "population dynamics between the two states under the same conditions."
    axes.flat[5].axis("off")
    axes.flat[5].text(0, -0.1, answer_4,
                      # transform=axes.flat[5].transAxes,
                      fontsize=18,
                      # verticalalignment='top',
                      bbox=props,
                      wrap=True)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
    fig.savefig("03_biggest_smallest.png", dpi=160)


def east_west(df: dict[str, pd.DataFrame]):
    east = ["Brandenburg", "Mecklenburg-Vorpommen", "Sachsen", "Sachsen-Anhalt", "Thüringen"]
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(30, 20), dpi=40)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    for index, (variation, dataframe) in enumerate(df.items()):
        ax = axes.flat[index]
        dataframe2 = dataframe.drop(["Berlin"])
        dataframe2["East/West"] = ["East" if index in east else "West" for index in dataframe2.index]
        dataframe2 = dataframe2.loc[:, ["2022", "2070", "East/West"]]
        dataframe2["Growth"] = (dataframe2["2070"] / dataframe2["2022"] * 100).round(2)
        sns.barplot(x=dataframe2["Growth"],
                    y=dataframe2.index,
                    order=dataframe2.sort_values("Growth", ascending=False).index,
                    ax=ax,
                    hue=dataframe2["East/West"],
                    palette="deep",
                    dodge=False,
                    )
        ax.set_title(f"Projected population growth in the period 2022-2070 with variation {variation}", fontsize=25)
        ax.set_xlabel("Population ratio of the year 2070 / the year 2022 in percentage", fontsize=15)
        ax.set_xticks(range(0, round(max(dataframe2["Growth"] + 10)), 10), fontsize=15)
        ax.tick_params(axis='both', which='major', labelsize=15)
        ax.tick_params(axis='both', which='minor', labelsize=8)
        ax.bar_label(ax.containers[0], fmt='%.1f', padding=-35)
        ax.bar_label(ax.containers[1], fmt='%.1f', padding=-35)
        ax.grid(axis="x")
        text_box_display(ax, variation)
    answer_5 = "Question 5: How do the population projections of the former East and West Germany\n" \
               "compare over the next five decades?\n\n" \
               "In a notable pattern, the states that previously constituted East Germany, Brandenburg\n" \
               "Sachsen, Sachsen-Anhalt and Thüringen, all underperform in comparison to their West\n" \
               "Germany counterparts. These states are projected to experience no population growth\n" \
               "over the forthcoming five decades, even under the most favourable scenarios.\n\n" \
               "A majority of the former West Germany states illustrate markedly superior performance\n" \
               "relative to those from East Germany. Exceptions to this are Saarland and Mecklenburg-\n" \
               "Vorpommen, albeit their projected growth still surpasses that of Thüringen and Sachsen-\n" \
               "Anhalt.\n\n" \
               "Berlin is excluded from this analysis owing to its historical partition between East and\n" \
               "West Germany."
    axes.flat[5].axis("off")
    axes.flat[5].text(0, -0.1, answer_5,
                      # transform=axes.flat[5].transAxes,
                      fontsize=18,
                      # verticalalignment='top',
                      bbox=props,
                      wrap=True)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
    fig.savefig(f"05_east_west.png", dpi=160)


def urban_vs_rural(df):
    urban = ["Berlin", "Hamburg", "Bayern", "Nordrhein-Westfalen", "Hesse"
             "Baden-Württemburg", "Sachsen", "Bremen", "Niedersachsen"]
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(30, 20), dpi=40)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    for index, (variation, dataframe) in enumerate(df.items()):
        ax = axes.flat[index]
        dataframe["Urban/Rural"] = ["Urban" if index in urban else "Rural" for index in dataframe.index]
        dataframe = dataframe.loc[:, ["2022", "2070", "Urban/Rural"]]
        dataframe["Growth"] = (dataframe["2070"] / dataframe["2022"] * 100).round(2)
        sns.barplot(x=dataframe["Growth"],
                    y=dataframe.index,
                    order=dataframe.sort_values("Growth", ascending=False).index,
                    ax=ax,
                    hue=dataframe["Urban/Rural"],
                    hue_order=["Urban", "Rural"],
                    palette="deep",
                    dodge=False,
                    )
        ax.set_title(f"Projected population growth in the period 2022-2070 with variation {variation}", fontsize=25)
        ax.set_xlabel("Population ratio of the year 2070 / the year 2022 in percentage", fontsize=15)
        ax.set_xticks(range(0, round(max(dataframe["Growth"] + 10)), 10), fontsize=15)
        ax.tick_params(axis='both', which='major', labelsize=15)
        ax.tick_params(axis='both', which='minor', labelsize=8)
        ax.bar_label(ax.containers[0], fmt='%.1f', padding=-35)
        ax.bar_label(ax.containers[1], fmt='%.1f', padding=-35)
        ax.grid(axis="x")
        text_box_display(ax, variation)
    answer_6 = "Question 6: Do states with larger cities have different population projection compared\n" \
               "more rural states?\n\n" \
               "In a notable pattern, the states that previously constituted East Germany, Brandenburg\n" \
               "Sachsen, Sachsen-Anhalt and Thüringen, all underperform in comparison to their West\n" \
               "Germany counterparts. These states are projected to experience no population growth\n" \
               "over the forthcoming five decades, even under the most favourable scenarios.\n\n" \
               "A majority of the former West Germany states illustrate markedly superior performance\n" \
               "relative to those from East Germany. Exceptions to this are Saarland and Mecklenburg-\n" \
               "Vorpommen, albeit their projected growth still surpasses that of Thüringen and Sachsen-\n" \
               "Anhalt.\n\n" \
               "Berlin is excluded from this analysis owing to its historical partition between East and\n" \
               "West Germany."
    axes.flat[5].axis("off")
    axes.flat[5].text(0, -0.1, answer_6,
                      # transform=axes.flat[5].transAxes,
                      fontsize=18,
                      # verticalalignment='top',
                      bbox=props,
                      wrap=True)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
    fig.savefig(f"06_urban_rural.png", dpi=160)

if __name__ == '__main__':
    data_path = r"data\12421-0003.xlsx"
    projections = data_loader(data_path)
    variations = "G2L2W1"
    sns.set_style("dark")
    # overall_trend(projections)
    growth_percentage(projections)
    # biggest_smallest(projections)
    # east_west(projections)
    # urban_vs_rural(projections)
