from enum import Enum
import requests
from bs4 import BeautifulSoup

class Class():
    def __init__(self):
        pass

class Section():
    class SectionType(Enum):
        LAB  = 1
        LECT = 2
        TUT  = 3

    def __init__(self):
        pass
