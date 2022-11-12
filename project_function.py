"""
project function
"""
import pandas as pd
from project_class import Client
import project_sub_function as psf
import os
clients = []

def input_preprocess(option_nums):
    '''
    to preprocess the input
    :param option_nums: options numbers in the menu
    :return: input value
    '''
    while True:
        a = input(f"Choose an option between 1 and {option_nums}: ")
        if a == '!Q':
            return '!Q'

        elif not(a.isdigit()):
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
          "2) Show all the clients in list\n"
          "3) Show Excel file clients and sales\n"
          "4) Analyse Excel file clients and sales\n"
          "5) Analyse CSV file\n"
          "6) Quit\n"
          "-----------!Q to force quit-------------"
          )


def format_birth_date():
    '''
    check the birth date format

    :return: correct birth date
    '''
    while True:
        date = input("What is the date of birth of the client?(DD/MM/YYYY) (!Q to force quit)  ")
        if date == '!Q':
            break

        elif len(date) != 10:
            # print('1')
            print("wrong format, need [DD/MM/YYYY]")
            # date = input("What is the date of birth of the client?(DD/MM/YYYY) (!Q to force quit)  ")
            continue

        elif date[2] != '/' or date[5] != '/':
            # print('2')
            print("wrong format, need [DD/MM/YYYY]")
            # date = input("What is the date of birth of the client?(DD/MM/YYYY) (!Q to force quit)  ")
            continue

        elif not(date[0:2].isdigit()) or not(date[3:5].isdigit()) or not(date[6:].isdigit()):
            # print('3')
            print("wrong format, need [DD/MM/YYYY]")
            # date = input("What is the date of birth of the client?(DD/MM/YYYY) (!Q to force quit) ")
            continue

        else:
            break

    return date


def create_client():
    while True:
        print("----------------------------------------\n"
              "CLIENT CREATION\n")
        client_info_list = []  # index: save client name, birth, city, email
        name = input("What is the name of the client? (!Q to force quit)  ")
        if name == '!Q':
            break
        else:
            client_info_list.append(name)

        date = format_birth_date()
        if date == '!Q':
            break
        else:
            client_info_list.append(date)

        city = input("What is the city of birth of the client? (!Q to force quit) ")
        if city == '!Q':
            break
        else:
            client_info_list.append(city)

        email = input("What is the email of the client? (!Q to force quit) ")
        if email == '!Q':
            break
        else:
            client_info_list.append(email)
            break
        # print(f"\nClient name : {client_info[0]}\n"
        #       f"Client date_birth : {client_info[1]}\n"
        #       f"Client city_birth : {client_info[2]}\n"
        #       f"Client email : {client_info[3]}\n"
        #       )

    if len(client_info_list) == 0:
        return False

    elif len(client_info_list) != 4:
        print("\nclient without save!!")
        return False
        # print("Save this clien or not (y or n)  ")

    elif psf.yn_process(1):
        client = Client(client_info_list)
        print(' ')
        client.show_client_info()
        return client



def save_client_to_list():
    client = create_client()
    if client:
            clients.append(client)
            print("the client has been created and saved in the list.\n")


def print_exist_clients_info():
    if os.path.exists('clients_info.csv'):
        df = pd.read_csv('clients_info.csv')
        for i in range(df.shape[0]):
            print(f"Client name : {df.iloc[i,0]}\n"
                  f"Client date_birth : {df.iloc[i,1]}\n"
                  f"Client city_birth : {df.iloc[i,2]}\n"
                  f"Client email : {df.iloc[i,3]}\n"
                 )

        return True
    else:
        return False



def show_clients_info():
    print("----------------------------------------\n"
          "CLIENT INFORMATION\n")
    if not(print_exist_clients_info()) and len(clients) == 0:
        print("No any client")
    else:
        # print_exist_clients_info()
        for client in clients:
            client.show_client_info()


def save_clients_to_csv():
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
        if os.path.exists('clients_info.csv'):
            old_clients_df = pd.read_csv('clients_info.csv')
            new_clients_df = pd.concat([old_clients_df, clients_df], axis=0)
            try:
                new_clients_df.to_csv('clients_info.csv', index=False)
                print("----------------------------------------\n"
                      "+++clients information save in 'clients_info.csv' file+++")
            except:
                print("Can not save, please check permission")
        else:
            try:
                clients_df.to_csv('clients_info.csv', index=False)
                print("----------------------------------------\n"
                      "+++clients information save in 'clients_info.csv' file+++")
            except:
                print("Can not save, please check permission or this file being opened by other application")


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

        elif input_value == 4 or input_value == '!Q':
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
            psf.unstack_category_region(sales_df)

        elif input_value == 2:
            psf.unstack_client_category(sales_df)

        elif input_value == 3:
            psf.merge_table(clients_df, sales_df)

        elif input_value == 4 or input_value == '!Q':
            break


def show_sub_menu_5():
    print("----------------------------------------\n"
          "ANALYSE EDUCATION COUNTRIES STATISTICS CSV FILE\n\n"
          "1) Show countries statistic for France and Population of compulsory school age, both sexes (number)\n"
          "2) Export data of France and Germany\n"
          "3) Calculate the mean of value grouped by country, time and indicator\n"
          "4) Go back\n")




def sub_frame_5(option_num):
    df = pd.read_csv("Education countries.csv")
    while True:
        show_sub_menu_5()
        input_value = input_preprocess(option_num)
        if input_value == 1:
            psf.menu_5_option_1(df)

        elif input_value == 2:
            psf.menu_5_option_2(df)

        elif input_value == 3:
            psf.menu_5_option_3(df)

        elif input_value == 4 or input_value == '!Q':
            break