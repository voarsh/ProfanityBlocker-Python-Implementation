from .ProfanityException import RaiseError
from .constants import constants
import requests

class ProfanityService:
    __slots__ = ("ApiKey", "EmailFilter", "LinkFilter", "PhoneFilter")

    def __init__(self, ApiKey, EmailFilter=False, LinkFilter=False, PhoneFilter=False):
        self.ApiKey = ApiKey
        self.EmailFilter = EmailFilter
        self.LinkFilter = LinkFilter
        self.PhoneFilter = PhoneFilter

    def FixFiltering(self, text, service):
        if text == service:
            return text
        ws = text.split(" ")
        ms = service.split(" ")
        NewText = ""
        for i in range(len(ws)):
            if ws[i] != ms[i]:
                NewW = ""
                for l in range(len(ws[i])): NewW += "*"
                NewText += "%s " % NewW
        return NewText

    def ParseText(self, text):
        url = constants.ProfanityService
        Query = {
            "type": "json",
            "link": self.LinkFilter,
            "phone": self.PhoneFilter,
            "email": self.EmailFilter,
            "key": self.ApiKey,
            "text": text
        }
        ServiceData = requests.post(url, data=Query)
        response = ServiceData.json()
        if "errorCode" in response.keys():
            return RaiseError(response["errorCode"])
        return self.FixFiltering(text, response['text_parsed'])