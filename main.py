import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    start_date = input("Введите дату начала периода (например, '2020-01-01'): ")
    end_date = input("Введите дату окончания периода (например, '2020-12-31'): ")



    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, start_date, end_date)


    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, start_date, end_date)

def notify_if_strong_fluctuations(data, threshold):




if __name__ == "__main__":
    main()
   
