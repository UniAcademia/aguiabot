import peewee

# Instância do banco de dados
db = peewee.SqliteDatabase('banco_dados.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Avisos(BaseModel):
    id_usuario = peewee.BigIntegerField()
    id_emissor = peewee.BigIntegerField()
    descricao = peewee.CharField()
    data_cadastro = peewee.DateTimeField(constraints=[peewee.SQL("DEFAULT (datetime('now'))")])


def criar_tabelas():
    # region Avisos
    try:
        Avisos.create_table()
    except peewee.OperationalError:
        pass
    # endregion
