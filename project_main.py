"""
Project_main is the main program
"""
import project_function as pf
MAIN_OPTIONS = 6
SUB_OPTIONS = 4

clients = []

if __name__ == '__main__':
    while True:
        pf.show_main_menu()
        input_value = pf.input_preprocess(MAIN_OPTIONS)
        # print(type(input_value))
        if input_value == 1:
            #client_index = len(clients)
            client = pf.create_client()
            if client:
                clients.append(client)
                print("the client has been created and saved in the list.\n")

        elif input_value == 2:
            # print("----------------------------------------\n"
            #       "CLIENT INFORMATION\n")
            # pf.print_exist_clients_info()
            pf.show_clients_info(clients)

        elif input_value == 3:
            # pf.show_sub_menu_3()
            pf.sub_frame_3(SUB_OPTIONS)

        elif input_value == 4:
            pf.sub_frame_4(SUB_OPTIONS)

        elif input_value == 5:
            pass

        elif input_value == 6 or input_value == '!Q':
            break
    # print(clients)
    pf.save_clients_to_csv(clients)
    print('bye!')


