import pandas as pd


def get_projects():
    # Extract projects
    PROJECTS_URL = "https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/datasets/projects.csv"
    return pd.read_csv(PROJECTS_URL)


def get_tags():
    # Extract tags
    TAGS_URL = "https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/datasets/tags.csv"
    return pd.read_csv(TAGS_URL)


def get_df():
    return pd.merge(get_projects(), get_tags(), on="id")
