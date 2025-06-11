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

### ⚡ Sistema de Velocidade

O jogo possui um sistema de velocidade em duas fases:

1. **Fase 1 - Redução de Delay** (50ms → 1ms)
   - Pressione `=` para reduzir delay
   - Cada tecla diminui 5ms
   - Mínimo: 1ms de delay

2. **Fase 2 - Múltiplos Movimentos** (1x → 100x)
   - Após atingir 1ms, aumenta movimentos por frame
   - Cada tecla adiciona +1 movimento
   - Máximo: 100 movimentos por frame

**Resultado:** Até **100.000 movimentos por segundo**!

## 🏗️ Arquitetura do Código

### 📁 Estrutura do Projeto
```
snake_game/
├── snake.py           # Código principal do jogo
├── requirements.txt   # Dependências Python
├── README.md         # Este arquivo
└── snake_env/        # Ambiente virtual (se criado)
```

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


## 🐛 Solução de Problemas

### Problema: "ModuleNotFoundError: No module named 'pygame'"
**Solução:**
```bash
pip install pygame==2.5.2
```

### Problema: "externally-managed-environment" (Arch Linux)
**Solução:**
```bash
sudo pacman -S python-pygame
```

### Problema: Jogo muito lento
**Solução:**
- Pressione `=` várias vezes para acelerar
- Use modo automático (`A`) para ver velocidade máxima

### 🆕 Funcionalidades Sugeridas
- [ ] Sistema de high scores
- [ ] Diferentes tipos de comida
- [ ] Múltiplos níveis/mapas
- [ ] Sons e música
- [ ] Multiplayer local
- [ ] Diferentes algoritmos de IA
- [ ] 
## 📝 Licença

Este projeto está sob a licença MIT. Veja arquivo LICENSE para detalhes.

## 🙏 Créditos

- **Pygame Community** - Framework de jogos Python
- **Algoritmo Hamiltoniano** - Inspirado em soluções clássicas de Snake
- **Python Community** - Linguagem e ecossistema

---

**Feito com ❤️ e Python** 🐍

Divirta-se jogando e explorando o código! 🎮
