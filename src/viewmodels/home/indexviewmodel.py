from typing import List
from viewmodels.shared.viewmodel import ViewModelBase
from fastapi import Request


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.package_count: int = 1
        self.release_count: int = 2
        self.user_count: int = 3
        self.packages: List = []

        # {
        #     'package_count': 274_000,
        #     'release_count': 2_234_847,
        #     'user_count': 73_874,
        #     'packages': [
        #         {'id': 'fastapi', 'summary': "A great web framework"},
        #         {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
        #         {'id': 'httpx', 'summary': "Requests for an async world"},
        #     ]
        # }

