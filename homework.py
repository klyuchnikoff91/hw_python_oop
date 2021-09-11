import datetime as dt


class Calculator:
    def __init__(self, limit: float):
        self.limit = limit
        self.records: list[object] = list()

    def add_record(self, record: object):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.date.today()
        today_amount = 0
        for r in self.records:
            if (dt.date(r.timestamp) == today):
                today_amount += r.amount
        return today_amount

    def get_week_stats(self):
        today = dt.datetime.now()
        start_dow = dt.date(today - dt.timedelta(7))
        week_amount = 0
        for r in self.records:
            if ((r.timestamp <= today) and (r.timestamp >= dt.datetime(start_dow))):
                week_amount += r.amount
        return week_amount


class Record:
    def __init__(self,
                 amount: float,
                 comment: str,
                 timestamp = dt.datetime.now()) -> None:
        try:
            self.amount = float(amount)
            self.comment = str(comment)
            date_format = '%d.%m.%Y'
            if (type(timestamp) is str):
                self.timestamp = dt.datetime.strptime(timestamp, date_format)  # Парсим строку в заданный формат
            elif isinstance(timestamp, dt.datetime):
                self.timestamp = timestamp
            else:
                raise ValueError  # Показываем ошибку, другие форматы не принимаем
        except ValueError:
            print('Запись не верна')


class CashCalculator(Calculator):
    def get_today_cash_remained(currency):
        USD_RATE = 73.13
        EUR_RATE = 86.47
        balance = super().limit - super().get_today_stats()
        format_str_currency = "руб"
        if (currency == 'usd'):
            balance *= USD_RATE
            format_str_currency = "USD"
        elif (currency == 'eur'):
            balance *= EUR_RATE
            format_str_currency = "Euro"
        if balance > 0:
            return f"На сегодня осталось {balance} {format_str_currency}"
        elif balance == 0:
            return "Денег нет, держись"
        else:
            return f"Денег нет, держись: твой долг - {balance} {format_str_currency}"


class CaloriesCalculator(Calculator):
    def get_calories_remained():
        balance = super().limit - super().get_today_stats()
        if (balance > 0):
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {balance} кКал"
        else:
            return "Хватит есть!"
