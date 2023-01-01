import os
from pathlib import Path


class LocalConfig:
    INCLUDED_EXTENTION = [".png", ".jpg"]  # DBにいれる拡張子
    DIR_NAME = "handwriting_pics"  # 画像があるディレクトリ
