import google.generativeai as genai
from newspaper import Article
import os

# osライブラリを使って環境変数からAPIキーを読み込む
import os
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("APIキーが設定されていません。環境変数 'GOOGLE_API_KEY' を設定してください。")▲▲▲▲▲▲▲▲▲▲▲▲▲▲

# APIキーを設定
genai.configure(api_key=API_KEY)

# URLから記事を要約する関数（プログラムの本体）
def summarize_news_url(url):
    """
    URLを受け取って、記事本文を抽出し、LLMで3行に要約する関数
    """
    try:
        # 1. URLから記事をダウンロードして内容を解析
        article = Article(url)
        article.download()
        article.parse()
        
        # 記事の本文を取得
        news_text = article.text
        
        # 本文が短すぎる場合は、処理を中断してメッセージを返す
        if len(news_text) < 200: # 200文字未満の場合は失敗とみなす
            return "エラー：記事の本文をうまく取得できませんでした。Webサイトの構造が特殊か、文字数が少なすぎる可能性があります。別のURLでお試しください。"

        # 2. LLM (Gemini 1.5 Flash) のモデルを準備
        model = genai.GenerativeModel('gemini-1.5-flash')

        # 3. LLMに渡す「指示書（プロンプト）」を作成
        prompt = f"""以下のニュース記事を、最も重要なポイントを抑えて、小学生にも分かるように簡単な日本語で3行に要約してください。

        ---
        記事本文：
        {news_text}
        ---

        要約：
        """
        
        # 4. LLMにリクエストを送信して要約を生成
        response = model.generate_content(prompt)
        
        return response.text

    except Exception as e:
        return f"エラーが発生しました: {e}"

print("関数の準備が完了しました。次のセルで実際に使ってみましょう！")