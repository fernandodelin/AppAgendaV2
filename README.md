# 🗓️ Sistema de Agendamento de Consultas 🇧🇷 / Appointment Scheduling System 🇺🇸




## 📋 Sobre o Projeto  🇧🇷 / About the Project  🇺🇸

🇧🇷
Este projeto é um sistema de agendamento de consultas desenvolvido em Django, criado através de uma colaboração única entre desenvolvedor humano e Inteligência Artificial (Claude - Anthropic). A proposta foi explorar como a IA pode auxiliar no desenvolvimento de software, desde o planejamento até a implementação.

🇺🇸
This project is an appointment scheduling system developed in Django, created through a unique collaboration between a human developer and Artificial Intelligence (Claude - Anthropic). The proposal was to explore how AI can assist in software development, from planning to implementation.


## 🤖 Desenvolvimento Assistido por IA  🇧🇷 / AI-Assisted Development  🇺🇸

🇧🇷
Este projeto foi desenvolvido com a assistência de Claude, uma IA da Anthropic, demonstrando como a colaboração entre humanos e IAs pode resultar em desenvolvimento de software eficiente e bem estruturado. A IA auxiliou em:
- Estruturação do projeto
- Decisões de arquitetura
- Implementação de funcionalidades
- Boas práticas de segurança
- Documentação

🇺🇸
This project was developed with the assistance of Claude, an AI from Anthropic, demonstrating how collaboration between humans and AIs can result in efficient and well-structured software development. AI assisted in:
- Project structuring
- Architectural decisions
- Feature implementation
- Security best practices
- Documentation


## 🚀 Funcionalidades  🇧🇷 / Features  🇺🇸

🇧🇷
- Sistema de login e registro de usuários
- Agendamento de consultas
- Dashboard administrativo
- Visualização de consultas agendadas
- Gerenciamento de horários disponíveis

🇺🇸
- User login and registration system
- Appointment scheduling
- Administrative dashboard
- View scheduled appointments
- Management of available times


## 🛠️ Tecnologias Utilizadas  🇧🇷 / Technologies Used  🇺🇸

- Python 3.13
- Django (Framework Web)
- SQLite (Banco de Dados)
- HTML/CSS (Frontend)
- Bootstrap (Framework CSS)


## 📋 Pré-requisitos  🇧🇷 / Prerequisites 🇺🇸

- Python 3.13+
- pip (gerenciador de pacotes Python)
- Virtual Environment


## ⚙️ Configuração e Instalação  🇧🇷 / Configuration and Installation 🇺🇸
 
1. Clone o repositório / Clone repo
```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
```

2. Crie e ative o ambiente virtual / Create and activate the virtual environment 
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências / Install dependencies
```bash
pip install -r requirements.txt
```

4. Execute as migrações / Run the migrations
```bash
cd agenda_web
python manage.py migrate
```

6. Crie um superusuário / create a superuser
```bash
python manage.py createsuperuser
```

7. Inicie o servidor / start server
```bash
python manage.py runserver
```


## 🔒 Segurança  🇧🇷 / Security 🇺🇸

🇧🇷
- Todas as senhas são hasheadas
- Proteção contra CSRF
- Variáveis sensíveis em arquivo .env
- Configurações de segurança do Django ativadas

🇺🇸
- All passwords are hashed
- CSRF protection
- Sensitive variables in .env file
- Django security settings enabled


## 📝 Estrutura do Projeto  🇧🇷 / Project Structure 🇺🇸

```
agenda_web/
├── agendamentos/        # App principal de agendamentos
├── registration/        # App de autenticação
├── templates/          # Templates HTML
├── static/            # Arquivos estáticos
└── agenda_web/        # Configurações do projeto
```


## 🤝 Contribuindo  🇧🇷 / Contributing 🇺🇸

🇧🇷
Contribuições são sempre bem-vindas! Para contribuir:
1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Faça o Commit de suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

🇺🇸
Contributions are always welcome! To contribute:
1. Fork the project
2. Create a Branch for your Feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull RequestContributing


## 📄 Licença  🇧🇷 / License 🇺🇸

🇧🇷
Este projeto está sob a licença MIT

🇺🇸
This project is under the MIT license


## 👥 Autores  🇧🇷 / Authors 🇺🇸

- Fernando Anisio Goulart - Desenvolvedor Principal / Lead Developer
- Claude (Anthropic) - Assistente de IA / AI Assistant


## 📞 Conecte-se comigo  🇧🇷 / Connect with me 🇺🇸

[![Perfil DIO](https://img.shields.io/badge/-Meu%20Perfil%20na%20DIO-30A3DC?style=for-the-badge)](https://web.dio.me/users/viapythoncolab/)
[![E-mail](https://img.shields.io/badge/-Email-000?style=for-the-badge&logo=microsoft-outlook&logoColor=E94D5F)](mailto:fernandoanisiomail@gmail.com)
[![Instagram](https://img.shields.io/badge/-Instagram-3f729b?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/fernandoanisio0/)
[![Twitch](https://img.shields.io/badge/-Twitch-6441A4?style=for-the-badge&logo=twitch&logoColor=white)](https://www.twitch.tv/anisio_0)
[![Discord](https://img.shields.io/badge/-Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/vCk4Fne7)
[![Telegram](https://img.shields.io/badge/-Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Fernandoanisio1/)

---
🇧🇷
⭐️ Desenvolvido com assistência de Claude (Anthropic) - Demonstrando o poder da colaboração entre humano e IA no desenvolvimento de software.

🇺🇸
⭐️ Developed with assistance from Claude (Anthropic) - Demonstrating the power of human-AI collaboration in software development.