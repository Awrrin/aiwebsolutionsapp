# 🤖 IA Web Solutions App

Assistente Pessoal Inteligente para Organização de Rotinas com Integração Total com Google Calendar e Google Drive.

---

## 🚀 Fase 2 Concluída

A segunda fase do projeto foi finalizada com sucesso! A IA está agora apta a:

### ✅ Funcionalidades Ativas:

- 🧠 Interpretação inteligente de comandos de voz ou texto
- 📅 Criação automática de eventos no **Google Calendar**
  - Detecção de data, hora e dia da semana
  - Extração de **título, descrição, local**
  - Criação automática de **link de videoconferência (Google Meet)**
  - Suporte a eventos **recorrentes**
- 🗣️ Geração de resposta por voz com texto sanitizado
- 📄 Geração de **PDF com log da conversa**
- ☁️ Upload automático dos relatórios para o **Google Drive**
- 🛡️ Fallback local caso o Drive falhe (voz/fallback_logs)

---

## 🔐 Configuração do Ambiente

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:

```env
# .env (exemplo)
OPENAI_API_KEY=sua_chave_api_da_openai_aqui
WEBHOOK_SECRET=seu_token_de_seguranca
```

Durante o teste no terminal, digite o valor do `WEBHOOK_SECRET` quando for solicitado.

**⚠️ Nunca compartilhe sua chave real publicamente!**
Esse é apenas um exemplo e a chave deve ser armazenada de forma segura.

---

## 📦 Estrutura do Projeto

- `api/app.py`: API principal (FastAPI)
- `parser_eventos.py`: Interpretação do prompt e extração de dados
- `google_calendar.py`: Integração com Google Calendar
- `drive_uploader.py`: Upload de relatórios para o Google Drive
- `voz/gerador_relatorio.py`: Geração de PDF com logs
- `tts/`: Engine de voz (pyttsx3)
- `testar-api-ia.ps1`: Script PowerShell para testar a IA

---

## ✨ Próxima Fase: [Fase 3 - Em breve]

- Painel Web para controle de eventos e relatórios
- Edição e cancelamento de compromissos
- Classificação automática por tipo
- Suporte multiusuário

---

Desenvolvido com ☕️ e inteligência por **Cleberson Barboza** com suporte do CTO virtual **Gerson** 🧠