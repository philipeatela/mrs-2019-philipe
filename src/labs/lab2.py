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

#item 3
def getFilesCountInEachCommit(repo):
  commits = list(repo.iter_commits('master'))
  for c in reversed(commits):
    print c.hexsha
    print getFileCountByCommit(repo, c)

#item 4
def getJavaFilesCountInEachCommit(repo):
  commits = list(repo.iter_commits('master'))
  for c in reversed(commits):
    print c.hexsha
    print getJavaLinesCountByCommit(repo, c)

#item 5
def getJavaLinesCountInEachCommit(repo):
  commits = list(repo.iter_commits('master'))
  for c in reversed(commits):
    print c.hexsha
    print getFileCountByCommit(repo, c, )

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

def getCommitNumOfFiles(repo, arg):
  commits = list(repo.iter_commits('master'))
  commit = commits[arg]
  return getFileCountByCommit(repo, commit)

def getCommitNumOfJavaFiles(repo, arg):
  commits = list(repo.iter_commits('master'))
  commit = commits[arg]
  return getFileCountByCommit(repo, commit, ".java")


repo = Repo(os.getcwd() + '/EventBus')

print("-- ITEM 01 --")
print("First commit:")
print(getCommitNumOfFiles(repo, -1))
print("Last commit:")
print(getCommitNumOfFiles(repo, 0))

print("-- ITEM 02 --")
print("First commit:")
print(getCommitNumOfJavaFiles(repo, -1))
print("Last commit:")
print(getCommitNumOfJavaFiles(repo, 0))

print("-- ITEM 03 --")
getFilesCountInEachCommit(repo)

print("-- ITEM 04 --")
getJavaFilesCountInEachCommit(repo)

print("-- ITEM 05 --")
getJavaLinesCountInEachCommit(repo)

print("-- ITEM 06 --")
getFileCountInEachYear(repo)

print("-- ITEM 07 --")
getJavaFileCountInEachYear(repo)

print("-- ITEM 08 --")
getJavaLinesCountInEachYear(repo)