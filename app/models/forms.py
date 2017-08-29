from flask_wtf import FlaskForm
from wtforms import StringField, TextField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired

class CadastroForm(FlaskForm):
    nome_bebida = StringField("nome_bebida", validators=[DataRequired()])
    nome_fabricante = SelectField(u'Fabricante',choices=[('0','Fabricante..'),('1','Budweiser'),('2', 'Hardys'), ('3', 'Bacardi'), ('4', 'Coca-Cola')])
    nome_fornecedor = SelectField(u'Fornecedor..', choices=[('0','Fornecedor..'),('1','Loja1'),('2', 'Loja2'), ('3', 'Loja3'), ('4', 'Loja4')])
    nome_categoria = SelectField(u'Categoria', choices=[('0','Categoria..'), ('1','Cerveja'),('2', 'Vinho'), ('3', 'Rum'), ('4', 'Refrigerante')])
    codigo_lote = StringField("codigo_lote",validators=[DataRequired()])
    ingredientes = TextField("ingredientes", validators=[DataRequired()])
    data_validade = StringField("data_validade", validators=[DataRequired()])
    preco = FloatField("preco",validators=[DataRequired()])
    teor_alcool = StringField("teor_alcool", validators=[DataRequired()])
    quantidade = IntegerField("quantidade", validators=[DataRequired()])
    max_estoque = IntegerField("max_estoque", validators=[DataRequired()])
    min_estoque = IntegerField("min_estoque", validators=[DataRequired()])

class ConsultaForm(FlaskForm):
    opcao_pesquisa = SelectField(u'opcao',choices=[('1','Categoria'),('2', 'Preço'), ('3', 'Fornecedor')])
    pesquisa = StringField("pesquisa", validators=[DataRequired()])
