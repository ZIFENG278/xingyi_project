# import pandas as pd
import pandas as pd


def yn_process(condition):
    while True:
        if condition == 1:
            yn = input("Save this clien or not (y or n)  ")
        else:
            yn = input("would you like to continue (y or n): ")

        if yn == 'n' or yn == '!Q':
            return False
        elif len(yn) != 1:
            print("please input y or n")
            continue
        elif yn == 'y':
            return True
        else:
            print("please input y or n")
            continue


def analyse_client(clients_df, sales_df):
    print("----------------------------------------\n"
          "RETRIEVE CLIENTS SALES INFORMATION\n")
    while True:
        client_name = input("What is the name of the client? (!Q to quit)  ")
        if client_name == '!Q':
            break
        elif client_name == '':
            continue
        try:
            client_search_result = clients_df.query(f'name == "{client_name}"').loc[0, 'client number']
            client_search_result = int(client_search_result)
            print(client_search_result)
            sales_search_result = sales_df[sales_df['Client number'] == 1]
            print("The client has bought "
                  + str(sales_search_result.shape[0]) + " products.")
            print("Here is the mean of its sales "
                  + str(round(sales_search_result['Sales'].mean(),2)))
            print("Here is the maximum spend for a sale "
                  + str(round(sales_search_result['Sales'].max(),2)))
            print("Here is the sum of sale "
                  + str(round(sales_search_result['Sales'].sum(),2)))
        except:
            print("no this client information")
        # else:
        #     client_num = clients_df.query(f'name == {client_name}').values[0][0]
        #     print(client_num)
        #     break
        if yn_process(2):
            continue
        else:
            break


def unstack_category_region(sales_df):
    group = sales_df.groupby(["Category", "Region"])["Sales"].sum()
    group_stack = group.unstack()
    try:
        group_stack.to_excel("Sum of sales cat reg.xlsx")
        print("+++++++'Sum of sales cat reg.xlsx'+++++++\n"
              "          Successfully saved!!           ")
    except:
        print("Can not save, please check permission or this file being opened by other application")


def unstack_client_category(sales_df):
    group_stack = sales_df.pivot_table(index=["Client number"], columns=["Category"], aggfunc="mean")
    # group = sales_df.groupby(["Client number", "Category"])["Sales"].mean()
    # group_stack = group.unstack().round(2)
    try:
        group_stack.to_excel("Mean of sales client cat.xlsx")
        print("+++++++'Mean of sales client cat.xlsx'+++++++\n"
              "           Successfully saved!!             ")
    except:
        print("Can not save, please check permission or this file being opened by other application")


def merge_table(clients_df, sales_df):
    merge_table = pd.merge(clients_df, sales_df, left_on="client number", right_on="Client number")
    merge_table.set_index('client number', inplace=True)
    try:
        merge_table.to_excel("Merge_tables.xlsx")
        print("+++++++'Merge_tables.xlsx'+++++++\n"
              "       Successfully saved!!      ")
    except:
        print("Can not save, please check permission or this file being opened by other application")

def menu_5_option_1(df):
    df_2 = df.loc[lambda df: df['Indicator'] == "Population of compulsory school age, both sexes (number)"]
    df_3 = df_2.loc[lambda df: df['Country'] == "France"]
    print(df_3[["Time", "Value"]])

def menu_5_option_2(df):
    df_france = df.loc[lambda df: df['Country'] == "France"]
    df_germany = df.loc[lambda df: df['Country'] == "Germany"]
    df_fg = pd.concat([df_france, df_germany], axis=0)
    try:
        df_fg.to_csv('France Germany education statistics.csv')
        print("+++++++'France Germany education statistics.csv'+++++++\n"
              "Statistics of France and Germany successfully exported")
    except:
        print("Can not save, please check permission or this file being opened by other application")

def menu_5_option_3(df):
    df_drop_Time = df.drop(columns='TIME')
    df_groupby_mean = df_drop_Time.pivot_table(index="Country", columns="Time", aggfunc='mean')
    try:
        df_groupby_mean.to_csv('mean countrytime ind.csv')
        print("+++++++'mean countrytime ind.csv'+++++++\n"
              "          Successfully saved!!      ")
    except:
        print("Can not save, please check permission or this file being opened by other application")