# KLAM API HOTEL

ROTAS DA TRANÇÃO

fazer uma transação ou listar
```python
api/transactions/
```
RETORNO
```python
***ROTAS DA TRASANÇÃO***

api/transactions/
Criação Ou Listagem

Criação sucedida
Mandei
{
    "method": "Pix",
    "amount_paid": 100,
        "discount_percentage": 10
}
Retorno 201
{
    "id": "83c6b5c01516449280e70c6cc85743a7",
    "user": "2f8654e0-1c1f-47b9-b660-54b06d89b8de",
    "user_name": "Mike_ADMIN",
    "user_cpf": "11111111111",
    "method": "Pix",
    "timestamp": "2023-11-24T16:02:19.647983Z",
    "amount_paid": "100.00",
    "discount_percentage": 10,
    "discount_amount": "0.00"
}
Listagem
Retorno 200
[
    {
        "id": "ce803c5a1ce9411983e0b296b4a9f8b7",
        "user": "6a3efe7d-e451-47e8-8cb3-57e550cf0a90",
        "user_name": "Mike_ADMIN",
        "user_cpf": "11111111111",
        "method": "Pix",
        "timestamp": "2023-11-27T16:30:04.310406Z",
        "amount_paid": "100.00",
        "discount_percentage": 10,
        "discount_amount": "0.00"
    },
    {
        "id": "178829d0692c4daaa4586e721f3a51ba",
        "user": "6a3efe7d-e451-47e8-8cb3-57e550cf0a90",
        "user_name": "Mike_ADMIN",
        "user_cpf": "11111111111",
        "method": "Pix",
        "timestamp": "2023-11-27T16:30:05.818251Z",
        "amount_paid": "100.00",
        "discount_percentage": 10,
        "discount_amount": "0.00"
    },
    {
        "id": "61afc2d7525a45919d877dfdbd45db64",
        "user": "6a3efe7d-e451-47e8-8cb3-57e550cf0a90",
        "user_name": "Mike_ADMIN",
        "user_cpf": "11111111111",
        "method": "Pix",
        "timestamp": "2023-11-27T16:30:06.928199Z",
        "amount_paid": "100.00",
        "discount_percentage": 10,
        "discount_amount": "0.00"
    }
]
```
---
ROTAS DO USUARIO

criação de usuarios
```python
api/users/
```
***RETORNO DE CRIACAO DE USUARIO***
api/users/
```python
Criação Sucedida
Mandar
{
   "name" : "MikeUS",
   "username": "Mike_USER",
   "email" : "mikeUS@kenzie.com",
   "password" : 1234,
   "contact" : 11963605188,
   "cpf" : "11111111112",
   "type_user" : "US"
}
Retornar 201
{
    "id": "cda3ef9bf60f455c83ab68ff0dc13191",
    "username": "Mike_USER",
    "email": "mikeUS@kenzie.com",
    "name": "MikeUS",
    "contact": "(11) 9636-05188",
    "cpf": "111.111.111-12",
    "nationality": "",
    "emergency_contact": "",
    "favorite_rooms": [],
    "type_user": "US"
}
Erros Possivel
400
"email": [
        "A user with this email already exists."
],
"cpf": [
    "A user with this cpf already exists."
]
```

listagem de usuarios
```python
api/users/list/
```
encontra informações ou deleção de um usuario especifico 
```python
api/users/<user_id>
```
editar informações de um usuário especifico 
```python
api/users/edit/
```
login de acesso
```python
api/login/
```
retorno
```python
api/login/
Login Sucedido
Mandei
{
    "email":"mikeDE@kenzie.com",
    "password":1234
}
retorno 200
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMTcwNDA0MywiaWF0IjoxNzAxMDk5MjQzLCJqdGkiOiIyMzZmZTg4YjUxOTU0NGFjOGY0OWQyNDdjNTZkZTE3ZCIsInVzZXJfaWQiOiIzOWY3ZWNkYS0yYjMyLTQyNTItYWRlOC1mZTc3YzM3MzBkYmEifQ.oIBARmg9vnF54z1RgX39tHRMnWhg8dFPfQejR6vzhyI",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAzNjkxMjQzLCJpYXQiOjE3MDEwOTkyNDMsImp0aSI6ImVlYWQ5ODI1MjUyMjQ2Mzg4YWQyNjRiMTQ5ZDBkZTQxIiwidXNlcl9pZCI6IjM5ZjdlY2RhLTJiMzItNDI1Mi1hZGU4LWZlNzdjMzczMGRiYSJ9.SuzljSTuYZ3i3JgNRz-Agad9SVNGivYfBkCbd20L47A"
}
erro possível
Senha ou Email Errado
401
{
    "detail": "No active account found with the given credentials"
}
```
---

ROTAS DOS QUARTOS

Criação ou Listagem de quartos
```python
api/rooms/
```
Adicionar ou Remover um Quarto aos favoritos
```python
api/rooms/<room_id>/user/<user_id>/
```
Ciração Ou Listagem de Camas
```python
api/beds/
```
Listagem  pelo Tipo da Cama
```python
api/beds/type/<beds_type>/
```

Listar um Cama especifica
```python
 api/beds/<bed_id>/
```

Criar ou Listar Características dos Quartos
```python
api/rooms/features/
```

Adionar ou Remover uma Características ao um Quarto 
```python
api/rooms/<room_id>/feature/<feature_id>/
```

---

ROTAS DA RESERVA

Criação e Listagem da Reserva
```shell
reservations/
```
Cancelamento Listagem ou Atualização de um Reserva especifica
```shell
reservations/<reservation_id>
```
---
ROTAS DA PROMOÇÃO

Criação ou Listagem da Promoção
```shell
promotions/
```
Lista , Atualizar ou Deletar um Promoção especifica 
```shell
Lista , Atualizar ou Deletar um Promoção especifica 
```
Adionar ou Remover uma Promoção ao um Quarto
```shell
promotions/<promotion_id>/rooms/<room_id/
```
---
ROTAS DA CHECKLIST

Criação ou Listagem da Checklist
```shell
checklist/
```
