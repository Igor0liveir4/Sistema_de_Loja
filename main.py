from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Categoria, Produto

#pip install jinja2 python-multipart

app = FastAPI(title="Sistema de loja")
templates = Jinja2Templates(directory="templates")

#Rodar api
#No terminal: python -m uvicorn main:app --reload

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"request":request}
    )

#Rota para cadastrar produto
@app.post("/produtos")
def criar_produto(
    nome: str = Form(...),
    preco: float = Form(...),
    estoque: int = Form(...)
):
    return {"nome": nome, "preco": preco, "estoque": estoque}