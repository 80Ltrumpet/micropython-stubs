from typing import Any

SMS_ALL: int
SMS_READ: int
SMS_UNREAD: int
SORT_ASC: int
SORT_DESC: int
SORT_NONE: int

def atcmd(*args) -> Any: ...
def checkSMS(*args) -> Any: ...
def connect(*args) -> Any: ...
def debug(*args) -> Any: ...
def deleteSMS(*args) -> Any: ...
def disconnect(*args) -> Any: ...
def readSMS(*args) -> Any: ...
def sendSMS(*args) -> Any: ...
def sms_cb(*args) -> Any: ...
def start(*args) -> Any: ...
def status(*args) -> Any: ...
def stop(*args) -> Any: ...
