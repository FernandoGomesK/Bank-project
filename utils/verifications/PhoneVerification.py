from pydantic import field_validator
from utils.exceptions.general_exceptions import InvalidNumberException
import re

def validate_phone_number(phone_number: str) -> str:
    pattern = r'^(\(?\d{2}\)?\s?)?(\d{4,5}\-?\d{4})$'

    if not re.match(pattern, phone_number):
       raise InvalidNumberException

    return phone_number