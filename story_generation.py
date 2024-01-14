import google.generativeai as palm

def generate_story(prompt):
    palm.configure(api_key="AIzaSyA6Ztezs8qXHae_9X42IFIYoD4zdT95GoU")

    models = [
        m for m in palm.list_models() if "generateText" in m.supported_generation_methods
    ]

    model = models[0].name

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.7,
        max_output_tokens=900,
    )

    return completion.result