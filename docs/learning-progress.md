# Progresso dos estudos

Este documento registra os conceitos trabalhados, as decisões tomadas e o estado
pedagógico do projeto. Ele não substitui o material das aulas.

## Aula 01 — Fundamentos: o que é dbt

Status: Concluída

### Conceitos trabalhados

- papel do dbt na transformação de dados dentro de uma arquitetura de dados;
- uso do dbt sobre dados já disponíveis em um warehouse;
- estrutura básica de um projeto dbt;
- organização inicial de models SQL;
- execução local de um projeto dbt.

### Decisões tomadas no projeto

- DuckDB adotado como warehouse local de estudos;
- schema `raw` utilizado para os dados de origem;
- models organizados inicialmente nos diretórios `staging` e `marts`;
- models de staging direcionados ao schema `staging` e materializados como views;
- models de marts direcionados ao schema `marts` e materializados como tables;
- banco local `lab.duckdb` mantido fora do versionamento.

### Arquivos ou configurações relevantes

- `dbt_project.yml`;
- `pyproject.toml`;
- `scripts/create_raw.py`;
- `models/staging/`;
- `models/marts/`.

### Observações

- o projeto utiliza o profile local `estudos_dbt`;
- a tabela `raw.orders` é criada localmente por `scripts/create_raw.py` para os exercícios;
- existem usos iniciais de `source()` e `ref()` no projeto, que serão aprofundados na aula correspondente;
- tests, documentação de models e demais recursos serão tratados conforme o avanço da trilha.

