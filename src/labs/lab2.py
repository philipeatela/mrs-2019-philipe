from git import Repo
import git
import os
import collections

def getJavaLinesCountByCommit(repo, commit):
  index = repo.index
  index.reset(commit)
  co = index.checkout(force=True)

  count = 0
  for file in co:
    if(".java" in file):
      f = open(os.getcwd() + "/EventBus/" + file)
      count += len(f.readlines())
  
  return count

def getFileCountByCommit(repo, commit, type=None):
  index = repo.index
  index.reset(commit)
  co = index.checkout(force=True)

  count = 0
  for file in co:
    if(type is None or type in file):
      count += 1

  return count

#item 5
def getJavaLinesCountInEachCommit(repo):
  commits = list(repo.iter_commits('master'))
  for c in reversed(commits):
    print c.hexsha
    print getJavaLinesCountByCommit(repo, c)

#item 6
def getFileCountInEachYear(repo):
  for year in range(2012,2020):
    dateSince = str(year) + "-01-01"
    dateUntil = str(year) + "-12-31"
    
    count = 0 
    commits = list(repo.iter_commits('master', since=dateSince, until=dateUntil))
    for c in commits:
      count += getFileCountByCommit(repo, c)

    print year, ": ", count

#item 7
def getJavaFileCountInEachYear(repo):
  for year in range(2012,2020):
    dateSince = str(year) + "-01-01"
    dateUntil = str(year) + "-12-31"
    
    count = 0 
    commits = list(repo.iter_commits('master', since=dateSince, until=dateUntil))
    for c in commits:
      count += getFileCountByCommit(repo, c, ".java")

    print year, ": ", count

#item 8
def getJavaLinesCountInEachYear(repo):
  for year in range(2012,2020):
    dateSince = str(year) + "-01-01"
    dateUntil = str(year) + "-12-31"
    
    count = 0 
    commits = list(repo.iter_commits('master', since=dateSince, until=dateUntil))
    for c in commits:
      count += getJavaLinesCountByCommit(repo, c)

    print year, ": ", count


repo = Repo(os.getcwd() + '/EventBus')

print("-- ITEM 05 --")
getJavaLinesCountInEachCommit(repo)

print("-- ITEM 06 --")
getFileCountInEachYear(repo)

print("-- ITEM 07 --")
getJavaFileCountInEachYear(repo)

print("-- ITEM 08 --")
getJavaLinesCountInEachYear(repo)