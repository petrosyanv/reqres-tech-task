from common.utility import first_name_generator, last_name_generator, email_generator, avatar_link_generator


class User:

    def __init__(self, user_email, user_first_name, user_last_name, user_avatar_link, user_id=None):
        self.user_id = user_id
        self.user_email = user_email
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.user_avatar_link = user_avatar_link

    @staticmethod
    def generate_random():
        return User(
            user_email=f'{email_generator()}',
            user_first_name=f'{first_name_generator()}',
            user_last_name=f'{last_name_generator()}',
            user_avatar_link=f'{avatar_link_generator()}'
        )

    @staticmethod
    def deserialize_from_dict(dict_obj: dict):
        data = dict_obj.get('data') if 'data' in dict_obj else dict_obj
        try:
            return User(
                user_id=int(data.get('id', 0)),
                user_email=data.get('email'),
                user_first_name=data.get('first_name'),
                user_last_name=data.get('last_name'),
                user_avatar_link=data.get('avatar')
            )
        except AttributeError:
            return data

    @staticmethod
    def deserialize_list_from_dict(dict_obj: dict):
        return [User.deserialize_from_dict(user) for user in dict_obj.get('data')]

    def serialize_to_dict(self):
        return {
            "id": self.user_id,
            "email": self.user_email,
            "first_name": self.user_first_name,
            "last_name": self.user_last_name,
            "avatar": self.user_avatar_link
        }

    def __eq__(self, other):
        try:
            assert self.user_id == other.user_id
            assert self.user_first_name == other.user_first_name
            assert self.user_last_name == other.user_last_name
            assert self.user_email == other.user_email
            assert self.user_avatar_link == other.user_avatar_link
            return True
        except AssertionError:
            return False
