import time
import socket
import flet as ft
import ast


def main(page: ft.Page):
    # page.window_full_screen = True
    global state_page
    state_page = 0

    def page_resize(e):
        w = page.window_width
        h = page.window_height
        page_reg = ft.Container(
            ft.Container(
                ft.Row(
                    [
                        ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                     width=(w / 3),
                                     height=h // 3),
                        ft.Container(ft.Text("Регистрация", size=30), alignment=ft.alignment.Alignment(-0.1, 0),
                                     width=w / 3 + 0, height=h // 3),
                    ],
                    width=w
                    # alignment=ft.MainAxisAlignment.CENTER
                ),
                # width=w,
                alignment=ft.alignment.Alignment(0, -1),
            )
        )
        page_aut = ft.Container(
            ft.Container(
                ft.Row(
                    [
                        ft.Container(c_or_y, alignment=ft.alignment.Alignment(-1, -1),
                                     width=w / 3,
                                     height=h // 3),
                        ft.Container(ft.Text("Авторизация", size=30), alignment=ft.alignment.Alignment(0, 0),
                                     width=w / 3 + 0, height=h // 3),
                    ],
                    width=w
                    # alignment=ft.MainAxisAlignment.CENTER
                ),
                # width=w,
                alignment=ft.alignment.Alignment(0, -1),
            )
        )
        page_aut1 = ft.Container(
            ft.Row(
                [
                    ft.Container(ft.Column(
                        [
                            ft.Container(width=15),
                            ft.Container(ft.Column([
                                ft.Row([login], alignment=ft.MainAxisAlignment.CENTER),
                                ft.Row([password], alignment=ft.MainAxisAlignment.CENTER),
                                ft.Row([btn_aut], alignment=ft.MainAxisAlignment.CENTER),
                                ft.Row([btn_reg, pass_], alignment=ft.MainAxisAlignment.CENTER)
                            ]),
                                width=310,
                            )

                        ],
                        # alignment=ft.MainAxisAlignment.CENTER,

                    ),
                        width=325,
                        height=275,
                        alignment=ft.alignment.Alignment(0, -0.5),
                        border_radius=10,
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.colors.BLUE_GREY_300,
                            offset=ft.Offset(0, 0),
                            blur_style=ft.ShadowBlurStyle.OUTER, ),
                        # bgcolor="green"
                    )

                ],
                alignment=ft.MainAxisAlignment.CENTER,
                # vertical_alignment=ft.CrossAxisAlignment,
            ),
        )
        page_reg0 = ft.Container(
            ft.Row(
                [
                    ft.Container(alignment=ft.alignment.Alignment(-0.9, -0.9), width=w // 3),
                    ft.Container(ft.Text("Регистрация", size=30), alignment=ft.alignment.Alignment(0, -0),
                                 width=w // 3),
                    ft.Container(alignment=ft.alignment.Alignment(0.8, -0.9), width=w // 3),
                ]
            ),
            alignment=ft.alignment.Alignment(0, -1), height=100
        )
        page_reg05 = ft.Container(
            ft.Row(
                [
                    ft.Column(
                        [
                            school, codschool, teacher, student, btn_next05,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                # vertical_alignment=ft.CrossAxisAlignment,
            )
        )
        page_reg1 = ft.Container(
            ft.Row(
                [
                    ft.Column(
                        [
                            name, surname, patronymic, btn_next,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                # vertical_alignment=ft.CrossAxisAlignment,
            )
        )
        page_reg2 = ft.Container(
            ft.Column([
                ft.Row(
                    [
                        ft.Column(
                            [
                                Class
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    # vertical_alignment=ft.CrossAxisAlignment,
                ),
                ft.Row(
                    [
                        ft.Column(
                            [
                                btn_next1
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    # vertical_alignment=ft.CrossAxisAlignment,
                )
            ])
        )
        page_reg3 = ft.Container(
            ft.Row(
                [
                    ft.Column(
                        [
                            login, password, btn_reg1,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                # vertical_alignment=ft.CrossAxisAlignment,
            )
        )
        global state_page
        page.clean()
        if state_page == 0:
            page.add(page_aut, page_aut1)
        elif state_page == 1:
            page.add(page_reg, page_reg1)
        elif state_page == 2:
            page.add(page_reg, page_reg05)
        elif state_page == 3:
            page.add(page_reg, page_reg3)
        elif state_page == 4:
            if ccc[0] == "Учитель":
                page.add(page_reg0, page_reg2)
            else:
                page.add(page_reg, page_reg20)
        else:
            page.add(page_aut, page_aut1)

    w = page.window_width
    h = page.window_height

    global cl
    cl = []
    global ccc
    ccc = []
    page.on_resize = page_resize
    page.title = "My project"

    # page.theme_mode = ft.ThemeMode.DARK
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = ft.padding.only(top=0, left=0)

    a = "Учитель"
    s = "Ученик"

    def valideate(e):
        if all([login.value, password.value]):
            btn_aut.disabled = False
            btn_reg1.disabled = False
        else:
            btn_aut.disabled = True
            btn_reg1.disabled = True
        page.update()

    def valideate1(e):
        if all([name.value, surname.value, patronymic.value]):
            btn_next.disabled = False
        else:
            btn_next.disabled = True
        page.update()

    def valideate2(e):
        if all([codschool.value, school.value]) and teacher.value or student.value:
            btn_next05.disabled = False
        else:
            btn_next05.disabled = True
        page.update()

    def valideate3(e):
        if all([class1.value]):
            btn_next1.disabled = False
        else:
            btn_next1.disabled = True
        page.update()

    def click_cy(e):
        if btn_c_or_y.text == s:
            c_or_y.title = ft.Text(btn_c_or_y.text)
            btn_c_or_y.text = a
        else:
            c_or_y.title = ft.Text(btn_c_or_y.text)
            btn_c_or_y.text = s
        c_or_y.initially_expanded = True
        page.update()

    def click_aut(e):
        if btn_c_or_y.text == "Учитель":
            f = "Ученик"
        else:
            f = "Учитель"

        client = socket.socket()  # создаем сокет клиента
        HOST = (socket.gethostname(), 55555)
        try:
            client.connect(HOST)  # подключаемся к серверу
        except ConnectionRefusedError:
            page.snack_bar = ft.SnackBar(ft.Text("Ошибка соиденения с сервером! Пожалуйста подождите и повторите попытку"))
            page.snack_bar.open = True
            page.update()

        gf = [2, f, login.value, password.value]
        client.send(str(gf).encode())
        data = client.recv(40000)
        if data.decode() == "1":
            page.snack_bar = ft.SnackBar(ft.Text("Вы авторизованы! "))
            page.snack_bar.open = True
            page.update()
            # page.window_destroy()
            time.sleep(1)
            page.clean()
            if btn_c_or_y.text == "Учитель":
                student_main(page)
            else:
                teacher_main(page, login, password)
        else:
            login.value = ""
            password.value = ""
            btn_aut.disabled = True
            page.snack_bar = ft.SnackBar(ft.Text("Неверно введённые данны! "))
            page.snack_bar.open = True
            page.update()
        page.update()
        client.close()

    def click_reg(e):
        global state_page
        state_page = 1
        page_resize(1)

    def click_reg1(e):
        global state_page
        state_page = 2
        page_resize(1)

    def click_reg05(e):
        global state_page
        state_page = 4
        page_resize(1)

    def click_reg2(e):
        global state_page
        state_page = 3
        page_resize(1)

    def click_reg3(e):

        client = socket.socket()  # создаем сокет клиента
        HOST = (socket.gethostname(), 55555)
        try:
            client.connect(HOST)  # подключаемся к серверу
        except ConnectionRefusedError:
            page.snack_bar = ft.SnackBar(ft.Text("Ошибка соиденения с сервером! Пожалуйста подаждите и повторите попытку"))
            page.snack_bar.open = True
            page.update()
        if ccc[0] == "Учитель":
            gf = [1, ccc[0], name.value, surname.value, patronymic.value, cl, school.value, codschool.value,
                  login.value,
                  password.value]
        else:
            gf = [1, ccc[0], name.value, surname.value, patronymic.value, class1.value, school.value, codschool.value,
                  login.value,
                  password.value]
        client.sendall(str(gf).encode())

        data = client.recv(40000)
        data = data.decode()
        if data == "0":
            page.snack_bar = ft.SnackBar(ft.Text("Вы зарегистрированы! "))
            page.snack_bar.open = True
            page.update()
            time.sleep(1)
            page.clean()
            client.close()
            if ccc[0] == "Учитель":
                teacher_main(page, login, password)
            else:
                student_main(page)
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Неподходящий логин или пароль"))
            login.value = ''
            password.value = ''
            btn_reg1.disabled = True
            page.snack_bar.open = True
            page.update()
            time.sleep(1)

    def click_box(e):
        for i in checkboxes:
            if i.value:
                if cl.count(i.label) == 0:
                    cl.append(i.label)
            else:
                if cl.count(i.label) == 1:
                    cl.remove(i.label)
        if cl:
            btn_next1.disabled = False
        else:
            btn_next1.disabled = True
        page.update()

    def click_box1(e):
        for i in checkboxes1:
            if i.value:
                if ccc.count(i.label) == 1:
                    ccc.remove(i.label)
                    i.value = False
                else:
                    ccc.append(i.label)
            else:
                if ccc.count(i.label) == 1:
                    ccc.remove(i.label)
                    i.value = False
        page.update()
        valideate2(1)

    # checkboxes
    A1 = ft.Checkbox("1-A", False, height=25, on_change=click_box)
    B1 = ft.Checkbox("1-Б", False, height=25, on_change=click_box)
    C1 = ft.Checkbox("1-В", False, height=25, on_change=click_box)
    D1 = ft.Checkbox("1-Г", False, height=25, on_change=click_box)
    E1 = ft.Checkbox("1-Д", False, height=25, on_change=click_box)
    A2 = ft.Checkbox("2-A", False, height=25, on_change=click_box)
    B2 = ft.Checkbox("2-Б", False, height=25, on_change=click_box)
    C2 = ft.Checkbox("2-В", False, height=25, on_change=click_box)
    D2 = ft.Checkbox("2-Г", False, height=25, on_change=click_box)
    E2 = ft.Checkbox("2-Д", False, height=25, on_change=click_box)
    A3 = ft.Checkbox("3-A", False, height=25, on_change=click_box)
    B3 = ft.Checkbox("3-Б", False, height=25, on_change=click_box)
    C3 = ft.Checkbox("3-В", False, height=25, on_change=click_box)
    D3 = ft.Checkbox("3-Г", False, height=25, on_change=click_box)
    E3 = ft.Checkbox("3-Д", False, height=25, on_change=click_box)
    A4 = ft.Checkbox("4-A", False, height=25, on_change=click_box)
    B4 = ft.Checkbox("4-Б", False, height=25, on_change=click_box)
    C4 = ft.Checkbox("4-В", False, height=25, on_change=click_box)
    D4 = ft.Checkbox("4-Г", False, height=25, on_change=click_box)
    E4 = ft.Checkbox("4-Д", False, height=25, on_change=click_box)
    A5 = ft.Checkbox("5-A", False, height=25, on_change=click_box)
    B5 = ft.Checkbox("5-Б", False, height=25, on_change=click_box)
    C5 = ft.Checkbox("5-В", False, height=25, on_change=click_box)
    D5 = ft.Checkbox("5-Г", False, height=25, on_change=click_box)
    E5 = ft.Checkbox("5-Д", False, height=25, on_change=click_box)
    A6 = ft.Checkbox("6-A", False, height=25, on_change=click_box)
    B6 = ft.Checkbox("6-Б", False, height=25, on_change=click_box)
    C6 = ft.Checkbox("6-В", False, height=25, on_change=click_box)
    D6 = ft.Checkbox("6-Г", False, height=25, on_change=click_box)
    E6 = ft.Checkbox("6-Д", False, height=25, on_change=click_box)
    A7 = ft.Checkbox("7-A", False, height=25, on_change=click_box)
    B7 = ft.Checkbox("7-Б", False, height=25, on_change=click_box)
    C7 = ft.Checkbox("7-В", False, height=25, on_change=click_box)
    D7 = ft.Checkbox("7-Г", False, height=25, on_change=click_box)
    E7 = ft.Checkbox("7-Д", False, height=25, on_change=click_box)
    A8 = ft.Checkbox("8-A", False, height=25, on_change=click_box)
    B8 = ft.Checkbox("8-Б", False, height=25, on_change=click_box)
    C8 = ft.Checkbox("8-В", False, height=25, on_change=click_box)
    D8 = ft.Checkbox("8-Г", False, height=25, on_change=click_box)
    E8 = ft.Checkbox("8-Д", False, height=25, on_change=click_box)
    A9 = ft.Checkbox("9-A", False, height=25, on_change=click_box)
    B9 = ft.Checkbox("9-Б", False, height=25, on_change=click_box)
    C9 = ft.Checkbox("9-В", False, height=25, on_change=click_box)
    D9 = ft.Checkbox("9-Г", False, height=25, on_change=click_box)
    E9 = ft.Checkbox("9-Д", False, height=25, on_change=click_box)
    A10 = ft.Checkbox("10-A", False, height=25, on_change=click_box)
    B10 = ft.Checkbox("10-Б", False, height=25, on_change=click_box)
    C10 = ft.Checkbox("10-В", False, height=25, on_change=click_box)
    D10 = ft.Checkbox("10-Г", False, height=25, on_change=click_box)
    E10 = ft.Checkbox("10-Д", False, height=25, on_change=click_box)
    A11 = ft.Checkbox("11-A", False, height=25, on_change=click_box)
    B11 = ft.Checkbox("11-Б", False, height=25, on_change=click_box)
    C11 = ft.Checkbox("11-В", False, height=25, on_change=click_box)
    D11 = ft.Checkbox("11-Г", False, height=25, on_change=click_box)
    E11 = ft.Checkbox("11-Д", False, height=25, on_change=click_box)
    checkboxes = [A1, B1, C1, D1, E1, A2, B2, C2, D2, A3, B3, C3, D3, E3, A4, B4, C4, D4, E4, A5, B5, C5, D5, E5, A6,
                  B6,
                  C6, D6, E6, A7, B7, C7, D7, E7, A8, B8, C8, D8, E8, A9, B9, C9, D9, E9, A10, B10, C10, D10, E10, A11,
                  B11, C11, D11, E11]

    teacher = ft.Checkbox("Учитель", False, height=27, on_change=click_box1)
    student = ft.Checkbox("Ученик", False, height=27, on_change=click_box1)
    checkboxes1 = [teacher, student]

    btn_c_or_y = ft.CupertinoButton(s, on_click=click_cy)
    c_or_y = ft.ExpansionTile(
        title=ft.Text(a),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[ft.ListTile(title=btn_c_or_y)],
        width=150,
        # shape=ft.CircleBorder()
    )

    _1 = ft.ExpansionTile(title=ft.Text("1 класс"),
                          # subtitle=ft.Text("Leading expansion arrow icon"),
                          affinity=ft.TileAffinity.LEADING,
                          initially_expanded=False,
                          collapsed_text_color=ft.colors.BLUE,
                          text_color=ft.colors.BLUE,
                          controls=[ft.ListTile(title=ft.Column([A1, B1, C1, D1, E1]))], )
    _2 = ft.ExpansionTile(
        title=ft.Text("2 класс"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[
            ft.ListTile(title=ft.Column([A2, B2, C2, D2, E2]))], )
    _3 = ft.ExpansionTile(
        title=ft.Text("3 класс"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[
            ft.ListTile(title=ft.Column([A3, B3, C3, D3, E3]))], )
    _4 = ft.ExpansionTile(
        title=ft.Text("4 класс"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[
            ft.ListTile(title=ft.Column([A4, B4, C4, D4, E4]))],
    )
    _5 = ft.ExpansionTile(
        title=ft.Text("5 класс"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[
            ft.ListTile(title=ft.Column([A5, B5, C5, D5, E5]))],
    )
    _6 = ft.ExpansionTile(
        title=ft.Text("6 класс"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[
            ft.ListTile(title=ft.Column([A6, B6, C6, D6, E6]))],
    )
    _7 = ft.ExpansionTile(
        title=ft.Text("7 класс"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[
            ft.ListTile(title=ft.Column([A7, B7, C7, D7, E7]))],
    )
    _8 = ft.ExpansionTile(
        title=ft.Text("8 класс"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[
            ft.ListTile(title=ft.Column([A8, B8, C8, D8, E8]))],
    )
    _9 = ft.ExpansionTile(
        title=ft.Text("9 класс"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[
            ft.ListTile(title=ft.Column([A9, B9, C9, D9, E9]))],
    )
    _10 = ft.ExpansionTile(
        title=ft.Text("10 класс"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[
            ft.ListTile(title=ft.Column([A10, B10, C10, D10, E10]))],
    )
    _11 = ft.ExpansionTile(
        title=ft.Text("11 класс"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[
            ft.ListTile(title=ft.Column([A11, B11, C11, D11, E11]))],
    )
    Class = ft.ExpansionTile(
        title=ft.Text("Выберете классы"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[ft.ListTile(title=ft.Row(
            [ft.Column([_1, _2, _3, _4], width=300), ft.Column([_5, _6, _7, _8], width=300),
             ft.Column([_9, _10, _11], width=300)]))],
        width=900,
        # shape=ft.CircleBorder()
    )

    # Text
    name = ft.TextField(label="Имя", width=300, on_change=valideate1)
    surname = ft.TextField(label="Фамилия", width=300, on_change=valideate1)
    patronymic = ft.TextField(label="Отчество", width=300, on_change=valideate1)
    school = ft.TextField(label="Школа", width=300, on_change=valideate2)
    codschool = ft.TextField(label="Код школы", width=300, on_change=valideate2)
    class1 = ft.TextField(label="Введите свой класс", width=300, on_change=valideate3)
    login = ft.TextField(label="Логин", width=300, on_change=valideate)
    password = ft.TextField(label="Пароль", width=300, password=True, on_change=valideate)

    # btn
    btn_aut = ft.CupertinoFilledButton("Авторизоваться", width=300, disabled=True, on_click=click_aut)
    btn_reg = ft.CupertinoButton("Регистрация", width=131, on_click=click_reg)
    pass_ = ft.CupertinoButton("Забыли пароль?", on_click=click_reg)
    btn_reg1 = ft.ElevatedButton("Зарегистрироваться", width=300, disabled=True, on_click=click_reg3)
    btn_next = ft.ElevatedButton("Далее", width=300, disabled=True, on_click=click_reg1)
    btn_next05 = ft.ElevatedButton("Далее", width=300, disabled=True, on_click=click_reg05)
    btn_next1 = ft.ElevatedButton("Далее", width=300, disabled=True, on_click=click_reg2)

    login.value = ""
    password.value = ""

    page_aut = ft.Container(
        ft.Container(
            ft.Row(
                [
                    ft.Container(c_or_y, alignment=ft.alignment.Alignment(-1, -1),
                                 width=(w / 3),
                                 height=h // 3),
                    ft.Container(ft.Text("Авторизация", size=30), alignment=ft.alignment.Alignment(-0.1, 0),
                                 width=w / 3 + 0, height=h // 3),
                ],
                width=w
                # alignment=ft.MainAxisAlignment.CENTER
            ),
            # width=w,
            alignment=ft.alignment.Alignment(0, -1),
        )
    )
    page_aut1 = ft.Container(
        ft.Row(
            [
                ft.Container(ft.Column(
                    [
                        ft.Container(width=15),
                        ft.Container(ft.Column([
                            ft.Row([login], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Row([password], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Row([btn_aut], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Row([btn_reg, pass_], alignment=ft.MainAxisAlignment.CENTER)
                        ]),
                            width=310,
                        )

                    ],
                    # alignment=ft.MainAxisAlignment.CENTER,

                ),
                    width=325,
                    height=275,
                    alignment=ft.alignment.Alignment(0, -0.5),
                    border_radius=10,
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.colors.BLUE_GREY_300,
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER, ),
                    # bgcolor="green"
                )

            ],
            alignment=ft.MainAxisAlignment.CENTER,
            # vertical_alignment=ft.CrossAxisAlignment,
        ),
    )
    page_reg = ft.Container(
        ft.Container(
            ft.Row(
                [
                    ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                 width=(w / 3),
                                 height=h // 3),
                    ft.Container(ft.Text("Регистрация", size=30), alignment=ft.alignment.Alignment(-0.1, 0),
                                 width=w / 3 + 0, height=h // 3),
                ],
                width=w
                # alignment=ft.MainAxisAlignment.CENTER
            ),
            # width=w,
            alignment=ft.alignment.Alignment(0, -1),
        )
    )
    page_reg0 = ft.Container(
        ft.Row(
            [
                ft.Container(alignment=ft.alignment.Alignment(-0.9, -0.9), width=w // 3),
                ft.Container(ft.Text("Регистрация", size=30), alignment=ft.alignment.Alignment(0, -0),
                             width=w // 3),
                ft.Container(alignment=ft.alignment.Alignment(0.8, -0.9), width=w // 3),
            ]
        ),
        alignment=ft.alignment.Alignment(0, -1), height=100
    )
    page_reg1 = ft.Container(
        ft.Row(
            [
                ft.Column(
                    [
                        name, surname, patronymic, btn_next,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            # vertical_alignment=ft.CrossAxisAlignment,
        )
    )
    page_reg05 = ft.Container(
        ft.Row(
            [
                ft.Column(
                    [
                        school, codschool, teacher, student, btn_next05,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            # vertical_alignment=ft.CrossAxisAlignment,
        )
    )
    page_reg2 = ft.Container(
        ft.Column([
            ft.Row(
                [
                    ft.Column(
                        [
                            Class, btn_next1
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                # vertical_alignment=ft.CrossAxisAlignment,
            ),
            ft.Row(
                [
                    ft.Column(
                        [

                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                # vertical_alignment=ft.CrossAxisAlignment,
            )
        ])
    )
    page_reg20 = ft.Container(
        ft.Column([
            ft.Row(
                [
                    ft.Column(
                        [
                            class1, btn_next1
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                # vertical_alignment=ft.CrossAxisAlignment,
            ),
            ft.Row(
                [
                    ft.Column(
                        [

                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                # vertical_alignment=ft.CrossAxisAlignment,
            )
        ])
    )
    page_reg3 = ft.Container(
        ft.Row(
            [
                ft.Column(
                    [
                        login, password, btn_reg1,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            # vertical_alignment=ft.CrossAxisAlignment,
        )
    )
    page.add(page_aut, page_aut1)


def student_main(page: ft.Page):
    def chang_(e):

        if e.control.selected_index == 0:
            pagelet.appbar.title = ft.Text("Задания")
            pagelet.content = ft.Text("asd")
        if e.control.selected_index == 1:
            pagelet.appbar.title = ft.Text("Успеваемость")
            pagelet.content = ft.Text("asda")
        if e.control.selected_index == 2:
            pagelet.appbar.title = ft.Text("Итоговые оценки")
            pagelet.content = ft.Text("asdas")
        if e.control.selected_index == 3:
            page.clean()
            main(page)
        pagelet.update()
        page.update()

    # page.window_full_screen = True
    page.padding = ft.padding.only(top=0, left=0)
    pagelet = ft.Pagelet(
        appbar=ft.AppBar(
            title=ft.Text("Задания"), bgcolor=ft.colors.LIGHT_BLUE_200
        ),
        content=ft.Text("Pagelet body"),
        drawer=ft.NavigationDrawer(
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_TO_HOME_SCREEN_SHARP, label="Задания",
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_COMMENT, label="Успеваимость"  # , ref=ft.Ref(ft.Text(sdfsfsfs))

                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_COMMENT, label="Итоговые оценки"  # , ref=ft.Ref(ft.Text(sdfsfsfs))

                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_COMMENT, label="Выйти"  # , ref=ft.Ref(ft.Text(sdfsfsfs))

                ),
                ft.Divider(thickness=2),
            ],
            selected_index=0,
            on_change=chang_
        ),
        floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_DOCKED,
        width=page.window_width,
        height=page.window_height,

    )

    page.add(pagelet)


def teacher_main(page: ft.Page, login, password):
    def click_new_tasks(e):
        client = socket.socket()  # создаем сокет клиента
        HOST = (socket.gethostname(), 55555)
        client.connect(HOST)  # подключаемся к серверу
        a = [3, "Учитель", login.value, password.value]
        client.send(str(a).encode())
        cla = client.recv(40000)
        cla = cla.decode()
        cla = ast.literal_eval(cla)
        cla.sort()

        for i in cla:
            c.append(ft.Checkbox(label=i, value=False, height=25))
        global state_page
        state_page = 1
        page_resize1(1)

    def page_resize1(e):
        make_tasks = ft.Row([
            ft.Column([ft.Container(height=page.window_height / 4),
                       ft.Row([ft.Container(width=page.window_width / 12), ft.Text("Тема", size=30)],
                              alignment=ft.MainAxisAlignment.CENTER),
                       ft.CupertinoTextField(),
                       ft.Row([ft.Container(width=page.window_width / 12), ft.Text("", size=30)],
                              alignment=ft.MainAxisAlignment.CENTER),
                       classu
                       ]),

        ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        tasks = ft.ListView(expand=100000, spacing=10, padding=20, controls=[
            ft.Row([ft.ElevatedButton("Создать новый тест", on_click=click_new_tasks)],
                   alignment=ft.MainAxisAlignment.CENTER), ft.Divider(thickness=2), ft.Text("asdfggghfgsdfv"),
            ft.Divider(thickness=2), ft.Text("asdfggghfgsdfv"), ft.Divider(thickness=2),
            ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
            ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
            ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
            ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
            ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
            ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
            ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
            ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
            ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
            ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
            ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
            ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv")])
        pagelet = ft.Pagelet(
            appbar=ft.AppBar(
                title=ft.Text("Задания"), bgcolor=ft.colors.LIGHT_BLUE_200
            ),
            content=tasks,
            drawer=ft.NavigationDrawer(
                controls=[
                    ft.Container(height=12),
                    ft.NavigationDrawerDestination(
                        icon=ft.icons.ADD_TO_HOME_SCREEN_SHARP, label="Задания",
                    ),
                    ft.Divider(thickness=2),
                    ft.NavigationDrawerDestination(
                        icon=ft.icons.ADD_COMMENT, label="Журнал"

                    ),
                    ft.Divider(thickness=2),
                    ft.NavigationDrawerDestination(
                        icon=ft.icons.ADD_COMMENT, label="Выйти"

                    ),
                    ft.Divider(thickness=2),
                ],
                selected_index=index,
                on_change=chang_
            ),
            floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_DOCKED,
            width=page.window_width,
            height=page.window_height,

        )
        global state_page
        page.clean()
        print(state_page)
        if state_page == 0:
            print(0)
            pagelet.appbar.title = ft.Text("Задания")
            pagelet.content = tasks
            page.add(pagelet)
            page.update()
        elif state_page == 1:
            print(1)
            pagelet.content = make_tasks
            page.add(pagelet)
            page.update()
        elif state_page == 2:
            print(2)
            pagelet.appbar.title = ft.Text("Журнал")
            pagelet.content = ft.Text("asda")
            page.add(pagelet)
            page.update()

    def chang_(e):
        global state_page, index
        if e.control.selected_index == 0:
            index = 0
            state_page = 0
            page_resize1(1)
        if e.control.selected_index == 1:
            index = 1
            state_page = 2
            page_resize1(1)
        if e.control.selected_index == 2:
            index = 2
            page.clean()
            main(page)
        pagelet.update()
        page.update()

    global c, state_page, index
    c = []
    state_page = 0
    index = 0

    page.on_resize = page_resize1

    classu = ft.ExpansionTile(
        title=ft.Text("Классы"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[ft.ListTile(title=ft.Row([ft.Column(c)]))],
        width=300,
        shape=ft.CircleBorder()
    )

    make_tasks = ft.Row([
        ft.Column([ft.Container(height=page.window_height / 4),
                   ft.Row([ft.Container(width=page.window_width / 12), ft.Text("Тема", size=30)],
                          alignment=ft.MainAxisAlignment.CENTER),
                   ft.CupertinoTextField(), ft.Row([ft.Container(width=page.window_width / 12), ft.Text("", size=30)],
                                                   alignment=ft.MainAxisAlignment.CENTER),
                   classu
                   ]),

    ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    tasks = ft.ListView(expand=100000, spacing=10, padding=20, controls=[
        ft.Row([ft.ElevatedButton("Создать новый тест", on_click=click_new_tasks)],
               alignment=ft.MainAxisAlignment.CENTER), ft.Divider(thickness=2), ft.Text("asdfggghfgsdfv"),
        ft.Divider(thickness=2), ft.Text("asdfggghfgsdfv"), ft.Divider(thickness=2),
        ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
        ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
        ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
        ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
        ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
        ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
        ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
        ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
        ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
        ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
        ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"),
        ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv"), ft.Text("asdfggghfgsdfv")])

    # page.window_full_screen = True
    page.padding = ft.padding.only(top=0, left=0)
    pagelet = ft.Pagelet(
        appbar=ft.AppBar(
            title=ft.Text("Задания"), bgcolor=ft.colors.LIGHT_BLUE_200
        ),
        content=tasks,
        drawer=ft.NavigationDrawer(
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_TO_HOME_SCREEN_SHARP, label="Задания",
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_COMMENT, label="Журнал"

                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_COMMENT, label="Выйти"

                ),
                ft.Divider(thickness=2),
            ],
            selected_index=index,
            on_change=chang_
        ),
        floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_DOCKED,
        width=page.window_width,
        height=page.window_height,

    )

    page.add(pagelet)


ft.app(target=main)
# view=ft.AppView.WEB_BROWSER
