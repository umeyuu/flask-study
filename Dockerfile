# ベースイメージの指定
FROM python:3.9

# apt-getのversionを更新し、SQLite3のインストール
RUN apt-get update && apt-get install -y sqlite3 && apt-get install -y libsqlite3-dev

# コンテナ上のワーキングディレクトリの指定
WORKDIR /user/src/

# ディレクトリとファイルのコピー
COPY ./apps /user/src/apps
COPY ./local.sqlite /user/src/local.sqlite
COPY ./requirements.txt /user/src/requirements.txt

# pipのversionの更新
RUN pip install --upgrade pip

# pytorchのインストール
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

RUN pip install -r requirements.txt

RUN echo "building..."

# 必要な各環境変数を設定
ENV FLASK_APP "apps.app:create_app('local')"
ENV IMAGE_URL "/storage/images"

# 特定のネットワーク・ポートをコンテナが実行時にリッスン
EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0"]
