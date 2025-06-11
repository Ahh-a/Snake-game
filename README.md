# 🐍 Snake Game Ultra-Fast

Um jogo Snake moderno e avançado desenvolvido em Python com Pygame, featuring modo automático com algoritmo Hamiltoniano e velocidades ultra-rápidas.

![Snake Game](https://img.shields.io/badge/Python-3.13-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.5.2-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎮 Características

### ✨ Funcionalidades Principais
- **Jogo Snake Clássico** com mecânicas modernas
- **Wraparound**: A cobra atravessa as bordas da tela
- **Cabeça Diferenciada**: Cor escura para identificar a direção
- **Tela de Início**: Interface amigável com instruções
- **Reinício Automático**: Jogo continua após game over

## 🚀 Instalação

### Pré-requisitos
- Python 3.7+ (testado com Python 3.13)
- pip (gerenciador de pacotes Python)

### Instalação Rápida

#### Opção 1: Usando ambiente virtual (Recomendado)
```bash
# Clone ou baixe o repositório
cd snake_game

# Crie um ambiente virtual
python -m venv snake_env

# Ative o ambiente virtual
source snake_env/bin/activate  # Linux/Mac
# ou
snake_env\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o jogo
python snake.py
```

#### Opção 2: Instalação global (Arch Linux)
```bash
# Instale pygame usando pacman
sudo pacman -S python-pygame

# Execute o jogo
python snake.py
```

#### Opção 3: Usando pip global
```bash
pip install pygame==2.5.2
python snake.py
```

## 🎯 Como Jogar

### 🕹️ Controles Básicos
| Tecla | Ação |
|-------|------|
| **Qualquer tecla** | Iniciar o jogo |
| **↑ ↓ ← →** | Mover a cobra (modo manual) |
| **A** | Alternar modo automático/manual |
| **=** | Acelerar o jogo |
| **-** | Desacelerar o jogo |

### 🎮 Modos de Jogo

#### 🎯 Modo Manual
- Controle tradicional com as setas
- Colete comida vermelha para crescer
- Evite colidir com o próprio corpo
- Use as bordas para atravessar a tela

#### 🤖 Modo Automático
- IA joga usando algoritmo hamiltoniano
- Movimento perfeito sem colisões
- Ideal para demonstrações e testes
- Colete comida automaticamente


### 🧮 Algoritmo Hamiltoniano

O modo automático utiliza um **ciclo hamiltoniano** que:
1. Cria um padrão zigue-zague cobrindo toda a tela
2. Visita cada célula exatamente uma vez
3. Garante que a cobra nunca colida consigo mesma
4. Permite coleta de toda comida eventualmente

```python
# Padrão do algoritmo
Linha 0: → → → → → → →
Linha 1: ← ← ← ← ← ← ←
Linha 2: → → → → → → →
Linha 3: ← ← ← ← ← ← ←
```
