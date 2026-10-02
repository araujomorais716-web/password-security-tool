Testa funcionalidades como:

Tamanho da senha;

Inclusão de letras maiúsculas;

Inclusão de números;

Validação de tamanhos inválidos;

Validação de categorias vazias;

Cálculo da entropia;

Classificação da entropia.

🚀 Como executar o projeto
1. Pré-requisitos
Antes de executar o projeto, certifique-se de ter instalado:

Python 3;

Git.

Pode verificar a versão do Python com:

python --version

No Linux/macOS, também pode utilizar:

python3 --version

2. Clonar o repositório
Clone o repositório utilizando:

git clone URL_DO_SEU_REPOSITORIO

Depois entre na pasta do projeto:

cd password-security-tool

Substitua URL_DO_SEU_REPOSITORIO pela URL real do seu repositório no GitHub.

3. Criar um ambiente virtual
É recomendado utilizar um ambiente virtual para manter as dependências do projeto isoladas.

Windows
python -m venv .venv

Ative o ambiente virtual:

.venv\Scripts\activate

Linux/macOS
python3 -m venv .venv

Ative o ambiente virtual:

source .venv/bin/activate

Quando o ambiente estiver ativo, o terminal normalmente apresentará algo semelhante a:

(.venv)

4. Instalar as dependências
Com o ambiente virtual ativado:

pip install -r requirements.txt

O requirements.txt contém as dependências necessárias para executar os testes do projeto.

5. Executar a aplicação
Na raiz do projeto, execute:

python src/gui.py

A interface gráfica será aberta numa nova janela.

🧪 Executando os testes
Para executar todos os testes:

pytest

Para obter informações mais detalhadas:

pytest -v

Os testes estão localizados na pasta:

tests/

Exemplo de execução:

============================= test session starts =============================
collected 7 items

tests/test_password_generator.py .......                     [100%]

============================== 7 passed =======================================

🖥️ Interface da aplicação
A aplicação possui uma interface gráfica simples que permite ao utilizador configurar a senha antes da sua geração.

É possível selecionar:

Tamanho da senha;

Letras maiúsculas;

Letras minúsculas;

Números;

Símbolos.

Depois de gerar a senha, a aplicação apresenta:

Tamanho: 16 caracteres
Entropia estimada: XX.XX bits
Classificação: Muito Forte

A classificação apresentada é baseada exclusivamente nos limites definidos no código para fins educacionais.

📊 Entropia
A aplicação utiliza a fórmula:

E = L × log₂(N)

Por exemplo, considerando uma senha de determinado tamanho e um conjunto de caracteres disponível, o programa estima quantos bits de entropia podem estar associados ao espaço de possibilidades considerado.

A classificação implementada no projeto é:

Entropia	Classificação
Menor que 64 bits	Fraca
64 a 79 bits	Média
80 a 119 bits	Forte
120 bits ou mais	Muito Forte

Essas categorias fazem parte da lógica educacional deste projeto e não devem ser interpretadas como um padrão universal de segurança.

🧪 Testes automatizados
O projeto utiliza Pytest para validar diferentes partes da aplicação.

Entre os testes implementados estão:

✓ Tamanho da senha
✓ Presença de letras maiúsculas
✓ Presença de números
✓ Rejeição de senhas muito curtas
✓ Rejeição de categorias vazias
✓ Cálculo da entropia
✓ Classificação da entropia

Os testes ajudam a garantir que alterações futuras no código não quebrem funcionalidades existentes.

🤖 Utilização de Inteligência Artificial
A Inteligência Artificial foi utilizada como ferramenta de apoio à aprendizagem e ao desenvolvimento deste projeto.

Durante o desenvolvimento, a IA foi utilizada para:

Pesquisar e compreender conceitos;

Explorar possíveis soluções;

Identificar possíveis erros;

Sugerir melhorias;

Apoiar a documentação;

Auxiliar na compreensão de determinadas funcionalidades.

O código foi estudado, testado e adaptado durante o desenvolvimento.

A utilização de IA teve como objetivo complementar o processo de aprendizagem e apoiar o desenvolvimento das competências técnicas.

📚 Aprendizados
Durante o desenvolvimento deste projeto, foram praticados conceitos relacionados a:

Programação em Python;

Funções;

Modularização;

Validação de dados;

Tratamento de exceções;

Geração segura de valores aleatórios;

Segurança de senhas;

Entropia;

Testes automatizados;

Interface gráfica com Tkinter;

Organização de projetos Python;

Documentação;

Git;

GitHub.

🔮 Próximos passos
Algumas melhorias que podem ser estudadas e implementadas futuramente:

 Adicionar botão para copiar a senha;

 Melhorar a interface gráfica;

 Adicionar indicador visual de segurança;

 Adicionar testes mais abrangentes;

 Melhorar o tratamento de erros;

 Adicionar documentação técnica;

 Estudar verificação de senhas comprometidas através de serviços apropriados;

 Criar uma versão web;

 Adicionar configurações adicionais de políticas de senha;

 Melhorar a experiência do utilizador.

⚠️ Aviso
Este projeto foi desenvolvido para fins educacionais.

O Password Security Tool não deve ser considerado uma ferramenta profissional de auditoria, pentest ou avaliação completa da segurança de senhas.

As informações apresentadas pela aplicação representam estimativas baseadas nos métodos implementados no projeto.

👨‍💻 Autor
Estudante de Informática | Foco em Cibersegurança

Projeto desenvolvido como parte do processo de aprendizagem e construção de portfólio na área de Tecnologia da Informação.

Atualmente, o foco de aprendizagem está direcionado para:

Python;

Cibersegurança;

Desenvolvimento de software;

Segurança de aplicações;

Testes automatizados;

Git e GitHub.

O objetivo é desenvolver competências práticas através da construção de projetos e continuar a evoluir profissionalmente na área de Tecnologia da Informação e Cibersegurança.

💬 Feedback
Sugestões, críticas construtivas e contribuições são bem-vindas.

Caso encontre algum problema ou tenha uma sugestão de melhoria, pode abrir uma Issue no repositório.

Contribuições através de Pull Requests também são bem-vindas.

⭐ Projeto educacional
Este projeto faz parte do meu processo de aprendizagem em Python e Cibersegurança, com o objetivo de transformar conhecimentos teóricos em aplicações práticas.

Se o projeto for útil para os seus estudos, considere deixar uma ⭐ no repositório.

