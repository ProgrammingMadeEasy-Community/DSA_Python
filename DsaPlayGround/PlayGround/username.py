import string


valid_character = set(string.ascii_letters + string.digits + '_' + '-')


message = ('@User_One @UserABC! Have you seen this from @Userxyz?').split()


def user_name(message, k):
    key = 1

    user_dict = {key: ' '}
    for word in message:
        if word.startswith('@'):
            username = word[1:]
            for i in range(len(username)):
                if not (set(username[i]).issubset(valid_character)):
                    username = username[0:i]
            user_dict[key] = username
            key += 1
    try:
        return user_dict[k]
    except:
        print(' ')


print(user_name(message, 3))
print(user_name(message, 2))
print(user_name(message, 1))
