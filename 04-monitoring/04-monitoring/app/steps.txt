Docker compose up

#STEPS FOR INITIALISING POSTGRES
$export POSTGRES_HOST = "localhost"
(Run) python prep.py

pip install pgcli
pgcli -h localhost -U your_username -d course_assistant -W #connecting to postgres
$ pgcli -h  localhost -U your_username -d course_assistant -W 

\l 

\c course_assistant #connect to course assistant dataves

\dt #list all the tables

select * from conversations
select * from feedback


#INITIALIZE DOCKER CONTAINER
docker-compose up (Incase it fails use : docker-compose rebuild)

#INITIALISE OLLAMA
Ollama and pull model

docker ps (to check ollama)
docker exec -t <container name/no.>  bash
ollama pull phi3 (can be any other model e.g.LLAMA)

#STOPPING SPECIFIC DOCKER SERVICE

docker-compose stop streamlit
docker-compose start streamlit
docker logs -f (#to check logs)


#TESTING APP ON STREAMLIT
localhost:8501

#Output all versions of packages

pip freeze > pip-freeze