# CRAWLER RETS

Este repositório contém um crawler leve para coletar notícias relacionadas à saúde pública, cooperação internacional e formação técnica em saúde, com base no perfil da RETS (Rede Internacional de Educação de Técnicos em Saúde).

## 🔍 O que o script faz

- Varre sites definidos em um CSV (RETS_reorganizado.csv)
- Busca por palavras-chave relevantes (ex: cooperação, formação, OPAS, OMS)
- Salva os resultados em `matches_rets.csv`

## 🚀 Execução automática (GitHub Actions)
O crawler roda automaticamente toda segunda-feira às 3h (UTC).  
Você também pode executar manualmente via GitHub Actions → "Run workflow".

## ▶️ Como usar localmente

1. Clone o repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute:
   ```bash
   python scan_rets.py
   ```

## 🧪 Arquivos principais

- `scan_rets.py`: código do crawler
- `RETS_reorganizado.csv`: base de sites a visitar (você deve adicionar esse arquivo)
- `matches_rets.csv`: resultados salvos
- `.github/workflows/crawl.yml`: agendamento no GitHub Actions

---
Desenvolvido para monitoramento automatizado com base no perfil editorial da RETS.
