#coding=utf-8
from pulp import *
from algorithms import dijkstra
from algorithms import dijkstra2
from algorithms import dijkstra3
#from operator import itemgetter
#from prioritydictionary import priorityDictionary
from graph_for_l2 import DiGraph
from collections import defaultdict
import json
import random
#import math
CODEC = 'utf-8'
start_path = "hosts.json" 
fd = open(start_path,'r')
start_node = json.loads(fd.read())
fd.close()
for i in range(0,len(start_node)):
    start_node[i] = start_node[i].encode(CODEC)
mynet = "200h100r.json"
g = DiGraph(mynet) 

all_node = []
all_node_alone = []	
all_edge = []	
all_edge_alone = []	
all_node = []
all_node_alone = []	
all_edge = []	
all_edge_alone = []
host = 199
flow_number = 100000
source1 = []
terminal1 = []
source_random = []
terminal_random = []
one_edge = []
one_node = []

for i in range (0,flow_number):
    source_random.append(random.randint(0,host))
for i in range(0,len(source_random)):
    source1.append(start_node[int(source_random[i])])
#print source 

for i in range (0,flow_number):
    terminal_random.append(random.randint(0,host))
for i in range(0,len(terminal_random)):
    terminal1.append(start_node[int(terminal_random[i])])

weight1 = []
bigsize = 4
smallsize = 0.25

for i in range(0,int(flow_number*0.2)):
    a = random.uniform(0,2)
    weight1.append(a*bigsize)
for i in range(int(flow_number*0.2),len(source_random)):             #elephant flow is about 6 while mice flow is about 1.5
    a = random.uniform(0.1,1.9)
    weight1.append(a*smallsize)
random.shuffle(weight1)
print len(weight1)



weight = []
source = []
terminal = []
source_random = []
terminal_random = []
for i in range (0,host):
    j=host-i
    a=i
    for jj in range(0,j):
        source_random.append(a)
print len(source_random)               
for i in range(0,len(source_random)):
    source.append(start_node[int(source_random[i])])


for i in range (0,host):
    j=host-i
    for jj in range(0,j):
        a=host-jj
        terminal_random.append(a)
#print terminal_random 
    
for i in range(0,len(terminal_random)):
    terminal.append(start_node[int(terminal_random[i])])
    
marco_number = int(host*(host+1)*0.5)
print marco_number
    
#number_of_bigflow = 190
#number_of_smallflow = len(source_random) - number_of_bigflow          #the number of elephant flow and mice flow, they obey 2-8 distribute 
#print source
#print"start SR"	,weight
for i in range(0,marco_number):
    weight.append(0)
    
for i in range(0,len(source)):
    if i%1000 == 0:
        print"i is ",i
    #print i
    for j in range(0,len(terminal1)):
        if source[i] == source1[j] and terminal[i] == terminal1[j]:
            weight[i] = weight[i] + weight1[j]
print len(weight)
                    
        





