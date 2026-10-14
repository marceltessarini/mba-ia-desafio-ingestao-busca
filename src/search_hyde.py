from prompts_mba import build_prompt_HyDE
from llm_models import invoke_llm, similarity_search, format_chunks_as_string

def search_HyDE(question):
    print("Search HyDE.")


    print("Gerando o prompt")
    prompt_HyDE = build_prompt_HyDE(question)
    print("Prompt gerado: {p}\n".format(p = prompt_HyDE));

    print("Invocando LLM")
    hypothetical_Document = invoke_llm(prompt_HyDE, temperature=0.3)
    print("\n\nDocumento hipotetico: {d}".format(d=hypothetical_Document));

    print("\n\nFazendo busca semântica")
    similarity_search_result = similarity_search(hypothetical_Document, k=3)
    chunksAsString = format_chunks_as_string(similarity_search_result)

    return chunksAsString
