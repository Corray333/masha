import re

def wordValidation(word):
    reg = r'^[A-Za-zА-Яа-я]+$'
    return re.match(reg, word) is not None

def phoneValidation(phone):
    reg = r'^(\+7-\(9)\d\d\)-\d\d\d-\d\d-\d\d$'
    return re.match(reg, phone) is not None

def emailValidation(email):
    reg = r'^((([0-9A-Za-z]{1}[-0-9A-z\.]{1,}[0-9A-Za-z]{1})|([0-9А-Яа-я]{1}[-0-9А-я\.]{1,}[0-9А-Яа-я]{1}))@([-A-Za-z]{1,}\.){1,2}[-A-Za-z]{2,})$'
    return re.match(reg, email) is not None

def passwordValidation(password):
    reg = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(reg, password) is not None