# News Summarizer Tool

A Python program that extracts the body text from a given news article URL and uses Google's Gemini API to summarize it in three lines.

## ✨ Features

* **Automatic Text Extraction:** Uses the `newspaper3k` library to automatically fetch the article's body text from a URL.
* **High-Quality AI Summarization:** Utilizes Google's latest model, `gemini-1.5-flash`, to generate a natural summary.
* **Simple Execution:** Can be run from the terminal with a simple command.

## 🛠️ Tech Stack

* Python 3
* Google Generative AI for Python
* newspaper3k

## Usage

1.  **Clone or download the repository.**

2.  **Install the required libraries.**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your API key.**
    To run this program, you need a Google AI API key. Set it up as an environment variable using the commands below.

    **(For Windows)**
    ```bash
    set GOOGLE_API_KEY="Paste your API key here"
    ```
    **(For Mac/Linux)**
    ```bash
    export GOOGLE_API_KEY="Paste your API key here"
    ```

4.  **Run the program.**
    ```bash
    python summarize_tool.py
    ```

## Notes

* Depending on the website's structure, extracting the article body may fail.
* When submitting this code as part of your portfolio, please be careful not to hardcode your API key directly into the code or expose it on GitHub.
