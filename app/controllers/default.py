from flask import render_template, url_for, request, redirect
from app import app, db

from app.models.tables import Bebida, Lote, Categoria, Fornecedor, Fabricante
from app.models.forms import CadastroForm, ConsultaForm

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cadastro", methods=["GET","POST"])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        return redirect(url_for('/salvar'))
    else:
        return render_template('cadastro.html',
                                form=form)

@app.route("/consulta", methods=["GET", "POST"])
def consulta():
    form = ConsultaForm()
    if form.validate_on_submit():
        consulta = resultado()
        print(consulta)
        return 'resultadooooo'
    else:
        return render_template('consulta.html',
                            form=form)

@app.route("/salvar", methods=["GET", "POST"])
def salvar():
    if salvar_bebida():
        if salvar_lote():
            return 'Salvo com sucesso'
        else:
            return 'Erro ao salvar'

@app.route("/salvar_bebida", methods=["GET", "POST"])
def salvar_bebida():
    bebida = Bebida(request.form['nome_bebida'],request.form['teor_alcool'], request.form['ingredientes'],request.form['max_estoque'], request.form['min_estoque'], request.form['nome_fabricante'], request.form['nome_categoria'])

    db.session.add(bebida)
    db.session.commit()
    return True

@app.route("/salvar_lote", methods=["GET", "POST"])
def salvar_lote():
    id_beb = Bebida.query.filter_by(nome_bebida=request.form['nome_bebida']).first()
    lote = Lote(request.form['preco'],request.form['quantidade'], request.form['codigo_lote'], id_beb.id_bebida, request.form['nome_fornecedor'])
    db.session.add(lote)
    db.session.commit()
    return True



@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    # opção 1 - Categoria
    if request.form['opcao_pesquisa']=="1":
        categoria = Categoria.query.filter_by(nome_categoria=request.form['pesquisa']).first()
        bebida = Bebida.query.filter_by(id_categoria=categoria.id_categoria).first()
        consulta = 
        return consulta
    # opção 2 - Preço
    else if: request.form['opcao_pesquisa']=="2":
        bebida = Bebida.query.filter_by(preco=request.form['pesquisa']).first()
        consulta=
        return consulta
    # opção 3 - Fornecedor
    else:
        fornecedor = Fornecedor.query.filter_by(nome_fornecedor=request.form['pesquisa']).first()
        bebida = Bebida.query.filter_by(id_fornecedor=fornecedor.id_fornecedor).first()
        consulta =
        return consulta






@app.route("/teste", methods=["GET", "POST"])
def teste():
    lote = Bebida(2,'Coca-cola 350ml', 0.0, 'Açucar, aguá, corante', '2500', '200', '4', '4')

    db.session.add(lote)
    db.session.commit()
    return 'Ok'
