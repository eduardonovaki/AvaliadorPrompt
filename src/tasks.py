tarefas = [
    {
        "nome": "classificacao_sentimento",
        "tipo": "classificacao",

        "instrucao": (
            "Classifique o sentimento da avaliação de cliente como "
            "POSITIVO, NEGATIVO, NEUTRO ou MISTO."
        ),

        "formato_output": (
            "Responda APENAS com uma das palavras: "
            "POSITIVO, NEGATIVO, NEUTRO ou MISTO. "
            "Nenhuma explicação adicional."
        ),

        "exemplos_fewshot": [
            {
                "input": "Adorei o produto! Chegou antes do prazo e a embalagem estava perfeita.",
                "output": "POSITIVO",
            },
            {
                "input": "Veio com defeito e o suporte demorou 5 dias para responder.",
                "output": "NEGATIVO",
            },
            {
                "input": "Entrega rápida, mas a qualidade do material decepcionou.",
                "output": "MISTO",
            },
        ],

        "passos_cot": [
            "1. Identifique todas as palavras e expressões com conotação positiva.",
            "2. Identifique todas as palavras e expressões com conotação negativa.",
            "3. Verifique se há contradição entre aspectos positivos e negativos.",
            "4. Se só houver positivos → POSITIVO. "
               "Se só negativos → NEGATIVO. "
               "Se ambos → MISTO. "
               "Se neutro/factual → NEUTRO.",
            "5. Responda com a classificação final.",
        ],

        "persona": "analista_cx",
    },

    # ------------------------------------------------------------------
    {
        "nome": "extracao_dados_produto",
        "tipo": "extracao",

        "instrucao": (
            "Extraia as informações estruturadas do texto sobre o produto. "
            "Retorne um JSON com os campos: "
            "produto, preco, defeito, categoria. "
            "Use null para campos não mencionados."
        ),

        "formato_output": (
            "Responda APENAS com um objeto JSON válido, sem markdown, "
            "sem explicações. Exemplo: "
            '{"produto": "...", "preco": "...", "defeito": "...", "categoria": "..."}'
        ),

        "exemplos_fewshot": [
            {
                "input": "Notebook Dell Inspiron de R$ 3.500 com pixels mortos na tela.",
                "output": '{"produto": "Notebook Dell Inspiron", "preco": "R$ 3.500", "defeito": "pixels mortos na tela", "categoria": "informatica"}',
            },
            {
                "input": "Tênis Nike Air Max 90 comprado por R$ 599, chegou com solado colando.",
                "output": '{"produto": "Tênis Nike Air Max 90", "preco": "R$ 599", "defeito": "solado colando", "categoria": "calcados"}',
            },
            {
                "input": "Fone Bluetooth JBL Tune 510BT, R$ 249, sem defeitos.",
                "output": '{"produto": "Fone Bluetooth JBL Tune 510BT", "preco": "R$ 249", "defeito": null, "categoria": "eletronicos"}',
            },
        ],

        "passos_cot": [
            "1. Identifique o nome completo do produto mencionado.",
            "2. Localize qualquer valor monetário (R$, reais, preço) associado ao produto.",
            "3. Identifique se há relato de defeito, problema ou dano.",
            "4. Infira a categoria do produto (eletrônicos, calçados, informática, etc.).",
            "5. Monte o JSON final com os 4 campos. Use null para os não encontrados.",
        ],

        "persona": "analista_dados",
    },

    # ------------------------------------------------------------------
    {
        "nome": "geracao_resposta_suporte",
        "tipo": "geracao",

        "instrucao": (
            "Você é um agente de suporte de e-commerce. "
            "Leia a mensagem do cliente e gere uma resposta profissional, "
            "empática e objetiva que: (1) reconheça o problema, "
            "(2) apresente a solução ou próximo passo, "
            "(3) finalize de forma cordial. "
            "Máximo de 5 linhas."
        ),

        "formato_output": (
            "Responda diretamente com o texto da mensagem de suporte. "
            "Sem aspas, sem prefixos como 'Resposta:'. "
            "Máximo 5 linhas."
        ),

        "exemplos_fewshot": [
            {
                "input": "Meu pedido #45231 não chegou e já faz 10 dias. O rastreio parou de atualizar.",
                "output": (
                    "Olá! Lamentamos o transtorno com seu pedido #45231. "
                    "Verificamos que houve uma interrupção no rastreamento pelo transportador. "
                    "Abrimos uma ocorrência prioritária e você receberá uma atualização em até 24 horas. "
                    "Caso o prazo não seja cumprido, garantimos o reenvio ou estorno completo. "
                    "Agradecemos sua paciência!"
                ),
            },
            {
                "input": "Comprei um celular e veio sem o carregador na caixa.",
                "output": (
                    "Entendemos o quanto isso é frustrante, e pedimos desculpas pelo inconveniente. "
                    "Por favor, envie uma foto da caixa e da nota fiscal para analisarmos. "
                    "Assim que confirmado, enviaremos o acessório em até 3 dias úteis sem custo. "
                    "Estamos à disposição para resolver!"
                ),
            },
        ],

        "passos_cot": [
            "1. Identifique o problema principal relatado pelo cliente.",
            "2. Determine a emoção predominante (frustração, dúvida, urgência).",
            "3. Pense na solução padrão para esse tipo de ocorrência.",
            "4. Redija uma frase de empatia, uma de solução e uma de encerramento.",
            "5. Revise para garantir tom profissional e máximo de 5 linhas.",
        ],

        "persona": "agente_suporte",
    },
]