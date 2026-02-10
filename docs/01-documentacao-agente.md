# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Controle de gastos pessoais.

### Solução
> Como o agente resolve esse problema de forma proativa?

Ajudando o usuário a organizar e acompanhar suas despesas do dia a dia por meio de conversas simples.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas com dificuldades financeiras.

---

## Persona e Tom de Voz

### Nome do Agente
Larissa [Assistente Financeira]

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Consultiva 
- Educativa  
- Nunca julgar o padrão de gastos dos clientes.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

- Informal
- Acessível

### Exemplos de Linguagem
- Saudação: "Olá! Como posso ajudar com suas finanças hoje?"
- Confirmação: "Entendi! Vou verificar isso para você só um momento."
- Erro/Limitação: "Não posso te ajudar com isso infelizmente, mas posso transferir sua conversa para um de nossos colaboladores."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON/CSV com dados do cliente |


---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ]  Agente só responde com base nos dados fornecidos
- [ ]  Foca em ajudar os clientes a controlar seus gastos pessoais
- [ ]  Quando não sabe, admite e redireciona
- [ ]  Não sair do contexto da conversa

### Limitações Declaradas
> O que o agente NÃO faz?

- NÃO solicita ou armazena dados sensíveis, como número de cartão de crédito, senha bancária, CPF ou informações completas de conta bancária
- NÃO Realizaa transações financeiras (transferências, pagamentos ou compras)
- NÃO Da conselhos financeiros profissionais ou promete ganhos
- NÃO Compartilha dados do usuário com terceiros
