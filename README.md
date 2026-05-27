# ThreatGuard AI

Plataforma de Detecção e Resposta a Ameaças Autônoma com IA.

## Visão geral

Este repositório contém a estrutura inicial do monorepo para o projeto **ThreatGuard AI**, com:

- Frontend em Next.js 15 + TypeScript
- Backend em FastAPI (Python)
- Pacotes compartilhados para tipos, UI e agentes de IA
- Base de infraestrutura (Terraform/Kubernetes)
- Documentação de arquitetura e schema inicial de dados

## Estrutura de pastas

```bash
threatguard-ai/
├── apps/
│   ├── frontend/
│   └── backend/
├── packages/
│   ├── shared/
│   ├── ui/
│   └── ai-agents/
├── infra/
├── docs/
└── docker-compose.yml
```

## Execução local (MVP base)

### Backend

```bash
cd apps/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# opcional para fluxos de IA:
# pip install -r requirements-ai.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd apps/frontend
npm install
npm run dev
```

## Desenvolvimento no VS Code

- Extensões recomendadas: Python (Pylance), ESLint, Prettier, Docker, Kubernetes, GitLens
- Estrutura pronta para evolução em fases (MVP, Fase 2, Fase 3)
