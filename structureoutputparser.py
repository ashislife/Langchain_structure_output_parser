from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

from langchain.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-9b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


# create schema 
schema=[
    ResponseSchema(name='fact1',description='Fact 1 about the topic'),
    ResponseSchema(name='fact2',description='Fact 1 about the topic'),
    ResponseSchema(name='fact3',description='Fact 1 about the topic'),
]

parser=StructuredOutputParser.from_response_schemas(schema)


# create template
template=PromptTemplate(
    template='Give 3 Fact about the {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt=template.invoke({'topic':'blackhole'})
result=model.invoke(prompt)

final_result=parser.parse(result.content)

print(final_result)

