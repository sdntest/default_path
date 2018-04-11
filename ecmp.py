#coding=utf-8
from pulp import *
from algorithms import dijkstra
from algorithms import dijkstra2
from algorithms import dijkstra3
from algorithms import ksp_yen
#from operator import itemgetter
#from prioritydictionary import priorityDictionary
from graph_for_l2 import DiGraph
from collections import defaultdict
import json
import random
#from chardet.test import count
#import math
CODEC = 'utf-8'
source = []
terminal = []
host_path = "hosts.json" 
fd = open(host_path,'r')
host_node = json.loads(fd.read())
fd.close()
for i in range(0,len(host_node)):
    host_node[i] = host_node[i].encode(CODEC)
    
switch_path = "switches.json" 
fd = open(switch_path,'r')
switch_node = json.loads(fd.read())
fd.close()
for i in range(0,len(switch_node)):
    switch_node[i] = switch_node[i].encode(CODEC)

mynet = "200h100r.json"
g = DiGraph(mynet) 
for i in range(0,100):
    terminal.append(host_node[i])
max_count = 0
avg_count = 0 
for sw in range(0,100):
    temp = 0
    for h in range(0,200):
        path = ksp_yen(g, switch_node[sw], host_node[h],2)
        if len(path) > 1:
            if path[0].get('cost') ==   path[1].get('cost'):
                temp = temp + 1
            
    if temp > max_count:
        max_count = temp
    print max_count
    avg_count = avg_count + temp
print max_count, avg_count/float(100)

    