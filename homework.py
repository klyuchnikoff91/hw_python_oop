import datetime as dt


class Calculator:
    """Шаблонный калькулятор."""
    def __init__(self, limit: float):
        self.limit = limit
        self.records: list[Record] = list()

    def add_record(self, record: object):
        self.records.append(record)

    def get_today_stats(self) -> float:
        today = dt.date.today()
        today_amount = sum(r.amount for r in self.records if r.date == today)
        return today_amount

    def get_week_stats(self) -> float:
        today = dt.date.today()
        start_dow = today - dt.timedelta(days=7)
        week_amount = sum(r.amount for r in self.records
                          if (r.date <= today) and (r.date > start_dow))
        return week_amount


class Record:
    """Структура, обрабатывающая и хранящая записи калькуляторов.
    Проверяет ошибки при вводе."""
    def __init__(self,
                 amount: float,
                 comment: str,
                 date=None) -> None:
        try:
            date_format = '%d.%m.%Y'
            if (type(date) is str):
                self.date = dt.datetime.strptime(date, date_format).date()
            elif isinstance(date, dt.date):
                self.date = date
            elif date is None:
                self.date = dt.date.today()
            else:
                raise ValueError
            self.amount = float(amount)
            self.comment = comment
        except ValueError:
            print("Запись не верна")
            pass


class CashCalculator(Calculator):
    """Ещё один скучный калькулятор"""
    USD_RATE = 72.76
    EURO_RATE = 86.15

    def get_today_cash_remained(self, currency: str) -> str:
        balance = self.limit - self.get_today_stats()
        format_str_currency = "руб"
        if (currency == 'usd'):
            balance = balance / self.USD_RATE
            format_str_currency = currency.upper()
        elif (currency == 'eur'):
            balance = balance / self.EURO_RATE
            format_str_currency = "Euro"
        if balance > 0:
            return (
                "На сегодня осталось "
                f"{round(balance, 2)} {format_str_currency}"
            )
        elif balance == 0:
            return "Денег нет, держись"
        else:
            return (
                "Денег нет, держись: твой долг - "
                f"{-round(balance, 2)} {format_str_currency}"
            )


class CaloriesCalculator(Calculator):
    """Опять калькулятор."""
    def get_calories_remained(self) -> str:
        balance = round(self.limit - self.get_today_stats())
        if (balance > 0):
            return (
                "Сегодня можно съесть что-нибудь ещё, но с общей калорийностью"
                f" не более {balance} кКал"
            )
        else:
            return "Хватит есть!"
