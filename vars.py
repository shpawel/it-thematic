"""
CONSTATNS
"""

""" API """
PROVIDERS_LIST_URL = 'https://dev.it-thematic.ru/ikpz-upload-scripts/ugeoapi/api/v1/ugeoapi/providers/'
PROVIDER_URL = PROVIDERS_LIST_URL+'%i/'
FEATURES_URL = PROVIDER_URL+'features/'
DELETE_URL = FEATURES_URL+'purge/'

""" PROVIDER'S NAME """
INFORMATION_OBJECT = 'ikpz_informationobject'
ORGANIZATION = 'ikpz_organization'
PROCUREMENT_POINT = 'ikpz_procurementpoint'
TELEPHONE = 'ikpz_telephone'

""" FIELDS """
NAME = 'Наименование'
EMAIL = 'Емайл'
PHONE = 'Телефон1'
SITE = 'Сайт'
ID = 'id'
PARENT_ID = 'id родителя'
ADDRESS = 'Адрес'
GEOM = 'местоположение'



""" VARS """
log_row_counter = 1
