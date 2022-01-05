from typing import Optional
from fastapi import Request


class ViewModelBase:

    def __init__(self, request: Request):
        self.request: Request = request
        self.error: Optional[str] = None
        self.user_id: Optional[int] = None

        # We will get this from cookies later
        self.is_logged_in: Optional[bool] = False

    def to_dict(self) -> dict:
        return self.__dict__

