import numpy as np
import pandas as pd

demand = pd.read_csv("demand_2016.08.06_110100_.csv")
distribute = pd.read_csv("distribute_2016.08.06_110100_.csv")

r = 0.01

#统计0点到23点
demand_data = []
distribute_data = []
myindex = []

times = [i for i in range(24)]

result = [0 for _ in range(len(times))]

for i in range(len(times)):
    index1 = (demand.hour == times[i])
    index2 = (distribute.hour == times[i])
    demand_data.append(demand[index1])
    distribute_data.append(distribute[index2])
    index = [0 for _ in range(len(demand[index1]))]
    myindex.append(index)


for i in range(len(times)):
    cars = distribute_data[i]
    men = demand_data[i]
    cars_number = cars.value.values
    men_number = men.value.values
    cars_longitude = cars.longitude.values
    men_longitude = men.longitude.values
    cars_latitude = cars.latitude.values
    men_latitude = men.latitude.values

    number1 = len(cars_number)
    number2 = len(men_number)
    for n in range(number1):
        alltargetmen = []
        mennumber = 0
        carnumber = cars_number[n]
        for m in range(number2):
            if (cars_longitude[n]-men_longitude[m])*(cars_longitude[n]-men_longitude[m])+(cars_latitude[n]-men_latitude[m])*(cars_latitude[n]-men_latitude[m]) <= r*r:
                alltargetmen.append(m)
                mennumber = mennumber + men_number[m]
        if mennumber == 0:
            continue
        added = carnumber/mennumber
        for target in alltargetmen:
            myindex[i][target] = myindex[i][target] + added


    number = len(myindex[i])
    allthecars = sum(cars_number)
    overall = 0
    for j in range(number):
        overall = myindex[i][j] * men_number[j] + overall
    allmen = sum(men_number)

    result[i] = overall / allmen

mean = np.mean(result)
var = np.var(result)
X = abs(mean - 1) * (var + 1)
#偏离程度 X=|η-1|*（D(η)+1）

print(result)
print(mean, var, X)

