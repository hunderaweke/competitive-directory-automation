from pathlib import Path
from git import Repo

path = Path()
repo = Repo(path.absolute())
untracked_files = repo.untracked_files
for untracked_file in untracked_files:
    repo.git.add(f=untracked_file)
    repo.git.commit(m=f"added: {untracked_file}")
repo.git.push()