from sqlalchemy import Column, INTEGER, VARCHAR, INT, DECIMAL, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CessaoFundo(Base):
    __tablename__ = 'cessao_fundo'
    id_cessao = Column(INTEGER, primary_key=True, autoincrement=True, nullable=False)
    originador = Column(VARCHAR(250), charset="utf8", nullable=False)
    doc_originador = Column(VARCHAR(50), charset="utf8", nullable=False)
    cedente = Column(VARCHAR(250), charset="utf8", nullable=False)
    doc_cedente = Column(VARCHAR(50), charset="utf8", nullable=False)
    ccb = Column(INT(22), charset="utf8", nullable=False)
    id_externo = Column(INT(22), charset="utf8", nullable=False)
    cliente = Column(VARCHAR(250), charset="utf8", nullable=False)
    cpf_cnpj = Column(VARCHAR(50), charset="utf8", nullable=False)
    endereco = Column(VARCHAR(250), charset="utf8", nullable=False)
    cep = Column(VARCHAR(50), charset="utf8", nullable=False)
    cidade = Column(VARCHAR(250), charset="utf8", nullable=False)
    uf = Column(VARCHAR(50), charset="utf8", nullable=False)
    valor_do_emprestimo = Column(DECIMAL(10, 2), nullable=False)
    valor_da_parcela = Column(DECIMAL(10, 2), nullable=False)
    total_parcelas = Column(INT(22), charset="utf8", nullable=False)
    parcela = Column(INT(22), charset="utf8", nullable=False)
    data_de_emissao = Column(DATE, nullable=False)
    data_de_vencimento = Column(DATE, nullable=False)
    preco_de_aquisicao = Column(DECIMAL(10, 2), nullable=False)
