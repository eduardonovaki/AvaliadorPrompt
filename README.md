Instalação

Para instalar e executar o projeto, primeiro é necessário ter o Python 3.10 ou superior e o Ollama instalados na máquina.
Após baixar o projeto, abra a pasta em uma IDE como o PyCharm ou em um terminal.
Em seguida, crie um ambiente virtual com o comando python -m venv .venv e ative-o utilizando .\.venv\Scripts\Activate.ps1 no Windows.
Com o ambiente virtual ativo, instale todas as dependências do projeto com pip install -r requirements.txt.

Configuração

Depois disso, é necessário configurar o Ollama baixando o modelo utilizado no projeto com o comando ollama pull llama3.2.
(Para verificar se o modelo foi instalado corretamente, pode-se testar com ollama run llama3.2).

Executar

Por fim, para executar o sistema completo, basta rodar o comando python main.py, que fará a leitura dos dados, enviará os prompts ao modelo e gerará automaticamente os arquivos de saída com os resultados.
