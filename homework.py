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
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, date_format).date()
        self.amount = amount
        self.comment = comment


class CashCalculator(Calculator):
    """Ещё калькулятор"""
    EURO_RATE = 86.15
    USD_RATE = 72.76

    @staticmethod
    def raise_unsupported_currency(currency):
        raise ValueError(f'{currency} not supported')


    def get_today_cash_remained(self, currency):
        CURRENCY_RATE = {
            'rub': (1, 'руб'),
            'eur': (self.EURO_RATE, 'Euro'),
            'usd': (self.USD_RATE, 'USD'),
        }
        if currency not in CURRENCY_RATE.keys():
            self.raise_unsupported_currency(currency)
        balance = self.get_balance()
        if balance == 0:
            return "Денег нет, держись"
        rate, view = CURRENCY_RATE[currency]
        if rate == 0:
            raise ArithmeticError()
        if balance > 0:
            balance = round(balance / rate, 2)
            return (
                "На сегодня осталось "
                f"{balance} {view}"
            )
        balance = abs(round(balance / rate, 2))
        return (
                "Денег нет, держись: твой долг - "
                f"{balance} {view}"
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
        return "Хватит есть!"
