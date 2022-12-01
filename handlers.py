from models import User


def exit_command(del_user_name: str, curr_users: dict[User]):
    for user in curr_users.values():
        user.transport.write(bytes(f"{user.name} exited chat"))

    curr_users.pop(del_user_name)


def enter_command(new_user_name, curr_users: dict[User]):
    for user in curr_users.values():
        user.transport.write(bytes(f"{user.name} in chat now"))
    curr_users.append(User(new_user_name))


def handle(tranport, comand: str, curr_users: dict[User]):
    comand_items = comand.split(' ')

    if comand_items[0] == 'enter':
        enter_command(tranport, curr_users)

    elif comand_items[0] == 'exit':
        exit_command(tranport, curr_users)

    else:
        raise Exception("no such comand")
