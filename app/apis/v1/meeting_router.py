from fastapi import APIRouter

edgedb_router = APIRouter(prefix="/v1/edgedb/mettings", tags=["Meeting"])
mysql_router = APIRouter(prefix="/v1/mysql/mettings", tags=["Meeting"])
