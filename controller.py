# import reading_data
# import print_all_data
import UI
# import add_data
# import logger



def button_click():
    UI.print_data("Вы можете выполнить следующие действия со справочником сотрудников: ")
    answer = UI.input_check_choice("1. Вывод всего справочника.\n2. Добавление нового сотрудника\n Введите цифру: ")
    if answer == 1:
        list_data = reading_data.get_info("uses.csv")  # читаем
        print_all_data.print_all(list_data)  # печатаем все
        UI.print_data(f"\nСправочник сотрудников состоит из {len(list_data)} записей")
    elif answer == 2:
        user_data = UI.input_name_directory()
        add_data.append_data("uses.csv", user_data)
        logger.result_loger(user_data)
        UI.print_data("\nДанные успешно добавлены в справочник сотрудников.")
