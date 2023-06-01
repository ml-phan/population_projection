#!/usr/bin/python3

import argparse
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import seaborn as sns
from utils import *

OUTPUT_PATH = Path.cwd().parent / "results"


def overall_trend(df: dict[str, pd.DataFrame]):
    """
    Plot the population growth of all 16 German states in all variations.
    Each plot for one variation.
    Save the graph in to a png file.
    :param df: data frame containing the dataset
    :return: None
    """
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
    answer_1 = "Question 1: How does the variation in birthrate, life " \
               "expectancy and\nimmigration across different German states " \
               "influence\ntheir respective projected population growth?\n\n" \
               "As the graph shows, except for the most optimistic " \
               "scenarios, with high\nbirth rate and immigration rate, most " \
               "German states will have a negative\npopulation growth in " \
               "the next five decades"
    display_answer(axes.flat[5], answer_1)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig(OUTPUT_PATH / "01_overall_trend.png", dpi=160)
    plt.show()


def growth_percentage(df):
    """
    Plot bar charts comparing the population of each state in the year 2070
    compared to 2022.
    Save the graph in to a png file.
    :param df: data frame containing the dataset
    :return: None
    """
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(30, 20), dpi=40)
    for index, (variation, dataframe) in enumerate(df.items()):
        ax = axes.flat[index]
        dataframe2 = dataframe.copy()
        dataframe2["Growth"] = (
                dataframe2["2070"] / dataframe2["2022"] * 100).round(2)
        sns.barplot(x=dataframe2["Growth"],
                    y=dataframe2.index,
                    order=dataframe2.sort_values("Growth",
                                                 ascending=False).index,
                    ax=ax
                    )
        ax.grid(axis="x")
        graph_annotation(ax, variation, dataframe2)
        text_box_display(ax, variation)
    answer_2 = "Question 2: Are there specific states that have consistently" \
               " shown higher growth in projected population\nfigures?\n\n" \
               "The graphs clearly illustrate that Berlin stands alone as " \
               "the only state projected to experience positive \npopulation" \
               " growth across all scenarios, ranging from 100-130%. Hamburg" \
               " ranks as the second-strongest\nperformer, only " \
               "projecting negative growth in " \
               "the most pessimistic of scenarios.\n\n" \
               "Question 3: Conversely, are there specific states that have" \
               " shown a consistent decline or stagnation in\n" \
               "their projected population figures?\n\n" \
               "Sachsen-Anhalt exhibits the most concerning performance " \
               "among the states, with a projected population \n" \
               "contraction of 20 to 30%, regardless of scenarios. " \
               "Thüringen, while marginally outperforming " \
               "Sachsen\n-Anhalt, is expected to see " \
               "a decline that is roughly 2-3% less severe.\n\n" \
               "States positioned in the median range, such as " \
               "Niedersachsen, Rheinland-Pfalz,Schleswig-Holstein, and\n" \
               "Nordrhein-Westfalen, are anticipated to maintain a " \
               "relatively stable population, hovering around 90-\n110% " \
               "depending on the scenarios.\n" \
               "These graphs indicate that the range of population changes " \
               "are very different between all German states."
    display_answer(axes.flat[5], answer_2, 18)
    display_footnote(axes.flat[5])
    fig.tight_layout(rect=[0, 0.01, 0.97, 0.98])
    fig.savefig(OUTPUT_PATH / "02_growth_percentage.png", dpi=160)
    plt.show()


