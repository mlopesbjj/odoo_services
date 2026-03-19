# Odoo Services

Ferramentas auxiliares para administracao e migracao de ambientes Odoo.

## Relatorio de modulos instalados

O script `tools/odoo_module_migration_report.py` permite:

- exportar os modulos instalados de um banco Odoo para Excel;
- comparar dois bancos Odoo; ou
- comparar um Excel exportado da versao antiga com um banco da versao nova.

### Dependencias

```bash
pip install -r requirements.txt
```

### Exportar modulos instalados

```bash
python tools/odoo_module_migration_report.py export \
  --host localhost \
  --port 5432 \
  --database odoo16_db \
  --user odoo \
  --password secret \
  --output odoo16_installed_modules.xlsx
```

### Comparar banco antigo com banco novo

```bash
python tools/odoo_module_migration_report.py compare \
  --source-host localhost \
  --source-port 5432 \
  --source-database odoo16_db \
  --source-user odoo \
  --source-password secret \
  --target-host localhost \
  --target-port 5432 \
  --target-database odoo18_db \
  --target-user odoo \
  --target-password secret \
  --output migration_modules_report.xlsx
```

### Comparar Excel antigo com banco novo

```bash
python tools/odoo_module_migration_report.py compare \
  --source-xlsx odoo16_installed_modules.xlsx \
  --target-host localhost \
  --target-port 5432 \
  --target-database odoo18_db \
  --target-user odoo \
  --target-password secret \
  --output migration_modules_report.xlsx
```

### Resultado

O arquivo Excel de comparacao contem:

- `source_modules`: modulos instalados na origem;
- `target_modules`: modulos instalados no destino;
- `missing_in_target`: modulos instalados na origem e ausentes no destino;
- `common_modules`: modulos encontrados em ambos;
- `summary`: contagem geral para apoio de migracao.
