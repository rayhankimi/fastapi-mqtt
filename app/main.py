from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config.koneksi import mongo_connection
from app.config.routes import main_router
from app.config.mqtt import mqtt_connection


@asynccontextmanager
async def lifespan(app: FastAPI):
    await mongo_connection.connect()
    mqtt_connection.start_connection()
    yield
    await mongo_connection.disconnect()


app = FastAPI(lifespan=lifespan)

app.include_router(main_router, prefix="/api/v1")


@app.get("/", name="root")
async def root():
    return {"message": "Hello World"}
