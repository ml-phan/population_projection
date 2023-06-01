def text_box_display(axe, var, pos=(0, -0.15)):
    """
    Display variation legend on each chart of a subplot
    :param axe: the ax of the subplot
    :param var: the specific projected variation displayed in the chart
    :param pos: position of the text box. Default (0, -0.15)
    :return: None
    """
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
        life_expectancy = "L1: " + "Life expectancy in 2070: 82.6 for men " \
                                   "and 86.1 for women."
    elif "L2" in var:
        life_expectancy = "L2: " + "Life expectancy in 2070: 84.6 for men " \
                                   "and 88.2 for women."
    elif "L3" in var:
        life_expectancy = "L3: " + "Life expectancy in 2070: 86.4 for men " \
                                   "and 90.1 for women."
    if "W1" in var:
        immigration = "W1: " + " Immigration decreases from 1.1 million in " \
                               "2022 to 150000 in 2033, constant thereafter."
    elif "W2" in var:
        immigration = "W2: " + "Immigration decreases from 1.3 million in " \
                               "2022 to 250000 in 2033, constant thereafter."
    elif "W3" in var:
        immigration = "W3: " + "Immigration decreases from 1.5 million in " \
                               "2022 to 350000 in 2033, constant thereafter."
    text_box = "\n".join([birth_rate, life_expectancy, immigration])
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    axe.text(*pos, text_box, transform=axe.transAxes, fontsize=14,
             verticalalignment='top', bbox=props)


def display_answer(ax, text, fontsize=18):
    """
    Display text box with answer to the research question.
    :param ax: The ax on which to display the text box containing the answer.
    :param text: The answer to the research question to be displayed.
    :param fontsize: Font size of the answer. Default: 18.
    Smaller is recommended for longer answer.
    :return: None
    """
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.axis("off")
    ax.text(0, -0.1, text,
            fontsize=fontsize,
            bbox=props,
            wrap=True)


def display_footnote(ax):
    """
    Display footnote, explaining the percentage of the charts.
    :param ax: The ax on which the footnote will be displayed.
    :return: None
    """
    ax.text(0, -0.4,
            "*A value of 90 means that the population in 2070 is "
            "90% that in 2022, in other words a 10% decline in 50 years.",
            fontsize=15,
            style='italic')


def graph_annotation(ax, variation, dataframe):
    """
    Customized the annotation of the bar charts
    :param ax: The ax of the chart
    :param variation: The specific projected variation displayed in the chart
    :param dataframe: The DataFrame containing data
    :return: None
    """
    ax.set_title(f"Projected population growth in the period 2022-2070 "
                 f"with variation {variation}",
                 fontsize=25)
    ax.set_xlabel("Population ratio of the year 2070 / the year 2022 "
                  "in percentage",
                  fontsize=15)
    ax.set_xticks(range(0, round(max(dataframe["Growth"] + 10)), 10))
    ax.tick_params(axis='both', which='major', labelsize=15)
    ax.tick_params(axis='both', which='minor', labelsize=8)
    ax.bar_label(ax.containers[0], fmt='%.1f', padding=-35, fontsize=14)
    ax.yaxis.label.set_visible(False)