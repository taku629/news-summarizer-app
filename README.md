# ニュース記事要約ツール (News Summarizer Tool)

指定したニュース記事のURLから本文を抽出し、Googleの生成AIであるGemini APIを利用して内容を3行で要約するPythonプログラムです。

## ✨ 特徴 (Features)

* **URLから自動で本文抽出:** `newspaper3k`ライブラリを使用して、記事の本文テキストを自動で取得します。
* **AIによる高品質な要約:** Googleの最新モデル`gemini-1.5-flash`を利用して、自然な日本語で要約を生成します。
* **簡単な実行:** ターミナルから簡単なコマンドで実行できます。

## 🛠️ 使用技術 (Tech Stack)

* Python 3
* Google Generative AI for Python
* newspaper3k

## 使い方 (Usage)

1.  **リポジトリをクローンまたはダウンロードします。**

2.  **必要なライブラリをインストールします。**
    ```bash
    pip install -r requirements.txt
    ```

3.  **APIキーを設定します。**
    このプログラムを実行するには、Google AIのAPIキーが必要です。以下のコマンドで環境変数として設定してください。
    
    **(Windowsの場合)**
    ```bash
    set GOOGLE_API_KEY="ここにあなたのAPIキーを貼り付け"
    ```
    **(Mac/Linuxの場合)**
    ```bash
    export GOOGLE_API_KEY="ここにあなたのAPIキーを貼り付け"
    ```

4.  **プログラムを実行します。**
    ```bash
    python main.py
    ```

## 注意事項

* Webサイトの構造によっては、記事本文の抽出に失敗する場合があります。
* このコードをポートフォリオとして提出する際は、APIキーを直接コードに書き込んだり、GitHubに公開したりしないようご注意ください。
