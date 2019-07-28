# --------------------------------------------------
# Qiita APIから取得したデータの記事部分を抜き出しファイル出力
# --------------------------------------------------
import json
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import os

start = datetime.strptime(os.getenv('START_DATE'), '%Y-%m-%d')  # 開始日を設定
end = datetime.strptime(os.getenv('END_DATE'), '%Y-%m-%d')  # 終了日を設定

for i in range((end - start).days):
    today = (start + timedelta(i)).strftime('%Y-%m-%d')
    print(today)

    # データ読み込み
    with open('data/qiita_' + today + '.json') as json_data:
        articles = json.load(json_data)

        # 記事の集約
        for article in articles:
            soup = BeautifulSoup(article['rendered_body'], 'html.parser')
            # 本文の抜き出し
            sentences = soup.find_all('p')
            for sentence in sentences:
                text = sentence.text + '\n'
                # ファイル書き込み
                with open('data/qiita.txt', 'a') as f:
                    f.write(text)
