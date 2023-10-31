import os
from git import Repo


path = os.getenv("DIR")
repo = Repo(path)
untracked_files = [i.split()[1:] for i in repo.git.status("--porcelain").split("\n")]
for untracked_file in untracked_files:
    repo.git.add(f=untracked_file[0])
    print(untracked_file)
    repo.git.commit(m=f"added: {untracked_file}")
origin = repo.remote(name="origin")
origin.push()
