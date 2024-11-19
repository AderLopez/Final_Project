#Libraries:
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def graph_histogram (name, values,x_label, y_label):
        
    #Use seaborn style
    sns.set_theme()

    #Create data
    #values = np.cumsum(np.random.randn(1000,1))

    #Flushing the plot to create a new graph:
    plt.clf()

    #Use the plot function
    plt.hist(values, bins=30, edgecolor='black', alpha=0.7)
    plt.title('Frequency Table (Histogram)')

    #To use names for the labels
    plt.xlabel(x_label)
    plt.ylabel(y_label) 
    #To rotate the axis
    plt.xticks(rotation=60)

    #Show the graph
    plt.show()

    #Code to save figure as SVG
    #tsla = [1,2,3,4]
    path = 'static/images/'+name+'.svg'
    print(path)
    #Tight option helps to get the graph complete:
    plt.savefig(path, format='svg', bbox_inches='tight')
    return

def graph_Barchar (name, values,x_label, y_label):
          
    #Use seaborn style
    sns.set_theme()

    #Create data
    #values = np.cumsum(np.random.randn(1000,1))

    #Flushing the plot to create a new graph:
    plt.clf()

    #Use the plot function
    # Create a bar chart
    categories = values.index  # This gets the country names or categories
    counts = values.values  # This gets the counts of players per country

    print(categories)
    print(counts)
    plt.barh(categories, counts, edgecolor='red', alpha=0.7)

    #To use names for the labels
    plt.xlabel(x_label)
    plt.ylabel(y_label) 
    #To rotate the axis
    plt.xticks(rotation=60)

    #Show the graph
    plt.show()

    #Code to save figure as SVG
    #tsla = [1,2,3,4]
    path = 'static/images/'+name+'.svg'
    print(path)
    #Tight option helps to get the graph complete:
    plt.savefig(path, format='svg', bbox_inches='tight')
    return