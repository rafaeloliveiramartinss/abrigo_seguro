### README.md

```markdown
```
# Abrigo Seguro - Aplicativo Python com Flet

Este é o repositório do projeto Abrigo Seguro, um aplicativo Python usando Flet para interface gráfica.

## Executando o Aplicativo

Para executar o aplicativo Abrigo Seguro em seu ambiente de desenvolvimento local, siga os passos abaixo:

### Passos

1. **Clone o Repositório**

   Clone este repositório em seu computador local usando Git:

   ```bash
   git clone https://github.com/rafaeloliveiramartinss/abrigo_seguro.git
   ```

2. **Instale as Dependências**

   Navegue até o diretório do projeto e instale as dependências listadas no arquivo `requirements.txt`:

   ```bash
   cd abrigo_seguro
   pip install -r requirements.txt
   ```

3. **Ative o Firebase**

   Para usar o Firebase, siga as etapas abaixo:

   - Descomente as linhas no arquivo `firebase/firebase_config.py` para importar os módulos necessários:

     ```python
     from firebase_admin import credentials, initialize_app, storage, firestore
     ```

   - Defina as credenciais do Firebase substituindo `'path/to/serviceAccountKey.json'` pelo caminho para o seu arquivo `serviceAccountKey.json`:

     ```python
     def initialize_firebase():
         cred = credentials.Certificate('path/to/serviceAccountKey.json')
         initialize_app(cred, {'storageBucket': 'your-bucket-name'})
         db = firestore.client()
         bucket = storage.bucket()
         return db, bucket
     ```

   Certifique-se de substituir `'your-bucket-name'` pelo nome do seu bucket do Firebase.

4. **Execute o Aplicativo**

   - Navegue até o diretório do projeto clonado:

     ```bash
     cd abrigo_seguro
     ```

   - Execute o aplicativo Python:

     ```bash
     python main.py
     ```

   Isso iniciará o aplicativo Abrigo Seguro com a interface gráfica definida por Flet e a integração com o Firebase ativada.

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Se você deseja contribuir com este projeto, por favor, siga os passos abaixo:

1. Fork o repositório
2. Crie uma branch para sua funcionalidade (`git checkout -b feature/SuaFuncionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona funcionalidade incrível'`)
4. Push para a branch (`git push origin feature/SuaFuncionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Suporte

Para qualquer dúvida ou problema, sinta-se à vontade para abrir uma issue neste repositório.

### Explicações Adicionais:

- **Ativando o Firebase**: Explicação detalhada sobre como descomentar e configurar o código no arquivo `firebase/firebase_config.py` para integrar o Firebase ao aplicativo Python usando Flet.