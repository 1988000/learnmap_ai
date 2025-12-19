# test_byllm_safe.py
from jaseci.extens.svc.llm import byllm

# Safe call without running Jac walkers
response = byllm.complete(
    prompt="Suggest a simple learning path for becoming a software engineer",
    max_tokens=50
)

print("AI Response (Safe Windows):", response)