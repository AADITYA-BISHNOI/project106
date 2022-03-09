# Very Important Code

import plotly.express as px
import csv

with open("Student Marks vs Days Present.csv") as csv_file:
    df = csv.DictReader(csv_file)

    fig = px.scatter(df, x = "Roll No", y = "\tMarks In Percentage")
    fig.show()
