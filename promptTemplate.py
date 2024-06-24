from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}."
)

from langchain_community.llms import Ollama

llm = Ollama(model="mistral", temperature=0)

chain = prompt_template | llm

response = chain.invoke({
    "adjective" : "sad",
    "content": "science" 
})

print(response)