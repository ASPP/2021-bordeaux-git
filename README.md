# git

## Warm-Up
- how to start a repo from scratch?
    - `git init` local method
    - on GitHub `git clone` and either `git push --force` or `git pull` methods
- how to revert mistakes?
    - `git revert` vs. …
    - `git reset` vs. …
    - `git reset --hard` vs. …
    - `git restore`
- how to go to a specific point in history?
    - `git checkout SHA` ⟶ `DETACHED HEAD` problem
    - interaction with branches
- `git gui`: building commits along the way interactively (for the *mess around* type of workflows)

## The Open Source model
- remotes: `pull`, `push`, `fetch`, `merge`
- GitHub: forks, branches and PRs: important ➔ explain fork vs. clone!!!
- strategies for keeping your fork up-to-date: your `main` and upstream's `main`, short-lived and long-lived topic branches
- a more thorough and detailed explanation can be found on the [Numpy Contributor's Guide](https://docs.scipy.org/doc/numpy/dev/gitwash/index.html). This guide can be adapted to your own needs, see [gitwash](https://github.com/matthew-brett/gitwash).
