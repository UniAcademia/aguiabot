# Como rodar o bot:
1. Instale as dependências: Na aba `Terminal`do PyCharm digite: `pip install -r requirements.txt`
2. Crie uma nova aplicação no portal de desenvolvedores do Discord (https://discord.com/developers/applications)
3. Na aba "Bot" adicione um Bot:

![](https://i.ibb.co/fXbdGj3/image.png)

4. Na raíz do projeto, crie um arquivo chamado `.env` e dentro dele coloque a variável de ambiente `DISCORD_TOKEN`:

![](https://i.ibb.co/t49CDtf/image.png) ![](https://i.ibb.co/f81JvkR/image.png)

5. Volte na aba Bot no portal de desenvolvedores do Discord e copie seu Token:

![](https://i.ibb.co/BTwwSng/image.png)

6. NÃO MOSTRE ESSE TOKEN PARA ABSOLUTAMENTE **NINGUÉM**, alguém mal intencionado pode fazer algo que não deve e banir sua conta pra sempre
7. No arquivo `.env`, troque SEU_TOKEN_AQUI pelo token que você copiou
8. Relaxe, se seu token vazar na internet, você vai receber uma mensagem do Discord e vão alterar o token pra você

![](https://i.ibb.co/WtSCWV5/image.png)

9. Adicione o Bot no seu servidor de testes.

---

## Como adicionar o bot em seu servidor:
1. Na aba OAuth2, no portal de desenvolvedores do Discord, nos scopes, marque a checkbox `bot` e, nas permissões, marque `Administrator`
![](https://i.ibb.co/g7k9M0r/image.png)
2. Copie o link que está em scopes e cole no navegador
3. Escolha aonde você quer que o bot entre e pronto!
