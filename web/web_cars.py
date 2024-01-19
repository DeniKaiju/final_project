from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')

router = APIRouter(
    prefix='',
    tags=['WEB', 'CARS'],
)


@router.get('/')
def index(request: Request):
    context = {
        'request': request,
    }
    return templates.TemplateResponse('index.html', context=context)
