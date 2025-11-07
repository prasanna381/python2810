import pandas as pd
import re
from bs4 import BeautifulSoup
from tqdm import tqdm




# Load Dataset
data_frame = pd.read_csv('IMDB Dataset.csv')

print(data_frame.head(10))

