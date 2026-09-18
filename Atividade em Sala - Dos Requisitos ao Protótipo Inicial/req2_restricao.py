# req2_restricao.py
class ValidadorVaga:
    def verificar_permissao(self, vaga_selecionada, mapa_atual):
        vaga = vaga_selecionada.upper()
        if vaga not in mapa_atual:
            print("\n[ERRO] Vaga inexistente.")
            return False
        
        status = mapa_atual[vaga]
        
        if status == "Ocupada":
            print(f"\n[AVISO] A vaga {vaga} já está ocupada.")
            return False
        elif "Funcionário" in status:
            print(f"\n[ALERTA] Atenção: A vaga {vaga} é de uso exclusivo para funcionários. Proibido estacionar!")
            return False
        else:
            print(f"\n[SUCESSO] Você selecionou a vaga {vaga}. Estacionamento liberado!")
            return True
