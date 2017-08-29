from app import db

class Bebida(db.Model):
    __tablename__   = "bebidas"

    id_bebida = db.Column(db.Integer, primary_key=True)
    nome_bebida = db.Column(db.String, unique=True)
    teor_alcool = db.Column(db.Numeric)
    ingredientes = db.Column(db.Text)
    max_estoque = db.Column(db.Integer)
    min_estoque = db.Column(db.Integer)
    id_fabricante = db.Column(db.Integer, db.ForeignKey('fabricantes.id_fabricante'))
    id_categoria = db.Column(db.Integer, db.ForeignKey('categorias.id_categoria'))

    fabricante_fk = db.relationship('Fabricante', foreign_keys=id_fabricante)
    categoria_fk = db.relationship('Categoria', foreign_keys=id_categoria)

    def __init__(self, nome_bebida, teor_alcool, ingredientes, max_estoque, min_estoque, id_fabricante, id_categoria):
        self.nome_bebida = nome_bebida
        self.teor_alcool = teor_alcool
        self.ingredientes = ingredientes
        self.max_estoque = max_estoque
        self.min_estoque = min_estoque
        self.id_fabricante = id_fabricante
        self.id_categoria = id_categoria

    def __repr__(self):
        return "<Bebida %r>" % self.nome_bebida

class Lote(db.Model):
    __tablename__   = "lotes"

    id_lote = db.Column(db.Integer, primary_key=True)
    preco = db.Column(db.Numeric)
    quantidade = db.Column(db.Integer)
    codigo = db.Column(db.String)
    id_bebida = db.Column(db.Integer, db.ForeignKey('bebidas.id_bebida'))
    id_fornecedor = db.Column(db.Integer, db.ForeignKey('fornecedores.id_fornecedor'))

    bebida_fk = db.relationship('Bebida', foreign_keys=id_bebida)
    fornecedor_fk = db.relationship('Fornecedor', foreign_keys=id_fornecedor)

    def __init__(self, preco, quantidade, codigo, id_bebida, id_fornecedor):
        self.preco = preco
        self.quantidade = quantidade
        self.codigo = codigo
        self.id_bebida = id_bebida
        self.id_fornecedor = id_fornecedor

    def __repr__(self):
        return "<Lote %r>" % self.codigo

class Fabricante(db.Model):
    __tablename__   = "fabricantes"

    id_fabricante = db.Column(db.Integer, primary_key=True)
    nome_fabricante = db.Column(db.String, unique=True)

    def __init__(self, nome_fabricante):
        self.nome_fabricante = nome_fabricante

    def __repr__(self):
        return "<Fabricante %r>" % self.nome_fabricante

class Categoria(db.Model):
    __tablename__   = "categorias"

    id_categoria = db.Column(db.Integer, primary_key=True)
    nome_categoria = db.Column(db.String, unique=True)

    def __init__(self, nome_categoria):
        self.nome_categoria = nome_categoria

    def __repr__(self):
        return "<Categoria %r>" % self.nome_categoria

class Fornecedor(db.Model):
    __tablename__   = "fornecedores"

    id_fornecedor = db.Column(db.Integer, primary_key=True)
    nome_fornecedor = db.Column(db.String, unique=True)

    def __init__(self, nome_fornecedor):
        self.nome_fornecedor = nome_fornecedor

    def __repr__(self):
        return "<Fornecedor %r>" % self.nome_fornecedor
