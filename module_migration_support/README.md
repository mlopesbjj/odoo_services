# Module Migration Support

## Objetivo

O aplicativo `Module Migration Support` foi criado para apoiar migracoes de versao do Odoo.

Ele permite:

- exportar a lista de modulos instalados da base atual para um arquivo Excel;
- importar um arquivo Excel gerado em uma base antiga;
- comparar os modulos da base antiga com os modulos instalados na base atual;
- identificar quais modulos ainda faltam ser instalados na versao mais recente.

O foco do aplicativo nao e executar a migracao dos modulos. O objetivo e entregar um relatorio confiavel para analise tecnica e acompanhamento do projeto de migracao.

## Visao geral visual

### Tela de exportacao da base atual

![Tela ficticia de exportacao](static/description/screen_export.svg)

### Tela de comparacao entre origem e destino

![Tela ficticia de comparacao](static/description/screen_compare.svg)

### Exemplo do arquivo final gerado

![Tela ficticia do relatorio final](static/description/screen_report.svg)

## Como o aplicativo funciona

O modulo cria um menu chamado `Migration Support` no Odoo.

Dentro desse menu existe a tela `Installed Modules Report`. Cada registro dessa tela representa uma analise de migracao.

O fluxo de uso foi pensado em duas etapas:

1. gerar o Excel da base atual;
2. comparar a base atual com um Excel gerado na base antiga.

## Fluxo recomendado

### 1. Exportar os modulos da base antiga

Instale o modulo na base antiga e abra:

`Migration Support > Installed Modules Report`

Depois:

1. crie um novo registro;
2. clique em `Export Current DB`;
3. baixe o arquivo gerado em `Download Export`.

Esse arquivo Excel sera a fotografia dos modulos instalados na versao antiga.

## 2. Comparar com a base nova

Na base nova, com o mesmo modulo instalado:

1. abra `Migration Support > Installed Modules Report`;
2. crie um novo registro;
3. envie no campo `Source XLSX` o arquivo exportado da base antiga;
4. clique em `Compare Modules`;
5. baixe o arquivo final em `Download Report`.

Ao final da comparacao, o proprio registro mostrara:

- quantidade de modulos da origem;
- quantidade de modulos instalados na base atual;
- quantidade de modulos faltantes;
- quantidade de modulos em comum;
- lista detalhada dos modulos faltantes.

## Estrutura do arquivo Excel exportado

O Excel gerado pela funcao `Export Current DB` contem uma aba chamada `modules`.

Cada linha representa um modulo instalado no banco de dados atual.

As colunas exportadas sao:

- `name`: nome tecnico do modulo;
- `display_name`: nome funcional do modulo;
- `installed_version`: versao instalada no banco;
- `latest_version`: ultima versao conhecida pelo Odoo naquela base;
- `author`: autor informado no modulo;
- `category`: categoria funcional;
- `application`: indica se o modulo e marcado como aplicacao;
- `auto_install`: indica se o modulo e auto-instalavel;
- `state`: estado atual do modulo.

## Estrutura do arquivo Excel de comparacao

O arquivo final gerado pela comparacao contem varias abas:

### `summary`

Mostra um resumo executivo da comparacao.

Campos principais:

- `Source installed modules`: total de modulos encontrados no arquivo da base antiga;
- `Current DB installed modules`: total de modulos instalados na base atual;
- `Missing in current DB`: total de modulos da origem que nao existem instalados na base nova;
- `Common modules`: total de modulos encontrados em ambas as bases.

Essa aba e a melhor visao inicial para acompanhamento do progresso da migracao.

### `source_modules`

Lista completa dos modulos instalados na base antiga, conforme o arquivo enviado.

Use essa aba quando quiser confirmar se um modulo realmente fazia parte da origem.

### `target_modules`

Lista completa dos modulos instalados na base atual no momento da comparacao.

Use essa aba para validar o estado atual da versao nova.

### `missing_in_target`

Essa e a aba principal para a migracao.

Ela mostra todos os modulos que existiam na base antiga, mas ainda nao aparecem como instalados na base atual.

Interpretacao:

- se um modulo aparece aqui, ele ainda precisa ser analisado;
- ele pode precisar ser instalado;
- ele pode precisar ser migrado antes de instalar;
- ele pode ter sido substituido por outro modulo;
- ele pode nao ser mais necessario na nova arquitetura.

Nem todo modulo faltante deve ser instalado automaticamente. O relatorio aponta a diferenca; a decisao funcional e tecnica continua sendo da equipe de migracao.

### `common_modules`

Mostra os modulos que existem tanto na origem quanto no destino.

Interpretacao:

- esses modulos ja estao contemplados na base nova;
- em geral, eles nao sao prioridade imediata de instalacao;
- ainda assim, a equipe pode validar versao, dependencia e comportamento funcional.

## Como interpretar o resultado corretamente

O aplicativo compara modulos pelo nome tecnico (`name`).

Isso significa que:

- se um modulo foi renomeado entre uma versao e outra, ele pode aparecer como faltante mesmo tendo sido substituido;
- se um modulo deixou de existir e sua funcao foi absorvida pelo core ou por outro addon, ele tambem pode aparecer como faltante;
- se um modulo customizado ainda nao foi portado, ele aparecera como faltante, o que ajuda a montar o backlog de migracao.

Por isso, a aba `missing_in_target` deve ser lida como uma lista de pendencias para analise, nao como uma lista cega de instalacao obrigatoria.

## Boas praticas de uso

- gere o Excel da base antiga o mais proximo possivel do inicio da migracao;
- use sempre um arquivo exportado pelo proprio aplicativo para evitar erro de formato;
- execute a comparacao novamente sempre que novos modulos forem instalados na base nova;
- use o total de `Missing in current DB` como indicador de progresso do projeto;
- trate modulos customizados e modulos OCA com atencao especial, porque geralmente exigem portabilidade ou validacao adicional.

## Limitacoes atuais

- a comparacao considera apenas modulos no estado `installed`;
- a comparacao nao verifica se o modulo foi substituido por outro de nome diferente;
- a comparacao nao valida compatibilidade funcional entre versoes;
- a comparacao nao instala modulos automaticamente;
- a comparacao nao analisa dependencias tecnicas pendentes.

## Resumo pratico

Em termos simples, o aplicativo responde a pergunta:

`quais modulos que eu tinha na base antiga ainda nao estao instalados na base nova?`

Esse e o uso correto da ferramenta dentro de um processo de migracao de versao do Odoo.
