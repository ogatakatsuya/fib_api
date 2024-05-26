# Flask REST API with Flask-RESTX

このプロジェクトは、PythonのフレームワークであるFlaskを用いて実装されたREST APIです。Flask-RESTXライブラリを使用してREST APIを構築しました。

## 概要

- **フレームワーク**: Flask
- **REST API**: Flask-RESTX
- **テスト**: Pytest
- **デプロイ**: Heroku
- **環境構築**: Docker
- **CI/CD**: GitHub Actions

### 構成

- `Dockerfile`: アプリケーションのDockerイメージを構築するための設定ファイル。
- `README.md`: プロジェクトの概要と設定方法を説明するドキュメント。
- `app.py`: Flaskアプリケーションのエントリーポイント。
- `docker-compose.yml`: 複数のDockerコンテナを一括で管理するための設定ファイル。
- `heroku.yml`: Herokuにデプロイするための設定ファイル。
- `pytest.ini`: Pytestの設定ファイル。
- `requirements.txt`: プロジェクトで必要なPythonパッケージを記載したファイル。
- `src/`: ソースコードを格納するディレクトリ。
  - `fib.py`: アプリケーションの主要なロジックを含むモジュール。
- `test/`: テストコードを格納するディレクトリ。
  - `test_main.py`: アプリケーションのテストコード。

## 環境構築

1. リポジトリをクローンします。
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

1. Dockerコンテナをビルドして起動します。
    ```sh
    docker-compose up --build
    ```

2. アプリケーションにアクセスします。
    - ローカル環境では、 `http://localhost:5000` にアクセスできます。

## テスト

Pytestを用いてテストを実行します。

1. Dockerコンテナ内でテストを実行します。
    ```sh
    docker-compose run fib_api pytest
    ```

テスト結果はGitHub ActionsによりPR作成時に自動で実行され、コメントとして反映されます。

## CI/CD

GitHub Actionsを用いて、以下のCI/CDパイプラインを実現しています。

- PR作成時に自動でテストを実行
- テスト結果をPRのコメントに反映
- デプロイ用のDockerイメージをビルドし、Herokuに自動デプロイ

ワークフローファイルは `.github/workflows/` に配置されています。

## コンタクト

質問やフィードバックがあれば、`katsuya151225@icloud.com` までご連絡ください。
