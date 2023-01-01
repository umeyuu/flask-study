import os
from pathlib import Path

basedir = Path(__file__).parent.parent


class LocalConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(basedir, "images.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    INCLUDED_EXTENTION = [".png", ".jpg"]  # DBにいれる拡張子
    DIR_NAME = "handwriting_pics"  # 画像があるディレクトリ
