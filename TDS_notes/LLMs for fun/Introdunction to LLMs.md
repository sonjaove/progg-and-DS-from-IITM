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

---
## Refrences:

- [OpenAI docs(for using the API key)]()

- There is a section in google colab called `userdata` which has the option of kepping some things secret, and you would have to write 

    ```python
    from google.colab import userdata
    userdata.get('secretName')
    ```

    so this becomes a potential to store your api keys temporarily  

