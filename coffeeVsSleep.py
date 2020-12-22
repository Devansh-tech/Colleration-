import plotly.express as plot
import csv

with open("./cups of coffee vs hours of sleep") as csv_file:
    df = csv.DictReader(csv_file)
    fig = plot.scatter(df, x="Coffee in ml", y="sleep in hours", color="week")
    fig.show()
