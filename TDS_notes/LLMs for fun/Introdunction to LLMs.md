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

- this code, would mean that you are simply asking the model, without any training and simply asking, we could also train it and customize it.

- you would actaully have to go through the response you get and convert it to json and then extract the given data.


- Zero-Shot, One-Shot, and Multi-Shot Learning: paradigms in machine learning and artificial intelligence that describe how models are trained and tested with limited examples

    1. **Zero-shot**: a type of learning where a model is asked to recognize or classify data that it has never seen during its training phase.

    2. **One-shot**: refers to the ability of a model to learn information about a class from a single training example.

    3. **Multi-shot/few shot**: refers to scenarios where a model is trained with a few (more than one, but still very few) examples of each new class.
---

## LLM Extraction.

- We use AI to do json extracion persay so that, we can basically reduce the use of softwares like OpenRefine and stuff or we particularly don't have to pay heavy prices for things like that, which somewhat automates the process.
* JSON Schema is a vocabulary that allows you to annotate and validate JSON documents.
* It provides a way to describe the structure and constraints of JSON data.
* With JSON Schema, you can define the expected properties, types, and formats of the data,
* ensuring that it conforms to a specific schema.
* This helps in ensuring data consistency and interoperability between different systems.

- [is it possible that LLM is not able to retrive any field form a given schema ? i dont see though why would it not be able to(given the fact that model is well trained), until and unless any kind of specific condition is mentioned](https://youtu.be/72514uGffPE?si=_UObj08WX9pJ0VTP&t=1800)
---

## LLM topic modeling.

- the LLM converts the text given to it to numbers and somolar numbers have similar weights, the LLM conerts the input to an array of numbers (vectors in multidimensional space), if 2 vectors are close by then that means they have similar ***embedding*** or to say the words close to each other have similar meaning, you can visualizie this using [tensorflow projector](https://projector.tensorflow.org/)

- earlier vectorization of words was pretty simple, a sentence would be a serries of 0s and 1s based on a the dictinoary of words given, so the word or a piece of text would actually be a vector in n dimensions, but eventually it became more concept based i.e what the word means and stuff, and if you want to see the **distance** betweeen them, just find the ***dot product*** between the vectors of the words/sentenecs.

- current LLMs are almost entirely in concept space. 

- once you get the embeddings of a word you can then perform clustering using any clustering algorithm to clusrer them together. 

- you can also create embeddings of the topics to which the particular word belongs to as well.
---

## Retrieval Augmented Generation

- The technique of retrieving and using relevant documents to enhance model responses.

- similarity search also helps in getting accurate repsonses from the output of a model, as it means to find the most relevant documents by calculating cosine similarity between embeddings

---
## Refrences:

- [OpneAI playground](https://platform.openai.com/playground/chat), [openAI API refs](https://platform.openai.com/docs/api-reference/) and [openAI docs](https://platform.openai.com/docs/overview)

- There is a section in google colab called `userdata` which has the option of kepping some things secret, and you would have to write 

    ```python
    from google.colab import userdata
    userdata.get('secretName')
    ```

    so this becomes a potential to store your api keys temporarily  

- [the colab notebook for sentimental analysis](https://colab.research.google.com/drive/1tVZBD9PKto1kPmVJFNUt0tdzT5EmLLWs#scrollTo=31N3ljM0qjlC)

- [colab notebook for extraction](https://colab.research.google.com/drive/1Z8mG-RPTSYY4qwkoNdzRTc4StbnwOXeE#scrollTo=pahJEt2kvL7v)

- [colab notebook for topic modeling](https://colab.research.google.com/drive/15L075RLrwXkxa29EGT-1sNm_dqJRBTe_)

- [JSON Schema](https://json-schema.org/learn/getting-started-step-by-step)

- [embedding model rankings](https://huggingface.co/spaces/mteb/leaderboard)

- [gte-large-en-v1.5 embedding model](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5)

- [Awesome vector database](https://github.com/mileszim/awesome-vector-database)