import scipy.stats as sp
import matplotlib.pyplot as plt
import numpy as np
import csv


def readData(file):
    with open(file, newline="") as file:
        reader = csv.reader(file, delimiter=';', dialect='excel')
        tmp = []
        for index, line in enumerate(reader):
            if "#" in line[0]:

                yield tmp
                tmp = []
                continue

            tmp.append(line)


def transform(data):
    """
    Transform 2d array to two 1d lists
    :param 2d-array like
    :return two arrays (mA, V)
    """

    x = []
    y = []

    for i, j in data:
        i = i.replace(",", ".")
        j = j.replace(",", ".")

        # Add two values to list
        x.append(float(i))
        y.append(float(j))

    return x, y


def trendline(X, Y):
    """
    Returns estimated intercept and slope
    :param data: 2d list
    :return intercept, slope
    """

    # Scipy.stats, least square method
    slope, intercept, r, s, err = sp.linregress(X, Y)

    return slope, intercept


def main():
    FILE = 'jannite.csv'

    fig, axs = plt.subplots(2, 1, constrained_layout=True)
    # Get data
    for n, measures in enumerate(readData(FILE)):

        mA, V = transform(measures)

        # Oikeajännite, pieni R
        if n == 1:
            # initialize subplots

            x = np.linspace(3, 5.5, 100)
            slope, intercept = trendline(mA, V)

            axs[0].scatter(mA, V)
            axs[0].plot(x, slope * x + intercept)

        # Oikeavirta, pieni R
        if n == 2:
            x = np.linspace(3, 5.5, 100)
            slope, intercept = trendline(mA, V)

            axs[0].scatter(mA, V)
            axs[0].plot(x, slope * x + intercept)
            axs[0].legend(["Oikeajannite, pieni resistanssi", "Oikeajannite, trendline", "Oikeavirta, pieni resistanssi", "Oikeavirta, trendline"])

            fig.suptitle("Vastuksen resistanssit")

        # Oikeajännite, suuri R
        if n == 3:
            x = np.linspace(15, 30, 100)
            slope, intercept = trendline(mA, V)
            axs[1].scatter(mA, V)
            axs[1].plot(x, slope * x + intercept)

        # Oikeavirta, suuri R
        if n == 4:
            x = np.linspace(15, 30, 100)
            slope, intercept = trendline(mA, V)

            axs[1].scatter(mA, V)
            axs[1].plot(x, slope * x + intercept)
            axs[1].legend(["Oikeajannite, suuri resistanssi", "Oikeajannite, sovite", "Oikeavirta, suuri resistanssi", "Oikeavirta, sovite"])

            plt.show()


main()
