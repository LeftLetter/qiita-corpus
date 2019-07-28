# --------------------------------------------------
# テキストファイルを分かち書き
# --------------------------------------------------
import os
import MeCab


# データ読み込み
with open('data/qiita.txt') as text_data:
    tagger = MeCab.Tagger(
        '-Owakati -b ' + os.getenv('MECAB_BUFFER') + ' -d ' + os.getenv('MECAB_DIC_PATH'))
    line = text_data.readline()
    while line:
        # 分かち書き
        result = tagger.parse(line)
        line = text_data.readline()
        if result != None:
            # ファイル書き込み
            with open('data/qiita_wakati.txt', 'a') as f:
                f.write(result)
