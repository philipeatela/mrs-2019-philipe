from git import Repo
import os
import git
import time

def normalizeFile(filename, old_string="\t", new_string=" "):
  # Safely read the input filename using 'with'
  with open(filename) as f:
      s = f.read()
      if old_string not in s:
        #print('"{old_string}" not found in {filename}.'.format(**locals()))
        return

  # Safely write the changed content, if found in the file
  with open(filename, 'w') as f:
    #print('Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
    s = s.replace(old_string, new_string)
    f.write(s)

def getFileMetrics(path):
  normalizeFile(path)
  f = open(path)
  lines = f.readlines()
  cta = 0
  lineCount = 0
  mca = 0
  for l in lines:
    # print(l)
    lineCount = lineCount + 1
    tabsCount = 0
    for index, c in enumerate(l):
      if (c != ' '):
        tabsCount = index
        cta = cta + tabsCount
        if (tabsCount > mca):
          mca = tabsCount
        break
    # print(str(tabsCount) + " espacos encontrados")
  if(lineCount > 0):
    cra = float(cta) / float(lineCount)
  else:
    cra = 0

  return cta, cra, mca

def getLastCommit(repo):
  commits = list(repo.iter_commits('master'))
  return commits[0]

def getYearAgoCommit(repo):
  commits = list(repo.iter_commits('master', until='2018-04-09'))
  return commits[0]

def getCommitMetrics(commit):
  index = repo.index
  index.reset(commit)
  co = index.checkout(force=True)

  maxCta = 0
  maxCra = 0
  maxMca = 0

  for file in co:
    #print(file)
    cta, cra, mca = getFileMetrics("EventBus/" + file)
    if (cta > maxCta):
      maxCta = cta
      ctaFile = file
    if (cra > maxCra):
      maxCra = cra
      craFile = file
    if (mca > maxMca):
      maxMca = mca
      mcaFile = file

  print('Commit ' + commit.hexsha +
   ' (' + time.strftime('%d/%m/%Y %H:%M:%S', time.gmtime(commit.committed_date)) + ')')
  print('O arquivo ' + ctaFile + ' possui o maior CTA neste commit (' + str(maxCta) + ')')
  print('O arquivo ' + craFile + ' possui o maior CRA neste commit (' + str(maxCra) + ')')
  print('O arquivo ' + mcaFile + ' possui o maior MCA neste commit (' + str(maxMca) + ')')


def getCommitCP(commit):
  index = repo.index
  index.reset(commit)
  co = index.checkout(force=True)

  fileCount = 0
  cp = 0

  for file in co:
    cta, cra, mca = getFileMetrics("EventBus/" + file)
    fileCount += 1
    cp += cra
  cp = cp/fileCount

  print('Complexidade do projeto no commit ' + commit.hexsha +
   ' (' + time.strftime('%d/%m/%Y %H:%M:%S', time.gmtime(commit.committed_date)) + ') : ' 
   + str(cp))

def getAllCommitsCP(repo):
  commits = list(repo.iter_commits('master'))
  for c in reversed(commits) :
    getCommitCP(c)


repo = Repo(os.getcwd() + '/EventBus')

lastCommit = getLastCommit(repo)
yearAgoCommit = getYearAgoCommit(repo)


print("--- ITEM 1 ---")
getCommitMetrics(lastCommit)

print("\n--- ITEM 2 ---")
getCommitMetrics(yearAgoCommit)

print("\n--- ITEM 3 ---")
getCommitCP(lastCommit)

print("\n--- ITEM 4 ---")
getCommitCP(yearAgoCommit)

print("\n--- ITEM 5 ---")
getAllCommitsCP(repo)