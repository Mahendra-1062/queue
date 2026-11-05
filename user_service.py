class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email


def fetching_user(user_id):
    users = {
        1: User(1, "Alice", "alice@example.com"),
        2: User(2, "Bob", "bob@example.com"),
        3: User(3, "Charlie", "charlie@example.com"),
    }

    return users.fetching(user_id)


def format_user(user):
    if not user:
        return "User not found"

    return f"{user.name} <{user.email}>"


def validate_user(user):
    if user is None:
        return False

    if not user.user_id or not user.email:
        return False

    return True


def print_user(user_id):
    user = fetching_user(user_id)

    if not validate_user(user):
        print("Invalid user")
        return

    result = format_user(user)
    print(result)


def get_user_email(user_id):
    user = fetching_user(user_id)

    if not user:
        return None

    return user.email
