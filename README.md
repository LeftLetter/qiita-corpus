# qiita_corpus

## 必要なもの
* pipenv
* MeCab

## 環境変数
.envに以下を設定しておいてください。
* ACCESS_TOKEN  
Qiita APIにアクセスするためのアクセストークン
* START_DATE  
記事取得開始日
* END_DATE  
記事取得終了日
* MECAB_DIC_PATH  
MeCabの辞書のパス
* MECAB_BUFFER  
MeCab実行時のバッファサイズ

## 実行方法
### 環境構築
```
pipenv install 
```
### 実行
```
pipenv run api
pipenv run text
pipenv run wakati
pipenv run pre
pipenv run model
pipenv run similar
```
