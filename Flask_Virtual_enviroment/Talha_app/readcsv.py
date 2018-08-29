import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from subprocess import check_output

def read():
    sns.set_style('whitegrid')
    laliga = pd.read_csv('F:\Python Projects\Flask_Virtual_enviroment\Talha_app\FootballEurope.csv')
    laliga['winner'] = laliga.apply(
        lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 2 if row['homeGoalFT'] < row['awayGoalFT'] else 0,
        axis=1)
    laliga = laliga[laliga.division == 'La_Liga']
    return laliga.head(100)