class dotdict(dict):
    """dot.notation access to dictionary attributes"""

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class APIModel(object):
    def __init__(self, data):
        self.date = data["date"]
        self.explanation = data["explanation"]
        self.hdurl = data["hdurl"]
        self.media_type = data["media_type"]
        self.url = data["url"]
        self.title = data["title"]
        self.service_version = data["service_version"]
        try:
            self.copyright = data["copyright"]
        except Exception:
            self.copyright = None
