# Desafio Medicar

Sistema para gestão de consultas em uma clínica médica.

## Api de Autenticação

### Registro de Usuário

> [POST] /rest_auth/registration

Requisição Exemplo:

- Body

```json
{
   "username": "username",
   "email": "email@email.com",
   "password1": "senha",
   "password2": "confirmarSenha"
}
```

- Retorno

```json
{
   "key": <Token>
}

```

### Login

> [POST] /rest_auth/login

- Body

```json
{
   "username": "username",
   "password": "senha"
}
```

- Retorno

```json
{
   "key": <Token>
}
```

### Logout

> [POST] /rest_auth/logout

- Header

```txt
Authorization: Token <Token>
```

- Retorno

```txt
204 no content (logout com sucesso)
```
