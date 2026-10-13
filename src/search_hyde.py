from prompts_mba import buildPromptHyDE
from llm_models import invokePrompt, similaritySearch

def searchHyde(pergunta:None):
    promptHyde = buildPromptHyDE(pergunta)

    hypotheticalDocument = invokePrompt(promptHyde, temperature=0.3)

    return similaritySearch(hypotheticalDocument, k=3)

if __name__ == "__main__":
    searchHyde()