def biggest_smallest(df: dict[str, pd.DataFrame]):
    """
    Plot the growth projection differences between the most and the least
    populous state.
    Save the graph in to a png file.
    :param df:data frame containing the dataset
    :return: None
    """
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(30, 20), dpi=40)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    for index, (variation, dataframe) in enumerate(df.items()):
        ax = axes.flat[index]
        dataframe2 = dataframe.loc[
            ["Nordrhein-Westfalen", "Bremen"], ["2022", "2070"]]
        dataframe2.T.plot(ax=ax, linewidth=3, kind="bar")
        ax.legend(loc=(1.04, 0), fontsize=16)
        ax.set_title(f"Comparison of population between Nordrhein-Westfalen "
                     f"and Bremen {variation}",
                     fontsize=20)
        ax.set_xlabel("Years", fontsize=15)
        ax.set_ylabel("Population in thousands", fontsize=15)
        ax.tick_params(axis='both', which='major', labelsize=15)
        ax.tick_params(axis='both', which='minor', labelsize=15)
        ax.bar_label(ax.containers[0], fmt='%.1f', padding=0)
        ax.bar_label(ax.containers[1], fmt='%.1f', padding=0)
        nw_growth = dataframe2.loc["Nordrhein-Westfalen", "2070"] / \
                    dataframe2.loc["Nordrhein-Westfalen", "2022"]
        br_growth = dataframe2.loc["Bremen", "2070"] / dataframe2.loc[

            "Bremen", "2022"]
        text = f"Growth:\n" \
               f"Nordrhein-Westfalen : {round(100 * nw_growth - 100, 2)} %\n" \
               f"Bremen: {round(100 * br_growth - 100, 2)} %"
        ax.text(1.05, 0.35, text, transform=ax.transAxes, fontsize=14,
                verticalalignment='top', bbox=props)
    answer_4 = "Question 4: How will the dynamic between the most and least " \
               "populous states\nchange over the next five decades?\n\n" \
               "After a detail investigation, Nordrhein-Westfalen seems to " \
               "face a more adverse\nimpact on its population compared to " \
               "Bremen. Under pessimistic scenarios,\nthe population " \
               "decline in Nordrhein-Westfalen substantially surpasses \n" \
               "that of Bremen, exhibiting a contraction range of 12.39 to " \
               "13.73%, whereas Bremen's\npopulation reduction is " \
               "relatively contained within a span of 6.42 to 7.58%.\n\n" \
               "Contrastingly, under optimistic circumstances, Bremen " \
               "exhibits a swifter pace\nof population growth than " \
               "Nordrhein-Westfalen. While the growth rate in Nordrhein-\n" \
               "Westfalen hovers between a modest 2.41 to 3.84%, Bremen " \
               "outperforms significantly,\nwith a robust growth estimate " \
               "ranging from 15.89 to 17.32%.\n\nA noteworthy deviation is " \
               "observed in the G2L2W2 scenario, wherein Nordrhein-\n" \
               "Westfalen's population undergoes a contraction of 4.51%, " \
               "while, intriguingly,\nBremen's population escalates by " \
               "5.44%. This highlights the stark contrast in\npopulation " \
               "dynamics between the two states under the same conditions."
    display_answer(axes.flat[5], answer_4)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig(OUTPUT_PATH / "03_biggest_smallest.png", dpi=160)
    plt.show()


def east_west(df: dict[str, pd.DataFrame]):
    """
    Plot bar charts with states grouped into former East and West Germany
    states.
    Save the graph in to a png file.
    :param df:data frame containing the dataset
    :return: None
    """
    east = ["Brandenburg", "Mecklenburg-Vorpommen", "Sachsen",
            "Sachsen-Anhalt", "Thüringen"]
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(30, 20), dpi=40)
    for index, (variation, dataframe) in enumerate(df.items()):
        ax = axes.flat[index]
        dataframe2 = dataframe.drop(["Berlin"])
        dataframe2["East/West"] = ["East" if index in east else "West" for
                                   index in dataframe2.index]
        dataframe2 = dataframe2.loc[:, ["2022", "2070", "East/West"]]
        dataframe2["Growth"] = (
                dataframe2["2070"] / dataframe2["2022"] * 100).round(2)
        sns.barplot(x=dataframe2["Growth"],
                    y=dataframe2.index,
                    order=dataframe2.sort_values("Growth",
                                                 ascending=False).index,
                    ax=ax,
                    hue=dataframe2["East/West"],
                    palette="deep",
                    dodge=False,
                    )
        graph_annotation(ax, variation, dataframe2)
        ax.bar_label(ax.containers[1], fmt='%.1f', padding=-35, fontsize=14)
        ax.grid(axis="x")
        ax.legend(fontsize=16)
        text_box_display(ax, variation)
    answer_5 = "Question 5: How do the population projections of the former " \
               "East and West Germany\ncompare over the next five decades?" \
               "\n\nIn a notable pattern, the states that previously " \
               "constituted East Germany, Brandenburg\nSachsen, Sachsen-" \
               "Anhalt and Thüringen, all underperform in comparison to " \
               "their West\nGermany counterparts. These states are " \
               "projected to experience no population growth\nover the " \
               "forthcoming five decades, even under the most favourable " \
               "scenarios.\n\nA majority of the former West Germany states " \
               "illustrate markedly superior performance\nrelative to those " \
               "from East Germany. Exceptions to this are Saarland and " \
               "Mecklenburg-\nVorpommen, albeit their projected growth " \
               "still surpasses that of Thüringen and Sachsen-\nAnhalt.\n\n" \
               "Berlin is excluded from this analysis owing to its " \
               "historical partition between East and\n" \
               "West Germany."
    display_answer(axes.flat[5], answer_5)
    display_footnote(axes.flat[5])
    fig.tight_layout(rect=[0, 0.01, 0.97, 0.98])
    fig.savefig(OUTPUT_PATH / "05_east_west.png", dpi=160)
    plt.show()


