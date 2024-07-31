Additional notes for those trying the streamlit/grafana out
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