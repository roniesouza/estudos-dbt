# Estudos de dbt

Repositório de aprendizado prático de dbt e Engenharia de Dados. O projeto usa
DuckDB como warehouse local para exercitar transformações e a organização de um
projeto dbt de forma progressiva.

## Tecnologias

- Python 3.14;
- dbt Core;
- dbt-duckdb;
- DuckDB;
- uv para gerenciamento do ambiente Python.

## Pré-requisitos

- Git;
- uv;
- um profile local do dbt chamado `estudos_dbt`, configurado para usar o arquivo
  `lab.duckdb`.

O arquivo `profiles.yml` contém configurações locais e fica fora deste
repositório. Consulte a documentação oficial do dbt para configurar um profile.

## Configuração do ambiente

Clone o repositório e instale as dependências:

```bash
uv sync
```

Crie o schema e os dados de origem usados nos exercícios:

```bash
uv run python scripts/create_raw.py
```

Valide a configuração e execute o projeto:

```bash
uv run dbt debug
uv run dbt build
```

## Estrutura do projeto

```text
.
├── docs/                  # Progresso pedagógico
├── models/
│   ├── marts/             # Models voltados ao consumo
│   └── staging/           # Preparação inicial dos dados de origem
├── scripts/               # Preparação do ambiente local de estudos
├── dbt_project.yml        # Configuração do projeto dbt
└── pyproject.toml         # Dependências e configuração Python
```

O banco `lab.duckdb`, ambientes virtuais, logs e artefatos gerados pelo dbt não
são versionados.

## Progresso dos estudos

As aulas concluídas, os conceitos estudados e as decisões tomadas estão
registrados em [`docs/learning-progress.md`](docs/learning-progress.md).

## Convenções

- alterações são registradas usando Conventional Commits em português;
- a branch principal do projeto é `main`;
- o conteúdo evolui de acordo com a trilha registrada, sem antecipar etapas.
