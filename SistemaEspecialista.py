#Base de Conhecimento
filmes = [
    {"Título": "De volta ao Jogo", "Gênero": "Ação", "Gênero_Pessoa": "Masculino", "Faixa Etária": "Jovem"},
    {"Título": "O Homem Invisível", "Gênero": "Terror", "Gênero_Pessoa": "Masculino", "Faixa Etária": "Jovem", "Horário": "Noite"},
    {"Título": "O Auto da Compadecida", "Gênero": "Comedia", "Gênero_Pessoa": "Masculino", "Faixa Etária": "Jovem"},

    {"Título": "Os Mercenários", "Gênero": "Ação", "Gênero_Pessoa": "Masculino", "Faixa Etária": "Adulto"},
    {"Título": "O Poderoso Chefão", "Gênero": "Drama", "Gênero_Pessoa": "Masculino", "Faixa Etária": "Adulto"},
    
    {"Título": "Titanic", "Gênero": "Romance", "Gênero_Pessoa": "Feminino", "Faixa Etária": "Jovem"},
    {"Título": "O Homem Invisível", "Gênero": "Terror", "Gênero_Pessoa": "Feminino", "Faixa Etária": "Jovem", "Horário": "Noite"},
    {"Título": "O Silêncio dos Inocentes", "Gênero": "Suspense", "Gênero_Pessoa": "Feminino", "Faixa Etária": "Jovem"},

    {"Título": "Romeu +", "Gênero": "Romance", "Gênero_Pessoa": "Feminino", "Faixa Etária": "Adulto"},
    {"Título": "A Culpa é das Estrelas", "Gênero": "Drama", "Gênero_Pessoa": "Feminino", "Faixa Etária": "Adulto"},
]

#Regras
regras = [
    {"Condição": {"Gênero": "Ação","Gênero_Pessoa": "Masculino", "Faixa Etária": "Jovem"}, "Recomendação": ["De volta ao Jogo"]},
    {"Condição": {"Gênero": "Terror", "Gênero_Pessoa": "Masculino", "Faixa Etária": "Jovem", "Horário": "Noite"}, "Recomendação": ["O Homem Invisível"]},
    {"Condição": {"Gênero": "Comedia", "Gênero_Pessoa": "Masculino", "Faixa Etária": "Jovem"}, "Recomendação": ["O Auto da Compadecida"]},

    {"Condição": {"Gênero": "Ação","Gênero_Pessoa": "Masculino", "Faixa Etária": "Adulto"}, "Recomendação": ["Os Mercenários"]},
    {"Condição": {"Gênero": "Drama", "Gênero_Pessoa": "Masculino", "Faixa Etária": "Adulto"}, "Recomendação": ["O Poderoso Chefão"]},


    {"Condição": {"Gênero": "Romance", "Gênero_Pessoa": "Feminino", "Faixa Etária": "Jovem"}, "Recomendação": ["Titanic"]},
    {"Condição": {"Gênero": "Terror", "Gênero_Pessoa": "Feminino", "Faixa Etária": "Jovem", "Horário": "Noite"}, "Recomendação": ["O Homem Invisível"]},
    {"Condição": {"Gênero": "Suspense", "Gênero_Pessoa": "Feminino", "Faixa Etária": "Jovem"}, "Recomendação": ["O Silêncio dos Inocentes"]},

    {"Condição": {"Gênero": "Romance", "Gênero_Pessoa": "Feminino", "Faixa Etária": "Adulto"}, "Recomendação": ["Romeu + Julieta"]},
    {"Condição": {"Gênero": "Drama", "Gênero_Pessoa": "Feminino", "Faixa Etária": "Adulto"}, "Recomendação": ["A Culpa é das Estrelas"]},
    
]

def recomendar_filmes(preferencias):   

    recomendacoes = []

    for regra in regras:
        condicao = regra["Condição"]

        if(preferencias["Gênero"] == condicao["Gênero"] and
            preferencias["Faixa Etária"] == condicao["Faixa Etária"] and
            preferencias["Gênero_Pessoa"] == condicao["Gênero_Pessoa"]):
                
                if "Horário" in condicao:
                    if "Horário" not in preferencias or preferencias["Horário"] != condicao["Horário"]:
                        return []
                    
                recomendacoes.extend(regra["Recomendação"])

    return recomendacoes

 

def main():
    #Coletar preferências do usuário
    genero = input("Qual gênero de filme você prefere? ")
    faixa_etaria = input("Qual é a sua faixa etária? ")
    genero_pesso = input("Qual o seu gênero? ")

    preferencias = {
        "Gênero": genero,
        "Faixa Etária": faixa_etaria,
        "Gênero_Pessoa": genero_pesso
    }

    if(faixa_etaria == "Jovem" and genero == "Terror"):
        horario = input("Qual o horário [Dia,Noite]? ")
        if horario == "Noite":
            preferencias["Horário"] = horario
    
    #Obter recomendações
    filmes_recomendados = recomendar_filmes(preferencias)

    #Mostrar recomendações 
    if filmes_recomendados:
        print("Filmes Recomendados:")
        for filme in filmes_recomendados:
            print(f"- {filme}")
    else:
        print("Nenhuma recomendação disponível para suas preferências.")

if __name__ == "__main__":
    main()