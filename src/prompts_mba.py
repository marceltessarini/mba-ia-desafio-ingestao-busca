TEMPLATE_PROMPT_DIRECT_RAG = """CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

TEMPLATE_PROMPT_HYDE = """
Escreva um parágrafo conciso que responda de forma clara
à pergunta abaixo. A resposta deve parecer um documento real,
com data, fatos ou descrições prováveis, mesmo que hipotéticas.
Não use linguagem especulativa (não diga "talvez" ou "possivelmente")

Pergunta: {pergunta}
"""

TEMPLATE_PROMPT_HYDE_ROLE = """
Você é um especialista em mercado imobiliário e em investimentos.
Sua tarefa é escrever um parágrafo curto, técnico e formal 
(como se fosse um trecho extraído de um manual técnico ou relatório corporativo)
que responda diretamente à pergunta do usuário.
REGRAS ESTRITAS:
1. Escreva apenas o conteúdo técnico explicativo e factual.
2. NUNCA inclua saudações, introduções (ex: 'Aqui está:'), conversas ou notas de rodapé.
3. Utilize vocabulário técnico preciso e termos diretos.

Pergunta: {pergunta}
"""

oldPrompt = [
    (
        "system",
        "Você é um especialista sênior em engenharia, negócios e análise de dados. "
        "Sua tarefa é escrever um parágrafo curto, técnico e formal "
        "(como se fosse um trecho extraído de um manual técnico ou relatório corporativo) "
        "que responda diretamente à pergunta do usuário.\n\n"
        "REGRAS ESTRITAS:\n"
        "1. Escreva apenas o conteúdo técnico explicativo e factual.\n"
        "2. NUNCA inclua saudações, introduções (ex: 'Aqui está:'), conversas ou notas de rodapé.\n"
        "3. Utilize vocabulário técnico preciso e termos diretos."
    ),
    ("human", "Pergunta do Usuário: {pergunta}")
]