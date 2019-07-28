# --------------------------------------------------
# Qiita APIからタグ一覧を取得
# --------------------------------------------------
import requests
import json
import time


headers = {
    'Authorization': 'Bearer dfa3ba2a623d5b09d4de7fcdaf50d7b6f033dfde'
}

# API実行
json_list = []
for i in range(1, 937):
    print('start ' + str(i))
    params = {
        'page': str(i),
        'per_page': 100,
        'sort': 'count'
    }

    res = requests.get('https://qiita.com/api/v2/tags',
                       params=params, headers=headers, verify=True)  # 社内だとFalse
    json_list.extend(res.json())
    time.sleep(3.6)  # 3600秒に1000回まで

# ファイル書き込み
with open('data/qiita_tag.json', 'a') as f:
    json.dump(json_list, f)
