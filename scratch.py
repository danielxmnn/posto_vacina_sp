import requests
import pandas as pd

headers = {
    'Host': 'deolhonafila.prefeitura.sp.gov.br',
    'Sec-Ch-Ua': '\\"Chromium\\";v=\\"91\\", \\" Not;A Brand\\";v=\\"99\\"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close',
}
body = {
    'dados': 'dados'
}
response = requests.post('https://deolhonafila.prefeitura.sp.gov.br/processadores/dados.php', headers=headers,
                         data=body, verify=True)
with open("response.json", "w", encoding='utf-8') as f:
    f.write(response.text)
df = pd.read_json(r'response.json')
df.to_csv(r'response.csv', index=None)
