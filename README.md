# 🎬 Sistema de Recomendação de Filmes (Baseado em Regras)

Este projeto implementa um sistema simples de recomendação de filmes utilizando **base de conhecimento fixa** e **regras condicionais**.  
A recomendação é feita com base nas preferências informadas pelo usuário: gênero do filme, faixa etária, gênero da pessoa e, em casos específicos, o horário.

---

## 📌 Funcionalidade

O programa:

1. Coleta preferências do usuário via `input()`.
2. Compara essas preferências com as regras definidas.
3. Retorna filmes recomendados de acordo com a combinação encontrada.
4. Caso nenhuma regra seja atendida, informa que não há recomendações disponíveis.

---

## 🧠 Estrutura do Sistema

### **Base de Conhecimento**

A base contém filmes com atributos como:

- **Título**
- **Gênero**
- **Gênero da pessoa**
- **Faixa etária**
- **Horário** (opcional)

### **Regras**

Cada regra contém:
- Uma **condição**, composta por atributos.
- Uma ou mais **recomendações** de filmes.

---

## 🔍 Como Funciona

### **Função `recomendar_filmes(preferencias)`**
- Percorre todas as regras.
- Compara a condição da regra com as preferências informadas.
- Adiciona os filmes recomendados à lista final.

### **Função `main()`**
- Solicita as preferências do usuário.
- Pede o horário **apenas quando necessário** (gênero *Terror* + faixa etária *Jovem*).
- Exibe a recomendação final.

---

## ▶️ Exemplo de Execução

Qual gênero de filme você prefere? Terror
Qual é a sua faixa etária? Jovem
Qual o seu gênero? Masculino
Qual o horário [Dia,Noite]? Noite

Filmes Recomendados:

O Homem Invisível

---

## 🚀 Como Executar

No terminal, execute:

```bash
python nome_do_arquivo.py

```
---

## 📌 Pontos Importantes

- O sistema funciona por **regras fixas**.
- Caso as preferências não existam nas regras, nenhum filme será recomendado.
- A pergunta sobre horário aparece apenas quando:
  - **Faixa Etária = Jovem**
  - **Gênero = Terror**

---

## 🛠 Melhorias Futuras

- Expandir a base de filmes.
- Permitir múltiplas preferências (ex.: mais de um gênero).
- Criar API, interface web ou interface gráfica.
- Implementar um sistema de recomendação baseado em pontuação ou aprendizado de máquina.

---
