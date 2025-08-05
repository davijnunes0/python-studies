class ConectorBancoDeDados:


    def __init__(self) -> None:
        self.connection =  None

    def conectar_ao_banco(self) -> None:
        self.connection = True


# O repositório de banco de dados depende da conexão, mas, usamos injenção de depedência através do construtor.
class RepositorioDeBanco:

    def __init__(self,conexao: ConectorBancoDeDados) -> None:
        self.__conexao = conexao

    def buscar_dados(self) -> list:
        if self.__conexao.connection:
            return [1,2,3,4,5]

        return None


# A regra de negócio depende do repositório de banco de dados, mas, usamos a injeção de dependência através do construtor.
class RegraDeNegocio:
    def __init__(self,repositorio: RepositorioDeBanco) -> None:
        self.__repositorio = repositorio

    def calcular_resultado(self) -> None:
        dados = self.__repositorio.buscar_dados()

        total = 0

        if dados:
            for dado in dados:
                total = total + dado

            print("Resposta:",total)
        else:
            print("Dados não encontraados. Verifique sua conexão com o banco de dados")



conectorBancoDeDados = ConectorBancoDeDados()
conectorBancoDeDados.conectar_ao_banco()

repositorioDeBanco = RepositorioDeBanco(conectorBancoDeDados)
regraDeNegocio = RegraDeNegocio(repositorioDeBanco)

regraDeNegocio.calcular_resultado()
