import time
import socket
import flet as ft
import ast


def main(page: ft.Page):
    # page.window_full_screen = True
    global state_page
    state_page = 0
    page.window_width = 1920
    page.window_height = 1080
    print('width', page.window_width, '\nheight', page.window_height)

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
        elif state_page == 5:
            pass
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

    А = "Учитель"
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
            btn_c_or_y.text = А
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
            page.snack_bar = ft.SnackBar(
                ft.Text("Ошибка соиденения с сервером! Пожалуйста подождите и повторите попытку"))
            page.snack_bar.open = True
            page.update()
            return

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
            page.snack_bar = ft.SnackBar(
                ft.Text("Ошибка соиденения с сервером! Пожалуйста подаждите и повторите попытку"))
            page.snack_bar.open = True
            page.update()
            return

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
    A1 = ft.Checkbox("1-А", False, height=25, on_change=click_box)
    B1 = ft.Checkbox("1-Б", False, height=25, on_change=click_box)
    C1 = ft.Checkbox("1-В", False, height=25, on_change=click_box)
    D1 = ft.Checkbox("1-Г", False, height=25, on_change=click_box)
    E1 = ft.Checkbox("1-Д", False, height=25, on_change=click_box)
    A2 = ft.Checkbox("2-А", False, height=25, on_change=click_box)
    B2 = ft.Checkbox("2-Б", False, height=25, on_change=click_box)
    C2 = ft.Checkbox("2-В", False, height=25, on_change=click_box)
    D2 = ft.Checkbox("2-Г", False, height=25, on_change=click_box)
    E2 = ft.Checkbox("2-Д", False, height=25, on_change=click_box)
    A3 = ft.Checkbox("3-А", False, height=25, on_change=click_box)
    B3 = ft.Checkbox("3-Б", False, height=25, on_change=click_box)
    C3 = ft.Checkbox("3-В", False, height=25, on_change=click_box)
    D3 = ft.Checkbox("3-Г", False, height=25, on_change=click_box)
    E3 = ft.Checkbox("3-Д", False, height=25, on_change=click_box)
    A4 = ft.Checkbox("4-А", False, height=25, on_change=click_box)
    B4 = ft.Checkbox("4-Б", False, height=25, on_change=click_box)
    C4 = ft.Checkbox("4-В", False, height=25, on_change=click_box)
    D4 = ft.Checkbox("4-Г", False, height=25, on_change=click_box)
    E4 = ft.Checkbox("4-Д", False, height=25, on_change=click_box)
    A5 = ft.Checkbox("5-А", False, height=25, on_change=click_box)
    B5 = ft.Checkbox("5-Б", False, height=25, on_change=click_box)
    C5 = ft.Checkbox("5-В", False, height=25, on_change=click_box)
    D5 = ft.Checkbox("5-Г", False, height=25, on_change=click_box)
    E5 = ft.Checkbox("5-Д", False, height=25, on_change=click_box)
    A6 = ft.Checkbox("6-А", False, height=25, on_change=click_box)
    B6 = ft.Checkbox("6-Б", False, height=25, on_change=click_box)
    C6 = ft.Checkbox("6-В", False, height=25, on_change=click_box)
    D6 = ft.Checkbox("6-Г", False, height=25, on_change=click_box)
    E6 = ft.Checkbox("6-Д", False, height=25, on_change=click_box)
    A7 = ft.Checkbox("7-А", False, height=25, on_change=click_box)
    B7 = ft.Checkbox("7-Б", False, height=25, on_change=click_box)
    C7 = ft.Checkbox("7-В", False, height=25, on_change=click_box)
    D7 = ft.Checkbox("7-Г", False, height=25, on_change=click_box)
    E7 = ft.Checkbox("7-Д", False, height=25, on_change=click_box)
    A8 = ft.Checkbox("8-А", False, height=25, on_change=click_box)
    B8 = ft.Checkbox("8-Б", False, height=25, on_change=click_box)
    C8 = ft.Checkbox("8-В", False, height=25, on_change=click_box)
    D8 = ft.Checkbox("8-Г", False, height=25, on_change=click_box)
    E8 = ft.Checkbox("8-Д", False, height=25, on_change=click_box)
    A9 = ft.Checkbox("9-А", False, height=25, on_change=click_box)
    B9 = ft.Checkbox("9-Б", False, height=25, on_change=click_box)
    C9 = ft.Checkbox("9-В", False, height=25, on_change=click_box)
    D9 = ft.Checkbox("9-Г", False, height=25, on_change=click_box)
    E9 = ft.Checkbox("9-Д", False, height=25, on_change=click_box)
    A10 = ft.Checkbox("10-А", False, height=25, on_change=click_box)
    B10 = ft.Checkbox("10-Б", False, height=25, on_change=click_box)
    C10 = ft.Checkbox("10-В", False, height=25, on_change=click_box)
    D10 = ft.Checkbox("10-Г", False, height=25, on_change=click_box)
    E10 = ft.Checkbox("10-Д", False, height=25, on_change=click_box)
    A11 = ft.Checkbox("11-А", False, height=25, on_change=click_box)
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
        title=ft.Text(А),
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
                          controls=[ft.ListTile(title=ft.Column([A1, B1, C1, D1, E1]))],
                          width=135, )
    _2 = ft.ExpansionTile(
        title=ft.Text("2 класс"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[
            ft.ListTile(title=ft.Column([A2, B2, C2, D2, E2]))],
        width=135, )
    _3 = ft.ExpansionTile(
        title=ft.Text("3 класс"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[
            ft.ListTile(title=ft.Column([A3, B3, C3, D3, E3]))],
        width=135, )
    _4 = ft.ExpansionTile(
        title=ft.Text("4 класс"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[
            ft.ListTile(title=ft.Column([A4, B4, C4, D4, E4]))],
        width=135,
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
        width=135,
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
        width=135,
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
        width=135,
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
        width=135,
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
        width=135,
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
        width=145,
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
        width=145,
    )
    Class = ft.ExpansionTile(
        title=ft.Text("Выберете классы"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[ft.ListTile(title=ft.Row(
            [ft.Column([_1, _2, _3, _4]), ft.Column([_5, _6, _7, _8]),
             ft.Column([_9, _10, _11])]))],
        width=450
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

    page_resize(1)


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


def teacher_main(page: ft.Page, login=ft.Text('a'), password=ft.Text('a')):
    def click_new_tasks(e):
        global state_page, vopr
        state_page = 1
        vopr = 1
        page_resize1(1)

    def page_resize1(e):
        global state_page, vopr, tasks, list_make_tasks, w, h, list_task, cc, c, visible_or_not, list_task, a, brp, viewtask
        w = page.window_width
        h = page.window_height

        for i in range(len(list_make_tasks)):
            if type(list_make_tasks[i]) == type(ft.Row()):
                list_make_tasks[i].controls[0].width = (w - w / 4.5) / 3

        pagelet = ft.Pagelet(
            appbar=ft.AppBar(
                title=ft.Text("Задания"), bgcolor=ft.colors.LIGHT_BLUE_200
            ),
            content=tasks,
            drawer=ft.NavigationDrawer(
                controls=
                [
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

        globalpage = ft.Container(ft.Row([tasks, ft.VerticalDivider(thickness=3)]), width=w / 4.5)

        time.sleep(0.000001)
        page.clean()
        if state_page == 0:
            page.clean()
            pagelet.appbar.title = ft.Text("Задания")
            pagelet.content = globalpage
            page.add(pagelet)
            page.update()
        elif state_page == 1:
            make_tasks = ft.Column(
                [
                    ft.Container(
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                                 width=(w - w / 4.5) / 3),
                                    ft.Container(ft.Text("Создание тестов", size=30),
                                                 alignment=ft.alignment.Alignment(-0.4, -0.99999),
                                                 width=(w - w / 4.5) / 3, height=h / 3.25),
                                    ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                                 width=(w - w / 4.5) / 3, ),
                                ],
                                width=w
                                # alignment=ft.MainAxisAlignment.CENTER
                            ),
                            # width=w,
                            alignment=ft.alignment.Alignment(0, -1),
                        )
                    ),
                    ft.Row(
                        [
                            ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                         width=(w - w / 4.5) / 3),
                            tema
                        ],
                    ),
                    ft.Row(
                        [
                            ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                         width=(w - w / 4.5) / 3),
                            classu
                        ],
                    ),
                    ft.Row(
                        [
                            ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                         width=(w - w / 4.5) / 3),
                            next_btn
                        ],
                    ),
                    ft.Container(width=w / 3, height=h / 3)
                ],
                scroll=ft.ScrollMode.ADAPTIVE
            )
            page.clean()
            pagelet.content = ft.Row([globalpage, make_tasks])
            page.add(pagelet)
            page.update()
        elif state_page == 2:
            page.clean()
            pagelet.appbar.title = ft.Text("Журнал")
            pagelet.content = ft.Text("asda")
            page.add(pagelet)
            page.update()
        elif state_page == 3:
            page.clean()
            if option.text == "Без вариантов ответов":
                make_tasks1 = ft.Column([
                    ft.Container(
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                                 width=(w - w / 4.5) / 3),
                                    ft.Container(ft.Text(f"{vopr} вопрос", size=33),
                                                 alignment=ft.alignment.Alignment(-0.4, -0.9999),
                                                 width=(w - w / 4.5) / 3),
                                    ft.Container(end_test, alignment=ft.alignment.Alignment(0.5, -1),
                                                 width=(w - w / 4.5) / 3),
                                ], width=w
                            ),
                            alignment=ft.alignment.Alignment(0, -1)
                        ),
                    ),
                    ft.Divider(thickness=2),
                ], scroll=ft.ScrollMode.ADAPTIVE)
                make_tasks1.controls = make_tasks1.controls + list_make_tasks
                make_tasks1.controls = make_tasks1.controls + [ft.Divider(thickness=2),
                                                               ft.Row([ft.Container(
                                                                   alignment=ft.alignment.Alignment(
                                                                       -0.9, -0.9),
                                                                   width=(w - w / 4.5) / 3),
                                                                   ansver0]),
                                                               ft.Row([ft.Container(
                                                                   alignment=ft.alignment.Alignment(
                                                                       -0.9, -0.9),
                                                                   width=(w - w / 4.5) / 3),
                                                                   next_tasks]),
                                                               ft.Container(height=h / 8)]
                make_tasks1.controls = make_tasks1.controls + [ft.Container(height=h)]
                pagelet.content = ft.Row([globalpage, make_tasks1])
            else:
                make_tasks10 = ft.Column([
                    ft.Container(
                        ft.Row(
                            [
                                ft.Container(alignment=ft.alignment.Alignment(-0.9, -0.9), width=(w - w / 4.5) / 3),
                                ft.Container(ft.Text(f"{vopr} вопрос", size=33),
                                             alignment=ft.alignment.Alignment(0, -0),
                                             width=(w - w / 4.5) / 3),
                                ft.Container(end_test, alignment=ft.alignment.Alignment(0.8, -0.9),
                                             width=(w - w / 4.5) / 3),
                            ]
                        ),
                        alignment=ft.alignment.Alignment(0, -1), height=h / 15
                    ), ft.Column([ft.Divider(thickness=2), ft.Row([ft.Container(
                        alignment=ft.alignment.Alignment(
                            -0.9, -0.9),
                        width=(w - w / 4.5) / 3), question1]),
                                  ft.Row([ft.Container(
                                      alignment=ft.alignment.Alignment(
                                          -0.9, -0.9),
                                      width=(w - w / 4.5) / 3), ansver]),
                                  ft.Divider(thickness=2), ft.Row([ft.Container(
                            alignment=ft.alignment.Alignment(
                                -0.9, -0.9),
                            width=(w - w / 4.5) / 3), next_tasks1]),
                                  ft.Container(height=h)])], scroll=ft.ScrollMode.ADAPTIVE)
                pagelet.content = ft.Row([globalpage, make_tasks10])
            page.add(pagelet)
            page.update()
        elif state_page == 4:
            visible_or_not = ft.Checkbox(label='Показать тест', value=list_task[2])
            classuc = ft.ExpansionTile(
                title=ft.Text("Классы"),
                # subtitle=ft.Text("Leading expansion arrow icon"),
                affinity=ft.TileAffinity.LEADING,
                initially_expanded=False,
                collapsed_text_color=ft.colors.BLUE,
                text_color=ft.colors.BLUE,
                controls=[ft.ListTile(title=ft.Row([ft.Column(controls=cc, scroll=ft.ScrollMode.ADAPTIVE)]))],
                width=300,
                shape=ft.CircleBorder()
            )
            task = ft.Column(
                [
                    ft.Text(list_task[0], size=30, text_align=ft.TextAlign.RIGHT, no_wrap=True),
                    classuc,
                    visible_or_not,
                    save_task,
                    view_task,
                    change_task,
                    delite_task
                ]
            )
            page.clean()
            pagelet.content = ft.Row([globalpage, task])
            page.add(pagelet)
            page.update()
        elif state_page == 5:
            if a == 1:
                brp = 0
                state_page = 4
                page_resize1(1)
            else:
                viewtask = ft.Column([ft.Container(
                    ft.Container(
                        ft.Row(
                            [
                                ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                             width=(w - w / 4.5) / 3),
                                ft.Container(content=ft.Text(value=a[0], size=30),
                                             alignment=ft.alignment.Alignment(-0.4, -0.99999),
                                             width=(w - w / 4.5) / 3, height=h / 9),
                                ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                             width=(w - w / 4.5) / 3, ),
                            ],
                            width=w
                            # alignment=ft.MainAxisAlignment.CENTER
                        ),
                        # width=w,
                        alignment=ft.alignment.Alignment(0, -1),
                    )
                ),
                    ft.Row(
                        [
                            ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                         width=(w - w / 4.5) / 3),
                            ft.Text("Вопрос:", size=20)
                        ],
                    ),
                ], scroll=ft.ScrollMode.ADAPTIVE)
                sda = 0
                for i in range(len(a) - 1, 0, -1):
                    if a[i] == 'otv':
                        viewtask.controls.insert(2, ft.Row(
                            [
                                ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                             width=(w - w / 4.5) / 3),
                                ft.Text("Ответ:", size=20)
                            ],
                        ))
                        continue
                    elif a[i] == 'Anya':
                        sda = 1
                        continue
                    viewtask.controls.insert(2, ft.Row(
                        [
                            ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                         width=(w - w / 4.5) / 3),
                            ft.Text(a[i], size=20)
                        ],
                    ))
                else:
                    if sda == 0:
                        viewtask.controls.insert(3, ft.Row(
                            [
                                ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                             width=(w - w / 4.5) / 3, height=h / 40),
                            ],
                        ))
                    viewtask.controls.insert(-2, ft.Row(
                        [
                            ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                         width=(w - w / 4.5) / 3, height=h / 40),
                        ],
                    ))
                    viewtask.controls.append(ft.Row(
                        [
                            ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                         width=(w - w / 4.5) / 3, height=h / 40),
                            ft.ElevatedButton("Далее", on_click=click_next_quest)
                        ],
                    ))
                page.clean()
                pagelet.content = ft.Row([globalpage, viewtask])
                page.add(pagelet)
                page.update()
        elif state_page == 6:
            if a == 1:
                brp = 0
                state_page = 4
                page_resize1(1)
            else:
                viewtask = ft.Column([ft.Container(
                    content=ft.Container(
                        content=ft.Row(
                            [
                                ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                             width=(w - w / 4.5) / 3),
                                ft.Container(ft.Text(a[0], size=30),
                                             alignment=ft.alignment.Alignment(-0.4, -0.99999),
                                             width=(w - w / 4.5) / 3, height=h / 9),
                                ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                             width=(w - w / 4.5) / 3, ),
                            ],
                            width=w
                            # alignment=ft.MainAxisAlignment.CENTER
                        ),
                        # width=w,
                        alignment=ft.alignment.Alignment(0, -1),
                    )
                ),
                    ft.Row(
                        [
                            ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                         width=(w - w / 4.5) / 3),
                            ft.Text("Вопрос:", size=20)
                        ],
                    ),
                ], scroll=ft.ScrollMode.ADAPTIVE)
                sda = 0
                for i in range(len(a) - 1, 0, -1):
                    if a[i] == 'otv':
                        viewtask.controls.insert(2, ft.Row(
                            [
                                ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                             width=(w - w / 4.5) / 3),
                                ft.Text("Ответ:", size=20)
                            ],
                        ))
                        continue
                    elif a[i] == 'Anya':
                        sda = 1
                        continue
                    viewtask.controls.insert(2, ft.Row(
                        [
                            ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                         width=(w - w / 4.5) / 3),
                            ft.TextField(a[i])
                        ],
                    ))
                else:
                    if sda == 0:
                        viewtask.controls.insert(3, ft.Row(
                            [
                                ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                             width=(w - w / 4.5) / 3, height=h / 40),
                            ],
                        ))
                    viewtask.controls.insert(-2, ft.Row(
                        [
                            ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                         width=(w - w / 4.5) / 3, height=h / 40),
                        ],
                    ))
                    viewtask.controls.append(ft.Row(
                        [
                            ft.Container(alignment=ft.alignment.Alignment(-1, -1),
                                         width=(w - w / 4.5) / 3, height=h / 40),
                            ft.ElevatedButton("Далее", on_click=click_next_quest1)
                        ],
                    ))
                    viewtask.controls.append(ft.Container(height=h/2))

                page.clean()
                pagelet.content = ft.Row([globalpage, viewtask])
                page.add(pagelet)
                page.update()

    def ansver():
        global brf, list_task
        lis = [list_task[3 + brf]]
        for i in list_task[4 + brf]:
            if i == 'otv':
                brf = list_task.index(i) + 1
                break
            if i == 'Anya':
                brf += 3
                lis.append(list_task[4 + brf + 1])
                break
            lis.append(i)
        return lis

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
        page.update()

    def val(e):
        breakp = 0
        global classs
        for i in c:
            if i.value:
                if i.label in classs:
                    pass
                else:
                    classs.append(i.label)
                breakp = 1
            else:
                if i.label in classs:
                    classs.remove(i.label)
        if breakp == 0 or not tema.value:
            next_btn.disabled = True
            page.update()
        else:
            next_btn.disabled = False
            page.update()

    def val1(e):
        for i in ansver1:
            if ansver0.value:
                pass
            else:
                next_tasks.disabled = True
                page.update()
                break
            if question.value:
                pass
            else:
                next_tasks.disabled = True
                page.update()
                break
            if i.value:
                pass
            else:
                next_tasks.disabled = True
                page.update()
                break
        else:
            next_tasks.disabled = False
            page.update()

    def val05(e):
        if question1.value:
            next_tasks1.disabled = False
        else:
            next_tasks1.disabled = True
        page.update()

    def quest(a):
        global ss, brp, change1, cc
        z = []
        for i in range(ss, len(a)):
            i = a[i]
            if i == 'otv' or i == 'Anya':
                z.append(i)
                z.append(a[a.index(i) + 1])
                ss = a.index(i) + 2
                break
            z.append(i)
        if brp == ss:
            click_next_quest1(1)
            client = socket.socket()  # создаем сокет клиента
            HOST = (socket.gethostname(), 55555)
            client.connect(HOST)  # подключаемся к серверу
            a = [8, login.value, password.value, task[nombertest][0], task[nombertest][1], task[nombertest][2]] + change1
            client.send(str(a).encode())
            client.close()
            print(a)
            change1 = []
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
                c.append(ft.Checkbox(label=i, value=False, height=25, on_change=val))
            client.close()

            cc = c.copy()
            return 1
        brp = ss
        return z

    def click_next_quest(e):
        global a
        a = quest(list_task)
        page_resize1(1)

    def click_next_quest1(e):
        global a, viewtask, change1
        if e != 1:
            a = quest(list_task)
        dddd = 0
        f = [viewtask.controls[0].content.content.controls[1].content.value]
        for i in viewtask.controls:
            if dddd == 0:
                dddd = 1
                continue
            try:
                if i.controls[len(i.controls) - 1].value == 'Вопрос:':
                    try:
                        if viewtask.controls[viewtask.controls.index(i)+2] == viewtask.controls[-2]:
                            f.append('Anya')
                    except IndexError:
                        pass
                elif i.controls[len(i.controls) - 1].value == 'Ответ:':
                    f.append('otv')
                else:
                    f.append(i.controls[len(i.controls) - 1].value)  # AttributeError
            except AttributeError:
                pass
        print(f)
        change1 += f
        page_resize1(1)

    def click_next(e):
        global state_page
        state_page = 3
        page_resize1(1)

    def change(e):
        if option.text == "С вариантам ответов":
            ansver.title = ft.Text(option.text)
            option.text = "Без вариантов ответов"
        else:
            ansver.title = ft.Text(option.text)
            option.text = "С вариантам ответов"
        ansver.initially_expanded = False
        page_resize1(1)

    def click_make_ansver(e):
        global list_make_ansver, w, h
        w = page.window_width
        h = page.window_height
        А = len(ansver1)
        ansver1.append(ft.TextField(label="Вариант ответа", on_change=val1))
        val1(1)
        list_make_tasks.append(ft.Row(
            controls=[ft.Container(alignment=ft.alignment.Alignment(-0.9, -0.9), width=(w - w / 4.5) / 3), ansver1[А]]))
        page_resize1(1)

    def click_nomber_tasks():
        global nombertest, state_page, list_task, cc, c
        state_page = 4
        print(task[nombertest])
        list_task = task[nombertest]
        for i in cc:
            i.value = False
        for i in cc:
            if i.label in list_task[1]:
                i.value = True
        page_resize1(1)

    def click_make_tasks(e):
        global test, ansver1, list_make_tasks, vopr, w, h
        w = page.window_width
        h = page.window_height
        test.append(vopr)
        test.append(question.value)
        for i in ansver1:
            test.append(i.value)
        test.append('otv')
        test.append(ansver0.value)
        del ansver1
        ansver1 = [ft.TextField(label="Вариант ответа", on_change=val1),
                   ft.TextField(label="Вариант ответа", on_change=val1), ]
        vopr += 1
        ansver0.value = ''
        question.value = ''
        list_make_tasks = [
            ft.Divider(thickness=2),
            ft.Row(
                [
                    ft.Container(alignment=ft.alignment.Alignment(-0.9, -0.9), width=(w - w / 4.5) / 3), question
                ],
            ),
            ft.Row(
                [
                    ft.Container(alignment=ft.alignment.Alignment(-0.9, -0.9), width=(w - w / 4.5) / 3), ansver
                ],
            ),
            ft.Divider(thickness=2),
            ft.Row(
                [
                    ft.Container(alignment=ft.alignment.Alignment(-0.9, -0.9), width=(w - w / 4.5) / 3), make_ansver
                ],
            ),
            ft.Row(
                [
                    ft.Container(alignment=ft.alignment.Alignment(-0.9, -0.9), width=(w - w / 4.5) / 3), ansver1[0]
                ],
            ),
            ft.Row(
                [
                    ft.Container(alignment=ft.alignment.Alignment(-0.9, -0.9), width=(w - w / 4.5) / 3), ansver1[1]
                ],
            ),
        ]
        next_tasks.disabled = True
        page.clean()
        page_resize1(1)

    def click_make_tasks1(e):
        global test, vopr
        test.append(vopr)
        test.append("Anya")
        test.append(question1.value)
        vopr += 1
        question1.value = ''
        next_tasks1.disabled = True
        page.clean()
        page_resize1(1)

    def click_end_test(e):
        global test, state_page, task, tasks
        client = socket.socket()  # создаем сокет клиента
        HOST = (socket.gethostname(), 55555)
        client.connect(HOST)  # подключаемся к серверу
        classs.sort()
        test.insert(0, False)
        test.insert(0, classs)
        test.insert(0, tema.value)
        t = test.copy()
        test.insert(0, password.value)
        test.insert(0, login.value)
        test.insert(0, 4)
        client.send(str(test).encode())
        tema.value = ''
        data = client.recv(40000)
        if data.decode() == '0':
            page.snack_bar = ft.SnackBar(ft.Text("У вас уже есть тест той же темой. Тетс не создан"))
            page.snack_bar.open = True
            page.update()
            time.sleep(1)
            page.clean()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Тест создан"))
            page.snack_bar.open = True
            tasks = ft.ListView(expand=100000, spacing=10, padding=20, controls=[
                ft.Row(
                    [
                        ft.ElevatedButton("Создать новый тест", on_click=click_new_tasks)],
                    alignment=ft.MainAxisAlignment.CENTER), ft.Divider(thickness=2),
            ])
            task.append(t)
            task.sort()
            make_tasks()
            page.update()
            time.sleep(1)
            page.clean()
        client.close()
        test = []
        state_page = 0
        page_resize1(1)

    def click_view_task(e):
        global state_page, a, ss, list_task
        print(list_task)
        ss = 3
        state_page = 5
        a = quest(list_task)
        page_resize1(1)

    def click_save_task(e):
        global task, tasks, visible_or_not, list_task, classs
        task.remove(list_task)
        list_task.pop(1)
        val(1)
        list_task.insert(1, classs)
        list_task.pop(2)
        if visible_or_not.value:
            list_task.insert(2, True)
        else:
            list_task.insert(2, False)
        task.append(list_task)
        tasks = ft.ListView(expand=100000, spacing=10, padding=20, controls=[
            ft.Row(
                [
                    ft.ElevatedButton("Создать новый тест", on_click=click_new_tasks)],
                alignment=ft.MainAxisAlignment.CENTER), ft.Divider(thickness=2),
        ])
        task.sort()
        make_tasks()
        client = socket.socket()  # создаем сокет клиента
        HOST = (socket.gethostname(), 55555)
        client.connect(HOST)  # подключаемся к серверу
        client.send(str([7, login.value, password.value] + list_task).encode())
        client.close()
        page_resize1(1)

    def click_delite_task(e):
        global state_page, tasks
        state_page = 0
        task.remove(list_task)
        client = socket.socket()  # создаем сокет клиента
        HOST = (socket.gethostname(), 55555)
        client.connect(HOST)  # подключаемся к серверу
        А = [6, login.value, password.value, list_task[0]]
        client.send(str(А).encode())
        client.close()
        А = 0.1
        for i in tasks.controls:
            try:
                if i.text == list_task[0]:
                    А = tasks.controls.index(i)
            except AttributeError:
                pass
        tasks.controls.pop(А)
        tasks.controls.pop(А)
        page_resize1(1)

    def click_change_task(e):
        global state_page, a, ss, list_task
        ss = 3
        state_page = 6
        a = quest(list_task)
        page_resize1(1)

    def _0(e):
        global nombertest
        nombertest = 0
        click_nomber_tasks()

    def _1(e):
        global nombertest
        nombertest = 1
        click_nomber_tasks()

    def _2(e):
        global nombertest
        nombertest = 2
        click_nomber_tasks()

    def _3(e):
        global nombertest
        nombertest = 3
        click_nomber_tasks()

    def _4(e):
        global nombertest
        nombertest = 4
        click_nomber_tasks()

    def _5(e):
        global nombertest
        nombertest = 5
        click_nomber_tasks()

    def _6(e):
        global nombertest
        nombertest = 6
        click_nomber_tasks()

    def _7(e):
        global nombertest
        nombertest = 7
        click_nomber_tasks()

    def _8(e):
        global nombertest
        nombertest = 8
        click_nomber_tasks()

    def _9(e):
        global nombertest
        nombertest = 9
        click_nomber_tasks()

    def _10(e):
        global nombertest
        nombertest = 10
        click_nomber_tasks()

    def _11(e):
        global nombertest
        nombertest = 11
        click_nomber_tasks()

    def _12(e):
        global nombertest
        nombertest = 12
        click_nomber_tasks()

    def _13(e):
        global nombertest
        nombertest = 13
        click_nomber_tasks()

    def _14(e):
        global nombertest
        nombertest = 14
        click_nomber_tasks()

    def _15(e):
        global nombertest
        nombertest = 15
        click_nomber_tasks()

    def _16(e):
        global nombertest
        nombertest = 16
        click_nomber_tasks()

    def _17(e):
        global nombertest
        nombertest = 17
        click_nomber_tasks()

    def _18(e):
        global nombertest
        nombertest = 18
        click_nomber_tasks()

    def _19(e):
        global nombertest
        nombertest = 19
        click_nomber_tasks()

    def _20(e):
        global nombertest
        nombertest = 20
        click_nomber_tasks()

    def _21(e):
        global nombertest
        nombertest = 21
        click_nomber_tasks()

    def _22(e):
        global nombertest
        nombertest = 22
        click_nomber_tasks()

    def _23(e):
        global nombertest
        nombertest = 23
        click_nomber_tasks()

    def _24(e):
        global nombertest
        nombertest = 24
        click_nomber_tasks()

    def _25(e):
        global nombertest
        nombertest = 25
        click_nomber_tasks()

    def _26(e):
        global nombertest
        nombertest = 26
        click_nomber_tasks()

    def _27(e):
        global nombertest
        nombertest = 27
        click_nomber_tasks()

    def _28(e):
        global nombertest
        nombertest = 28
        click_nomber_tasks()

    def _29(e):
        global nombertest
        nombertest = 29
        click_nomber_tasks()

    def _30(e):
        global nombertest
        nombertest = 30
        click_nomber_tasks()

    def _31(e):
        global nombertest
        nombertest = 31
        click_nomber_tasks()

    def _32(e):
        global nombertest
        nombertest = 32
        click_nomber_tasks()

    def _33(e):
        global nombertest
        nombertest = 33
        click_nomber_tasks()

    def _34(e):
        global nombertest
        nombertest = 34
        click_nomber_tasks()

    def _35(e):
        global nombertest
        nombertest = 35
        click_nomber_tasks()

    def _36(e):
        global nombertest
        nombertest = 36
        click_nomber_tasks()

    def _37(e):
        global nombertest
        nombertest = 37
        click_nomber_tasks()

    def _38(e):
        global nombertest
        nombertest = 38
        click_nomber_tasks()

    def _39(e):
        global nombertest
        nombertest = 39
        click_nomber_tasks()

    def _40(e):
        global nombertest
        nombertest = 40
        click_nomber_tasks()

    def _41(e):
        global nombertest
        nombertest = 41
        click_nomber_tasks()

    def _42(e):
        global nombertest
        nombertest = 42
        click_nomber_tasks()

    def _43(e):
        global nombertest
        nombertest = 43
        click_nomber_tasks()

    def _44(e):
        global nombertest
        nombertest = 44
        click_nomber_tasks()

    def _45(e):
        global nombertest
        nombertest = 45
        click_nomber_tasks()

    def _46(e):
        global nombertest
        nombertest = 46
        click_nomber_tasks()

    def _47(e):
        global nombertest
        nombertest = 47
        click_nomber_tasks()

    def _48(e):
        global nombertest
        nombertest = 48
        click_nomber_tasks()

    def _49(e):
        global nombertest
        nombertest = 49
        click_nomber_tasks()

    def _50(e):
        global nombertest
        nombertest = 50
        click_nomber_tasks()

    def _51(e):
        global nombertest
        nombertest = 51
        click_nomber_tasks()

    def _52(e):
        global nombertest
        nombertest = 52
        click_nomber_tasks()

    def _53(e):
        global nombertest
        nombertest = 53
        click_nomber_tasks()

    def _54(e):
        global nombertest
        nombertest = 54
        click_nomber_tasks()

    def _55(e):
        global nombertest
        nombertest = 55
        click_nomber_tasks()

    def _56(e):
        global nombertest
        nombertest = 56
        click_nomber_tasks()

    def _57(e):
        global nombertest
        nombertest = 57
        click_nomber_tasks()

    def _58(e):
        global nombertest
        nombertest = 58
        click_nomber_tasks()

    def _59(e):
        global nombertest
        nombertest = 59
        click_nomber_tasks()

    def _60(e):
        global nombertest
        nombertest = 60
        click_nomber_tasks()

    def _61(e):
        global nombertest
        nombertest = 61
        click_nomber_tasks()

    def _62(e):
        global nombertest
        nombertest = 62
        click_nomber_tasks()

    def _63(e):
        global nombertest
        nombertest = 63
        click_nomber_tasks()

    def _64(e):
        global nombertest
        nombertest = 64
        click_nomber_tasks()

    def _65(e):
        global nombertest
        nombertest = 65
        click_nomber_tasks()

    def _66(e):
        global nombertest
        nombertest = 66
        click_nomber_tasks()

    def _67(e):
        global nombertest
        nombertest = 67
        click_nomber_tasks()

    def _68(e):
        global nombertest
        nombertest = 68
        click_nomber_tasks()

    def _69(e):
        global nombertest
        nombertest = 69
        click_nomber_tasks()

    def _70(e):
        global nombertest
        nombertest = 70
        click_nomber_tasks()

    def _71(e):
        global nombertest
        nombertest = 71
        click_nomber_tasks()

    def _72(e):
        global nombertest
        nombertest = 72
        click_nomber_tasks()

    def _73(e):
        global nombertest
        nombertest = 73
        click_nomber_tasks()

    def _74(e):
        global nombertest
        nombertest = 74
        click_nomber_tasks()

    def _75(e):
        global nombertest
        nombertest = 75
        click_nomber_tasks()

    def _76(e):
        global nombertest
        nombertest = 76
        click_nomber_tasks()

    def _77(e):
        global nombertest
        nombertest = 77
        click_nomber_tasks()

    def _78(e):
        global nombertest
        nombertest = 78
        click_nomber_tasks()

    def _79(e):
        global nombertest
        nombertest = 79
        click_nomber_tasks()

    def _80(e):
        global nombertest
        nombertest = 80
        click_nomber_tasks()

    def _81(e):
        global nombertest
        nombertest = 81
        click_nomber_tasks()

    def _82(e):
        global nombertest
        nombertest = 82
        click_nomber_tasks()

    def _83(e):
        global nombertest
        nombertest = 83
        click_nomber_tasks()

    def _84(e):
        global nombertest
        nombertest = 84
        click_nomber_tasks()

    def _85(e):
        global nombertest
        nombertest = 85
        click_nomber_tasks()

    def _86(e):
        global nombertest
        nombertest = 86
        click_nomber_tasks()

    def _87(e):
        global nombertest
        nombertest = 87
        click_nomber_tasks()

    def _88(e):
        global nombertest
        nombertest = 88
        click_nomber_tasks()

    def _89(e):
        global nombertest
        nombertest = 89
        click_nomber_tasks()

    def _90(e):
        global nombertest
        nombertest = 90
        click_nomber_tasks()

    def _91(e):
        global nombertest
        nombertest = 91
        click_nomber_tasks()

    def _92(e):
        global nombertest
        nombertest = 92
        click_nomber_tasks()

    def _93(e):
        global nombertest
        nombertest = 93
        click_nomber_tasks()

    def _94(e):
        global nombertest
        nombertest = 94
        click_nomber_tasks()

    def _95(e):
        global nombertest
        nombertest = 95
        click_nomber_tasks()

    def _96(e):
        global nombertest
        nombertest = 96
        click_nomber_tasks()

    def _97(e):
        global nombertest
        nombertest = 97
        click_nomber_tasks()

    def _98(e):
        global nombertest
        nombertest = 98
        click_nomber_tasks()

    def _99(e):
        global nombertest
        nombertest = 99
        click_nomber_tasks()

    def _100(e):
        global nombertest
        nombertest = 100
        click_nomber_tasks()

    def _101(e):
        global nombertest
        nombertest = 101
        click_nomber_tasks()

    def _102(e):
        global nombertest
        nombertest = 102
        click_nomber_tasks()

    def _103(e):
        global nombertest
        nombertest = 103
        click_nomber_tasks()

    def _104(e):
        global nombertest
        nombertest = 104
        click_nomber_tasks()

    def _105(e):
        global nombertest
        nombertest = 105
        click_nomber_tasks()

    def _106(e):
        global nombertest
        nombertest = 106
        click_nomber_tasks()

    def _107(e):
        global nombertest
        nombertest = 107
        click_nomber_tasks()

    def _108(e):
        global nombertest
        nombertest = 108
        click_nomber_tasks()

    def _109(e):
        global nombertest
        nombertest = 109
        click_nomber_tasks()

    def _110(e):
        global nombertest
        nombertest = 110
        click_nomber_tasks()

    def _111(e):
        global nombertest
        nombertest = 111
        click_nomber_tasks()

    def _112(e):
        global nombertest
        nombertest = 112
        click_nomber_tasks()

    def _113(e):
        global nombertest
        nombertest = 113
        click_nomber_tasks()

    def _114(e):
        global nombertest
        nombertest = 114
        click_nomber_tasks()

    def _115(e):
        global nombertest
        nombertest = 115
        click_nomber_tasks()

    def _116(e):
        global nombertest
        nombertest = 116
        click_nomber_tasks()

    def _117(e):
        global nombertest
        nombertest = 117
        click_nomber_tasks()

    def _118(e):
        global nombertest
        nombertest = 118
        click_nomber_tasks()

    def _119(e):
        global nombertest
        nombertest = 119
        click_nomber_tasks()

    def _120(e):
        global nombertest
        nombertest = 120
        click_nomber_tasks()

    def _121(e):
        global nombertest
        nombertest = 121
        click_nomber_tasks()

    def _122(e):
        global nombertest
        nombertest = 122
        click_nomber_tasks()

    page.on_resize = page_resize1
    # page.window_full_screen = True
    page.padding = ft.padding.only(top=0, left=0)

    global c, state_page, index, vopr, test, ansver1, list_make_tasks, classs, tasks, w, h, foc, nombertest, list_task, cc, task, visible_or_not, brf, ss, a, brp, viewtask, change1
    change1 = []
    brp = 0
    ss = 3
    nombertest = 0.1
    c = []
    cc = []
    brf = 0
    state_page = 0
    index = 0
    vopr = 0
    test = []
    classs = []
    w = page.window_width
    h = page.window_height
    foc = 0
    list_task = [0, [], False]

    # btn
    next_btn = ft.ElevatedButton("Далее", width=300, disabled=True, on_click=click_next)
    option = ft.CupertinoButton("Без вариантов ответов", width=300, on_click=change)
    make_ansver = ft.ElevatedButton("Новый вариант ответа", width=300, on_click=click_make_ansver)
    next_tasks = ft.ElevatedButton("Следующие задание", width=300, disabled=True, on_click=click_make_tasks)
    next_tasks1 = ft.ElevatedButton("Следующие задание", width=300, disabled=True, on_click=click_make_tasks1)
    end_test = ft.ElevatedButton("Закончить тест", on_click=click_end_test)
    view_task = ft.ElevatedButton("Просмотреть тест", on_click=click_view_task)
    save_task = ft.ElevatedButton("Сохранить", on_click=click_save_task)
    delite_task = ft.ElevatedButton("Удалить тест", on_click=click_delite_task)
    change_task = ft.ElevatedButton("Измененить тест", on_click=click_change_task)

    # text
    tema = ft.TextField(label="Тема", border=ft.InputBorder.UNDERLINE, on_change=val)
    question = ft.TextField(label="Вопрос", on_change=val1)
    question1 = ft.TextField(label="Вопрос", on_change=val05)
    ansver0 = ft.TextField(label="Ответ", on_change=val1)

    ansver1 = [ft.TextField(label="Вариант ответа", on_change=val1),
               ft.TextField(label="Вариант ответа", on_change=val1), ]

    # chtckbox
    visible_or_not = ft.Checkbox(label='Показать тест', value=list_task[2])

    w = page.window_width
    h = page.window_height

    classu = ft.ExpansionTile(
        title=ft.Text("Классы"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[ft.ListTile(title=ft.Row([ft.Column(c, scroll=ft.ScrollMode.ADAPTIVE)]))],
        width=300,
        shape=ft.CircleBorder()
    )
    classuc = ft.ExpansionTile(
        title=ft.Text("Классы"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[ft.ListTile(title=ft.Row([ft.Column(controls=cc, scroll=ft.ScrollMode.ADAPTIVE)]))],
        width=300,
        shape=ft.CircleBorder()
    )
    ansver = ft.ExpansionTile(
        title=ft.Text("С вариантам ответов"),
        # subtitle=ft.Text("Leading expansion arrow icon"),
        affinity=ft.TileAffinity.LEADING,
        initially_expanded=False,
        collapsed_text_color=ft.colors.BLUE,
        text_color=ft.colors.BLUE,
        controls=[option],
        width=300,
        # shape=ft.CircleBorder()
    )
    tasks = ft.ListView(expand=100000, spacing=10, padding=20, controls=[
        ft.Row(
            [
                ft.ElevatedButton("Создать новый тест", on_click=click_new_tasks)],
            alignment=ft.MainAxisAlignment.CENTER), ft.Divider(thickness=2),
    ])

    list_make_tasks = [
        ft.Row([ft.Container(alignment=ft.alignment.Alignment(-0.9, -0.9), width=(w - w / 4.5) / 3), question], ),
        ft.Row(
            [
                ft.Container(alignment=ft.alignment.Alignment(-0.9, -0.9), width=(w - w / 4.5) / 3), ansver
            ],
        ),
        ft.Divider(thickness=2),
        ft.Row(
            [
                ft.Container(alignment=ft.alignment.Alignment(-0.9, -0.9), width=(w - w / 4.5) / 3), make_ansver
            ],
        ),
        ft.Row(
            [
                ft.Container(alignment=ft.alignment.Alignment(-0.9, -0.9), width=(w - w / 4.5) / 3), ansver1[0]
            ],
        ),
        ft.Row(
            [
                ft.Container(alignment=ft.alignment.Alignment(-0.9, -0.9), width=(w - w / 4.5) / 3), ansver1[1]
            ],
        ),
    ]

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
        c.append(ft.Checkbox(label=i, value=False, height=25, on_change=val))
    client.close()

    cc = c.copy()

    client = socket.socket()  # создаем сокет клиента
    HOST = (socket.gethostname(), 55555)
    client.connect(HOST)  # подключаемся к серверу
    А = [5, login.value, password.value]
    client.send(str(А).encode())
    task = client.recv(40000)
    task = task.decode()
    task = ast.literal_eval(task)
    client.close()

    def make_tasks():
        global task, tasks
        А = 0
        for i in task:
            if А == 0:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_0, ))
            if А == 1:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_1, ))
            if А == 2:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_2, ))
            if А == 3:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_3, ))
            if А == 4:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_4, ))
            if А == 5:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_5, ))
            if А == 6:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_6, ))
            if А == 7:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_7, ))
            if А == 8:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_8, ))
            if А == 9:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_9, ))
            if А == 10:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_10, ))
            if А == 11:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_11, ))
            if А == 12:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_12, ))
            if А == 13:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_13, ))
            if А == 14:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_14))
            if А == 15:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_15))
            if А == 16:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_16))
            if А == 17:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_17))
            if А == 18:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_18))
            if А == 19:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_19))
            if А == 20:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_20))
            if А == 21:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_21))
            if А == 22:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_22, ))
            if А == 23:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_23, ))
            if А == 24:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_24, ))
            if А == 25:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_25, ))
            if А == 26:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_26))
            if А == 27:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_27))
            if А == 28:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_28))
            if А == 29:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_29))
            if А == 30:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_30))
            if А == 31:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_31))
            if А == 32:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_32))
            if А == 33:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_33))
            if А == 34:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_34, ))
            if А == 35:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_35, ))
            if А == 36:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_36, ))
            if А == 37:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_37, ))
            if А == 38:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_38, ))
            if А == 39:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_39, ))
            if А == 40:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_40, ))
            if А == 41:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_41, ))
            if А == 42:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_42, ))
            if А == 43:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_43, ))
            if А == 44:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_44, ))
            if А == 45:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_45, ))
            if А == 46:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_46, ))
            if А == 47:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_47, ))
            if А == 48:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_48))
            if А == 49:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_49))
            if А == 50:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_50))
            if А == 51:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_51))
            if А == 52:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_52))
            if А == 53:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_53))
            if А == 54:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_54))
            if А == 55:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_55))
            if А == 56:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_56))
            if А == 57:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_57))
            if А == 58:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_58))
            if А == 59:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_59))
            if А == 60:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_60))
            if А == 61:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_61))
            if А == 62:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_62))
            if А == 63:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_63))
            if А == 64:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_64))
            if А == 65:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_65))
            if А == 66:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_66))
            if А == 67:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_67))
            if А == 68:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_68))
            if А == 69:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_69))
            if А == 70:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_70))
            if А == 71:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_71))
            if А == 72:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_72))
            if А == 73:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_73))
            if А == 74:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_74))
            if А == 75:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_75))
            if А == 76:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_76))
            if А == 77:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_77))
            if А == 78:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_78))
            if А == 79:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_79))
            if А == 80:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_80))
            if А == 81:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_81))
            if А == 82:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_82))
            if А == 83:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_83))
            if А == 84:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_84))
            if А == 85:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_85))
            if А == 86:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_86))
            if А == 87:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_87))
            if А == 88:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_88))
            if А == 89:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_89))
            if А == 90:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_90))
            if А == 91:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_91))
            if А == 92:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_92))
            if А == 93:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_93))
            if А == 94:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_94))
            if А == 95:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_95))
            if А == 96:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_96))
            if А == 97:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_97))
            if А == 98:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_98))
            if А == 99:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_99))
            if А == 100:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_100))
            if А == 101:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_101))
            if А == 102:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_102))
            if А == 103:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_103))
            if А == 104:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_104))
            if А == 105:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_105))
            if А == 106:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_106))
            if А == 107:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_107))
            if А == 108:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_108))
            if А == 109:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_109))
            if А == 110:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_110))
            if А == 111:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_111))
            if А == 112:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_112))
            if А == 113:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_113))
            if А == 114:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_114))
            if А == 115:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_115))
            if А == 116:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_116))
            if А == 117:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_117))
            if А == 118:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_118))
            if А == 119:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_119))
            if А == 120:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_120))
            if А == 121:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_121))
            if А == 122:
                tasks.controls.append(ft.TextButton(text=f"{i[0]}", on_click=_122))
            tasks.controls.append(ft.Divider(thickness=2))
            А += 1

    make_tasks()

    page_resize1(1)


ft.app(target=main)
# view=ft.AppView.WEB_BROWSER
