"""
--- Plano ---
Requisitos escolhidos: 
1. Visualização de vagas em tempo real.
2. Alerta de restrição para vagas de funcionários.
Ordem de implementação: Primeiro o mapeamento (req 1), pois o sistema de validação (req 2) depende de existir um mapa para consultar.
Tempo: 20 min para Req 1, 20 min para Req 2, 10 min para integração no main.py.
Uso de IA: Utilizado para estruturar as classes em Python já que nunca tinha mexido com python.
-------------------------
"""

from req1_visualizacao import MapaEstacionamento
from req2_restricao import ValidadorVaga
import sys

def iniciar_prototipo():
    print("Iniciando Protótipo do Estacionamento...\n")
    
    # Executando Requisito 1
    mapa = MapaEstacionamento()
    vagas_atuais = mapa.mostrar_vagas()
    
    # Executando Requisito 2
    validador = ValidadorVaga()
    print("\nSimulando a interação do usuário...")
    validador.verificar_permissao("a1", vagas_atuais) # Deve permitir
    validador.verificar_permissao("b2", vagas_atuais) # Deve bloquear (Funcionário)
    
if __name__ == "__main__":
    iniciar_prototipo()
    
"""
--- Autoavaliação ---
Critérios atingidos: A pasta contém a lista de requisitos (1), arquivos separados por classe/requisito (2), ponto de entrada único sem erro (3 e 6),
3 commits realizados (4) e README documentado (5).
Uso de IA: A ajuda da IA/minha dificuldade foi fazer o código, pois ainda não sei como fazer o código em Python, apenas acompanhei o raciocinio para ver se a implementação está correta.

"""
