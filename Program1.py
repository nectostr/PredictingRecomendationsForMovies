import pandas as pd
pdata = pd.read_csv('data.csv', sep = ',')
# print(pdata.iloc[17,:]) # мой список
# print([i for i in range(len(pdata.iloc[17,:])) if pdata.iloc[17,i]==-1 ]) # список тех, кого мне надо оценить
pdata["simulTo18"] = pd.Series([0] * (len(pdata)))
pdata["averageValue"] = pd.Series([0] * (len(pdata)))

for i in range(len(pdata)):
	sum = 0
	num = 30
	for j in range(1,31):
		if pdata.iloc[i,j] != -1:
			sum += pdata.iloc[i,j]
		else:
			num -= 1
	pdata.iloc[i,32] = sum / num

for j in range(0,40):
	if j != 17:
		sum = 0
		sumu = 0
		sumv = 0
		for k in range(1,31):
			if pdata.iloc[j,k] != -1 and pdata.iloc[17,k] != -1:
				sum += int(pdata.iloc[j,k]) * int(pdata.iloc[17,k])
				sumu += int(pdata.iloc[j,k]) ** 2
				sumv += int(pdata.iloc[17,k]) ** 2
		pdata.iloc[j, 31] = sum / (sumu ** 0.5 * sumv ** 0.5)
a = pdata.sort_values(['simulTo18'], ascending='false').iloc[35:40,:]


res = []
for i in [i for i in range(len(pdata.iloc[17,:])) if pdata.iloc[17,i]==-1 ]:
	sum = 0
	sumsim = 0
	for k in range(len(a)):
		if a.iloc[k,i] != -1:
			# print(a.iloc[k,i+1])
			# print('!')
			sum += a.iloc[k,31] * (a.iloc[k,i] - a.iloc[k,32])
			# print(a.iloc[k,i+1])
			sumsim += a.iloc[k,31]
	res.append([i,pdata.iloc[17,32]+sum/sumsim])
print(res)
# print(a)
# print(pdata)

