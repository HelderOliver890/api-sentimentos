#Aluno: Helder De Oliveira Barros
# API de análise de sentimentos

# Descrição
API REST com FastAPI para análise de sentimentos.

# Como executar

# Local
pip install -r requirements.txt
uvicorn main:app --reload

# Docker
docker build -t api-sentimentos .
docker run -p 8000:8000 api-sentimentos

https://hub.docker.com/repository/docker/helderolv8521/api-sentimentos/general

# Deploy
https://api-sentimentos-latest.onrender.com

# Endpoints
GET /
POST /sentimento

