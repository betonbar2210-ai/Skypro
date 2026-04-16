from src.output_of_categories import process_bank_search
from src.utils import read_json
from src.reader_csv_xlsl import reader_csv, reader_excel
from src.processing import filter_by_state, sort_by_date
from datetime import datetime


def read_main():
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    user_answer_1 = input('Выберите необходимый пункт меню:\n'
                          '1. Получить информацию о транзакциях из JSON-файла\n'
                          '2. Получить информацию о транзакциях из CSV-файла\n'
                          '3. Получить информацию о транзакциях из XLSX-файла\n')
    while True:
        if user_answer_1 == '1':
            print('Для обработки выбран JSON-файл\n')
            json_file = read_json('data/operations.json')
            return json_file
            break
        elif user_answer_1 == '2':
            print('Для обработки выбран CSV-файл\n')
            csv_file = reader_csv('data/transactions.csv')
            return csv_file
            break
        elif user_answer_1 == '3':
            print('Для обработки выбран XLSX-файл\n')
            excel_file = reader_excel('data/transactions_excel.xlsx')
            return excel_file
            break
        else:
            user_answer_1 = input('Введен некорректный номер\n'
                                  'Выберите необходимый пункт меню:\n'
                                  '1 Получить информацию о транзакциях из JSON-файла\n'
                                  '2 Получить информацию о транзакциях из CSV-файла\n'
                                  '3 Получить информацию о транзакциях из XLSX-файла\n')

def filter_main():
    filter_file = read_main()
    user_answer_2 = input('Введите статус, по которому необходимо выполнить фильтрацию.\n'
                          'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n').upper()
    while True:
        if user_answer_2 == 'EXECUTED':
            print('Операции отфильтрованы по статусу "EXECUTED"')
            execud_file = filter_by_state(filter_file, user_answer_2)
            return execud_file
            break

        elif user_answer_2 == 'CANCELED':
            print('Операции отфильтрованы по статусу "CANCELED"')
            cancel_file = filter_by_state(filter_file, user_answer_2)
            return cancel_file
            break
        elif user_answer_2 == 'PENDING':
            print('Операции отфильтрованы по статусу "PENDING"')
            pen_file = filter_by_state(filter_file, user_answer_2)
            return pen_file
            break
        else:
            user_answer_2 = input(f'Статус операции "{user_answer_2}" недоступен\n'
                                  'Введите статус, по которому необходимо выполнить фильтрацию.\n'
                                  'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n').upper()

def sort_main():
    sort_file = filter_main()
    user_answer_3 = input('Отсортировать операции по дате?\nДа/Нет\n').lower()
    if "да" in user_answer_3:
        user_answer_4 = input('Отсортировать по возрастанию или по убыванию?\n').lower()
        while True:
            if 'по убыванию' in user_answer_4:
                descending_list = sort_by_date(sort_file)
                return descending_list
                break
            elif 'по возрастанию' in user_answer_4:
                increasing_list = sort_by_date(sort_file, type_filter = False)
                return increasing_list
                break
            else:
                user_answer_4 = input(f'Команда {user_answer_4} не распознана, введите:\n'
                                      f'по убыванию\n'
                                      f'по возрастанию\n')
    else:
        return sort_file


# def sort_rub():
#     result_file = sort_main()
#     user_answer_5 = input('Выводить только рублевые транзакции?\nДа\Нет\n').lower()
#     if 'да' in user_answer_5:
#         sort_yes = process_bank_search(result_file, 'RUB')
#         return sort_yes
#     else:
#         return result_file
#
#
# def finish_sort():
#     finish_file = sort_rub()
#     user_answer_5 = input('Отфильтровать список транзакций по определенному слову в описании?\nДа\Нет\n').lower()
#     if 'да' in user_answer_5:
#         user_answer_6 = input('По какому слову фильтровать:\n')
#         file_sort = process_bank_search(finish_file, user_answer_6)
#         return file_sort
#     else:
#         return finish_file


#def total_main():

date_string = datetime.now().strftime('%d.%m.%Y')

if __name__ == "__main__":
    #print(read_main())
    #print(finish_sort())
    #sort_main()
    print('Распечатываю итоговый список транзакций...')
    print(f'Всего банковских операций в выборке: 4')
    print(f'{date_string}')

