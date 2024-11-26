import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import index as indexRoute
from .models import model_loader
from .dependencies.config import conf
from routers import customers, menu_items, payment_info, ratings_reviews




app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()
indexRoute.load_routes(app)

app.include_router(customers.router)
app.include_router(menu_items.router)
app.include_router(payment_info.router)
app.include_router(ratings_reviews.router)


if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)