for sr in range (0,len(source_random)):
    if sr%1000 == 0:
        print"source is ",sr
    main_path_all = []
    one_source_edge = []
    one_source_node = []
    path = dijkstra(g, source[sr], terminal[sr])
    main_path = path.get('path')
    for i in range(0,len(main_path)):
        main_path[i] = main_path[i].encode(CODEC)
        main_path_all.append(main_path[i])
    for f in range(0,len(main_path)-3):
        siwtch1 = int(main_path[f+1][1])
        siwtch2 = int(main_path[f+2][1])
        if len(main_path[f+1]) == 3:
            siwtch1 = siwtch1*10 + int(main_path[f+1][2])
        if len(main_path[f+1]) == 4:
            siwtch1 = siwtch1*100 + int(main_path[f+1][2])*10 + int(main_path[f+1][3])
        if len(main_path[f+2]) == 3:
            siwtch2 = siwtch2*10 + int(main_path[f+2][2])
        if len(main_path[f+2]) == 4:
            siwtch2 = siwtch2*100 + int(main_path[f+2][2])*10 + int(main_path[f+2][3])
        if siwtch1 < siwtch2:
            one_edge = main_path[f+1] + main_path[f+2]
        else:
            one_edge = main_path[f+2] + main_path[f+1]
        if one_edge not in all_edge:
            all_edge.append(one_edge)	
        one_source_edge.append(one_edge)
    all_edge_alone.append(one_source_edge)


    for f in range(0,len(main_path)-2):
        one_node = main_path[f+1]
        if one_node not in all_node:
            all_node.append(one_node)
        one_source_node.append(one_node)
    all_node_alone.append(one_source_node)

    one_source_node = []
    one_source_edge = []
    path = dijkstra2(g, source[sr], terminal[sr],main_path_all)
    main_path = path.get('path')
    for i in range(0,len(main_path)):
        main_path[i] = main_path[i].encode(CODEC)
        main_path_all.append(main_path[i])
    for f in range(0,len(main_path)-3):
        siwtch1 = int(main_path[f+1][1])
        siwtch2 = int(main_path[f+2][1])
        if len(main_path[f+1]) == 3:
            siwtch1 = siwtch1*10 + int(main_path[f+1][2])
        if len(main_path[f+1]) == 4:
            siwtch1 = siwtch1*100 + int(main_path[f+1][2])*10 + int(main_path[f+1][3])
        if len(main_path[f+2]) == 3:
            siwtch2 = siwtch2*10 + int(main_path[f+2][2])
        if len(main_path[f+2]) == 4:
            siwtch2 = siwtch2*100 + int(main_path[f+2][2])*10 + int(main_path[f+2][3])
        if siwtch1 < siwtch2:
            one_edge = main_path[f+1] + main_path[f+2]
        else:
            one_edge = main_path[f+2] + main_path[f+1]
        if one_edge not in all_edge:
            all_edge.append(one_edge)	
        one_source_edge.append(one_edge)
    all_edge_alone.append(one_source_edge)

    for f in range(0,len(main_path)-2):
        one_node = main_path[f+1]
        if one_node not in all_node:
            all_node.append(one_node)
        one_source_node.append(one_node)
    all_node_alone.append(one_source_node)
    
    
    one_source_node = []
    one_source_edge = []
    path = dijkstra3(g, source[sr], terminal[sr],main_path_all)
    main_path = path.get('path')
    for i in range(0,len(main_path)):
        main_path[i] = main_path[i].encode(CODEC)
        main_path_all.append(main_path[i])
    for f in range(0,len(main_path)-3):
        siwtch1 = int(main_path[f+1][1])
        siwtch2 = int(main_path[f+2][1])
        if len(main_path[f+1]) == 3:
            siwtch1 = siwtch1*10 + int(main_path[f+1][2])
        if len(main_path[f+1]) == 4:
            siwtch1 = siwtch1*100 + int(main_path[f+1][2])*10 + int(main_path[f+1][3])
        if len(main_path[f+2]) == 3:
            siwtch2 = siwtch2*10 + int(main_path[f+2][2])
        if len(main_path[f+2]) == 4:
            siwtch2 = siwtch2*100 + int(main_path[f+2][2])*10 + int(main_path[f+2][3])
        if siwtch1 < siwtch2:
            one_edge = main_path[f+1] + main_path[f+2]
        else:
            one_edge = main_path[f+2] + main_path[f+1]
        if one_edge not in all_edge:
            all_edge.append(one_edge)	
        one_source_edge.append(one_edge)
    all_edge_alone.append(one_source_edge)


    for f in range(0,len(main_path)-2):
        one_node = main_path[f+1]
        if one_node not in all_node:
            all_node.append(one_node)
        one_source_node.append(one_node)
    all_node_alone.append(one_source_node)
    #print all_edge_alone,all_node_alone
    
    p1 = "./data/paths.json"  #rounding
    fd1 = open(p1, 'a')
    fd1.write(json.dumps(main_path_all))
                
    p2 = "./data/flows.json"  #rounding
    fd2 = open(p2, 'a')
    fd2.write(json.dumps(source[sr]))
    fd2.write(json.dumps(terminal[sr]))
    fd2.write(json.dumps(weight[sr]))
    
