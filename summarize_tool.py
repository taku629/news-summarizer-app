import google.generativeai as genai
from newspaper import Article
import os

# Use the os library to read the API key from an environment variable
import os
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("API key is not set. Please set the 'GOOGLE_API_KEY' environment variable.")

# Configure the API key
genai.configure(api_key=API_KEY)

# Function to summarize an article from a URL (the main part of the program)
def summarize_news_url(url):
    """
    A function that takes a URL, extracts the article body, 
    and summarizes it into three lines using an LLM.
    """
    try:
        # 1. Download and parse the article from the URL
        article = Article(url)
        article.download()
        article.parse()
        
        # Get the article's body text
        news_text = article.text
        
        # If the body text is too short, stop processing and return a message
        if len(news_text) < 200: # Treat as failure if less than 200 characters
            return "Error: Could not retrieve the article body successfully. The website's structure might be unusual, or the text content may be too short. Please try a different URL."

        # 2. Prepare the LLM model (Gemini 1.5 Flash)
        model = genai.GenerativeModel('gemini-1.5-flash')

        # 3. Create the prompt (instructions) to pass to the LLM
        prompt = f"""Please summarize the following news article into three simple lines, capturing the most important points as if you were explaining it to a grade school student.

        ---
        Article Text:
        {news_text}
        ---

        Summary:
        """
        
        # 4. Send the request to the LLM to generate the summary
        response = model.generate_content(prompt)
        
        return response.text

    except Exception as e:
        return f"An error occurred: {e}"

print("Function is ready. Let's try using it in the next cell!")
