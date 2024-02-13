import configparser
from connections.database.models import User

def get_text(target_key: str, user: User):
    if user.language == 0:
        lang_file = 'ru'
    else:
        lang_file = 'en'

    file_name = f"tgbot/data/texts/{lang}.ini"
    config = configparser.ConfigParser()
    config.read(file_name, encoding='utf-8')

    if config.has_section(lang) and config.has_option(lang, target_key):
        return config.get(lang, target_key).replace('\\n', '\n')
    else:
        return 'Error!'  # Вернуть None или другое значение, если ключ или язык не найдены