from . import db, bcrypt
from datetime import datetime

produtos_agendamentos = db.Table('produtos_agendamentos',
    db.Column('produto_id', db.Integer, db.ForeignKey('produto.id'), primary_key=True),
    db.Column('agendamento_id', db.Integer, db.ForeignKey('agendamento.id'), primary_key=True)
)

servicos_agendamentos = db.Table('servicos_agendamentos',
    db.Column('servico_id', db.Integer, db.ForeignKey('servico.id'), primary_key=True),
    db.Column('agendamento_id', db.Integer, db.ForeignKey('agendamento.id'), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    endereco = db.Column(db.String(255), nullable=True)
    cidade = db.Column(db.String(255), nullable=True)
    estado = db.Column(db.String(255), nullable=True)
    telefone = db.Column(db.String(20), nullable=True)
    cpf = db.Column(db.String(11), unique=True, nullable=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    # Relacionamento com Fornecedor (um usuário pode ter um fornecedor associado)
    fornecedor = db.relationship('Fornecedor', backref='usuario', uselist=False)

    # Relacionamento com Agendamentos (um usuário pode ter vários agendamentos)
    agendamentos = db.relationship('Agendamento', backref='usuario', lazy=True)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    endereco = db.Column(db.String(255), nullable=True)
    cidade = db.Column(db.String(255), nullable=True)
    estado = db.Column(db.String(255), nullable=True)
    telefone = db.Column(db.String(20), nullable=True)
    cpf = db.Column(db.String(11), unique=True, nullable=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    # Relacionamento com Fornecedor (um usuário pode ter um fornecedor associado)
    fornecedor = db.relationship('Fornecedor', backref='usuario', uselist=False)




class Fornecedor(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    telefone = db.Column(db.String(20), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)

    # Relacionamento com Calendários e Agendamentos
    calendarios = db.relationship('Calendario', backref='fornecedor', lazy=True)
    agendamentos = db.relationship('Agendamento', backref='provedor', lazy=True)


class Calendario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    disponibilidade = db.Column(db.PickleType, nullable=False)


class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # 'pendente', 'confirmado', 'cancelado'

    produtos = db.relationship('Produto', secondary=produtos_agendamentos, backref='agendamentos')
    servicos = db.relationship('Servico', secondary=servicos_agendamentos, backref='agendamentos')


class Agenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(300), nullable=True)
    hora = db.Column(db.String(4), nullable=False)
    __table_args__ = {'extend_existing': True}


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'), nullable=False)

    fornecedor = db.relationship('Fornecedor', backref='produtos', lazy=True)


class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'), nullable=False)

    fornecedor = db.relationship('Fornecedor', backref='servicos', lazy=True)
