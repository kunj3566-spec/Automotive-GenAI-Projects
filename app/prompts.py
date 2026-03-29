def build_rag_prompt(context, memory, question):
    return f"""
You are an automotive AI assistant.

Conversation history:
{memory}

Retrieved context:
{context}

User question:
{question}

Provide a clear, concise, and technically grounded answer.
"""