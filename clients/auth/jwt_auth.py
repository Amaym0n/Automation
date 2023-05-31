import requests


class JWTAuth:
    def __init__(self, token_url: str, username: str, password: str) -> None:
        """
        Initialize JWTAuth object.

        :param token_url: URL to get JWT token.
        :type token_url: str
        :param username: Username for authentication.
        :type username: str
        :param password: Password for authentication.
        :type password: str
        """
        self.token_url = token_url
        self.username = username
        self.password = password
        self.token = None

    def __call__(self, request: requests.PreparedRequest) -> requests.PreparedRequest:
        """
        Add JWT authorization header to a prepared request.

        :param request: Prepared request.
        :type request: requests.PreparedRequest
        :return: Prepared request with added authorization header.
        :rtype: requests.PreparedRequest
        """
        if self.token is None:
            self.token = self._get_token()
        request.headers['Authorization'] = f'{self.token}'
        return request

    def _get_token(self) -> str:
        """
        Get JWT token using the provided username and password.

        :return: JWT token.
        :rtype: str
        """
        response = requests.post(self.token_url, data={
            'username': self.username,
            'password': self.password
        }, verify=False)
        response.raise_for_status()
        return response.json()['access_token']
