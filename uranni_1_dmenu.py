import tls_client
from bs4 import BeautifulSoup
import re
import json
import boto3

#下準備
session = tls_client.Session(
    client_identifier="chrome112",
    random_tls_extension_order=True
)
url = "https://service.smt.docomo.ne.jp/portal/fortune/src/fortune_ranking.html"
response = session.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#絞り込み
ele = str(soup.find(class_='postRank__list'))
ele_add = str(soup.find(class_='rankTggl'))
ele = ele.__add__(ele_add)

za_pattern = re.compile('alt=".*座"')
za = re.findall(za_pattern,str(ele))
za_sub1 = 'alt="'
za_sub2 = '"'
za = re.sub(za_sub1,"",str(za))
za = re.sub(za_sub2,"",str(za))
za = za.replace('[', '').replace(']', '').replace("'", '')
za = za.split(', ')

i_pattern = re.compile('alt=".*位"')
i = re.findall(i_pattern,str(ele))
i_sub1 = 'alt="'
i_sub2 = '位"'
i = re.sub(i_sub1,"",str(i))
i = re.sub(i_sub2,"",str(i))
i = i.replace('[', '').replace(']', '').replace("'", '')
i = i.split(', ')

url_pattern = re.compile('href=".*"')
url = re.findall(url_pattern,str(ele))
url_sub1 = 'href="'
url_sub2 = '"'
url = re.sub(url_sub1,"",str(url))
url = re.sub(url_sub2,"",str(url))
url = url.replace('[', '').replace(']', '').replace("'", '')
url = url.split(', ')
urls = []
for url in url:
    urlx = "https://service.smt.docomo.ne.jp/portal/fortune/src/" + str(url)
    urls.append(urlx)

zodiac_data = []

for zodiac, rank, link in zip(za, i, urls):
    zodiac_data.append({
        'zodiac': zodiac,
        'rank': rank,
        'link': link
    })

#rankをint型に直す
def convert_rank_to_int(rank):
    try:
        return int(rank)
    except ValueError:
        return 0  # エラーが発生した場合は0を返す
        
for data in zodiac_data:
    data['rank'] = convert_rank_to_int(data['rank'])

print(zodiac_data)
#jsonで出力
s3 = boto3.resource('s3')

def lambda_handler(event, context):
    
    bucket = 'lineuranaibucket' # バケット名
    key = 'line_uranai_1.json'
    contents = json.dumps(zodiac_data)
    
    obj = s3.Object(bucket,key)
    obj.put(Body=contents)
    return

#pandasで出力
"""
import pandas as pd
df_1 = pd.DataFrame(zodiac_data, columns=['zodiac', 'rank', 'link'])
print(df_1)
"""