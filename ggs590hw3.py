
# coding: utf-8

# ## Assignment 3-1 (a)

# In[1]:


def getUserInfo(id):
    
    filename_checkin = 'data/Gowalla_totalCheckins.txt'
    
    output = [];
    
    with open(filename_checkin) as f:
        for line in f:
            if (line.split('	')[0] == userId):

                checkInTime = line.split('	')[1]
                location = (float(line.split('	')[2]), float(line.split('	')[3]))
                locationId = int(line.split('	')[4])

                record = {'Check-in Time': checkInTime, 'Location': location, 'Location ID': locationId}
                output.append(record)

    return output


# In[2]:


def getUserNetwork(id): 
    
    filename_edge = 'data/Gowalla_edges.txt'
    
    network = []
    
    with open(filename_edge) as f:
        for line in f:
            if (line.split('	')[0] == userId):
                friendId = int(line.split('	')[1])
                network.append(friendId)

    return network


# In[3]:


print("Please enter the user ID")

userId = input()

userInfo = getUserInfo(userId)
userNetwork = getUserNetwork(userId)


# In[4]:


print(userInfo)
print(userNetwork)


# In[11]:


from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q = [(0,f,())]
    seen = set()
    mins = {f: 0}
    
    while q:        
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            
            seen.add(v1)
            path += (v1, )
            
            if v1 == t: 
                return (cost, path)

            for c, v2 in g.get(v1, ()):
                
                if v2 in seen: 
                    continue
                    
                prev = mins.get(v2, None)
                next = cost + c
                
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf")


# In[12]:


def parseEdge(file): 
    
    filename_edge = 'data/Gowalla_edges.txt'
    
    edge = []
    
    with open(filename_edge) as f:
        for line in f:
            userId = str(int(line.split('	')[0]))
            mappingId = str(int(line.split('	')[1]))
            distance = 1
            edge.append((userId, mappingId, distance))

    return edge


# In[15]:


gowalla_edges = parseEdge('data/Gowalla_edges.txt')
start = '3'
end = '196576'
print('Distance: ', dijkstra(gowalla_edges, start, end)[0])
print('Path: ', dijkstra(gowalla_edges, start, end)[1])

