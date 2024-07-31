# Git Reset Command

The `git reset` command is used to reset the current branch to a specific state. It has different modes, including \
`--soft`, `--mixed`, and `--hard`, which determine the extent of changes that are undone.

## `--soft` Option

### Command Used:
```bash
git reset --soft HEAD~1
```
  - Moves the HEAD pointer to the specified commit, but does not modify the index or working directory.
  - In my repository my remote origin/main pointer was in the latest commit just my local HEAD moved to previous commit

## `--mixed` Option
### Command Used:
```bash
git reset --mixed HEAD~1
```
  - Resets the index to the specified commit, but does not affect the working directory.
  - In my case Local head moved to the previous commit as well as All modified filed was unstaged at the same time

## `--hard` Option
### Command Used:
```bash
git reset --hard HEAD~1
```
  - Resets the index and working directory to the specified commit, discarding all changes.
  - In my case the newly added file named "intermediate_program.py" got deleted from my working directory and now i only have that file in remote repository
