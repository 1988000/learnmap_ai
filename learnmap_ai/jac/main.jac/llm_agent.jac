walker ai_recommend():
    report byllm.complete(
        prompt="Suggest a simple learning path for becoming a software engineer",
        max_tokens=80
    )