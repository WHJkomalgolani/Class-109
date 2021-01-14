import random
import statistics
import plotly.express as px
import plotly.figure_factory as ff

count = []
dice_result = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1 + dice2)
    count.append(i)

mean = sum(dice_result) / len(dice_result)
print("Mean of this data is ",mean)
std_deviation = statistics.stdev(dice_result)
print("Standard deviation of this data is ",std_deviation)
   

median = statistics.median(dice_result)
print("Median of this data is ",median)
mode = statistics.mode(dice_result)
print("Mode of this data is ",mode)


fig = ff.create_distplot([dice_result],["Result"],show_hist=False) 
fig.show()   