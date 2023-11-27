# M5 - BandKamp Generic View

## Preparando ambiente para execução dos testes

1. Verifique se os pacotes **pytest**, **pytest-testdox** e/ou **pytest-django** estão instalados globalmente em seu sistema:
```shell
pip list
```

2. Caso eles apareçam na listagem, rode os comandos abaixo para realizar a desinstalação:

```shell
pip uninstall pytest pytest-testdox pytest-django -y
```

3. Após isso, crie seu ambiente virtual:
```shell
python -m venv venv
```

4. Ative seu ambiente virtual:

```shell
# Linux e Mac:
source venv/bin/activate

# Windows (PowerShell):
.\venv\Scripts\activate

# Windows (GitBash):
source venv/Scripts/activate
```

5. Instale as bibliotecas necessárias:

```shell
pip install pytest-testdox pytest-django
```


## Execução dos testes:

Como este projeto se trata de uma refatoração, não terá divisão de testes por tarefa, pois o objetivo é que todos os testes continuem passando após a refatoração.
Deste modo, para rodar a bateria de todos os testes, utilize:
```shell
pytest --testdox -vvs
```
---

Caso você tenha interesse em rodar apenas um diretório de testes específico, utilize os comandos abaixo:

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
