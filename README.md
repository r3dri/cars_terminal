# Автомобильная база данных (Terminal Edition)

## Описание

**Университетская лабораторная работа**

**Предмет:** [Основы программной инженерии]

Это консольное приложение на Python для управления базой данных автомобилей. Оно позволяет:

*   Просматривать список автомобилей в табличном виде.
*   Добавлять новые автомобили в базу данных, выбирая параметры из предложенных списков (производитель, модель, цвет и т.д.).
*   Удалять автомобили из базы данных по их номеру.
*   Изменять информацию об автомобилях.
*   Осуществлять поиск автомобилей по номеру.
*   Управлять списками параметров:
    *   Добавлять и удалять производителей.
    *   Добавлять и удалять модели для конкретного производителя.
    *   Добавлять и удалять цвета.

Программа использует текстовые файлы для хранения данных и библиотеку `tabulate` для удобного отображения данных в виде таблиц в терминале.

## Функциональность

Приложение предоставляет следующие функции:

*   **Главное меню:**
    *   Список машин
    *   Добавить авто
    *   Удалить авто
    *   Изменить авто
    *   Поиск авто
    *   Списки параметров
    *   Выйти

*   **Список машин:**  Отображение всех автомобилей в табличном формате. Возможность перехода к добавлению, удалению, изменению авто.

*   **Добавить авто:**  Интерактивное добавление нового автомобиля в базу данных с выбором параметров из существующих списков.

*   **Удалить авто:**  Удаление автомобиля из базы данных по его номеру.

*   **Изменить авто:**  Редактирование информации о существующем автомобиле.

*   **Поиск авто:**  Поиск автомобиля по номеру и отображение его данных.

*   **Списки параметров:** Управление списками производителей, моделей и цветов. Добавление и удаление элементов.

## Использование

1.  **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/r3dri/cars_terminal.git
    cd cars_terminal
    ```

2.  **Установите необходимые библиотеки:**

    ```bash
    pip install tabulate
    ```

3.  **Запустите приложение:**

    ```bash
    python cars_terminal.py
    ```

## Структура файлов

*   `main.py` – Основной файл с кодом приложения.
*   `data_source.txt` – Файл, содержащий данные об автомобилях (основная база данных).  Формат: `номер/производитель/модель/цвет/коробка передач/привод/тип двигателя/заведена/открыта/фары горят`
*   `data_proizvod.txt` – Файл, содержащий список производителей.
*   `data_marka.txt` – Файл, содержащий список моделей для каждого производителя. Формат: `производитель/модель1/модель2/...`
*   `data_color.txt` – Файл, содержащий список цветов.
