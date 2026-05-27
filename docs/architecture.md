# Arquitetura de Alta Nível — ThreatGuard AI

## Camadas

1. **Ingestão**: logs de EDR, CloudTrail, Office 365, Firewalls e outras fontes.
2. **Processamento**:
   - Motor de regras
   - Motor de ML (anomalia comportamental)
   - Agentes de IA para investigação
3. **Decisão**: pontuação de risco + human-in-the-loop para ações críticas.
4. **Resposta**: integração SOAR para isolamento, bloqueios e revogação de acesso.
5. **Apresentação**: dashboard com timeline, kill chain e mapeamento MITRE ATT&CK.

## Fases

- **MVP (Fase 1)**: ingestão/normalização, detecção de anomalias, timeline, alertas.
- **Fase 2**: investigação autônoma, UEBA, threat intel e playbooks.
- **Fase 3**: multi-tenancy completo, RBAC/ABAC, auditoria imutável e cadeia de custódia.
