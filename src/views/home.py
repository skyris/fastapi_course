import fastapi
from fastapi import Request
from fastapi_chameleon import template
from viewmodels.home.indexviewmodel import  IndexViewModel


router = fastapi.APIRouter()


@router.get('/')
@template(template_file='home/index.html')
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()
    # return {
    #     'package_count': 274_000,
    #     'release_count': 2_234_847,
    #     'user_count': 73_874,
    #     'packages': [
    #         {'id': 'fastapi', 'summary': "A great web framework"},
    #         {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
    #         {'id': 'httpx', 'summary': "Requests for an async world"},
    #     ]
    # }


@router.get('/about')
@template(template_file='home/about.html')
def about():
    return {}
