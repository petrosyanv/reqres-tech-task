import json
from api.controllers.base_controller import BaseController
from api.entities.user import User


class Users(BaseController):

    def create(self, user: User = None):
        if user is None:
            user = User.generate_random()
        body = user.serialize_to_dict()
        response = self.caller.call(method='post', uri=f'/api/users', body=body)
        dict_response = json.loads(response.text)
        user.user_id = int(dict_response['id'])
        return User.deserialize_from_dict(dict_response)

    def get_user(self, user_id, status_code=200):
        response = self.caller.call(method='get', uri=f'/api/users/{user_id}')
        assert response.status_code == status_code
        return User.deserialize_from_dict(json.loads(response.text))

    def get_all_users(self):
        response = self.caller.call(method='get', uri='/api/users')
        return User.deserialize_list_from_dict(json.loads(response.text))

    def update(self, user: User):
        body = user.serialize_to_dict()
        response = self.caller.call(method='put', uri=f'/api/users', body=body)
        return int(json.loads(response.text)['id'])

    def delete(self, user_id):
        return self.caller.call(method='delete', uri=f'/api/users/{user_id}')


