from financetoolkit import Toolkit
import yfinance as yf
import pandas as pd
import datetime
import sys
import json

def main():
    print("=====================================================")
    print("Welcome! to Stock Seener")
    print("Screener for Indian Stock Market")
    print("Choose One Option to get started")
    print("Option 1: Stock Overview")
    print("Option 2: Stock Fundamentals")
    print("Option 3: Stock Returns")
    print("Option 4: Stock Analisis")
    print("=====================================================\n")

    while True:
        choice = get_int("ENTER: ")
        if choice in [1,2,3,4]:
            break
        else:
            print("Invalid Input Enter a Valid Number (1-4)")
        
        
    
    print("=====================================================")
    print("Enter stock quote to get current price of stock: ")
    print("=====================================================\n")
    d = input("ENTER: ").strip().upper()
    print()
    print("=====================================================")
    print("Choose Stock Exchange: ")
    print("TYPE 1 FOR NSE")
    print("TYPE 2 FOR BSE")
    print("=====================================================\n")
    
    while True:
        exc = get_int("ENTER: ")
        if exc == 1:
            quote = f"{d}.NS"
            break
        elif exc == 2:
            quote = f"{d}.BO"
            break
        else:
            print("Enter 1 for NSE or 2 for BSE")

    match choice:
        case 1:
            data1 =get_current_stock_overview(quote)
            if data1 is None:
                sys.exit(f"Error while fetching stock overview")

            print("=====================================================")
            print(f"Overview of {quote}")
            print("=====================================================\n")
            print(f'{data1["Exchange_Name"]} SYMBOL ➨➤ {data1["quote"]}')
            print(f'Full Name of Company ➨➤ {data1["Name"]}')
            print(f'Current Price ➨➤ {data1["Price"]} {data1["fin_currency"]}')
            print(f'1D Returns ➨➤ {safe_decimal(data1["1d_return_inr"])} {data1["fin_currency"]} ({safe_decimal(data1["1d_return_per"])}%)')
            print("=====================================================")
            print("=====================================================\n")
        case 2:
            data2 =get_current_stock_fundamentals(quote)
            
            if data2 is None:
                sys.exit(f"Error while fetching stock fundamentals")

            print("=====================================================")
            print(f"Fundamentals of {quote}")
            print("=====================================================\n")
            print(f'Company Name ➨➤ {data2["short_name"]} ')
            print(f'ROE ➨➤ {data2["ROE"]} ')
            print(f'PE_ratio_TTM ➨➤ {safe_decimal(data2["PE_ratio_TTM"]) if data2["PE_ratio_TTM"] else "N/A"}  ')
            print(f'EPS_TTM ➨➤ {data2["EPS_TTM"]} ')
            print(f'PB_ratio ➨➤ {safe_decimal(data2["PB_ratio"])} ')
            print(f'Divident ➨➤ {data2["Divident"]} %')
            print(f'Book_Value ➨➤ {safe_decimal(data2["Book_Value"])} Rs.')
            print(f'Face_val ➨➤ {data2["Face_val"]} ')
            print(f'Debt_to_equity ➨➤ {data2["Debt_to_equity"]} Rs.')
            print(f'Market Cap ➨➤ {data2["Mkt_cap"]} Rs.')
            print("=====================================================")
            print("=====================================================\n")
        case 3:
            horizons = {"5 Year": 5*365, "1 Year": 365, "6 Month": 182, "3 Month": 91, "1 Month": 30, "1 Week": 49, "1 Day": 1}
            print("=====================================================")
            print(f"Returns of {quote}")
            print("=====================================================\n")
            for label, days in horizons.items():
                ret = get_current_stock_returns(quote, days)
                if ret is None:
                    print(f"{label} Returns ➨➤ No Data Available")
                else:
                    print(f"{label} Returns ➨➤ {ret:.2f} %")
            print("=====================================================")
            print("=====================================================\n")
        case 4:
            print("=====================================================")
            print(f"Analysis of {quote} by FinanceToolKit")
            print("=====================================================\n")
            data=get_analysis(quote)
            data1 =get_current_stock_overview(quote)

            if "error" in data:
                return f"Analysis Unavailable fo {data["error"]}"
            else:
                print("=====================================================\n")
                print("If ROE is consistently rising and debt is stable or falling → positive signal.")
                print("If earnings are shrinking or debt is rising → caution.")
                print("=====================================================\n")
                print(f'ROE of {quote.upper()}\n')
                print(f'{data["ROE"]}')
                print("=====================================================\n")
                print(f'Debt to Equity of {quote.upper()}\n')
                print(f'{data["Debt_to_Equity"]}\n')
                print("=====================================================\n")
                print(f'ROE Trend ➨➤ {analize_trend(data["ROE"], "ROE")}')
                print(f'Debt_to_Equity Trend ➨➤ {analize_trend(data["Debt_to_Equity"], "Debt_to_Equity")}')
                print("=====================================================\n")
                print(f'Analysis Rating ➨➤ {data1["analysis_rating"]}')
                print("=====================================================\n")

    # print(**data1)
    
    
