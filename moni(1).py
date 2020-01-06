import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt
np.random.seed(0)
#以下超参是可以更改的
k1=1
k2=0.5
cost=5 #出租车司机行驶单位里程所需要的成本
r0=3 #没有补贴时的接客半径
lambda_1=0
lambda_2=0  #司机补贴
a1=0.5
a2=0.3
sampleNo_init_car = 2000 #测试时车的数据点数上限
sampleNo_init_man = 1000 #测试时人的数据点数上限
test_num=10 #测试10次取平均
mu = 0 #正态分布的均值和方差
sigma = 50

#以下参数是算出来的
sampleNo_man=int((1-a1*(np.e**(-k1*lambda_1)))*sampleNo_init_man)
sampleNo_car=int((1-a2*(np.e**(-k2*lambda_2)))*sampleNo_init_car)
r=r0+lambda_2/cost  #接客半径

result=[]
for test_idx in range(test_num):
    #生成数据点
    man_x=np.random.normal(mu, sigma, sampleNo_man)
    man_y=np.random.normal(mu, sigma, sampleNo_man)
    car_x=np.random.normal(mu, sigma, sampleNo_car)
    car_y=np.random.normal(mu, sigma, sampleNo_car)
    myindex=[0 for _ in range(sampleNo_man)]
    
    for i in range(sampleNo_car):
        alltargetman=[]
        for j in range(sampleNo_man):
            if (man_x[j]-car_x[i])**2+(man_y[j]-car_y[i])**2<=r**2:
                alltargetman.append(j)
        if len(alltargetman)==0:
            continue
        added=1/len(alltargetman)
        for target in alltargetman:
            myindex[target]+=added
    
    overall=sum(myindex)
    result.append(overall/sampleNo_man)
print('average yita:',sum(result)/test_num)

#画图
plt.scatter(man_x,man_y,s=1,marker='+',c=(0,0,1))
plt.scatter(car_x,car_y,s=1,marker='+',c=(1,0,0))
plt.xlim((-150, 150))
plt.ylim((-150, 150))
plt.show()