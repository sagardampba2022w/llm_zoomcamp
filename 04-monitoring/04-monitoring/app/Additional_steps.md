Additional notes for those trying the streamlit/grafana out

export POSTGRES_HOST="localhost” before running python prep.py

ELASTIC_URL_LOCAL=http://localhost:9200

The following packages are required when you run some of .py scripts

```
pip install psycopg2-binary python-dotenv
pip install pgcli
```


To download the phi3 model to the container
```
docker-compose up -d
docker-compose exec ollama ollama pull phi3
```

Prep.py

uncomment first time and then comment back after running

def main():
  

    documents = fetch_documents()
    ground_truth = fetch_ground_truth()
    model = load_model()
    es_client = setup_elasticsearch()
    index_documents(es_client, documents, model)
   
