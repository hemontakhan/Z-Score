from pandas.tseries.offsets import Second
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

import pandas as pd
import csv

observer = pd.read_csv('School1.csv')
file = observer['Math_score'].tolist()

def random_intergers(counter):
  scorelist = []
  for x in range(0,counter):
      random_number = random.randint(0,len(file)-1)
      score = file[random_number]
      scorelist.append(score)
  mean = statistics.mean(scorelist)
  return mean

mean_set = []
for z in range(0,100):
   list_mean = random_intergers(30)
   mean_set.append(list_mean)

def show_chart(mean_set):
    chart_data = mean_set
    flow = ff.create_distplot([chart_data],['Math_score'],show_hist=False)
    flow.show()

show_chart(mean_set)

standard_dev = statistics.stdev(mean_set)
mean = statistics.mean(mean_set)
print("Mean of Sample Distribution :- ",mean)
print("Standard Deviation of Sampling Distribution :- ",standard_dev)

first_stddev_start,first_stddev_end = mean - standard_dev,mean+standard_dev
second_stddev_start,second_stddev_end = mean-(2*standard_dev),mean+(2*standard_dev)
third_stddev_start,third_stddev_end = mean - (3*standard_dev),mean+(3*standard_dev)
print('standard deviation 1st',first_stddev_start,first_stddev_end)
print('Standard deviation 2nd',second_stddev_start,second_stddev_end)
print('standard deviation 3rd',third_stddev_start,third_stddev_end)


df = pd.read_csv("School_1_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample1)
fig = ff.create_distplot([mean_set], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[first_stddev_end, first_stddev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_stddev_end, second_stddev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_stddev_end, third_stddev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()




reader = pd.read_csv("School_2_Sample.csv")
data = reader["Math_score"].tolist()
sample2_mean = statistics.mean(data)
print("mean of performance of School 2:- ",sample2_mean)
fig = ff.create_distplot([mean_set], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[sample2_mean, sample2_mean], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO USED THE APP"))
fig.add_trace(go.Scatter(x=[first_stddev_end, first_stddev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_stddev_end, second_stddev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_stddev_end, third_stddev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


# finding the mean of the STUDENTS WHO WERE ENFORCED WITH REGISTERS and plotting it on the plot.
df = pd.read_csv("School_3_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)
print("mean of sample3:- ",mean_of_sample3)
fig = ff.create_distplot([mean_set], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO WERE ENFORCED WITH MATH REGISTERS"))
fig.add_trace(go.Scatter(x=[second_stddev_end, second_stddev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_stddev_end, third_stddev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


z_score = (mean - mean_of_sample1)/standard_dev
print("Z-Score is :- ",z_score)