def urban_vs_rural(df):
    """
    Plot bar charts with states grouped into either "Urban" or "Rural" states.
    States with cities with a population bigger than 500,000 is considered
    "Urban".
    Save the graph in to a png file.
    :param df:data frame containing the dataset
    :return: None
    """
    urban = ["Berlin", "Hamburg", "Bayern", "Nordrhein-Westfalen", "Hessen",
             "Baden-Württemberg", "Sachsen", "Bremen", "Niedersachsen"]
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(30, 20), dpi=40)
    for index, (variation, dataframe) in enumerate(df.items()):
        ax = axes.flat[index]
        dataframe2 = dataframe.copy()
        dataframe2["Urban/Rural"] = ["Urban" if index in urban else "Rural" for
                                     index in dataframe2.index]
        dataframe2 = dataframe2.loc[:, ["2022", "2070", "Urban/Rural"]]
        dataframe2["Growth"] = (
                dataframe2["2070"] / dataframe2["2022"] * 100).round(2)
        sns.barplot(x=dataframe2["Growth"],
                    y=dataframe2.index,
                    order=dataframe2.sort_values("Growth",
                                                ascending=False).index,
                    ax=ax,
                    hue=dataframe2["Urban/Rural"],
                    hue_order=["Urban", "Rural"],
                    palette="deep",
                    dodge=False,
                    )
        graph_annotation(ax, variation, dataframe2)
        ax.grid(axis="x")
        ax.bar_label(ax.containers[1], fmt='%.1f', padding=-35, fontsize=14)
        ax.legend(fontsize=16)
        text_box_display(ax, variation)
    answer_6 = "Question 6: Do states with larger cities have different " \
               "population projection compared\nmore rural states?\n\n" \
               "Using a population threshold of 500,000, we have " \
               "categorized the states into two\nclassifications: 'Urban' " \
               "and 'Rural'. 'Urban' states are characterized by having at\n" \
               "least one city with a population exceeding 500,000, while " \
               "'Rural' states do not have\nsuch large urban centers.\n\n" \
               "Our graphs reveals a trend favoring 'Urban' states, showing " \
               "their potential advantages\n in term of population growth " \
               "when contrasted with 'Rural' states.\n\nThe bottom four " \
               "states have no city with a population larger than 250,000, " \
               "while the top\nseven are all states that have at least " \
               "one city with a population larger than 500,000."
    display_answer(axes.flat[5], answer_6)
    display_footnote(axes.flat[5])
    fig.tight_layout(rect=[0, 0.01, 0.97, 0.98])
    fig.savefig(OUTPUT_PATH / "06_urban_rural.png", dpi=160)
    plt.show()


def main():

    # Set style for all seaborn charts
    sns.set_style("dark")

    # Add ArgumentParser
    parser = argparse.ArgumentParser(
        "Research on German states' population growth")
    parser.add_argument("FILE", type=str,
                        help="Path to dataset file")
    parser.add_argument("--question", "--q", dest="question", type=int,
                        required=True,
                        choices=[1, 2, 3, 4, 5, 6],
                        help="Enter the question number to display the result")


    # If there is no argument given when the script is run,
    # display the parser's help message
    if len(sys.argv) < 4:
        parser.print_help()
        sys.exit()

    args = parser.parse_args()

    projections = None
    if args.FILE:
        # Load data using data_loader function
        try:
            projections = data_loader(args.FILE)
        except ValueError:
            print("The input file seems to be in the wrong format.")
            sys.exit()
        # Run appropriate function depends on the selected question
        # Else print the parser's help message when input is not in
        # range of [1,2,3,4,5,6]
        if args.question == 1:
            overall_trend(projections)
        elif args.question in [2, 3]:
            growth_percentage(projections)
        elif args.question == 4:
            biggest_smallest(projections)
        elif args.question == 5:
            east_west(projections)
        elif args.question == 6:
            urban_vs_rural(projections)
        else:
            parser.print_help()


if __name__ == '__main__':
    main()
