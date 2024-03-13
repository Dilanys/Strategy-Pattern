class IAtaqueBehavior:
    def ataque(self):
        pass


class AtaquePuño(IAtaqueBehavior):
    def ataque(self):
        print("Estoy atacando con puño")


class AtaqueArco(IAtaqueBehavior):
    def ataque(self):
        print("Estoy atancando con arco")


class AtaqueEspada(IAtaqueBehavior):
    def ataque(self):
        print("Estoy atancando con espada")


class IMovimientoBehavior():
    def movimiento(self):
        pass


class MovimientoCaminando(IMovimientoBehavior):
    def movimiento(self):
        print("Estoy caminado")


class MovimientoEnCaballo(IMovimientoBehavior):
    def movimiento(self):
        print("Estoy andando en caballo")


class UnidadesMilitares:
    def __init__(self, ataque_behavior: IAtaqueBehavior, movimiento_behavior: IMovimientoBehavior) -> None:
        self.ataque_behavior=ataque_behavior
        self.movimiento_behavior=movimiento_behavior


    def perfore_ataque(self):
        self.ataque_behavior.ataque()


    def perfore_movimiento(self):
        self.movimiento_behavior.movimiento()


class Soldado(UnidadesMilitares):
    def __init__(self) -> None:
        super().__init__(AtaquePuño(),MovimientoCaminando())


class Arquero(UnidadesMilitares):
    def __init__(self) -> None:
        super().__init__(AtaqueArco(),MovimientoEnCaballo())


class Caballero(UnidadesMilitares):
    def __init__(self) -> None:
        super().__init__(AtaqueEspada(),MovimientoCaminando())


if __name__ == "__main__":
    unidad_militar=Soldado()
    unidad_militar.perfore_ataque()
    unidad_militar.perfore_movimiento()