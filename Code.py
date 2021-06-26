import pandas as pd
import plotly.figure_factory as ff
import statistics
import csv

df = pd.read_csv("data.csv")
math = df["math"].to_list()
reading = df["reading"].to_list()

result_m1 = []
result_m2 = []
result_m3 = []

result_r1 = []
result_r2 = []
result_r3 = []

#math
m_mean = statistics.mean(math)
m_median = statistics.median(math)
m_mode = statistics.mode(math)
m_stdev = statistics.stdev(math)

#reading
r_mean = statistics.mean(reading)
r_median = statistics.median(reading)
r_mode = statistics.mode(reading)
r_stdev = statistics.stdev(reading)

#print math data
print("Mean of math score is: " + str(m_mean))
print("Median of math score is: " + str(m_median))
print("Mode of math score is: " + str(m_mode))
print("Standard Deviation of math score is: " + str(m_stdev))

#print reading data
print("Mean of reading score is: " + str(r_mean))
print("Median of reading score is: " + str(r_median))
print("Mode of reading score is: " + str(r_mode))
print("Standard Deviation of reading score is: " + str(r_stdev))

#bell curve graphs
fig_1 = ff.create_distplot([math], ["Math Score"], show_hist = False)
fig_2 = ff.create_distplot([reading], ["Reading Score"], show_hist = False)
fig_1.show()
fig_2.show()

#math
start_point_m1 = m_mean - m_stdev
end_point_m1 = m_mean + m_stdev

start_point_m2 = m_mean - 2*m_stdev
end_point_m2 = m_mean + 2*m_stdev

start_point_m3 = m_mean - 3*m_stdev
end_point_m3 = m_mean + 3*m_stdev

#reading
start_poin_r1 = r_mean - r_stdev
end_point_r1 = r_mean + r_stdev

start_poin_r2 = r_mean - 2*r_stdev
end_point_r2 = r_mean + 2*r_stdev

start_poin_r3 = r_mean - 3*r_stdev
end_point_r3 = r_mean + 3*r_stdev

#percentage calculation of math score START
for result in math:
    if result > start_point_m1 and result < end_point_m1:
        result_m1.append(result)

percentage_m1 = (len(result_m1)*100)/len(math)
print(percentage_m1)

for result in math:
    if result > start_point_m2 and result < end_point_m2:
        result_m2.append(result)

percentage_m2 = (len(result_m2)*100)/len(math)
print(percentage_m2)

for result in math:
    if result > start_point_m3 and result < end_point_m3:
        result_m3.append(result)

percentage_m3 = (len(result_m3)*100)/len(math)
print(percentage_m3)
#percentage calculation of math score END

#percentage calculation of reading score START
for result in reading:
    if result > start_poin_r1 and result < end_point_r1:
        result_r1.append(result)

percentage_r1 = (len(result_r1)*100)/len(reading)
print(percentage_r1)

for result in reading:
    if result > start_poin_r2 and result < end_point_r2:
        result_r2.append(result)

percentage_r2 = (len(result_r2)*100)/len(reading)
print(percentage_r2)

for result in reading:
    if result > start_poin_r3 and result < end_point_r3:
        result_r3.append(result)

percentage_r3 = (len(result_r3)*100)/len(reading)
print(percentage_r3)
#percentage calculation of reading score END
#program END