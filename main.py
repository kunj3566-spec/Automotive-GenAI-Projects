from dotenv import load_dotenv
load_dotenv()

from app.vector_store import get_or_create_vector_store
from app.retriever import retrieve_context
from app.llm import generate_answer
from app.prompts import build_rag_prompt
from app.memory import Memory
from app.agent import route_query

db = get_or_create_vector_store()
memory = Memory()

print("AI Assistant (type 'exit' to quit)")

while True:
    query = input("\nYou: ")

    if query.lower() == "exit":
        break

    route, tool_result = route_query(query)

    if route == "tool":
        answer = tool_result
    else:
        context = retrieve_context(db, query)
        mem_context = memory.get_context()
        prompt = build_rag_prompt(context, mem_context, query)
        answer = generate_answer(prompt)

    print("\nAssistant:", answer)
    memory.add(query, answer)