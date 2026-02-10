# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilizações da Larissa |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores com base em usos anteriores. |
| `perfil_investidor.json` | JSON | Personalizar recomendações ao cliente com base na base de dados. |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao cliente, com valores mais baixos. |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente, para ajudar no controle de gastos. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Sim, modifiquei alguns dados com base em um perfil de cliente que está buscando ajuda com controle de gastos.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Carregando os arquivos via código como no exemplo abaixo ou usando os dados direto no prompt (Copiando e Colando)

 import json
import pandas as pd 


perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para facilitar as consultas do nossa a gente podemos inserir os dados direto no prompt, porémm se a base de dados for muito grande, é recomendável que os dados sejam gerados por código.

```
Dados do cliente:
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Resolver problemas financeiros",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 0,
  "aceita_risco": true,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Sair do vermelho",
      "valor_necessario": 10000.00,
      "prazo": "2027-12"
    }
  ]
}

Resumo de transações:
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

Histórico de Atendimento:
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim


Produtos e serviços disponíves para ensino:
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]

```
## Exemplo de Contexto Montado


> Mostre um exemplo de como os dados são formatados para o agente.

Contém quase todos os dados listamos acima, mas de forma mais sentetizada e resumida.

Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000
- Objetivo Principal: Resolver problemas financeiros
- Meta 1: Completar reservar de emergência
- Meta 2: Sair do vermelho


Últimas transações:
- Data, Descricao, Categoria, Calor, Tipo:
- 2025-10-01 Salário, receita, 5000.00, entrada:
- 2025-10-02 Aluguel, moradia, 1200.00, saida:
- 2025-10-03 Supermercado,alimentacao, 450.00, saida:
- 2025-10-05 Netflix,lazer, 55.90, saida:
- 2025-10-07 Farmácia,saude ,89.00, saida:
- 2025-10-10 Restaurante, alimentacao,120.00, saida:
- 2025-10-12 Uber, transporte, 45.00, saida:
- 2025-10-15 Conta de Luz, moradia,180.00, saida:
- 2025-10-20 Academia,saude, 99.00, saida:
- 2025-10-25 Combustível, transporte, 250.00, saida:

Serviços e Ajuda:
- Tesouro Celic:
- CDB Liquidez diária:
- LCI/LCA:
- Fundo multimercado:
- Fundo de ações:

Histórico de Atendimento:
- Data, Canal, Tema, Resumo, Resolvido:
- 2025-09-15 chat, CDB, Cliente perguntou sobre rentabilidade e prazos, sim:
- 2025-09-22 telefone, Problema no app,Erro ao visualizar extrato foi corrigido, sim:
- 2025-10-01 chat, Tesouro Selic, Cliente pediu explicação sobre o funcionamento do Tesouro Direto, sim:
- 2025-10-12 chat, Metas financeiras, Cliente acompanhou o progresso da reserva de emergência, sim:
- 2025-10-25 email, Atualização cadastral, Cliente atualizou e-mail e telefone, sim:





