from git import Repo
import git
import os
import collections

def createGraph(repo):
  commits = list(repo.iter_commits('master'))
  uniqueFiles = []
  
  for c in commits:
    index = repo.index
    index.reset(c)
    files = index.checkout(force=True)
    for f in files:
      if (f not in uniqueFiles):
        uniqueFiles.append(f)

  numOfFiles = len(uniqueFiles)
  graph = [[0 for x in range(numOfFiles)] for x in range(numOfFiles)]
  
  for c in commits:
    repoIndex = repo.index
    repoIndex.reset(c)
    files = list(repoIndex.checkout(force=True))
    for index, f in enumerate(files):
      fileIndex = uniqueFiles.index(f)
      for df in files[index:]:
        dfGraphIndex = uniqueFiles.index(df)
        graph[fileIndex][dfGraphIndex] += 1
        graph[dfGraphIndex][fileIndex] += 1

  # for i in range(numOfFiles):
  #  for j in range(numOfFiles):
  #    print(graph[i][j])

  print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in graph]))

repo = Repo(os.getcwd() + '/EventBus')

createGraph(repo)
    