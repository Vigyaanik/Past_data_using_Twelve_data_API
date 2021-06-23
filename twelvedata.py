import requests
from secrets import TWELVE_DATA_API_KEY
import pandas as pd
import datetime
base_url = "https://api.twelvedata.com"


# Batch requests: /time_series?symbol=AAPL,MSFT,EUR/USD,SBUX,NKE

# HTML requests example: https://api.twelvedata.com/time_series?symbol=AAPL,EUR/USD,ETH/BTC:Huobi,RY:TSX&interval=1min&apikey=your_api_key
# link = f'https://api.twelvedata.com/time_series?symbol=AAPL,EUR/USD,ETH/BTC:Huobi,RY:TSX&interval=1min&apikey={TWELVE_DATA_API_KEY}'
# r = requests.get(link)
# The key of this JSON will be the symbol passed.
# print(r.json()['AAPL'])

# Parmeters are sperated by &
# Word casing doesn't matter while passing parameters.
# Symbol might be also passed in the form symbol:exchange_name
# When the format parameter is set to CSV, additional filename parameter might be used to specify the custom name of the output file
#E.g., ?format=CSV&filename=my_own_csv_name


# link = 'https://api.twelvedata.com/stocks?symbol=AAPL'
# r = requests.get(link)
# print(r.json())

# stocks_list = ['AAPL', 'CSCO', 'AMZN', 'FB', 'SBUX', 'ZNGA', 'QCOM', 'TSLA', 'GS', 'AMD', 'MSFT', 'NVDA']
# stocks_list = ['AAPL', 'CSCO', 'AMZN', 'FB', 'TSLA', 'GS', 'MSFT', 'NVDA']
# stock_string = ""
# for each in stocks_list:
#     stock_string = stock_string + each + ','
# stock_string = stock_string[:-1]
# Link using a time interval for historical data.
# link = f'https://api.twelvedata.com/time_series?symbol={stock_string}&start_date=2021-01-01&end_date=2021-06-21&interval=1day&apikey={TWELVE_DATA_API_KEY}'
# r = requests.get(link)
# data = r.json()
# for each in data:
#     stocks_data = pd.DataFrame(data[each]['values'])
    #print(stocks_data)
    # stocks_data.to_csv(each+'.csv', index=False)


# crypto_list = ['BTC', 'ADA', 'XRP', 'DOGE']
# crypto_string = ""
# for each in crypto_list:
#     crypto_string = crypto_string + each + ','
# crypto_string = crypto_string[:-1]
#
# link = f'https://api.twelvedata.com/time_series?symbol={crypto_string}&interval=1min&apikey={TWELVE_DATA_API_KEY}'
# r = requests.get(link)
# print(r.json())
# for i in stocks_list:
#     link = f'https://api.twelvedata.com/stocks?symbol={i}'
#     r = requests.get(link)
#     print(r.json())
#     print()
def start_date_selector():
    start_date = input("Enter the start data to retrieve data in the format YYYY-MM-DD: ")
    try:
        if start_date == "":
            start_date = "1990-01-01"
        objDate = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        objDate = str(objDate)
        return objDate[:10]
    except:
        print("Wrong date format")
        start_date_selector()


def end_date_selector():
    end_date = input("Enter the end date in the format YYYY-MM-DD: ")
    try:
        if end_date == "":
            end_date = "2021-12-31"
        objDate = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        objDate = str(objDate)
        return objDate[:10]
    except:
        print("Wrong date format")
        end_date_selector()


def start_time_selector():
    start_time = input("Enter the start time in the format HH:MM:SS ")
    try:
        if start_time == "":
            start_time = "00:00:00"
        objDate = datetime.datetime.strptime(start_time, '%H:%M:%S')
        objDate = str(objDate)
        return objDate[len(objDate)-8:]
    except:
        print("Wrong date format")
        start_date_selector()


def end_time_selector():
    end_time = input("Enter the end time in the format HH:MM:SS ")
    try:
        if end_time == "":
            end_time = "23:59:59"
        objDate = datetime.datetime.strptime(end_time, '%H:%M:%S')
        objDate = str(objDate)
        return objDate[len(objDate)-8:]
    except:
        print("Wrong date format")
        start_date_selector()


def stocks_string_getter():
    stocks_string = input("Enter the symbols of all the stocks that you want to include in your results, use a ',' to separate them with no spaces: ")
    return stocks_string


