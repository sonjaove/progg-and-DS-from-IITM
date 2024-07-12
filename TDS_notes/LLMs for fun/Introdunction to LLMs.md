# Aim of this module 

- perform some - 

    - **Sentimental analysis**

    - **Extraction**

    - **Topic modeling**

    - **Retrieval Augmented Generation (RAG)**

- We'll perform these taskes using GPT 3.5 turbo (the least capable model rn and the token for that is provided.)

- generally $token = {0.75} \times {word}$ as every model has a way of breaking up the word in its own way.

---

## Sentimental analysis 

- this is a very subjective thing, so is it possible that model itself might as well have a "personality" of its own? 
   
    now that depends on the model you're using, for eg, gpt 3.5 turbo would have to be given clear cut instructions about taking some things into account before giving the review, while gpt 4o might do it implicitly and yet there will be drastic difference in the answers you would get.

- use the api token provided and run
```python
def get_sentiment(review, debug=False):
    response = requests.post(
        f"{LLM_url}",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "gpt-4o",
            "messages": [
                {"role": "system", "content": "Identify the sentiment of the movie. JUST say positive / negative"}, #system field recieves the prompt.
                {"role": "user", "content": review} #this is the input you give, i.e the context of the prompt.     
            ]
        }
    )
    result = response.json()
    answer = result["choices"][0]["message"]["content"]
    print(answer)
    return answer
```

    this code, would mean that you are simply asking the model, without any training and simply asking, we could also train it and customize it.

- Zero-Shot, One-Shot, and Multi-Shot Learning: paradigms in machine learning and artificial intelligence that describe how models are trained and tested with limited examples

    1. **Zero-shot**: a type of learning where a model is asked to recognize or classify data that it has never seen during its training phase.

    2. **One-shot**: refers to the ability of a model to learn information about a class from a single training example.

    3. **Multi-shot/few shot**: refers to scenarios where a model is trained with a few (more than one, but still very few) examples of each new class.
---

## LLM Extraction.

---
## Refrences:

- [OpenAI docs(for using the API key)](https://github.com/sanand0/aiproxy)

- There is a section in google colab called `userdata` which has the option of kepping some things secret, and you would have to write 

    ```python
    from google.colab import userdata
    userdata.get('secretName')
    ```

    so this becomes a potential to store your api keys temporarily  

- [the colab notebook](https://colab.research.google.com/drive/1tVZBD9PKto1kPmVJFNUt0tdzT5EmLLWs#scrollTo=31N3ljM0qjlC)

- [OpneAI playground](https://platform.openai.com/playground/chat)