from git import Repo
import git
import os
import collections
import networkx as nx
import matplotlib.pyplot as plt

def createGraph(repo, test=0):
  commits = list(repo.iter_commits('master'))
  if(test):
    commits = commits[-10:]

  uniqueFiles = []
  graph = []
  
  for c in commits:
    diff = c.diff(git.NULL_TREE)

    for i, d1 in enumerate(diff):
      f1 = d1.a_path

      if(".java" in f1):
        if (f1 not in uniqueFiles):        
          uniqueFiles.append(f1)
          graph.append({})
        
        #adicionar uma aresta entre f1 e arquivo f2 que foi alterado
        f1Index = uniqueFiles.index(f1)
        for d2 in diff[i+1:]:
          f2 = d2.a_path

          if(".java" in f2):
            if (f2 not in uniqueFiles):        
              uniqueFiles.append(f2)
              graph.append({})

            f2Index = uniqueFiles.index(f2)

            #criar ou incrementar peso da aresta de f1 para f2
            if(f2Index not in graph[f1Index]):
              graph[f1Index][f2Index] = 1
            else:
              graph[f1Index][f2Index] += 1

            #criar ou incrementar peso da aresta de f2 para f1
            if(f1Index not in graph[f2Index]):
              graph[f2Index][f1Index] = 1
            else:
              graph[f2Index][f1Index] += 1

  if(test):
    for i, f in enumerate(uniqueFiles):
      print(i, f)
    for i, v in enumerate(graph):
      print(i, v)

  return graph, uniqueFiles

def getFilesMostChangedTogether(graph, files):
  #encontrar maior peso de aresta
  maxWeight = 0
  for v in graph:
    weights = list(v.values())

    if(len(weights) > 0):
      if(max(weights) > maxWeight):
        maxWeight = max(weights)

  #print maxWeight

  #encontrar todas as arestas com maior peso
  mostChangedFiles = []
  for i,v in enumerate(graph):
    vertexes = list(v.keys())
    weights = list(v.values())
    for j,w in enumerate(weights):
      if(w == maxWeight):
        if(files[i] not in mostChangedFiles):
          mostChangedFiles.append(files[i])

        if(files[vertexes[j]] not in mostChangedFiles):          
          mostChangedFiles.append(files[vertexes[j]])

  for f in mostChangedFiles:
    print (str(files.index(f)) + " - " + f)

def getFileWithMostNumberOfRelationships(graph, files):
  maxRelationships = 0
  maxRelationshipsFiles = []

  for v in graph:
    if (len(v) > maxRelationships):
      maxRelationships = len(v)
  
  for i,v in enumerate(graph):
    if(len(v) == maxRelationships):
      maxRelationshipsFiles.append(files[i])

  print(maxRelationships)
  for f in maxRelationshipsFiles:
    print (str(files.index(f)) + " - " + f)

def getMostImportantFiles(graph, files):
  maxWeightSum = 0
  maxWeightSumFiles = []

  for v in graph:
    weightSum = sum(list(v.values()))
    if(weightSum > maxWeightSum):
      maxWeightSum = weightSum

  for i,v in enumerate(graph):
    weightSum = sum(list(v.values()))
    if(weightSum == maxWeightSum):
      maxWeightSumFiles.append(files[i])

  print(maxWeightSum)
  for f in maxWeightSumFiles:
    print (str(files.index(f)) + " - " + f)

def prepareEdgesToVisualization(graph):
  edges = []
  weights = []
  uniqueWeights = []
  for i,v in enumerate(graph):
    for j, w in graph[i].iteritems():

      if(w > 6):
        if(w not in uniqueWeights):
          uniqueWeights.append(w)

        edges.append([i,j,w])
        weights.append(w)

  return edges, weights, uniqueWeights

repo = Repo(os.getcwd() + '/EventBus')



graph, files = createGraph(repo)
print("--- ITEM 1 ---")
getFilesMostChangedTogether(graph, files)

print("--- ITEM 2 ---")
getFileWithMostNumberOfRelationships(graph, files)

print("--- ITEM 3 ---")
getMostImportantFiles(graph, files)



edges, weights, uniqueWeights = prepareEdgesToVisualization(graph)
print edges

G = nx.Graph()
G.add_weighted_edges_from(edges)

pos=nx.circular_layout(G)
nx.draw_networkx_nodes(G,pos,node_color='green',node_size=1000)
nx.draw_networkx_labels(G,pos,font_size=16)

for uw in uniqueWeights:
  uniqueWeightEdges = []
  for e in edges:
    if(e[2] == uw):
      uniqueWeightEdges.append([e[0],e[1]])

  nx.draw_networkx_edges(G,pos,edgelist=uniqueWeightEdges,width=float(uw)/sum(uniqueWeights)*10)

plt.axis('off')
plt.show()
