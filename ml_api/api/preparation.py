import os
import sqlite3
import uuid
from pathlib import Path

from api.models import ImageInfo, db
from flask import abort, current_app, jsonify
from sqlalchemy.exc import SQLAlchemyError

dbname = "images.db"  # DBの名前


# 手書き文字画像が置いてあるパスからファイル名を取得し、リストを作成
def load_filenames(dir_name: str) -> list[str]:
    included_ext = current_app.config["INCLUDED_EXTENTION"]
    dir_path = Path(__file__).parent.parent / dir_name
    files = Path(dir_path).iterdir()
    filenames = sorted(
        [Path(file).name for file in files if Path(file).suffix in included_ext]
    )

    return filenames


# 手書き文字画像のファイル名をデータベースに保存
def insert_filenames(request) -> tuple:
    dir_name = request.json["dir_name"]
    filenames = load_filenames(dir_name)
    file_id = str(uuid.uuid4())
    for filename in filenames:
        db.session.add(ImageInfo(file_id=file_id, filename=filename))
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        abort(500, {"error_message": str(e)})
    return jsonify({"file_id": file_id}), 201


# 手書き文字画像のファイル名をデータベースから取得
def extract_filenames(file_id: str) -> list[str]:
    img_obj = db.session.query(ImageInfo).filter(ImageInfo.file_id == file_id)
    filenames = [img.filename for img in img_obj if img.filename]
    if not filenames:
        return (
            jsonify({"message": "filenames are not found in database", "result": 400}),
            400,
        )
    return filenames
