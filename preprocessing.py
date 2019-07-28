# --------------------------------------------------
# 分かち書きされたテキストの前処理
# --------------------------------------------------
import os
import re
import jaconv


# データ読み込み
with open('data/qiita_wakati.txt') as wakati_data:
    data = wakati_data.read()
    # 大文字→小文字
    data = data.lower()
    # 半角→全角
    data = jaconv.h2z(data)
    # 記号（-など）の正規化
    data = jaconv.normalize(data)
    # 数字の置き換え
    data = re.sub(r'[0-9]+', '0', data)

    # ファイル書き込み
    with open('data/qiita_corpus.txt', 'w') as f:
        f.write(data)
