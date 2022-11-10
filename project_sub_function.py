
def yn_process():
    while True:
        yn = input("would you like to continue (y or n): ")
        if len(yn) != 1:
            print("please input y or n")
            continue
        elif yn == 'y':
            return True
        elif yn == 'n':
            return False
        else:
            print("please input y or n")
            continue


def analyse_client(clients_df, sales_df):
    print("----------------------------------------\n"
          "RETRIEVE CLIENTS SALES INFORMATION\n")
    while True:
        client_name = input("What is the name of the client? (Q to quit)  ")
        if client_name == 'Q':
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
        if yn_process():
            continue
        else:
            break