def analyze_financials(data):
    ratios = {}

    try:
        ratios['ROE'] = round(data['net_income'] / data['total_equity'], 2)
        ratios['ROA'] = round(data['net_income'] / data['total_assets'], 2)
        ratios['Debt to Equity'] = round(data['total_liabilities'] / data['total_equity'], 2)
        ratios['Profit Margin'] = round(data['net_income'] / data['total_revenue'], 2)
    except (KeyError, ZeroDivisionError):
        pass

    return ratios