fd1.close()
fd2.close()












for flow_traffic in range(1,2):
    alg0=0
    alg1=0
    alg2=0
    alg3=0
    for randome_time in range(0,1):
        '''
        weight = []
        bigsize = 4*flow_traffic
        smallsize = 0.25*flow_traffic
        for i in range(0,number_of_bigflow):
            a = random.randint(1,1)
            weight.append(a*bigsize)
        for i in range(0,len(source_random)):             #elephant flow  mice flow 
            a = random.randint(1,1)
            weight.append(a*smallsize)
        random.shuffle(weight)



        print "flow_traffic,randome_time",flow_traffic,randome_time


'''

        for entries in range(30,31):              #300-4200
            entries = entries *10
            ce = 10000
            #print entries
            for alg in range(0,10):
                if alg == 0:  
                    x_e = defaultdict(lambda:(defaultdict(lambda:(defaultdict(lambda:None)))))
                    x_v = defaultdict(lambda:(defaultdict(lambda:(defaultdict(lambda:None)))))
                    x = [[0 for col in range(3)] for row in range(len(source_random))] #3 is the number of path that each flow can choose
                    for i in range(0,len(source_random)):
                        for j in range(0,3):          #3 is the number of path that each flow can choose
                            x[i][j] = "x"
                            if len(source_random) < 100000:
                                if i < 10:
                                    x[i][j] = x[i][j] + "0000"
                                elif i < 100:
                                    x[i][j] = x[i][j] + "000"
                                elif i < 1000:
                                    x[i][j] = x[i][j] + "00"
                                elif i < 10000:
                                    x[i][j] = x[i][j] + "0"
                            x[i][j] = x[i][j] + str(i) + str(j)
        
                    z = []
                    for i in range(0,len(source_random)):
                        z.append("z"+str(i))
        
                    temp = []
                    for i in range(0,len(source_random)):
                        for j in range(0,3):              #3 si the number of path that each flow can choose
                            temp.append(x[i][j])
                    for i in range(0,len(source_random)):
                        temp.append(z[i])
                    #print x
                                
                    #print"start  pulp1"
        
                
                    #prob = LpProblem('lptest', LpMaximize)
                    prob = LpProblem('lptest', LpMinimize)
                    r = LpVariable('r', lowBound = 0)
                    #tradeoff = LpVariable('tradeoff', lowBound = 0)
                    xx = LpVariable.dicts("",temp, lowBound = 0,upBound = 1)
                    #print xx
                    print"------------"
                    prob += r
                    for i in range(0,len(source_random)):
                        prob += lpSum([xx[j] for j in x[i]]) == xx[z[i]]       #that means, x[i][0]+x[i][1]....+x[i][len(x[i])-1] = 1
                        #print "j",j,len(x[i])
                        prob += xx[z[i]] == 1
                    #prob += lpSum(reciprocal_gt*weight[i]*xx[z[i]] for i in range(0,len(source_random))) >= tradeoff
                    
                
                    #print  "len(all_edge_alone)",len(all_edge_alone)
                    for i in range(0,len(all_edge_alone)):
                        for j in range(0,len(all_edge_alone[i])):           #for example, all_edge_alone[i][j] = v1v2
                            length_x_e = len( x_e[all_edge_alone[i][j]])
                            #print "length_x_e",length_x_e,all_edge_alone[i],all_edge_alone[i][j]
                            x_e[all_edge_alone[i][j]][length_x_e][0] = x[i/3][i%3]
                            x_e[all_edge_alone[i][j]][length_x_e][1] = weight[i/3]
                    #print"222"
                    for h in all_edge:
                        prob += lpSum(x_e[h][i][1]*xx[x_e[h][i][0]] for i in x_e[h]) <= ce*r
        
                    #print  "x_e",x_e
                    #print len(all_node_alone)
        
                    for i in range(0,len(all_node_alone)):
                        for j in range(0,len(all_node_alone[i])):
                            length_x_v = len( x_v[all_node_alone[i][j]])
                            #print length_x_v
                            if i%3 == 0:
                                x_v[all_node_alone[i][j]][length_x_v][0] = x[0][2]  #make some approximations 
                            else:
                                x_v[all_node_alone[i][j]][length_x_v][0] = x[i/3][i%3]
                            if j ==0:
                                x_v[all_node_alone[i][j]][length_x_v][1] = 1                 
                            else:
                                x_v[all_node_alone[i][j]][length_x_v][1] = 1                  
                    #print"333"
                    for v in all_node:
                        prob += lpSum(x_v[v][i][1]*xx[x_v[v][i][0]] for i in x_v[v]) <= entries
                        #print v
                        #print lpSum(x_v[v][i][1]*xx[x_v[v][i][0]] for i in x_v[v])
                        #print x_v[v]
        
                    #print"start solve pulp1"
                    GLPK().solve(prob)
        
                    #for v in prob.variables():
                       # print v.name, '=', v.varValue
        
                    print 'objective_sr =', value(prob.objective)
                    #print reciprocal_gt
        
                  
                    p1 = "./data/alg0.json"
                    fd = open(p1, 'a')
                    fd.write(json.dumps(value(prob.objective)))
                    fd.write(json.dumps("/"))
                    fd.close()
                    alg0 = alg0 + float(value(prob.objective))
      
                    
