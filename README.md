# StockSeener
    #### Video Demo:  <URL HERE>
    #### Description:
    A Python CLI tool for screening indian stocks using yfinance and financetoolkit.
    It provides access to stock Overview, Fundamentals, returns and analysis for the stocks listed on NSE and BSE.


# Features

    #### Stock Overview:

            Gives Company Full Name, current price of the stock, daily returns and overall stock Analysis (whether it is good to buy or not).

    #### Stock Fundamentals:
            It gives :

                -ROE       : Return on Equity
                -P/E ratio : price-to-earnings ratio
                -P/B ratio : Price-to-Book ratio
                -EPS       : Earnings Per Share
                -Dividend yield
                -Book-value
                -Debt-to-Equity
                -Market Cap

    #### Stock Returns:

            It gives historical returns across multiple 
            horizones (1d, 1w, 1m, 3m, 6m, 1y, 5y)

    #### Stock Analisys:

            It gives simple fundamental analysis of given stock based on 
            ROE and debt-to-equity with simple interpretation.

# Tool Structure

    StockSeener
    ├── project.py          # Main CLI tool
    ├── test_project.py     # Pytest test suite
    ├── requirements.txt    # Dependencies
    └── README.md           # Documentation



# Installation

    clone the repository and install the dependencies:

    $ git clone https://github.com/KaranGB83/StockSeener.git
    $ cd StockSeener
    $ pip install -r requirements.txt

    Optional : you can create and activate the virtual environment before installing it.

# Tech used

    #### yfinance:

        Fetches real-time and historical stock market data from Yahoo Finance.

        Docs: [text](https://pypi.org/project/yfinance) 
    
    #### pandas:

        Handles data manipulation and analysis (Series, DataFrames, returns).

        Docs: [text](https://pandas.pydata.org/docs/) 
    
    #### financetoolkit:

        Provides financial ratios and analysis tools (ROE, Debt-to-Equity, etc.).

        Docs: [text](https://github.com/JerBouma/FinanceToolkit)
    
    #### pytest:

        Testing framework used for unit tests and API-dependent checks.

        Docs: [text](https://docs.pytest.org/)
    
    #### datetime:

        Standard Python library for handling dates and time ranges.

        Docs: [text](https://docs.python.org/3/library/datetime.html)
    
    #### sys:

        Standard Python library for system-specific parameters and exit handling.

        Docs: [text](https://docs.python.org/3/library/sys.html)

    ## Notes for the API's

        #yfinance - Company details or stock data may change over time. 
                    So test relying on strings can break.
    
        #FinanceToolkit - Some ratios may not be available for the all stocks.



# Usage

## Example Runs

### 1. Stock Overview (JIOFIN.NS)

```bash
$ python project.py
=====================================================
Welcome! to Stock Seener
=====================================================

ENTER: 1
=====================================================
Enter stock quote to get current price of stock:
=====================================================

ENTER: jiofin

=====================================================
Choose Stock Exchange:
TYPE 1 FOR NSE
TYPE 2 FOR BSE
=====================================================

ENTER: 1
=====================================================
Overview of JIOFIN.NS
=====================================================

NSE SYMBOL ➨➤ JIOFIN
Full Name of Company ➨➤ Jio Financial Services Limited
Current Price ➨➤ 258.6 INR
1D Returns ➨➤ 0.0 INR (0.0%)
=====================================================



###  2. Stock Fundamentals (IRFC.BO)
$ python project.py
=====================================================
Welcome! to Stock Seener
=====================================================

ENTER: 2
=====================================================
Enter stock quote to get current price of stock:
=====================================================

ENTER: irfc

=====================================================
Choose Stock Exchange:
TYPE 1 FOR NSE
TYPE 2 FOR BSE
=====================================================

ENTER: 2
=====================================================
Fundamentals of IRFC.BO
=====================================================

Company Name ➨➤ Indian Railway Finance Corpora
ROE ➨➤ 0.12895
PE_ratio_TTM ➨➤ 20.88
EPS_TTM ➨➤ 5.36
PB_ratio ➨➤ 2.58
Dividend ➨➤ 2.29 %
Book_Value ➨➤ 43.36 Rs.
Face_val ➨➤ None
Debt_to_equity ➨➤ 744.593 Rs.
Market Cap ➨➤ 1462365847552 Rs.
=====================================================

### 3. Stock Returns (HDFCBANK.BO)
$ python project.py
=====================================================
Welcome! to Stock Seener
=====================================================

ENTER: 3
=====================================================
Enter stock quote to get current price of stock:
=====================================================

ENTER: hdfcbank

=====================================================
Choose Stock Exchange:
TYPE 1 FOR NSE
TYPE 2 FOR BSE
=====================================================

ENTER: 2
=====================================================
Returns of HDFCBANK.BO
=====================================================

5 Year Returns ➨➤ 33.02 %
1 Year Returns ➨➤ 11.81 %
6 Month Returns ➨➤ -7.16 %
3 Month Returns ➨➤ -8.72 %
1 Month Returns ➨➤ -0.47 %
1 Week Returns ➨➤ -6.73 %
1 Day Returns ➨➤ 0.00 %
=====================================================

### 4. Stock Analisys (TCS.NS)
$ python project.py
=====================================================
Welcome! to Stock Seener
=====================================================

ENTER: 4
=====================================================
Enter stock quote to get current price of stock:
=====================================================

ENTER: tcs

=====================================================
Choose Stock Exchange:
TYPE 1 FOR NSE
TYPE 2 FOR BSE
=====================================================

ENTER: 1
=====================================================
Analysis of TCS.NS by FinanceToolKit
=====================================================

If ROE is consistently rising and debt is stable or falling → positive signal.
If earnings are shrinking or debt is rising → caution.
=====================================================

ROE of TCS.NS

        2021   2022   2023   2024   2025
TCS.NS   NaN 0.8532 0.4656 0.503 0.519
=====================================================

Debt to Equity of TCS.NS

        2021  2022   2023   2024   2025
TCS.NS   NaN 0.087 0.0843 0.0878 0.0981

=====================================================

ROE Trend ➨➤ ROE is stable
Debt_to_Equity Trend ➨➤ Debt_to_Equity is stable
=====================================================

Analysis Rating ➨➤ 2.0 - Buy
=====================================================
