# Chatter
A chat bot builder app
## Usecase
-
## Environmental variables
Please set these environmental variable before running the solution.
| Environment Variables      | Description | Default |
| :----        |    :-----:   |    ---:    |
| ```OPENAI_API_KEY```      | OpenAI api key       |    |
| ```OPENAI_EMBEDD_MODEL```   | Name of the openAI embedding model        |    ```text-embedding-ada-002```  |
| ```PINECONE_API_KEY```      | Pinecone vectorDB key       |    |
| ```PINECONE_ENVIRONMENT```      | Pinecone environment name      |    |
| ```PINECONE_INDEX_NAME```      | Pinecone index name       |    |

## How to Run
After download the chatter repository, need to follow the mentioned steps.
- Install all the requested packages using this command before running the solution.

    ``` pip install -r requirements.txt ```
- To run the solution please type the below commands

  ``` streamlit run app.py ```