def converting_stocks_string_to_list(stocks_string):
    stocks_name_list = stocks_string.split()
    return stocks_name_list


def interval_selector():
    intervals = ['1min', '5min', '15min', '30min', '45min', '1h', '2h', '4h', '8h', '1day', '1week', '1month']
    interval_select = input("Enter the interval for the data that you want to test. Choose: 1min, 5min, 15min, 30min, 45min, 1h, 24, 8h, 1day, 1week, 1month: ")
    if interval_select in intervals:
        return interval_select
    else:
        interval_selector()


def order_selector():
    orders = ['asc', 'desc']
    order = input("Enter order of data: asc or desc: ")
    if order in orders:
        return order
    else:
        order_selector()


def technical_indicator_file_reader():
    with open("techcinal_indicators_12data.csv") as data:
        data = data.read().replace('/n', '')
        data = data.split('\n')
        data[0] = data[0][3:]
        return data


def technical_indicator_selector(data):
    print("Indicators Available: ", data)
    tech_indicator = input("Please choose one of these indicators: ")
    tech_indicator = tech_indicator.upper()
    if tech_indicator in data:
        tech_indicator = tech_indicator.lower()
        return tech_indicator
    else:
        technical_indicator_selector(data)



def main():
    data_type = input("Enter time series or tech indicator: ")
    if data_type.upper() == "TIME SERIES":
        stock_string = input("Enter the symbols of all the stocks that you want to include in your results, use a ',' to separate them with no spaces: ")
        start_date = start_date_selector()
        start_time = start_time_selector()
        end_date = end_date_selector()
        end_time = end_time_selector()
        interval_selected = interval_selector()
        # order = order_selector()
        link = f'https://api.twelvedata.com/time_series?symbol={stock_string}&start_date={start_date} {start_time}&end_date={end_date} {end_time}&interval={interval_selected}&apikey={TWELVE_DATA_API_KEY}'
        r = requests.get(link)
        data = r.json()
        if stock_string.count(',') > 0:
            print(stock_string.count(','))
            for each in data:
                stocks_data = pd.DataFrame(data[each]['values'])
                print(stocks_data)
        else:
            # print(data)
            stocks_data = pd.DataFrame(data['values'])
            print(stocks_data)

    elif data_type.upper() == "TECH INDICATOR":
        tech_indicator = technical_indicator_selector(technical_indicator_file_reader())
        stock_string = input("Enter the symbols of all the stocks that you want to include in your results, use a ',' to separate them with no spaces: ")
        start_date = start_date_selector()
        start_time = start_time_selector()
        end_date = end_date_selector()
        end_time = end_time_selector()
        interval_selected = interval_selector()
        link = f'https://api.twelvedata.com/{tech_indicator}?symbol={stock_string}&start_date={start_date} {start_time}&end_date={end_date} {end_time}&interval={interval_selected}&apikey={TWELVE_DATA_API_KEY}'
        data = requests.get(link).json()
        if stock_string.count(',') > 0:
            for each in data:
                # print(each)
                stocks_data = pd.DataFrame(data[each]['values'])
                print(stocks_data)
        else:
            stocks_data = pd.DataFrame(data['values'])
            print(stocks_data)

    else:
        print("Wrong input for data type")
        main()
            # interval_select = input("Enter the interval for the data that you want to test. Choose: 1min, 5min, 15min, 30min, 45min, 1h, 24, 8h, 1day, 1week, 1month")
    # except:
    #     print("There was an error please try again")
    #     main()


# link = f'https://api.twelvedata.com/time_series?symbol={stock_string}&start_date={start_date} {start_time}&end_date={end_date} {end_time}&interval={interval_selected}&apikey={TWELVE_DATA_API_KEY}'
# r = requests.get(link)
# data = r.json()
# for each in data:
#     stocks_data = pd.DataFrame(data[each]['values'])
#     print(stocks_data)

# link = f'https://api.twelvedata.com/time_series?symbol=AAPL,TSLA&start_date=2021-01-01 00:00:00&end_date=2021-06-23 23:59:59&interval=1day&apikey={TWELVE_DATA_API_KEY}'
# r = requests.get(link)
# data = r.json()
# for each in data:
#     stocks_data = pd.DataFrame(data[each]['values'])
#     print(stocks_data)
main()
