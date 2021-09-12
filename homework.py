import datetime as dt


class Calculator:
    """Калькулятор."""
    def __init__(self, limit: float):
        self.limit = limit
        self.records = list()

    def add_record(self, record: object):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.date.today()
        today_amount = sum(iter.amount for iter in self.records
                           if iter.date == today)
        return today_amount

    def get_week_stats(self):
        today = dt.date.today()
        start_dow = today - dt.timedelta(days=7)
        week_amount = sum(iter.amount for iter in self.records
                          if start_dow < iter.date <= today)
        return week_amount

    def get_balance(self):
        return self.limit - self.get_today_stats()


class Record:
    """Структура, хранящая записи калькуляторов."""
    def __init__(self,
                 amount,
                 comment,
                 date=None):
        date_format = '%d.%m.%Y'
        if (date is None):
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, date_format).date()
        self.amount = amount
        self.comment = comment


class CashCalculator(Calculator):
    """Ещё калькулятор"""
    USD_RATE = 72.76
    EURO_RATE = 86.15
    CURRENCY_RATE = {
        'rub': (1, 'руб'),
        'usd': (USD_RATE, 'USD'),
        'eur': (EURO_RATE, 'Euro'),
    }

    def get_today_cash_remained(self, currency):
        balance = self.get_balance()
        balance = round(balance / self.CURRENCY_RATE[currency][0], 2)
        if balance > 0:
            return (
                "На сегодня осталось "
                f"{balance} {self.CURRENCY_RATE[currency][1]}"
            )
        elif balance == 0:
            return "Денег нет, держись"
        else:
            balance = abs(balance)
            return (
                "Денег нет, держись: твой долг - "
                f"{balance} {self.CURRENCY_RATE[currency][1]}"
            )


class CaloriesCalculator(Calculator):
    """Опять калькулятор."""
    def get_calories_remained(self):
        balance = self.get_balance()
        if balance > 0:
            return (
                "Сегодня можно съесть что-нибудь ещё, но с общей калорийностью"
                f" не более {balance} кКал"
            )
        else:
            return "Хватит есть!"
