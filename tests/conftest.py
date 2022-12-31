import os
import shutil

import pytest

from apps.app import create_app, db
from apps.crud.models import User
from apps.detector.models import UserImage, UserImageTag


@pytest.fixture
def fixture_app():
    app = create_app("testing")

    # データベースを利用するための宣言
    app.app_context().push()

    # テスト用のデータベースのテーブルを作成
    with app.app_context():
        db.create_all()

    # テスト用の画像アップロード先
    os.mkdir(app.config["UPLOAD_FOLDER"])

    # テストを実行
    yield app

    # クリーンナップ処理
    # テーブルのレコードを削除
    User.query.delete()
    UserImage.query.delete()
    UserImageTag.query.delete()

    # テスト用の画像アップロード先を削除
    shutil.rmtree(app.config["UPLOAD_FOLDER"])

    db.session.commit()


@pytest.fixture
def client(fixture_app):
    return fixture_app.test_client()
