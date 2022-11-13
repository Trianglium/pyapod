"""
PyApod
~~~~~~~

PyApod is a Python Wrapper for apod - Nasa's Astronomy Picture of the Day API

"""
import requests

from datetime import datetime
from .models import APIModel


class Apod(object):
    BASE_URL = "https://api.nasa.gov/planetary/apod"

    def __init__(
        self,
        date=None,
        start_date=None,
        end_date=None,
        count: int = None,
        thumbs: bool = False,
        api_key: str = "DEMO_KEY",
    ):
        self._date = datetime.now().strftime("%Y-%m-%d")
        self.start_date = start_date
        self.end_date = end_date
        self.count = count
        self.thumbs = thumbs
        self.api_key = api_key
        self.base_url = self.BASE_URL
        self._params = {}
        self._response = None

    @property
    def date(self):
        self._date = datetime.now().strftime("%Y-%m-%d")
        return self._date

    @property
    def params(self):
        self._params = {"api_key": self.api_key, "date": self.date}
        return self._params

    @params.setter
    def params(self, new_params: dict):
        for p in new_params:
            if p not in self._params:
                self._params.update({p: new_params[p]})

        return self._params

    def get(self):
        try:
            r = requests.get(url=self.base_url, params=self.params)
            if r.status_code == 200:
                data = r.json()
                return data
        except Exception as e:
            return e

    @property
    def response(self):
        self._response = APIModel(data=self.get())
        return self._response
