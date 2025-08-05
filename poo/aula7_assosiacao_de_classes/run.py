from pessoa import Pessoa
from interruptor import Interruptor

def main():
    interruptor_quarto = Interruptor("Quarto")
    pessoa_com_nome_julia = Pessoa(interruptor_quarto)
    
    pessoa_com_nome_julia.acender_luz()
    pessoa_com_nome_julia.apagar_luz()
    pessoa_com_nome_julia.dormir()

if __name__ == "__main__":
    main()
