from sqlalchemy import  Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key = True, autoincrement = True )
    nome = Column(String(100), nullable = False)
    descricao = Column(String(150), nullable = False)
    
    # Relacionamento 1:N
    produtos = relationship("Produto", back_populates="categoria")

    def __repr__(self):
        return f"Categoria = id: {self.id} - Nome: {self.nome}"
    
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key = True, autoincrement = True)
    nome = Column(String(100), nullable = False)
    preco = Column(DECIMAL, nullable = False)
    estoque = Column(Integer, nullable = False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    # Relacionamento N:1
    categoria = relationship("Categoria", back_populates = "produtos")

    def __repr__(self):
        return f"Produtos = id: {self.id} - Nome: {self.nome} - preço: {self.preco}"
    
# Rodar o codigo