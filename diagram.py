import matplotlib.pyplot as plt #Python library for visualization.
import numpy as np              #Data processing library.
import hand_over_results        #From hand_over_results.py (Usecase is the sentiment analysis).


def display_diagram():          #Function which is supplied to the gui so that it can execute the diagram.
    try:                        #If try does not work the error is caught below.
        negativ = []            #Different lists which are empty at the beginning.
        positiv = []
        neutral = []

        zahlen = hand_over_results.get_digitsentimentresults()
        """
        Access the sentiment column in the database and pass a list of decimal numbers.
           hand_over_results.py is the program for sentiment evaluation from the database and the function get_digitsentimentresults
           called on hand_over_results returns the list of floats 'zahlen'.
        """

        for zahl in zahlen:
            (round(zahl, 0))  # , f"= round({zahl}, 2)")    #All decimal numbers from the list 'zahlen' are rounded here and added accordingly to the three different lists.

            if (round(zahl, 0)) == 0:               #If number is between -0.4... and 0.4... then add it to the list 'neutral'.
                neutral.append(round(zahl, 0))

            if (round(zahl, 0)) == -1:              #If number is between -1.4... and - 0.5... then add it to the list 'negativ'.
                negativ.append(round(zahl, 0))

            if (round(zahl, 0)) == 1:               #If number is greater than 0.5... then add it to the list 'positiv'.
                positiv.append(round(zahl, 0))

        data = [len(positiv), len(neutral), len(negativ)]   #'len' outputs the number of elements in the different lists and from this the opinion distribution can be inferred.

        # print(data) //was only for testing. No need for running!

        opinions = ['POSITIVE', 'NEUTRAL', 'NEGATIVE'] #The three components for the diagram.

        explode = (0.1, 0.0, 0.2)  #If you want distances between the three components.

        colors = ("white", "#0f65af", "black") ##Colors in order like 'opinions' line 32: All colors for matplotlib in python:'https://matplotlib.org/stable/gallery/color/named_colors.html'.

        wp = {'linewidth': 1, 'edgecolor': "black"} #the black line for better view

        def func(pct, allvalues):

            absolute = int(pct / 100. * np.sum(allvalues)) #numpy method sum is a sum of array elements over a given axis.
            return "{:.1f}%\n({:d} g)".format(pct, absolute) #Only formating the graph and the :.1f is only the rounding, g stands for the number of elements in the individual lists.

        fig, ax = plt.subplots(figsize=(8, 5), facecolor='white') ##size and background color of graphic
        """
        The functions from above are initialized here and Shadow=True provides a slight 3D effect with the black edge (line 60).
        """
        wedges, texts, autotexts = ax.pie(data,
                                          autopct=lambda pct: func(pct, data),          #lamda passes the pct function
                                          explode=explode,  # siehe oben bei explode
                                          labels=opinions,
                                          shadow=True,
                                          colors=colors,
                                          startangle=90,
                                          wedgeprops=wp,
                                          textprops=dict(color="black"))
        """
        Giving title to the diagram and place it!
        """
        ax.legend(wedges, opinions,
                  title="different opinions",
                  loc="center left",  
                  bbox_to_anchor=(1, 0.5, 0.5, 1), facecolor='#d5d5d5') #Placing of the diagram box.

        plt.setp(autotexts, size=8, weight="bold") #Setting the final diagram parts together.

        # ax.set_title('Title')
        plt.close()             #Diagram closing for saving CPU.
        plt_get = fig           #Transfer of the configuration values.
        return plt_get
    except:                         #Exception handling. If try does not work the except method is running!
        print('database is empty')  #In case of an empty database.
