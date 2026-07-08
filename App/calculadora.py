class Calculadora:
    
    @staticmethod
    def sumar(a: int, b: int) -> int:
        return a + b
    
    @staticmethod
    def restar(a: int, b: int) -> int:
        return a - b
    
    @staticmethod
    def multiplicar(a: int, b: int) -> int:
        return a * b
    
    @staticmethod
    def dividir(a:int, b:int) -> float:
        return a / b
    
    @staticmethod
    def potencia(base:int, exponente:int) -> int:
        if exponente <= 0:
            return None
        return base ** exponente
    
