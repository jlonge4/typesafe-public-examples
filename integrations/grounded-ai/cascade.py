"""Jev answers first; only the questions it is unsure of go to an LLM judge.

pip install "grounded-ai[jev]"
Needs TYPESAFE_API_KEY, plus the judge's key (ANTHROPIC_API_KEY here).
"""

from grounded_ai import CascadeEvaluator
from grounded_ai.backends.jev import HALLUCINATION, JevInput

cascade = CascadeEvaluator(
    jev="jev/jev-latest",
    judge="anthropic/claude-haiku-4-5",  # any grounded-ai model string: openai/, anthropic/, bedrock/, hf/
    min_confidence=0.9,
)

context = "Michael Collins stayed in orbit while Armstrong and Aldrin walked on the Moon."
for response in ["Collins stayed in orbit.", "Aldrin stayed in orbit."]:
    result = cascade.evaluate(JevInput(
        state={"context": context, "response": response},
        questions={"verdict": HALLUCINATION},
    ))
    answer = result.answers["verdict"]
    if result.judged:
        print(f"{response:26} {answer.answer} (judge)")
    else:
        print(f"{response:26} {answer.choice} (Jev, confidence {answer.confidence:.2f})")