'''                    
                    i=0
                    j=0
                    l=0
                    for v in prob.variables():
                        l =l +1
                        if l<571:  #(the number of flows /cdot 3) +1
                            x[i][j]=v.varValue
                            if j<2:
                                j =j+1
                            else:
                                i=i+1
                                j=0
                    lambda1 = 0
                    used_ce = defaultdict(lambda:None)
                    for e in all_edge:
                        used_ce[e] = 0     
                                       
                    for i in range(0,source_number):
                        k=0
                        choose=0

                        for j in range(0,3):
                            if x[i][j]>=k:
                                choose=j
                                k=x[i][j]
                                #print choose
                        for n in range(0,len(all_edge_alone[3*i+choose])):
                                #print n       
                                used_ce[all_edge_alone[3*i+choose][n]] = used_ce[all_edge_alone[3*i+choose][n]] + weight[i]
                                if used_ce[all_edge_alone[3*i+choose][n]]/float(ce) > lambda1:
                                    #print "hhhhh"
                                    lambda1 = used_ce[all_edge_alone[3*i+choose][n]]/float(ce)
                                    #print "lambda1,i:", lambda1,i
                        #print weight[i],source[i],terminal[i],lambda1,all_edge_alone[3*i+choose]
                      
                    p1 = "./data/alg1.json"  #rounding
                    fd = open(p1, 'a')
                    fd.write(json.dumps(lambda1))
                    fd.write(json.dumps("/"))
                    fd.close()    
                    alg1=alg1+lambda1                            

 
                    
                if alg == 2:  #启发式算法
                    used_ce = defaultdict(lambda:None)
                    used_entries  = defaultdict(lambda:None)
                    for v in all_node:
                        used_entries[v] = 0
                    for e in all_edge:
                        used_ce[e] = 0
                    lambda1 = 0
                    temp2 = 0
                    for i in range(0,source_number):
                        temp = [[0 for col in range(2)] for row in range(3)]
                        for row in range(0,3):
                            for col in range(0,2):
                                temp[row][col] = 0  
                               
                        for j in range(0,3):
                            for n in range(0,len(all_node_alone[3*i+j])):
                                if used_entries[all_node_alone[3*i+j][n]] + 1 > entries:
                                    temp[j][0] = 1
                            for n in range(0,len(all_edge_alone[3*i+j])):
                                if temp[j][1]<(used_ce[all_edge_alone[3*i+j][n]] + weight[i])/float(ce):
                                    temp[j][1] = (used_ce[all_edge_alone[3*i+j][n]] + weight[i])/float(ce)  
                        temp1 = 10000
                        k = 0 #表示选几个可行路径中的哪一条
                        for j in range(0,3):
                            if temp[j][0] != 1:
                                if temp[j][1] < temp1:   #选择满足流表约束条件下的，负载最轻的那条可行路径.
                                    k = j;
                                    temp1 = temp[j][1];
                        if temp1 == 10000: #表示几条可行路径均不满足流表约束，此时直接ospf，  那么只需要使用链路容量
                            temp2 = temp2 + 1
                            for n in range(0,len(all_edge_alone[3*i])): 
                                used_ce[all_edge_alone[3*i][n]] = used_ce[all_edge_alone[3*i][n]] + weight[i]
                                if used_ce[all_edge_alone[3*i][n]]/float(ce) > lambda1:
                                    lambda1 = used_ce[all_edge_alone[3*i][n]]/float(ce)   #记录最大的lambda
                        else:           #否则的话从可行路径中选择一条（第k条），需要使用链路容量和流表项
                            for n in range(0,len(all_edge_alone[3*i+k])):
                                used_ce[all_edge_alone[3*i+k][n]] = used_ce[all_edge_alone[3*i+k][n]] + weight[i]
                                if used_ce[all_edge_alone[3*i+k][n]]/float(ce) > lambda1:
                                    lambda1 = used_ce[all_edge_alone[3*i+k][n]]/float(ce)   #记录最大的lambda
                            for n in range(0,len(all_node_alone[3*i+k])):
                                used_entries[all_node_alone[3*i+k][n]] = used_entries[all_node_alone[3*i+k][n]] + 1
                        #print lambda1,all_edge_alone[3*i+k]       
                    p1 = "./data/alg2.json"
                    fd = open(p1, 'a')
                    fd.write(json.dumps(lambda1))
                    fd.write(json.dumps("/"))
                    fd.close()     
                    alg2=alg2+lambda1             
                                    
                    p1 = "./data/ospf_times.json"
                    fd = open(p1, 'a')
                    fd.write(json.dumps(temp2))
                    fd.write(json.dumps("/"))
                    fd.close() 
                          
                             
                        
                if alg == 3:  #ospf
                    lambda1=0  
                    used_ce = defaultdict(lambda:None)
                    used_entries  = defaultdict(lambda:None)
                    for v in all_node:
                        used_entries[v] = 0
                    for e in all_edge:
                        used_ce[e] = 0
                        
                    for i in range(0,source_number):
                        for n in range(0,len(all_edge_alone[3*i])):
                                #print n       
                                used_ce[all_edge_alone[3*i][n]] = used_ce[all_edge_alone[3*i][n]] + weight[i]
                                if used_ce[all_edge_alone[3*i][n]]/float(ce) > lambda1:
                                    #print "hhhhh"
                                    lambda1 = used_ce[all_edge_alone[3*i][n]]/float(ce)
                        #print weight[i],source[i],terminal[i],lambda1,all_edge_alone[3*i+choose]
                      
                    p1 = "./data/alg3.json"  #rounding
                    fd = open(p1, 'a')
                    fd.write(json.dumps(lambda1))
                    fd.write(json.dumps("/"))
                    fd.close()  
                    alg3=alg3+lambda1   

    p1 = "./data/avg_alg0.json"  #rounding
    fd = open(p1, 'a')
    fd.write(json.dumps(float(alg0)/30))
    fd.write(json.dumps("/"))
    fd.close()  
    
    p1 = "./data/avg_alg1.json"  #rounding
    fd = open(p1, 'a')
    fd.write(json.dumps(float(alg1)/30))
    fd.write(json.dumps("/"))
    fd.close()  
    
    p1 = "./data/avg_alg2.json"  #rounding
    fd = open(p1, 'a')
    fd.write(json.dumps(float(alg2)/30))
    fd.write(json.dumps("/"))
    fd.close()  
    
    p1 = "./data/avg_alg3.json"  #rounding
    fd = open(p1, 'a')
    fd.write(json.dumps(float(alg3)/30))
    fd.write(json.dumps("/"))
    fd.close()  
    '''       