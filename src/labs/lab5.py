from git import Repo
import git
import os
import collections
import networkx as nx
import matplotlib.pyplot as plt

def createGraph(repo, test=0):
  commits = list(repo.iter_commits('master'))
  if(test):
    commits = commits[-2:]

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

def prepareEdgesToVisualization(graph):
  edges = []
  for i,v in enumerate(graph):
    for j, w in graph[i].iteritems():
      edges.append([i,j,w])

  return edges

repo = Repo(os.getcwd() + '/EventBus')

graph, files = createGraph(repo)
edges = prepareEdgesToVisualization(graph)

G = nx.Graph()
G.add_weighted_edges_from(edges)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()