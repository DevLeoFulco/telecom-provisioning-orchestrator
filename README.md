Aqui está o conteúdo formatado em **Markdown editável** para você usar diretamente como `README.md` no seu projeto:

```markdown
# 📡 Telecom Provisioning Orchestrator

Projeto de estudo voltado à orquestração de processos de provisionamento de serviços de telecomunicações utilizando **Python**, **FastAPI** e **Camunda 8**.

---

## 🎯 Objetivo

Simular um fluxo real de provisionamento de serviços de telecomunicações, aplicando conceitos de:

- BPMN  
- Camunda 8  
- Zeebe  
- Job Workers  
- Python  
- FastAPI  
- APIs REST  
- Clean Architecture  
- Arquitetura Hexagonal  
- SOLID  
- DDD  
- Resiliência  
- Idempotência  
- Observabilidade  
- Testes automatizados  

---

## 🏗 Arquitetura atual

```text
HTTP
 ↓
FastAPI Router
 ↓
Application Use Case
 ↓
Domain
 ↓
Repository Port
 ↓
Infrastructure Adapter
```

---

## ⚙️ Requisitos

- Python 3.11+  
- pip  

---

## 🔧 Configuração

Criar ambiente virtual:

```bash
python -m venv .venv
```

Ativar no Windows:

```bash
.\.venv\Scripts\Activate.ps1
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

---

## 🚀 Executando a aplicação

Rodar servidor:

```bash
uvicorn app.main:app --reload
```

Swagger UI:  
[http://localhost:8000/docs](http://localhost:8000/docs)

Health check:  
[http://localhost:8000/health](http://localhost:8000/health)

---

## 🧪 Executando os testes

```bash
pytest
```

---

## 📌 Próximas etapas

- Integração com **Camunda 8**  
- Modelagem de processo **BPMN** de provisionamento  
- Configuração do **Zeebe**  
- Implementação de **Job Workers** em Python  
- Integrações REST  
- Retry e tratamento de incidentes  
- Idempotência  
- Observabilidade  

---
