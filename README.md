# KLAM API HOTEL

ROTAS DA TRANÇÃO

fazer uma transação ou listar
```python
api/transactions/
```
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