def get_current_stock_overview(quote):

    stock_info = validate_stock(quote)
    if not stock_info:
        return None 

    exchange_name = stock_info.get("fullExchangeName")
    full_name = stock_info.get("longName")
    symbol=stock_info.get("symbol")
    stock_quote = symbol.replace(".NS", "").replace(".BO", "")
    regular_price = stock_info.get("regularMarketPrice")
    financial_currency = stock_info.get("financialCurrency")
    one_day_return_perc = stock_info.get("regularMarketChangePercent")
    one_day_return_inr = stock_info.get("regularMarketChange")
    analysis_rating = stock_info.get("averageAnalystRating")
    return {
        "quote":stock_quote,
        "Exchange_Name":exchange_name,
        "Name": full_name,
        "Price" : regular_price,
        "fin_currency":financial_currency,
        "1d_return_per" : one_day_return_perc,
        "1d_return_inr" : one_day_return_inr,
        "analysis_rating" :analysis_rating
    }


def get_current_stock_fundamentals(quote):

    stock_info = validate_stock(quote)
    if not stock_info:
        return None

    short_name = stock_info.get("shortName")
    Mkt_cap = stock_info.get("marketCap")
    ROE = stock_info.get("returnOnEquity")
    PE_ratio = stock_info.get("trailingPE")
    EPS_TTM = stock_info.get("epsTrailingTwelveMonths")
    PB_ratio = stock_info.get("priceToBook")
    Div = stock_info.get("dividendYield")
    Div_yield = Div if Div is not None else None
    Book_Value = stock_info.get("bookValue")
    Debt_to_equity = stock_info.get("debtToEquity")
    Face_val = stock_info.get("faceValue")
    
    return {
        "short_name": short_name,
        "Mkt_cap" :  Mkt_cap,
        "ROE" :  ROE,
        "PE_ratio_TTM" :  PE_ratio,
        "EPS_TTM" :  EPS_TTM,
        "PB_ratio" :  PB_ratio,
        "Divident" :  Div_yield,
        "Book_Value" : Book_Value,
        "Debt_to_equity" :  Debt_to_equity,
        "Face_val" : Face_val
    }
    
    
def get_current_stock_returns(quote:str, tFilter:int):
    end = datetime.date.today()
    start = end - datetime.timedelta(days=tFilter)

    try:
        stock_info = yf.download(quote, start=start, end=end)
    except Exception as e:
        print(f"Error fetching data {e}")
        return None

    if stock_info.empty:
        return None

    if "Adj Close" in stock_info.columns: 
        AdjClose = stock_info["Adj Close"] 
    elif "Close" in stock_info.columns: 
        AdjClose = stock_info["Close"] 
    else: 
        raise KeyError("Neither 'Adj Close' nor 'Close' found in data")

    startP = AdjClose.iloc[0]
    endP = AdjClose.iloc[-1]
    ret = ((endP - startP)/startP)*100

    if isinstance(ret, pd.Series):
        ret = ret.iloc[0]

    return float(ret)

def get_analysis(stock):
    toolkit = Toolkit(stock)

    try:
        # Return on Equity 
        roe = toolkit.ratios.get_return_on_equity() 
        # Debt-to-Equity 
        de_ratio = toolkit.ratios.get_debt_to_equity_ratio() 
    except Exception as e:
        return {"error": f"failed analysis {e}"}

    return {"ROE": roe.tail(), "Debt_to_Equity": de_ratio.tail(1)}     


#================Helper Functions=======================
def validate_stock(s):
    try:
        st = yf.Ticker(s)
        info = st.info
    except Exception:
        return None
    
    if not info or info.get("symbol") is None:
        return None
    return info


def get_int(prompt:str):
    while True:
        try:
            n = int(input(prompt))
        except ValueError:
            print("Invalid Input. Enter a number")
        else:
            break
    return n




def analize_trend(series, metric):
    try:
        if series.empty or series.shape[1] < 2 or len(series.iloc[0]) < 2:
            return f"{metric} has insufficient data"

        first = series.iloc[0].values[0]
        last = series.iloc[-1].values[0]

        if last > first:
            return f"{metric} is Rising"
        elif last < first:
            return f"{metric} is falling"
        else:
            return f"{metric} is stable"
    except Exception as e:
        return f"{metric} trend is unavailable"


def safe_decimal(s, n=2):
    if isinstance(s, (int, float)):
        return round(s, n)
    return 'N/A'

if __name__=="__main__":
    main()