import json
from bokeh.plotting import figure, show, output_file
from collections import Counter

with open("scientist_birthdays.json", "r") as f:
    birthdays = json.load(f)

num_to_string = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

months = []
for name, birthday_string in birthdays.items():
    month = int(birthday_string.split("/")[0])
    months.append(num_to_string[month])
d = dict(Counter(months))
x = [k for k in d.keys()]
x_categories = [k for k in num_to_string.values()]
y = [v for v in d.values()]

output_file('plot.html')

p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)
show(p)
