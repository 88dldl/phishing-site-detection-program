from datetime import datetime


def check_creation_date(creation_date):
    if creation_date:
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        age_days = (datetime.now() - creation_date).days
        if 365 <= age_days:
            return 1
        else:
            return -1
    else:
        return 0


def check_expiration_date(expiration_date):
    if expiration_date:
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]
        days_to_expire = (expiration_date - datetime.now()).days
        if days_to_expire >= 180:
            return -1
        else:
            return 1
    else:
        return 1
