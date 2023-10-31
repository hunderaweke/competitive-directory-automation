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
if path.absolute() == "/home/hundera/Documents/competitve-programming":
    readme = open(f"{path.absolute()}/README.md", "a+")
    if len(untracked_files[0]) and len(untracked_files) > 1:
        for untracked_file in untracked_files:
            repo.git.add(untracked_file[0])
            logging.info(f"added: {untracked_file[0]}")
            problem_name = input("Enter the name of the problem: ")
            problem_number = input("Enter the number of the problem: ")
            problem_difficulty = input("Enter difficulty level: ")
            problem_link = input("Enter problem link: ")
            platform = input("Enter plaform: ")
            readme.write(
                f"| {problem_number}. | [{problem_name}]({problem_link}) | {problem_difficulty} | | {platform}| ||[{'Python' if 'py' in untracked_file[0] else 'C++' }](./{untracked_file[0]})|"
            )
            problem_status = input("Enter problem status: ")
            repo.git.commit(m=f"{problem_status}: {problem_name}")
    repo.git.add("README.md")
    repo.git.commit(m="updated: readme.md")
else:
    if len(untracked_files[0]):
        for untracked_file in untracked_files:
            repo.git.add(untracked_file[0])
            logging.info(f"added: {untracked_file[0]}")
            repo.git.commit(m=f"updated: {untracked_file[0]}")
logging.info("Initializing the remote origin for push")
origin = repo.remote(name="origin")
logging.info(f"origin: {origin.url}")
origin.push()
logging.info("Finished Successfully")
