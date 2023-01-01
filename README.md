# flask-study

Flaskの勉強レポジトリ

`apps` : 物体検知アプリを開発

`flaskbook_api` : 物体検知アプリの機械学習モジュールのAPIを実装

`ml_api` : 手書き数字画像をロジスティクス回帰で分類するモデルのAPI実装

## 物体検知モデルを取得する

`apps/detector`配下に`model.pt`を設置する

```
(venv) $ python
>>> import torch
>>> import torchvision
>>> model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
>>> torch.save(model, "model.pt")
```

## DBマイグレート

`flask-study`がカレントディレクトリの時に以下を実行
```
(venv) $ flask db init
(venv) $ flask db migrate
(venv) $ flask db upgrade
```

## アプリケーション起動

```
(venv) $ flask run
```
