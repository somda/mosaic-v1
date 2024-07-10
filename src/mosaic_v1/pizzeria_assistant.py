from fastapi import FastAPI, APIRouter, Request
from starlette.templating import Jinja2Templates

from mosaic_v1.utils import TEMPLATES_DIR

app = FastAPI()
router = APIRouter()
templates = Jinja2Templates(directory=TEMPLATES_DIR)


@app.get("/", name="assistant")
async def index(request: Request):
    return templates.TemplateResponse(
        "ai_pizza_ordering_page.jinja2", {"request": request}
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "mosaic_v1.pizzeria_assistant:app", host="0.0.0.0", port=8001, reload=True
    )
