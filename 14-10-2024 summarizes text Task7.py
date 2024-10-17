from langchain.prompts import PromptTemplate

template = "Summarize the following text : '{text}'"

prompt = PromptTemplate.from_template(template)

text_to_summarize = "In facte this tasks it is need more practes and need more informatino ,so in the later time it is only need more study"

formatted_prompet = prompt.format(text=text_to_summarize)

print(formatted_prompet)
