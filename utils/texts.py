from utils.translations import _, __

# _ is for general texts
# __ is for texts with pluralisation, use keyword {number} to automatically substitute number

# To get value use .value (texts.HELLO_WORLD.value)
# To get plural value use .value(number) (texts.HELLO_WORLD.value(5))

# In decorators use .lazy (F.text == texts.HELLO_WORLD.lazy)
# Don't use pluralisation in decorators, but if you do: F.text == texts.PLURAL.lazy(static_number)

class TranslationTextss:
    HELLO = _("""
Hi, you can use this bot to check other bots' stats and to add your bot to the list

Send bot's username to get stats
                   
/add - add your bot to the list
/language - change language
              """)
    HELLO_ADD_BOT = _("Add my bot to the list")
    HELLO_HELP = _("Bot's username")
    ERROR = _("Something went wrong...")
    # Singular and plural
    HELLO_WORLD_PLURALIZATION = __("Hello, {number} world!", "Hello, {number} worlds!")

class TranslationTexts:
    HELLO = _("""
Вы можете использовать этого бота для проверки статистики других ботов и добавления своего бота в список

Отправьте юзернейм бота, чтобы получить его статистику

/add - добавить бота в список
    """)
    HELLO_ADD_BOT_BUTTON = _("Добавить моего бота в список")
    HELLO_HINT = _("Юзернейм бота")
    ERROR = _("Что-то пошло не так...")
    ADD_BOT = _("""
Отправьте токен бота, которого вы хотите добавить (его можно получить, отправив команду /token в @botfather)
    """)
    ADD_BOT_HINT = _("Токен бота")
    ADD_BOT_SUCCESS = _("""
Бот успешно добавлен. Подсчет статистики идет с момента добавления бота в систему. Получить статистику можно отправив мне юзернейм бота
    """)
    ADD_BOT_ERROR = _("""
Данный токен недействителен. Попробуйте еще раз
    """)
    BOT_NOT_FOUND = _("Не удалось найти аккаунт с таким юзернеймом")
    IS_NOT_BOT = _("Данный юзернейм не принадлежит боту")
    BOT_NOT_ADDED = _("Данного бота нет в системе. Если вы владелец бота, вы можете добавить его командой /add")
    BOT_STATS = _("Для получения статистики перейдите по ссылке: {link}")
    BOT_STATS_LINK = _("https://metabase.4u.studio/public/dashboard/3be0c8ae-63d3-4633-bc02-767d1deeb427?app_name={app_name}&bot_id={bot_id}")
    DELETE_BOT = _("""
Отправьте юзернейм или токен бота, которого вы хотите удалить.

⚠️ Внимание, при удалении бота будет так же удалена вся его статистика
    """)
    DELETE_BOT_SUCCESS = _("Бот успешно удален")
    DELETE_BOT_NOT_FOUND = _("Данного бота нет в системе, поэтому его удаление невозможно")
    DELETE_BOT_NOT_OWNER = _("Вы не являетесь владельцем данного бота, поэтому его удаление невозможно")
    CANCEL = _("Отмена")
    CANCEL_ADD_TEXT = _("Добавление бота отменено")
    CANCEL_DELETE_TEXT = _("Удаление бота отменено")
    
texts = TranslationTexts