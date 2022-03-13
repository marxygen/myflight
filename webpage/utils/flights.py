from .radar_api import FlightsAPI
from typing import Tuple
from webpage.utils.exceptions import NotFound, APIRequestError
import logging


def fetch_flight_information(flight_code: str, suppress: bool = True) -> dict:
    """
    Fetch information about a flight

    Args:
        flight_code: Flight code
        suppress: Whether to suppress exceptions if they occur. If True, empty dict will be returned

    Returns:
        dict: JSON information about the flight
    """
    try:
        flight_data = FlightsAPI().get_flight_data(flight_code)
        response = flight_data.get('response', {})
        if not response:
            logging.info(f'No flight data is available for "{flight_code}": {flight_data}')
            raise NotFound(f'No flight data is available for "{flight_code}"')
        return response
    except (NotFound, APIRequestError):
        if suppress:
            return {}
        raise


def validate_flight_code(flight_code: str) -> Tuple[bool, str]:
    """
    Validate given flight code
    Returns True if:
        - Flight exists
        - Flight is in progress

    :param flight_code: str Flight code
    :type flight_code: str

    Returns:
        is_valid, message
    """
    try:
        fetch_flight_information(flight_code, suppress=False)
    except (NotFound, APIRequestError) as e:
        return False, str(e)

    return True, ''
