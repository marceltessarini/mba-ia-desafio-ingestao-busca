def build_direct_RAG_prompt(contexto, pergunta):
    promptTemplate = """
    CONTEXTO:
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

    return promptTemplate.format(contexto = contexto, pergunta = pergunta)

def build_prompt_HyDE(pergunta):
    templatePrompt = """
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

    return templatePrompt.format(pergunta=pergunta)
