Vamos adicionar os passos para integrar o código do Firebase ao README, explicando como ativá-lo. Aqui está a seção atualizada:

### README.md

```markdown
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

   Certifique-se de ter Flet instalado. Se ainda não tiver instalado, você pode instalar usando pip:

   ```bash
   pip install flet
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

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
```

### Explicações Adicionais:

- **Ativando o Firebase**: Explicação detalhada sobre como descomentar e configurar o código no arquivo `firebase/firebase_config.py` para integrar o Firebase ao aplicativo Python usando Flet.