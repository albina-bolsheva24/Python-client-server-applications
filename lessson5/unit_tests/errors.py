class IncorrectDataRecivedError(Exception):
    def __str__(self):
        return


class NonDictInputError(Exception):
    def __str__(self):
        return


class ReqFieldMissingError(Exception):
    def __init__(self, missing_field):
        self.missing_field = missing_field

    def __str__(self):
        return f'В принятом словаре отсутствует обязательное поле {self.missing_field}.'
