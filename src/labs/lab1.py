from git import Repo
import git
import os
import collections

def getAllCommits(repo):
  return len(list(repo.iter_commits('master')))

def getCommitsByYear(repo, dateSince, dateUntil):
  return len(list(repo.iter_commits('master', since=dateSince, until=dateUntil)))

def getCommitsByMsg(repo, msg):
  return len(list(repo.iter_commits('master', grep=msg)))

def getMostModifiedFiles(repo, dateSince='2000-01-01', dateUntil='2050-01-01'):
  commits = list(repo.iter_commits('master', since=dateSince, until=dateUntil))
  fileChanges = []
  for c in commits:
    for d in c.diff():
      fileName = d.a_path
      if ('.java' in fileName):
        fileChanges.append(fileName)
  print(collections.Counter(fileChanges).most_common(5))

def getMostActiveAuthorsByDate(repo, dateSince='2000-01-01', dateUntil='2050-01-01'):
  commits = list(repo.iter_commits('master', since=dateSince, until=dateUntil))

  authors = []
  for c in commits:
    authors.append(c.author.name)

  mostActive = collections.Counter(authors).most_common(3)
  for author, count in mostActive:
    print(author)

#type='+'-> added
#type='-' -> removed
def getAlteredCodeCountByText(repo, text, typ='+'):
  commits = list(repo.iter_commits('master'))
  lines = []
  count = 0
  for c in commits:
    for d in c.diff(git.NULL_TREE, create_patch=True, S=text):
      for line in d.diff.splitlines():
        if(line.startswith(typ) and text in line):
          count = count + 1

  print (count)

repo = Repo(os.getcwd() + '/EventBus')

print("-- ITEM 01 --")
print(getAllCommits(repo))

print("-- ITEM 02 --")
print(getCommitsByYear(repo, '2019-01-01', ''))
print(getCommitsByYear(repo, '2018-01-01', '2019-01-01'))
print(getCommitsByYear(repo, '2017-01-01', '2018-01-01'))

print("-- ITEM 03 --")
print(getCommitsByMsg(repo, 'feature'))
print(getCommitsByMsg(repo, 'fix'))

print("-- ITEM 04 --")
getMostModifiedFiles(repo)

print("-- ITEM 05 --")
getMostModifiedFiles(repo, '2018-01-01')

print("-- ITEM 06 --")
getMostModifiedFiles(repo, '2017-01-01', '2018-01-01')

print("-- ITEM 07 --")
getMostActiveAuthorsByDate(repo)

print("-- ITEM 08 --")
getMostActiveAuthorsByDate(repo,'2019-01-01','2019-12-31')

print("-- ITEM 09 --")
getAlteredCodeCountByText(repo, 'ArrayList', '+')

print("-- ITEM 10 --")
getAlteredCodeCountByText(repo, 'Vector', '-')
