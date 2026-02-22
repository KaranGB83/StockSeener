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



# Usage:

## Example Run

```bash
$ python project.py
=====================================================
Welcome! to Stock Seener
Screener for Indian Stock Market
Choose One Option to get started
Option 1: Stock Overview
Option 2: Stock Fundamentals
Option 3: Stock Returns
Option 4: Stock Analysis
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

Obtaining financial statements: 100%|████████████████████████████████████████████████████████████████████████████████| 3/3 [00:04<00:00,  1.64s/it]
Obtaining historical data: 100%|█████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00,  9.72it/s]
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
