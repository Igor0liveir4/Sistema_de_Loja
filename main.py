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

@app.get("/produtos/cadastro")
def exibir_cadastro(request: Request, db: Session = Depends(get_db)):
    # Busca todas as categorias no banco
    categorias = db.query(Categoria).all()
    return templates.TemplateResponse(
        request,
        "cadastrar_produto.html",
        {"request": request, "categorias": categorias}
    )

@app.post("/produtos")
def criar_produto(
    nome: str = Form(...),
    preco: float = Form(...),
    estoque: int = Form(...),
    categoria_id: int = Form(...), # Recebendo o ID do formulário
    db: Session = Depends(get_db)
):
    # Cria a instância do modelo
    novo_produto = Produto(
        nome=nome, 
        preco=preco, 
        estoque=estoque, 
        categoria_id=categoria_id
    )
    
    # Salva no banco
    db.add(novo_produto)
    db.commit()
    
    # Redireciona de volta para a home após salvar
    return RedirectResponse(url="/", status_code=303)

@app.get("/categorias/cadastro")
def exibir_cadastro_categoria(request: Request):
    return templates.TemplateResponse(
        request,
        "nova_categoria.html",
        {"request": request}
    )

@app.post("/categorias")
def criar_categoria(
    nome: str = Form(...),
    descricao: str = Form(...),
    db: Session = Depends(get_db)
):
    nova_categoria = Categoria(nome=nome, descricao=descricao)

    db.add(nova_categoria)
    db.commit()

    return RedirectResponse(url="/", status_code=303)