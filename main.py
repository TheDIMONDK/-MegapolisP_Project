import csv

def merge(left, right, compare):
    """ Сортировка слиянием

    :param left: Левый массив
    :param right: Правый массив
    :param compare: Центральный массив
    :return: Отсортированный массив
    """

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


data = []

# Считываем исходные данные из файла
with open("songs.txt", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="?")
    for row in reader:
        data.append(row)


def task_1():
    """ 1 задание
    """

    arName = input("1) Введите имя артиста: ")
    curArData = []
    for row in data:
        if row[1] == arName:
            curArData.append(row)

    with open("songs_artist.csv", "w", encoding="utf-8") as f2:
        # Очистим файл
        f2.truncate()

        writer = csv.writer(f2, delimiter="?")

        arr = []

        # Подготоваливаем данные к записи
        arr.append(["track_name", "streams", "date"])
        for i in range(0, len(curArData)):
            arr.append([curArData[i][2], curArData[i][0], curArData[i][3]])

        # Записываем данные
        writer.writerows(arr)

def task_2():
    """ 2 задание
    """

    # with open("songs.txt", "w", encoding="utf-8") as f3:
    #     # Очистим файл
    #     f3.truncate()
    #
    #     writer = csv.writer(f3, delimiter="?")
    #
    #     sortedData = merge(data, [], [])
    #
    #     print("2) ", end="")
    #     print(sortedData)


def task_3():
    """ 3 задание
    """

    pesName = input("3) Введите название песни: ")
    while pesName != "0":
        curArData2 = []
        for row in data:
            # Если название песни совпадает
            if row[2] == pesName:
                curArData2.append(row)

        if len(curArData2) > 0:
            for i in range(0, len(curArData2)):
                print(f"Песня {pesName} принадлежит {curArData2[i][1]}")
        else:
            print("К сожалению, ничего не удалось найти")

        pesName = input("3) Введите название песни: ")


def task_4():
    """ 4 задание
    """

    lessArr = []

    for i in range(0, len(data)):
        if int(data[i][3].split(".")[2]) < 1900:
            lessArr.append(data[i])

    with open("songs_average.txt", "w", encoding="utf-8") as f4:
        # Очистим файл
        f4.truncate()

        writer = csv.writer(f4, delimiter="?")

        # Записываем данные
        writer.writerow(["streams", "artist_name", "track_name", "date"])
        writer.writerows(lessArr)

def task_5():
    """ 5 задание
    """

    hTable = {}
    for i in range(1, len(data)):
        # Название песни
        sName = data[i][2]

        # Данные об артисте
        arData = [ { "artist_name": data[i][1], "streams": data[i][2], "date": data[i][3] } ]

        co = 0
        for row in data:
            if row[2] == sName:
                co += 1

                # Если композиций с таким названием больше одной
                if co > 1:
                    arData.append({ "artist_name": row[1], "streams": row[2], "date": row[3] })

        hTable[sName] = arData

    print("5) ", end="")
    print(hTable)


############################################


num = int(input("Введите номер задания: "))
if num == 1: task_1()
elif num == 2: task_2()
elif num == 3: task_3()
elif num == 4: task_4()
elif num == 5: task_5()
else: print("Некорректный номер задания!")