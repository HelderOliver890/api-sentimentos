# API de análise de sentimentos

# Descrição
API REST feita com FastAPI para análise simples de sentimentos.

# Como executar

# Local
pip install -r requirements.txt
uvicorn main:app --reload

# Docker
docker build -t api-sentimentos .
docker run -p 8000:8000 api-sentimentos

# Deploy
https://api-sentimentos-latest.onrender.com

# Endpoints
GET /
POST /sentimento
