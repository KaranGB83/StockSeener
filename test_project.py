import pytest
import project
import pandas as pd


#test which can fail in future due to API updates
def test_get_current_stock_overview_name():
    name = project.get_current_stock_overview("IRFC.NS")
    assert name["Name"] == "Indian Railway Finance Corporation Limited"


def test_get_current_stock_fundamentals_name():
    name = project.get_current_stock_fundamentals("IRFC.NS")
    assert name["short_name"] == "INDIAN RAILWAY FIN CORP L"


def test_validate_stock():
    assert project.validate_stock("503681.NS") == None
    assert project.validate_stock("512026.NS") == None

#test which cannot fail in future due to API updates
def test_analize_trend():
    assert project.analize_trend(pd.Series([9,8,7,5,4]), "test") == "test trend is unavailable"

def test_safe_decimal():
    assert project.safe_decimal("two")  == 'N/A'
    assert project.safe_decimal(3.142857142857143)  == 3.14
