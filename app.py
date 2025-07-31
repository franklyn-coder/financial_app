from flask import Flask, render_template, request
from utils.pdf_parser import extract_financial_data
from utils.financial_analysis import analyze_financials
from utils.news_fetcher import fetch_ngx_news

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    financial_data = {}
    ratios = {}
    news = []

    if request.method == 'POST':
        file = request.files['pdf']
        if file:
            raw_data = extract_financial_data(file)
            financial_data = raw_data
            ratios = analyze_financials(raw_data)
            news = fetch_ngx_news()

    return render_template('index.html', financial_data=financial_data, ratios=ratios, news=news)

if __name__ == '__main__':
    app.run(debug=True)
    
