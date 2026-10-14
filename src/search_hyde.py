from prompts_mba import build_prompt_HyDE, build_prompt_with_context
from llm_models import invoke_llm, similarity_search, format_chunks_as_string

def search_HyDE(question):
    print("Search HyDE.")

    print("Gerando o prompt do documento hipotético")
    prompt_HyDE = build_prompt_HyDE(question)

    print("Invocando LLM para obter documento hipotético")
    hypothetical_Document = invoke_llm(prompt_HyDE, temperature=0.3)

    print("Fazendo busca semântica")
    similarity_search_result = similarity_search(hypothetical_Document, k=10)
    context = format_chunks_as_string(similarity_search_result)

    promptContext = build_prompt_with_context(context, question)
    print("Invocando novamente a LLM usando prompt com mais contexto")
    response = invoke_llm(promptContext, temperature=0)

    return response
