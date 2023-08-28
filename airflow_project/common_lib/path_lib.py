import pandas as pd
import os
from airflow_project.project_settings import BASE_PATH
import datetime
import logging
import json

logger = logging.getLogger(__name__)


def create_path():
    """
    Create folders to save arquives.
    """
    arquive_folder = os.path.join(BASE_PATH, 'arquives')
    today = datetime.date.today().strftime('%Y_%m_%d')
    path = os.path.join(arquive_folder, today)
    if not os.path.exists(path):
        os.makedirs(path)
        return path
    return path


def get_path():
    """
    Return path to save arquives.
    """
    arquive_folder = os.path.join(BASE_PATH, 'arquives')
    today = datetime.date.today().strftime('%Y_%m_%d')
    path = os.path.join(arquive_folder, today)
    return path


def create_file_path(filename) -> str:
    """
    Create path to save arquives.
    """
    path = create_path()
    hour = datetime.datetime.now().strftime('%H_%M')
    file_path = os.path.join(path, f'{filename}_{hour}.csv')
    return file_path


def data_to_file(data, filename: str) -> str:
    """
    ### Save dataframe to csv file

    ##### Params:
    :param df: Dataframe
    :param filename: Filename

    :return: None

    ##### Usage:
    ```python
    instance = Service()
    whater_response = instance.whater('São Paulo', 2)
    instance.data_to_file()
    ```
    """
    if isinstance(data, str):
        data = eval(data)
        print(data)
        print(type(data))
    df = pd.DataFrame(data)
    filename = create_file_path(filename)
    df.to_csv(filename, index=False)
    return filename
