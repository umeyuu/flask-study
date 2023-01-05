# 物体検知APIの動作確認

## setup
```
$ export FLASK_APP=run.py
$ export FLASK_ENV=develpoment
$ flask run
```

## 動作確認
curlコマンドでリクエストを送る
```
$ curl -X POST http://127.0.0.1:5000/detect -H "Content-Type:application/json" -d '{"filename":"test.jpg"}'
```
APIが問題なく動作すれば、次のレスポンスが返ってくる

```
{"bicycle":98,"dog":99,"truck":84}
```
