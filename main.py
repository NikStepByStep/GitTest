from prettytable import PrettyTable #Библиотека красивых таблиц)

#Обновление и вывод таблицы
def t_update():
    T = PrettyTable()
    T.field_names = ["ISBN", "Author", "Caption", "Year", "Pages"] #Заголовки таблицы

    with open("database.txt", "r") as f: #Открываем фаел
        f_info = [str(i) for i in f]  #Получаем строчки файла
        for j in range(len(f_info)):
            f_current_info_prepare = [str(n) for n in f_info[j]] #Получаем символы кадой строчки
            f_current_info = ""
            #Собираем отдельные символы строчик в полноценные слова
            for k in range(len(f_current_info_prepare)-2):
                if f_current_info_prepare[k] != " ":
                    f_current_info = f_current_info + f_current_info_prepare[k]
                elif f_current_info_prepare[k] == " ":
                    f_current_info = f_current_info + " "

            # print(f_current_info.split()) Строчка для вывода каждой строки отдельно, использовалась для проверки при разработке
            T.add_row([(f_current_info.split())[0],(f_current_info.split())[1], (f_current_info.split())[2], (f_current_info.split())[3], (f_current_info.split())[4]])
    #Вывод таблицы
    print(T)

#Добавление в базу данных информации из файла
def t_add(file):
    with open(file, "r") as f_start:    #Открываем файл, откуда будем брать информацию
        with open("database.txt", "r+") as f_end: #Открываем нашу базу данных
            f_start_info = [str(i) for i in f_start.readlines()]    #Разделяем файл на отдельные строчки
            f_end_info = [str(i) for i in f_end.readlines()]    #Разделяем файл на отдельные строчки
            k = ""
            for j in range(4): #Исключаем лишние слова, которые помогали нам при обычном чтении в входящем файле
                if j == 0:
                    rep = "Author: "
                elif j == 1:
                    rep = "Caption: "
                elif j == 2:
                    rep = "Year: "
                elif j == 3:
                    rep = "Pages: "

                k = k + (f_start_info[j])[:len(f_start_info[j])-1].replace(rep, '') + " " #Создаём строчку, имеющую всю необходимую информацию, которую мы выведем в таблицу

            #Определение номера в строчке (НУЖНО ПЕРЕДЕЛАТЬ, ТАК КАК В СЛУЧАЕ [1, 3, 4, 2] ОН ДОБАВИЛ НОМЕР 3!!!!, В ДРУГИХ СЛУЧАЯХ РАБОТАЕТ)
            number = 1 #Если она пустая, то будет 1
            if int(len(f_end_info)) > 1: #Если нет, то определяем, есть ли "дырка"
                for m in range(len(f_end_info)-1):
                    if int((f_end_info[m+1])[0]) - int((f_end_info[m])[0]) != 1:
                        number1 = min(int((f_end_info[m+1])[0]), int((f_end_info[m])[0])) + 1 #Если есть, то присваем номер "дырки" новой ячеке
                    else:
                        number2 = int((f_end_info[len(f_end_info)-1])[0]) + 1 #Если нет, то даём следующий номер, идущий после последнего
                number = min(number1, number2)
            #Наконец, заносим строчку в базу данных таблицы
            f_end.write(str(number) + " " + k + "\n")
    print("Данные успешно добавлены\n")

#Удаление определённой ячейки, которую мы указали при вводе команды
def t_delete(ISBN):
    f = open("database.txt", "r") #Открываем базу данных для чтения всех строчек
    f_info = [str(i) for i in f]
    f.close()

    #Проверим, какие номера у нас есть
    numbers = []
    for j in range(len(f_info)):
        if ((f_info[j])[0]) not in numbers:
            numbers.append((f_info[j])[0]) #Получаем их список

    if str(ISBN) in numbers: #Если номер ячейки входит в данный список номеров
        fw = open("database.txt", "w") #Открываем базу данных для перезаписи

        #Проверяем каждую строчку, не совпадает ли её номер с той, что необходимо удалить
        for j in range(len(f_info)):
            if (int((f_info[j])[0]) != ISBN):
                fw.write(f_info[j]) #Если не совпадает, то заносим назад в базу данных
            elif (int((f_info[j])[0]) == ISBN):
                pass #Если совпадает, то не заносим(можно было не писать данную часть кода, но при разработке я её использовал для проверки, так что оставил на всякий случай на будущее)
        print("Ячейка под номером " + str(ISBN) + " успешно удалена\n")
        fw.close()
    else: #Если не входит в данный список номеров
        print("Ячейки под данным номером не существует\n")




#Основной цикл для ввода команд, просто проверка того, что вводит пользователь
while True:
    I = input("Введите команду (/help для вывода всех возможных команд)\n")
    #ГОТОВА
    if I == "/help":
        print("Команда     Результат\n" + "/list       Вывод всей базы данных \n" + "/find       Вывод искомой информации\n" + "/add        Добавление информации в базу данных\n" + "/edit       Изменение имеющейся информации\n" + "/delete     Удаление ячейки базы данных\n")
    #ГОТОВА
    elif I == "/list":
        t_update()
    #ГОТОВА, НО НУЖНО НЕМНОГО ПЕРЕДЕЛАТЬ
    elif I == "/add":
        filename = input("Укажите расположение файла, который вы хотите внести в электронную библиотеку\n")
        t_add(filename)
    #ГОТОВА
    elif I== "/delete":
        ISBN = int(input("Укажите номер ячейки, которую вы хотите удалить\n"))
        t_delete(ISBN)
    #НЕ ГОТОВА
    elif I == "/edit":
        print("Данная команда пока не работает, приходите позже\n")
    #НЕ ГОТОВА
    elif I == "/find":
        print("Данная команда пока не работает, приходите позже\n")
    else:
        print("Введёной команды не существует. Пожалуйста, ознакомтесь с списком коммандпри помощи ввода \help\n")