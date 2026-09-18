class MapaEstacionamento:
    def __init__(self):
    # Simulando o banco de dados de vagas
        self.vagas = {
            "A1": "Livre",
            "A2": "Livre",
            "B1": "Ocupada",
            "B2": "Livre (Funcionário)",
            "C1": "Ocupada"
        }

    def mostrar_vagas(self):
        print("\n--- MAPA DE VAGAS EM TEMPO REAL ---")
        for vaga, status in self.vagas.items():
            print(f"Vaga {vaga}: {status}")
        print("-----------------------------------")
        return self.vagas
