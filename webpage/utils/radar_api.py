import os
import requests
from webpage.utils.exceptions import APIRequestError, NotFound
from webpage.utils.singleton import Singleton


class FlightsAPI(metaclass=Singleton):
    """Airlab API"""

    BASE_API_URL = 'https://airlabs.co/api/v9/{endpoint}'

    def __init__(self, api_key: str = None):
        """
        Create a FlightsAPI instance

        Args:
            api_key: Optional API key. If not specified, will be retrieved from env variable `AIRLABS_API_KEY`
        """
        self.api_key = api_key or os.getenv('AIRLABS_API_KEY')
        assert self.api_key, "You have to specify AIRLABS_API_KEY. You can do this either by setting " \
                             "`AIRLABS_API_KEY` environment variable or passing `api_key` param to FlightsAPI " \
                             "constructor "

    def __request(self, endpoint: str = 'flights',
                  query_params: dict = None) -> dict:
        """
        Make a request to Airlab API

        Args:
            endpoint: Optional parameter which signifies the endpoint that will be appended to `BASE_API_URL`.
        Default to `flights` to retrieve information about a flight
            query_params: A dictionary of query params to use

        Returns:
            dict: JSON response
        """
        self.api_key = os.getenv('AIRLABS_API_KEY')
        query_params.update(api_key=self.api_key)
        r = requests.get(
            self.BASE_API_URL.format(
                endpoint=endpoint),
            params=query_params)
        if r.status_code == 404:
            raise NotFound(f'Requested item was not found"')
        if not r.status_code == 200:
            raise APIRequestError(f'Request finished with code {r.status_code}')
        return r.json()

    def get_flight_data(self, flight_code: str) -> dict:
        """
        Fetch flight data for a given flight

        Args:
            flight_code: a string representing flight code

        Returns:
            a dict: JSON response
        """
        return self.__request(query_params={'flight_iata': flight_code})
