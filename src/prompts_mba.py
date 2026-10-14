def build_prompt_with_context(context, question):
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

    return promptTemplate.format(contexto = context, pergunta = question)

def build_prompt_HyDE(question):
    templatePrompt = """
    Escreva um parágrafo conciso que responda de forma clara
    à pergunta abaixo. A resposta deve parecer um documento real,
    com datas, fatos ou descrições prováveis, mesmo que hipotéticas.
    Não use linguagem especulativa (não diga "talvez" ou "possivelmente").
    Pergunta: "{pergunta}"
    """

    return templatePrompt.format(pergunta=question)

def build_prompt_HyDETestar(question):
    templatePrompt = """
    Você é um especialista em investimentos. Escreva um parágrafo técnico e detalhado para responder à pergunta do usuário. 
    Não se preocupe se o dado exato é real ou inventado, foque em usar a terminologia correta do mercado e a estrutura de um relatório financeiro.
    Pergunta: {pergunta}
    """

    return templatePrompt.format(pergunta=question)
