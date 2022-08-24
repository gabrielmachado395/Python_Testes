from typing import List, Union, Tuple, Dict, NewType, Callable, Sequence, Iterable

# Primitivos
numero: int = 10
flutuante: float = 10.5
booleano: bool = False
string: str = 'Otta'

# SequÊncias
lista: List[int] = [1, 2, 3]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Otta']
tupla: Tuple[int, int, int, bool] = (1, 2, 3, True)

# Dicionários e Conjutos

# Meu Tipo
MeuDict = Dict[str, Union[str, int, List[int]]] #Alias

pessoa: Dict[str, Union[str, int]] = {'nome': 'Otta', 'idade': 19}
pessoa2: MeuDict = {'nome': 'Otta', 'idade': 19, 'l': [1, 2]}

# Meu outro tipo
UserId = NewType('UserId', int)
user_id = UserId(563852)

def retorna_funcao(funca: Callable[[int, int], int]) -> Callable:
    return funcao

def soma(x: int, y: int) -> int:
    return x + y

print(retorna_funcao)

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome: str = nome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')

def iterar(sequencia: Sequence(int)):
    return [x for x in sequencia]

def iterar2(sequencia, Iterable[int]):
    return [x for x in sequencia]