
# 🧠 IA Web Solutions App

Um assistente pessoal inteligente, baseado em Machine Learning e IA generativa, com captura de voz, síntese de fala e integração com OpenAI GPT-4o. Projetado como um MVP para evoluir em direção a uma plataforma de automação pessoal e profissional.

---

## 🚀 Funcionalidades principais

✅ Compreensão de linguagem natural (GPT-4o via OpenAI)  
✅ Entrada de comandos via **texto** ou **voz**  
✅ Geração de respostas com **síntese de fala (TTS)**  
✅ Endpoint seguro com **validação via webhook**  
✅ Preparado para **resumos de reuniões, alertas e agendas**  
✅ Estrutura modular pronta para escalar com **Docker e Kubernetes**  
✅ API REST em FastAPI  
✅ Proteção de variáveis com `.env` + `GitHub Secrets`

---

## 🛠️ Tecnologias utilizadas

- **Python 3.10+**
- **FastAPI**
- **pyttsx3** (TTS local)
- **SpeechRecognition** (STT via microfone)
- **OpenAI SDK (GPT-4o)**
- **Docker + Docker Compose**
- **Kubernetes (YAML pronto para deploy)**
- **GitHub Actions + Secrets**
- **PowerShell script interativo**

---

## 📦 Estrutura do projeto

```
aiwebsolutionsapp/
├── api/                  # FastAPI com endpoints seguros
├── tts/                  # Módulo de saída de voz
├── voz/                  # Captura e transcrição por voz
├── k8s/                  # Arquivos de deploy Kubernetes
├── .env.example          # Modelo de variáveis sensíveis
├── .gitattributes        # Compatibilidade multiplataforma
├── .gitignore            # Proteção de arquivos sensíveis
├── main.py               # Entrada local para testes
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🛡️ Segurança

- Nenhum dado sensível é versionado.
- A API é protegida por token de webhook.
- Deploys são feitos via GitHub Actions usando `SSH + Secrets`.

---

## 🧠 Próximas evoluções

- [ ] Integração com Notion, Google Calendar e Trello  
- [ ] Exportação de resumos para Markdown/PDF  
- [ ] Interface Web com dashboard (frontend React ou Next.js)  
- [ ] Sincronização com assistentes móveis

---

## 🧪 Testar localmente

```bash
git clone https://github.com/Awrrin/aiwebsolutionsapp.git
cd aiwebsolutionsapp
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn api.app:app --reload
```

---

## 📢 Comandos úteis

### Via PowerShell interativo:

```powershell
.	estar-api-ia-ajustado.ps1
```

---

## 👨‍💻 Autor

Cleberson Barboza • Desenvolvedor de soluções com foco em IA, automação e educação digital.  
🔗 [LinkedIn](https://linkedin.com/in/clebersonezb)  
📫 clebersonezb@gmail.com

---

## 📜 Licença

MIT © 2025 IA Web Solutions
