from typing import TypedDict


class InvestigationState(TypedDict):
    question: str
    answer: str


def investigate_last_6h_activity(user_id: str) -> InvestigationState:
    question = f"O que o usuário {user_id} fez nas últimas 6h?"
    answer = "Fluxo inicial configurado. Integrações de dados serão conectadas na Fase 2."
    return {"question": question, "answer": answer}
