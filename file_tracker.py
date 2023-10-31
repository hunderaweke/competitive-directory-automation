#!/usr/bin/python
import logging
from pathlib import Path
from git import Repo

logging.basicConfig(level=logging.INFO)
path = Path()
repo = Repo(path.absolute())
logging.info(f"repository : {repo}")
untracked_files = [i.split()[1:] for i in repo.git.status("--porcelain").split("\n")]
logging.info(f"untracked_files: {untracked_files}")
if len(untracked_files[0]):
    for untracked_file in untracked_files:
        repo.git.add(untracked_file[0])
        logging.info(f"added: {untracked_file[0]}")
        repo.git.commit(m=f"added: {untracked_file[0]}")
logging.info("Initializing the remote origin for push")
origin = repo.remote(name="origin")
logging.info(f"origin: {origin.url}")
origin.push()
