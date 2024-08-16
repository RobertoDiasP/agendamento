from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, jsonify
from app.models import User, Fornecedor, Produto
from app import db

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({'message': 'This is a protected route'})



@main_blueprint.route('/fornecedor', methods=['POST'])
def cadastrar_fornecedor():
    data = request.get_json()

    # Valida os dados recebidos
    if not all(key in data for key in ('user_id', 'telefone', 'endereco', 'especialidade')):
        return jsonify({'message': 'Dados inválidos'}), 400

    user_id = data['user_id']
    telefone = data['telefone']
    endereco = data['endereco']
    especialidade = data['especialidade']
    descricao = data.get('descricao', '')

    # Verifica se o usuário existe
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'Usuário não encontrado'}), 404

    # Cria o novo fornecedor
    fornecedor = Fornecedor(
        id=user_id,
        telefone=telefone,
        endereco=endereco,
        especialidade=especialidade,
        descricao=descricao
    )

    try:
        db.session.add(fornecedor)
        db.session.commit()
        return jsonify({'message': 'Fornecedor cadastrado com sucesso!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500


@main_blueprint.route('/produtos', methods=['POST'])
@jwt_required()
def cadastrar_produto():
    # Obter informações do JWT
    user_id = get_jwt_identity()

    # Verificar se o usuário é um fornecedor
    fornecedor = Fornecedor.query.filter_by(id=user_id).first()
    if not fornecedor:
        return jsonify({'message': 'Apenas fornecedores podem cadastrar produtos.'}), 403

    # Obter dados do produto da requisição
    data = request.get_json()
    nome = data.get('nome')
    descricao = data.get('descricao')
    preco = data.get('preco')

    # Criar um novo produto
    novo_produto = Produto(
        nome=nome,
        descricao=descricao,
        preco=preco,
        fornecedor_id=user_id  # Adiciona o ID do fornecedor automaticamente
    )

    # Adicionar o produto ao banco de dados
    db.session.add(novo_produto)
    db.session.commit()

    return jsonify({'message': 'Produto cadastrado com sucesso.'}), 201