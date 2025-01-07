# Sistema de Agendamento de Consultas 🗓️

## Sobre o Projeto
Este projeto é um sistema de agendamento de consultas desenvolvido em Django, criado através de uma colaboração única entre desenvolvedor humano e Inteligência Artificial (Claude - Anthropic). A proposta foi explorar como a IA pode auxiliar no desenvolvimento de software, desde o planejamento até a implementação.

## 🤖 Desenvolvimento Assistido por IA
Este projeto foi desenvolvido com a assistência de Claude, uma IA da Anthropic, demonstrando como a colaboração entre humanos e IAs pode resultar em desenvolvimento de software eficiente e bem estruturado. A IA auxiliou em:
- Estruturação do projeto
- Decisões de arquitetura
- Implementação de funcionalidades
- Boas práticas de segurança
- Documentação

## 🚀 Funcionalidades
- Sistema de login e registro de usuários
- Agendamento de consultas
- Dashboard administrativo
- Visualização de consultas agendadas
- Gerenciamento de horários disponíveis

## 🛠️ Tecnologias Utilizadas
- Python 3.13
- Django (Framework Web)
- SQLite (Banco de Dados)
- HTML/CSS (Frontend)
- Bootstrap (Framework CSS)

## 📋 Pré-requisitos
- Python 3.13+
- pip (gerenciador de pacotes Python)
- Virtual Environment

## ⚙️ Configuração e Instalação

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
```

2. Crie e ative o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. Execute as migrações
```bash
python manage.py migrate
```

6. Crie um superusuário
```bash
python manage.py createsuperuser
```

7. Inicie o servidor
```bash
python manage.py runserver
```

## 🔒 Segurança
- Todas as senhas são hasheadas
- Proteção contra CSRF
- Variáveis sensíveis em arquivo .env
- Configurações de segurança do Django ativadas

## 📝 Estrutura do Projeto
```
agenda_web/
├── agendamentos/        # App principal de agendamentos
├── registration/        # App de autenticação
├── templates/          # Templates HTML
├── static/            # Arquivos estáticos
└── agenda_web/        # Configurações do projeto
```

## 🤝 Contribuindo
Contribuições são sempre bem-vindas! Para contribuir:
1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Faça o Commit de suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença
Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes

## 👥 Autores
- Fernando Anisio Goulart - Desenvolvedor Principal
- Claude (Anthropic) - Assistente de IA

## 📞 Conecte-se comigo
[![Perfil DIO](https://img.shields.io/badge/-Meu%20Perfil%20na%20DIO-30A3DC?style=for-the-badge)](https://web.dio.me/users/viapythoncolab/)
[![E-mail](https://img.shields.io/badge/-Email-000?style=for-the-badge&logo=microsoft-outlook&logoColor=E94D5F)](mailto:fernandoanisiomail@gmail.com)
[![Instagram](https://img.shields.io/badge/-Instagram-3f729b?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/fernandoanisio0/)
[![Twitch](https://img.shields.io/badge/-Twitch-6441A4?style=for-the-badge&logo=twitch&logoColor=white)](https://www.twitch.tv/anisio_0)
[![Discord](https://img.shields.io/badge/-Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/vCk4Fne7)
[![Telegram](https://img.shields.io/badge/-Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Fernandoanisio1/)

---
⭐️ Desenvolvido com assistência de Claude (Anthropic) - Demonstrando o poder da colaboração entre humano e IA no desenvolvimento de software.
