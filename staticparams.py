import json
MAILTEMPLATES = {
    "clicklink":                open('mail-templates/magictime.html', 'r').read(),
    "mail_confirmation":        open('mail-templates/reg.html', 'r').read(),
    # "reg_congrats":             open('mail-templates/reg_congrats.html', 'r').read(),
    # "login_attempt":            open('mail-templates/log_attmpt.html', 'r').read(),
    # "pass_change":              open('mail-templates/passwordchange.html', 'r').read(),
    # "pass_changed":             open('mail-templates/passwordchanged.html', 'r').read()
}

setsfile = open('settings.json', 'r')
SETTINGS = json.load(setsfile)
setsfile.close()

RECORDS_TYPES = {
    'income': 0,
    'expenses': 1,
    'users': 2
}