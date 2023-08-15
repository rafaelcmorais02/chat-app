from .account.service import update_account


def update_account_with_company(pk, company):
    return update_account(pk=pk, company=company)
