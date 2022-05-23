import matplotlib.pyplot as plt
import numpy as np
import hand_over_results


def display_diagram():
    negativ = []
    positiv = []
    neutral = []

    zahlen = hand_over_results.get_digitsentimentresults()

    for zahl in zahlen:
        (round(zahl, 0))  # , f"= round({zahl}, 2)")

        if (round(zahl, 0)) == 0:
            neutral.append(round(zahl, 0))

        if (round(zahl, 0)) == -1:
            negativ.append(round(zahl, 0))

        if (round(zahl, 0)) == 1:
            positiv.append(round(zahl, 0))

    data = [len(positiv), len(neutral), len(negativ)]

    # print(data)

    opinions = ['POSITIVE', 'NEUTRAL', 'NEGATIVE']

    explode = (0.1, 0.0, 0.2)  # Falls man Abstände zwischen den drei Komponenten möchte

    colors = ("white", "#0f65af", "black")

    wp = {'linewidth': 1, 'edgecolor': "black"}

    def func(pct, allvalues):
        absolute = int(pct / 100. * np.sum(allvalues))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)

    fig, ax = plt.subplots(figsize=(8, 5), facecolor='white')
    wedges, texts, autotexts = ax.pie(data,
                                      autopct=lambda pct: func(pct, data),
                                      explode=explode,  # siehe oben bei explode
                                      labels=opinions,
                                      shadow=True,
                                      colors=colors,
                                      startangle=90,
                                      wedgeprops=wp,
                                      textprops=dict(color="black"))

    ax.legend(wedges, opinions,
              title="different opinions",
              loc="center left",
              bbox_to_anchor=(1, 0.5, 0.5, 1), facecolor='#d5d5d5')

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title('Title')

    plt_get = fig
    return plt_get
