"""
project function
"""
import pandas as pd
from project_class import Client
import project_sub_function as psf

def input_preprocess(option_nums):
    '''
    to preprocess the input
    :param option_nums: options numbers in the menu
    :return: input value
    '''
    while True:
        a = input(f"Choose an option between 1 and {option_nums}: ")
        if not (a.isdigit()):
            print("wrong input")
            continue
        elif int(a) < 1 or int(a) > option_nums:
            print("wrong input")
            continue
        else:
            break

    return int(a)


def show_main_menu():
    print("----------------------------------------\n"
          "Welcome to the client and sales analysis\n\n"
          "1) Create a new client in list\n"
          "2) show all the clients in list\n"
          "3) Show Excel file clients and sales\n"
          "4) Analyse Excel file clients and sales\n"
          "5) Analyse CSV file\n"
          "6) Quit\n"
          )


def format_birth_date(date):
    '''
    check the birth date format
    :param date: birth date
    :return: correct birth date
    '''
    while True:
        if len(date) != 10:
            # print('1')
            print("wrong format[DD/MM/YYYY]")
            date = input("What is the date of birth of the client?(DD/MM/YYYY)  ")
            continue

        elif date[2] != '/' or date[5] != '/':
            # print('2')
            print("wrong format[DD/MM/YYYY]")
            date = input("What is the date of birth of the client?(DD/MM/YYYY)  ")
            continue

        elif not(date[0:2].isdigit()) or not(date[3:5].isdigit()) or not(date[6:].isdigit()):
            # print('3')
            print("wrong format[DD/MM/YYYY]")
            date = input("What is the date of birth of the client?(DD/MM/YYYY)  ")
            continue

        else:
            break

    return date


def create_client():
    print("----------------------------------------\n"
          "CLIENT CREATION\n")
    client_info_list = []  # index: save client name, birth, city, email
    name = input("What is the name of the client?  ")
    client_info_list.append(name)

    date = input("What is rhe date of birth of the client?(DD/MM/YYYY)  ")
    date = format_birth_date(date)
    client_info_list.append(date)

    city = input("What is the city of birth of the client?  ")
    client_info_list.append(city)

    email = input("What is the email of the client?  ")
    client_info_list.append(email)
    # print(f"\nClient name : {client_info[0]}\n"
    #       f"Client date_birth : {client_info[1]}\n"
    #       f"Client city_birth : {client_info[2]}\n"
    #       f"Client email : {client_info[3]}\n"
    #       )
    print(" ")
    client = Client(client_info_list)
    client.show_client_info()

    return client


def show_clients_info(clients):
    print("----------------------------------------\n"
          "CLIENT INFORMATION\n")
    for client in clients:
        client.show_client_info()


def save_clients_to_csv(clients):
    if len(clients) != 0:
        names, birth_dates, birth_cities, emails = [], [], [], []
        for client in clients:
            names.append(client.name)
            birth_dates.append(client.birth_date)
            birth_cities.append(client.city)
            emails.append(client.email)

        clients_dict = {
            'Name': names,
            'Birth_date': birth_dates,
            'Birth_city': birth_cities,
            'Email': emails
        }

        clients_df = pd.DataFrame(clients_dict)
        # if os.path.isfile('clients_info.csv'):
        #     os.remove('clients_info.csv')

        clients_df.to_csv('clients_info.csv', index=False)
        print("----------------------------------------\n"
              "+++clients information save in 'clients_info.csv' file+++")


def show_sub_menu_3():
    print("----------------------------------------\n"
          "EXCEL CLIENTS AND SALES INFORMATION\n\n"
          "1) Show clients\n"
          "2) Show sales\n"
          "3) Analyse clients sales\n"
          "4) Go back\n")


def sub_frame_3(option_num):
    clients_df = pd.read_excel('clients_sales.xlsx')
    sales_df = pd.read_excel('clients_sales.xlsx', sheet_name=-1)
    while True:
        show_sub_menu_3()
        input_value = input_preprocess(option_num)
        if input_value == 1:
            print(clients_df)

        elif input_value == 2:
            print(sales_df)

        elif input_value == 3:
            psf.analyse_client(clients_df, sales_df)

        elif input_value == 4:
            break

def show_sub_menu_4():
    print("----------------------------------------\n"
          "ANALYSE CLIENTS SALES INFORMATION\n\n"
          "1) Sum of sales per category rows per region columns\n"
          "2) Mean of sales per clients rows and category columns\n"
          "3) Merge tables of clients and sales\n"
          "4) Go back\n")

def sub_frame_4(option_num):
    clients_df = pd.read_excel('clients_sales.xlsx')
    sales_df = pd.read_excel('clients_sales.xlsx', sheet_name=-1)
    while True:
        show_sub_menu_4()
        input_value = input_preprocess(option_num)
        if input_value == 1:
            print(clients_df)

        elif input_value == 2:
            print(sales_df)

        elif input_value == 3:
            psf.analyse_client(clients_df, sales_df)

        elif input_value == 4:
            break