# docker-with-python-flask

Estou aprendendo a usar o docker/docker-compose

Caso clone este repositório, para rodar a aplicação é necessário que você tenha instalado na sua máquina o docker e o docker-compose


Para verificar se já tem instalado o docker e o docker-compose:
```
  docker -v
```

```
  docker-compose -v
```

<br>

Caso não os tenha instalado, instale seguindo o passo a passo da documentação oficial

Após clonar este reṕositório, roda os seguintes comandos para iniciar a aplicação:
```
  docker-compose build
```

```
  docker-compose up
```

<br>

Após isso seu servidor flask estará rodando

* Caso encontre problemas ao usar o comando docker, tente usar a palavra sudo antes dos comandos, exemplo:
```
  sudo docker-compose build
```