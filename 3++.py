from re import T


class Contact:
    def __init__(self, name, number, group):
        self.name = name
        self.number = number
        self.group = group


# 通讯录中存储联系人的类
#  Attributes:
#     name (str): 联系人姓名
#     umber (str): 联系人标签
#     group (str): 联系人分组


class AddressBook:
    from re import T


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        # 通讯录类
        # Attributes:
        #     contacts (list): 存储联系人
        self.contacts.append(contact)

    # 向通讯录中添加联系人
    # Args:
    #     contact (Contact): 待添加的联系人对象
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"{name}已删除\n")
                return
        print(f"未找到{name}\n")

    # 从通讯录中删除联系人
    # Args:
    #     name (str): 待删除联系人的姓名
    # Returns:
    #     None
    def display_all_contacts(self):
        for contact in self.contacts:
            print(f"名称: {contact.name}, 标签: {contact.number}, 分组: {contact.group}")
        print("\n")


# 显示所有联系人信息
# Returns:
#     None
# """

address_book = AddressBook()


def main_menu():
    # 显示菜单选项
    # Returns:5
    #     None
    print("***********欢迎访问通讯录系统***********")
    print("1. 添加联系人")
    print("2. 删除联系人")
    print("3. 查询联系人信息")
    print("4. 显示所有联系人")
    print("5. 退出")
    print("**************************************")


def add_contact_menu():
    # 添加联系人的子菜单
    # Returns:
    #     None
    name = input("请输入名称: ")
    number = input("请输入标签: ")
    group = input("请输入分组: ")
    new_contact = Contact(name, number, group)
    address_book.add_contact(new_contact)
    print("联系人已添加\n")


def delete_contact_menu():
    # 删除联系人的子菜单
    # Returns:
    name = input("请输入要删除的联系人的名称: ")
    address_book.delete_contact(name)


def display_contact_menu():
    # 查询联系人信息的子菜单
    # Returns:
    #     None
    search_by = input("按名称(1)、标签(2)或分组(3)查询: ")
    if search_by == "1":
        name = input("请输入名称: ")
        find = False
        for contact in address_book.contacts:
            if contact.name == name:
                find = True
                print(f"标签: {contact.number}, 分组: {contact.group}")
        if not find:
            print(f"未找到{name}\n")
            return
        else:
            print("\n")

    elif search_by == "2":
        find = False
        number = input("请输入标签: ")
        for contact in address_book.contacts:
            if contact.number == number:
                find = True
                print(f"名称: {contact.name}, 分组: {contact.group}")
        if not find:
            print(f"未找到{number}\n")
            return
        else:
            print("\n")

    elif search_by == "3":
        find = False
        group = input("请输入分组: ")
        for contact in address_book.contacts:
            if contact.group == group:
                find = True
                print(f"名称: {contact.name}, 标签: {contact.number}")
        if not find:
            print(f"未找到{number}组成员\n")
            return
        else:
            print("\n")


while True:
    main_menu()
    choice = input("请输入选项: \n")

    if choice == "1":
        add_contact_menu()
    elif choice == "2":
        delete_contact_menu()
    elif choice == "3":
        display_contact_menu()
    elif choice == "4":
        address_book.display_all_contacts()
    elif choice == "5":
        break

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"{name}已删除\n")
                return
        print(f"未找到{name}\n")

    def display_all_contacts(self):
        for contact in self.contacts:
            print(f"名称: {contact.name}, 标签: {contact.number}, 分组: {contact.group}")
        print("\n")


address_book = AddressBook()


def main_menu():
    print("***********欢迎访问通讯录系统***********")
    print("1. 添加联系人")
    print("2. 删除联系人")
    print("3. 查询联系人信息")
    print("4. 显示所有联系人")
    print("5. 退出")
    print("**************************************")


def add_contact_menu():
    name = input("请输入名称: ")
    number = input("请输入标签: ")
    group = input("请输入分组: ")
    new_contact = Contact(name, number, group)
    address_book.add_contact(new_contact)
    print("联系人已添加\n")


def delete_contact_menu():
    name = input("请输入要删除的联系人的名称: ")
    address_book.delete_contact(name)


def display_contact_menu():
    search_by = input("按名称(1)、标签(2)或分组(3)查询: ")
    if search_by == "1":
        name = input("请输入名称: ")
        find = False
        for contact in address_book.contacts:
            if contact.name == name:
                find = True
                print(f"标签: {contact.number}, 分组: {contact.group}")
        if not find:
            print(f"未找到{name}\n")
            return
        else:
            print("\n")
            return

    elif search_by == "2":
        find = False
        number = input("请输入标签: ")
        for contact in address_book.contacts:
            if contact.number == number:
                find = True
                print(f"名称: {contact.name}, 分组: {contact.group}")
        if not find:
            print(f"未找到{number}\n")
            return
        else:
            print("\n")
            return

    elif search_by == "3":
        find = False
        group = input("请输入分组: ")
        for contact in address_book.contacts:
            if contact.group == group:
                find = True
                print(f"名称: {contact.name}, 标签: {contact.number}")
        if not find:
            print(f"未找到{number}组成员\n")
            return
        else:
            print("\n")
            return


while True:
    main_menu()
    choice = input("请输入选项: \n")

    if choice == "1":
        add_contact_menu()
    elif choice == "2":
        delete_contact_menu()
    elif choice == "3":
        display_contact_menu()
    elif choice == "4":
        address_book.display_all_contacts()
    elif choice == "5":
        print("已退出\n")
        break
