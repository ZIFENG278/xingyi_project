

class Client():
    def __init__(self, client_info_list):
        self.name = client_info_list[0]
        self.birth_date = client_info_list[1]
        self.city = client_info_list[2]
        self.email = client_info_list[3]

    def show_client_info(self):
        print(f"Client name : {self.name}\n"
              f"Client date_birth : {self.birth_date}\n"
              f"Client city_birth : {self.city}\n"
              f"Client email : {self.email}\n"
              )