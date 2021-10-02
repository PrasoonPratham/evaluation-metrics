Follow this guide if you would like to add new metrics or contribute to any existing metrics. The project is hosted using JupyterBook. Find out more about Jupyter book [here](https://jupyterbook.org/intro.html).

# Setting up your remote

Download the project repository and set up the build environment.

- Click the fork button in the project repository. This will create a new copy of a repo with the URL `https://gitlab.aicrowd.com/<user-name>/evaluation-metrics-book`.
- Clone the repository by running the following command:
```
git clone git@gitlab.aicrowd.com:<user-name>/evaluation-metrics-book.git
```
- Build the repository in your local computer by running the following commands:
```
cd evaluation-metrics-book
pip install -r requirements.txt
```
- Create a new remote for the upstream remote with the command:
```
git remote add upstream https://gitlab.aicrowd.com/aicrowd/evaluation-metrics-book
```

# Building the site

Start a local http server to view the site locally.

```
jupyter-book .

cd _build/html/
python -m http.server

# Now, point your browser to localhost:8000
```

# Making a contribution

- If you would like to make changes to an existing metric, edit the relevant metric in metrics/ folder. 
- Use the sample metric template `sample.MD` in the home folder to add a new metric.  
- The new metric should be added to the `metrics/` .Add the relevant images must be present to the `images/` folder. 
- Ensure that your changes are properly reflected using the build instructions in the above section. 

# Creating a Merge Request

## Adding your contributions

- Create a new branch by issuing the command:
```
git checkout -b new_metric_branch
```
- Make your changes, and add and commit them
```
git add metrics/new_metric.md
git commit -m "Add metric new_metric"
git push origin new_metric_branch
```

## Creating a merge request

- Navigate to the project repository [here](https://gitlab.aicrowd.com/aicrowd/evaluation-metrics-book).
- Use the `Create merge Request` button on the top right corner of the page and open a new merge request. 
- Choose the relevant source branch and set the target branch as `master` in `aicrowd/evaluations-metrics-book`.  
- Fill in the Title and Description appropriate to your contributions. 
- Submit your Pull Request for review. One of our project maintainers will review the merge Request, and can choose to merge it or suggest changes.

