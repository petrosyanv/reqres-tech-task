# import requests
# from requests.auth import HTTPBasicAuth
#
#
#
# #def test_authentication_positive():
#    # url = "https://restful-booker.herokuapp.com/auth"
#
#     #response = requests.post(url, auth=HTTPBasicAuth('admin', 'password123'))
#
#     #assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
#
#     #print("Authentication successful! Status Code:", response.status_code)
#
# def test_authentication_negative():
#     url = "https://restful-booker.herokuapp.com/auth"
#
#     response = requests.post(url, auth=HTTPBasicAuth('incorrect', 'passwordincorrect'))
#
#     expected_error_message = "Bad credentials"
#
#     assert expected_error_message in response.text, f"Expected error message in response body, but got {response.text}"
#
#     print("Authentication successful! Status Code:", response.status_code)
#
# def test_id_without_filters():
#     url = "https://restful-booker.herokuapp.com/booking"
#
#     response = requests.get(url)