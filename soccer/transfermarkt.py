import requests
from bs4 import BeautifulSoup
import pandas as pd

from utils.scraping import get_headers

def get_most_valueable_players():

    response = requests.get('https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop', headers=get_headers())
    df = pd.read_html(response.text)[1].rename({'#': 'rank'}, axis=1)
    df = df.dropna(subset=['rank'])
    df = df.drop(columns=['Nat.', 'club'])
    df[['rank', 'Age']] = df[['rank', 'Age']].astype(int)
    df['Player'] = df['Player'].str.replace('Centre', '').str.replace('Left', '').str.replace('Right', '').str.replace('Winger', '').str.replace('Midfield', '')
    df['Player'] = df['Player'].str.replace('Attacking', '').str.replace('Defensive', '').str.replace('Central', '').str.replace('Back', '').str.replace('-', ' ').str.strip()

    return df