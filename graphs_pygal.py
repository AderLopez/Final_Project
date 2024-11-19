#second example:
#To install the nasdaqdatalink run = python -m pip install nasdaq-data-link    

import pandas as pd
import pygal
import nba 


def graph_bar_chart(name, values,x_label, y_label):
    #Configuring the information for a dataframe to be displayed when printing:
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 12)
    pd.set_option('display.width', 400)

    print(values)

    # Create a bar chart
    categories = values.index  # This gets the country names or categories
    counts = values.values  # This gets the counts of players per country

    print(categories)
    print(counts)

     # Prepare the chart
    chart = pygal.Bar()
    # Add the data to the chart (countries and their player counts)

    chart.title=(name)
    chart.x_title = x_label
    chart.y_title = y_label
    # Add the data to the chart (countries and their player counts)
    chart.x_labels = categories  # Country names (x-axis)
    chart.add('Players per Country', counts)  # Player counts (y-axis)

    path = f'static/images/{name}_bar_pygal.svg'
    chart.render_to_file(path) #svg format


    return 

