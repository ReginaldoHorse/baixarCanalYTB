# Baixa Todo o Canal 5000 by Reginaldo Horse
### Isso foi criado especialmente para o usuário ⚡Arthur -@unknown_BTC_usr lá do twitter que solicitou uma solução fácil para fazer backup do canal dele.

Este é um programa para baixar vídeos de um canal do YouTube com uma interface gráfica simples. Ele permite inserir o link do canal, escolher a pasta de destino e exibe uma barra de progresso durante o download.

## Instalação e Configuração

### 1. Instalando o Python

O script requer Python 3. Se não tiver ainda, melhor baixar. Essa é a terceira melhor linguagem do mundo logo após Cobol e Basic.

#### Se estiver usando Ubuntu/Debian:
```sh
sudo apt update && sudo apt install -y python3 python3-pip
```

#### Se estiver usando Fedora porque gosta de testar coisa nova:
```sh
sudo dnf install -y python3 python3-pip
```

#### Se estiver usando Arch Linux, deveria saber fazer isso aqui de olhos vendados
```sh
sudo pacman -Sy python python-pip
```

### 2. Instalando o FFmpeg (necessário para pós-processamento de vídeos)

#### Ubuntu/Debian:
```sh
sudo apt install -y ffmpeg
```

#### Fedora:
```sh
sudo dnf install -y ffmpeg
```

#### Arch Linux:
```sh
sudo pacman -Sy ffmpeg
```

### 3. Instalando as dependências do projeto

Clone o repositório ou baixe o código e instale as dependências:

```sh
git clone https://github.com/seuusuario/seurepositorio.git
cd baixarCanalYTB
pip install -r requisitos.txt
```

### 4. Executando o script

Após instalar todas as dependências, execute o programa com:

```sh
python3 baixarCanal.py
```

Agora, basta inserir o link do canal, escolher a pasta de destino e iniciar o download!

## Licença
Este projeto está sob a licença MIT. Sinta-se livre para contribuir!

