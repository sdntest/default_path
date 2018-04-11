import re
import json
import random
f = open("latencies.intra","r")
topo = {}
for line in f:
	m = re.findall("\d+",line)
	v1 = 'v' + str(m[0])
	v2 = 'v' + str(m[1])
	topo.setdefault(v1,{})
	topo[v1][v2] = int(m[2])
	topo.setdefault(v2,{})
	topo[v2][v1] = int(m[2])
f.close()
# switch_list = list(topo.keys())
# switch_num = len(topo)
# i = 0
# for switch in switch_list:
# 	i += 1
# 	topo[switch]['h'+str(i)] = 1
# 	topo['h'+str(i)] = {}
# 	topo['h'+str(i)][switch] = 1
# for j in range(0,switch_num):
# 	i += 1
# 	switch = random.sample(switch_list,1)[0]
# 	topo[switch]['h'+str(i)] = 1
# 	topo['h'+str(i)] = {}
# 	topo['h'+str(i)][switch] = 1
print(len(topo))
f = open("rocketfuel0.json", 'w')
jsObj = json.dumps(topo)
f.write(jsObj)
f.close()