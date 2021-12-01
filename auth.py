from pywebio.output import put_buttons, put_column, put_error, put_markdown
from pywebio.input import PASSWORD
from pywebio.pin import pin, put_input
from pywebio.session import go_app
from classes.user import User
from messages import show_message
from cookie_io import get_current_user_id, init_js_cookie_io, remove_all_cookies, set_cookie
from sql import validate_credentials

# переход на страницу регистрации
def register():
    go_app('register_page', new_window=False)


# вход в систем
def login():
    answer = validate_credentials(pin.username, pin.password)

    if(type(answer) is User):
        set_cookie('current_user_id', f'{answer.id}')
        go_app('home_page', new_window=False)
    else:
        put_error(answer, closable=True)


# редирект в случае пойманных куки
def redirect():
    id = get_current_user_id()
    print(f'полученное значение id={id}')
    
    if id != None:
        go_app('test_list_page', new_window=False)


# основной код страницы авторизации
def auth_page():
    init_js_cookie_io()
    remove_all_cookies()
    redirect()
    show_message()
    put_markdown('# ✅ Авторизация')
    put_column([
        put_input('username', label='Логин'),
        put_input('password', label='Пароль', type=PASSWORD)
    ])
    put_buttons(['Войти', 'Регистрация'], onclick=[login, register])
    