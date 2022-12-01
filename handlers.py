from models import User


def exit_command(transport, del_user_name: str, curr_users: dict):
    curr_users.pop(del_user_name)

    for user in curr_users.values():
        user.transport.write(f"{user.name} exited chat".encode(encoding='utf-8'))

    transport.write(f"BB, {del_user_name}".encode(encoding="utf-8"))


def enter_command(transport, new_user_name, curr_users: dict):
    for user in curr_users.values():
        user.transport.write(f"{new_user_name} in chat now".encode(encoding='utf-8'))

    curr_users[new_user_name] = User(transport, new_user_name)
    transport.write(f"Hello, {new_user_name}".encode("utf-8"))


def handle(tranport, comand: str, curr_users: dict):
    comand_items = comand.split(' ')

    if comand_items[0] == 'enter':
        enter_command(tranport, comand_items[1].strip(), curr_users)

    elif comand_items[0] == 'exit':
        exit_command(tranport, comand_items[1].strip(), curr_users)

    else:
        raise Exception("no such comand")
