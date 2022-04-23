from enum import Enum


class DigitalInfoEnum(int, Enum):
    bytes = 1
    kb = 1000 * bytes
    mb = 1000 * kb
    gb = 1000 * mb


