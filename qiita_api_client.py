# --------------------------------------------------
# Qiita APIから記事データを取得
# --------------------------------------------------
import requests
import json
import time
from datetime import datetime, timedelta
import os


headers = {
    'Authorization': 'Bearer ' + os.getenv('ACCESS_TOKEN')
}
start = datetime.strptime(os.getenv('START_DATE'), '%Y-%m-%d')  # 開始日を設定
end = datetime.strptime(os.getenv('END_DATE'), '%Y-%m-%d')  # 終了日を設定

# API実行
results = []
for i in range((end - start).days):
    today = (start + timedelta(i)).strftime('%Y-%m-%d')
    print(today)

    params = {
        'page': 1,
        'per_page': 100,
        'query': 'created:' + today
    }
    res = requests.get('https://qiita.com/api/v2/items',
                       params=params, headers=headers)
    results.extend(res.json())
    total_count = int(res.headers['Total-Count'])
    print('total_count: ' + str(total_count))
    print(1)
    time.sleep(3.6)  # 3600秒に1000回まで

    # １日に101件以上投稿されていた場合
    for j in range(2, total_count // 100 + 2):
        params['page'] = j
        res = requests.get('https://qiita.com/api/v2/items',
                           params=params, headers=headers)
        results.extend(res.json())
        print(j)
        time.sleep(3.6)  # 3600秒に1000回まで

    # ファイル書き込み
    with open('data/qiita_' + today + '.json', 'w') as f:
        json.dump(results, f)
    results = []
