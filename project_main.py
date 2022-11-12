"""
Project_main is the main program
"""
import project_function as pf
MAIN_OPTIONS = 6
SUB_OPTIONS = 4

if __name__ == '__main__':
    while True:
        pf.show_main_menu()
        input_value = pf.input_preprocess(MAIN_OPTIONS)
        # print(type(input_value))
        if input_value == 1:
            pf.save_client_to_list()

        elif input_value == 2:
            pf.show_clients_info()

        elif input_value == 3:
            pf.sub_frame_3(SUB_OPTIONS)

        elif input_value == 4:
            pf.sub_frame_4(SUB_OPTIONS)

        elif input_value == 5:
            pf.sub_frame_5(SUB_OPTIONS)

        elif input_value == 6 or input_value == '!Q':
            break

    pf.save_clients_to_csv()
    print('bye!')


