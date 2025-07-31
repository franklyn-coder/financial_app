import pdfplumber
import re

def extract_financial_data(file):
    data = {}
    with pdfplumber.open(file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()

        fields = {
            'total_revenue': r'Total Revenue\s+([\d,\.]+)',
            'net_income': r'Net Income\s+([\d,\.]+)',
            'total_assets': r'Total Assets\s+([\d,\.]+)',
            'total_equity': r'Total Equity\s+([\d,\.]+)',
            'total_liabilities': r'Total Liabilities\s+([\d,\.]+)'
        }

        for key, pattern in fields.items():
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                data[key] = float(match.group(1).replace(',', ''))

    return data
