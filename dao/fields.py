from django.db.models import CharField
from django.core.validators import int_list_validator, MinLengthValidator


class PhoneField(CharField):
    PHONE_NUMBER_LEN = 13

    def __init__(self, *args, verbose_name=None, **kwargs):
        kwargs['max_length'] = self.PHONE_NUMBER_LEN
        kwargs['verbose_name'] = verbose_name
        super().__init__(*args, **kwargs)
        self.validators.append(int_list_validator(sep='', message='Phone number must contain only digits'))
        self.validators.append(MinLengthValidator(self.PHONE_NUMBER_LEN, message=f'Phone number must have {self.PHONE_NUMBER_LEN} digits'))


class CnpjField(CharField):
    CNPJ_LEN = 14

    def __init__(self, *args, verbose_name=None, **kwargs):
        kwargs['max_length'] = self.CNPJ_LEN
        kwargs['verbose_name'] = verbose_name
        super().__init__(*args, **kwargs)
        self.validators.append(int_list_validator(sep='', message='CNPJ must contain only digits'))
        self.validators.append(MinLengthValidator(self.CNPJ_LEN, message=f'CNPJ must have {self.CNPJ_LEN} digits'))


class CpfField(CharField):
    CPF_LEN = 11

    def __init__(self, *args, verbose_name=None, **kwargs):
        kwargs['max_length'] = self.CPF_LEN
        kwargs['verbose_name'] = verbose_name
        super().__init__(*args, **kwargs)
        self.validators.append(int_list_validator(sep='', message='CPF must contain only digits'))
        self.validators.append(MinLengthValidator(self.CPF_LEN, message=f'CPF must have {self.CPF_LEN} digits'))
