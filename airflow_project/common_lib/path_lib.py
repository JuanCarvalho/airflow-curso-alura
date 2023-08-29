import pandas as pd
import os
from airflow_project.project_settings import BASE_PATH
import datetime
import logging

logger = logging.getLogger(__name__)


def create_path(folder):
    """
    Create folders to save arquives.
    """
    arquive_folder = os.path.join(BASE_PATH, 'arquives')
    path_create = os.path.join(arquive_folder, folder)
    today = datetime.date.today().strftime('%Y_%m_%d')
    path = os.path.join(path_create, today)
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


def create_file_path(filename, folder) -> str:
    """
    Create path to save arquives.
    """
    path = create_path(folder)
    hour = datetime.datetime.now().strftime('%H_%M')
    file_path = os.path.join(path, f'{filename}_{hour}.csv')
    return file_path


def data_to_file(data, filename: str, folder: str) -> str:
    """
    ### Save to csv file
    """
    if isinstance(data, str):
        data = eval(data)
    df = pd.DataFrame(data)
    filename = create_file_path(filename, folder)
    df.to_csv(filename, index=False)
    return filename
