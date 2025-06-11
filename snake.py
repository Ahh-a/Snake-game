import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Definir cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_GREEN = (0, 150, 0)  # Cor mais escura para a cabeça

# Configurações da tela
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
CELL_NUMBER_X = WINDOW_WIDTH // CELL_SIZE
CELL_NUMBER_Y = WINDOW_HEIGHT // CELL_SIZE

# Configurações do jogo
FPS = 60
SNAKE_SPEED = 50  # Velocidade inicial mais rápida (50ms)

class Snake:
    def __init__(self):
        self.body = [pygame.Vector2(5, 10), pygame.Vector2(4, 10), pygame.Vector2(3, 10)]
        self.direction = pygame.Vector2(1, 0)
        self.new_block = False
        
    def draw_snake(self, screen):
        for index, block in enumerate(self.body):
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            
            # Cabeça tem cor diferente (primeiro segmento)
            if index == 0:
                pygame.draw.rect(screen, DARK_GREEN, block_rect)
            else:
                pygame.draw.rect(screen, GREEN, block_rect)
            
    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            
    def add_block(self):
        self.new_block = True
        
    def check_collision(self):
        # Verificar colisão com as bordas - agora a cobra passa através das bordas
        head = self.body[0]
        
        # Wraparound horizontal
        if head.x < 0:
            self.body[0].x = CELL_NUMBER_X - 1
        elif head.x >= CELL_NUMBER_X:
            self.body[0].x = 0
            
        # Wraparound vertical
        if head.y < 0:
            self.body[0].y = CELL_NUMBER_Y - 1
        elif head.y >= CELL_NUMBER_Y:
            self.body[0].y = 0
            
        # Verificar colisão com o próprio corpo
        for block in self.body[1:]:
            if block == self.body[0]:
                return True
                
        return False

class Food:
    def __init__(self):
        self.randomize()
        
    def draw_food(self, screen):
        food_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, food_rect)
        
    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER_X - 1)
        self.y = random.randint(0, CELL_NUMBER_Y - 1)
        self.pos = pygame.Vector2(self.x, self.y)

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.font = pygame.font.Font(None, 74)
        self.game_started = False
        self.title_font = pygame.font.Font(None, 100)
        self.subtitle_font = pygame.font.Font(None, 50)
        self.auto_mode = False
        self.hamiltonian_path = self.generate_hamiltonian_cycle()
        self.current_path_index = 0
        self.speed = SNAKE_SPEED
        self.moves_per_frame = 1  # Quantos movimentos por frame para velocidades ultra-altas
        
    def update(self):
        if self.game_started:
            # Executar múltiplos movimentos por frame para velocidades ultra-altas
            for _ in range(self.moves_per_frame):
                if self.auto_mode:
                    self.auto_move()
                self.snake.move_snake()
                self.check_collision()
                if self.snake.check_collision():
                    self.game_over()
                    break
        
    def draw_elements(self, screen):
        self.draw_grass(screen)
        if self.game_started:
            self.food.draw_food(screen)
            self.snake.draw_snake(screen)
            self.draw_score(screen)
            self.draw_mode_indicator(screen)
        else:
            self.draw_start_screen(screen)
        
    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_block()
            self.score += 1
            
        # Verificar se a comida não spawnou no corpo da cobra
        for block in self.snake.body[1:]:
            if block == self.food.pos:
                self.food.randomize()
                
    def check_fail(self):
        if self.snake.check_collision():
            self.game_over()
            
    def start_game(self):
        self.game_started = True
        
    def restart_game(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_started = False
        self.auto_mode = False
        self.current_path_index = 0
        
    def toggle_auto_mode(self):
        self.auto_mode = not self.auto_mode
        if self.auto_mode:
            self.current_path_index = self.find_closest_hamiltonian_point()
            
    def increase_speed(self):
        if self.speed > 1:
            self.speed = max(1, self.speed - 5)  # Diminui o delay mais rapidamente
        else:
            # Quando chegamos ao delay mínimo, aumentamos os movimentos por frame
            self.moves_per_frame = min(100, self.moves_per_frame + 1)
        
    def decrease_speed(self):
        if self.moves_per_frame > 1:
            # Primeiro diminuir os movimentos por frame
            self.moves_per_frame = max(1, self.moves_per_frame - 1)
        else:
            # Depois aumentar o delay
            self.speed = min(1000, self.speed + 5)
    def restart_game(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_started = False
        self.auto_mode = False
        self.current_path_index = 0
        self.moves_per_frame = 1
            
    def game_over(self):
        self.restart_game()
        
    def generate_hamiltonian_cycle(self):
        """Gera um ciclo hamiltoniano para cobrir toda a tela"""
        path = []
        
        # Criar um padrão zigue-zague que cobre toda a tela
        for row in range(CELL_NUMBER_Y):
            if row % 2 == 0:
                # Linha par: da esquerda para direita
                for col in range(CELL_NUMBER_X):
                    path.append(pygame.Vector2(col, row))
            else:
                # Linha ímpar: da direita para esquerda
                for col in range(CELL_NUMBER_X - 1, -1, -1):
                    path.append(pygame.Vector2(col, row))
        
        return path
    
    def find_closest_hamiltonian_point(self):
        """Encontra o ponto mais próximo no caminho hamiltoniano"""
        head = self.snake.body[0]
        min_distance = float('inf')
        closest_index = 0
        
        for i, point in enumerate(self.hamiltonian_path):
            distance = abs(head.x - point.x) + abs(head.y - point.y)
            if distance < min_distance:
                min_distance = distance
                closest_index = i
                
        return closest_index
    
    def auto_move(self):
        """Move a cobra automaticamente seguindo o ciclo hamiltoniano"""
        if len(self.hamiltonian_path) == 0:
            return
            
        current_pos = self.snake.body[0]
        target_pos = self.hamiltonian_path[self.current_path_index]
        
        # Calcular direção para o próximo ponto
        dx = target_pos.x - current_pos.x
        dy = target_pos.y - current_pos.y
        
        # Ajustar para wraparound
        if abs(dx) > CELL_NUMBER_X // 2:
            dx = -dx / abs(dx) if dx != 0 else 0
        if abs(dy) > CELL_NUMBER_Y // 2:
            dy = -dy / abs(dy) if dy != 0 else 0
            
        # Definir nova direção
        if abs(dx) > abs(dy):
            new_direction = pygame.Vector2(1 if dx > 0 else -1, 0)
        else:
            new_direction = pygame.Vector2(0, 1 if dy > 0 else -1)
            
        # Verificar se a nova direção não é oposta à atual
        if new_direction != -self.snake.direction:
            self.snake.direction = new_direction
            
        # Avançar para o próximo ponto se chegamos perto do atual
        if abs(dx) <= 1 and abs(dy) <= 1:
            self.current_path_index = (self.current_path_index + 1) % len(self.hamiltonian_path)
    
    def draw_mode_indicator(self, screen):
        """Desenha o indicador de modo na tela"""
        mode_text = "AUTO" if self.auto_mode else "MANUAL"
        mode_surface = self.subtitle_font.render(mode_text, True, (56, 74, 12))
        mode_rect = mode_surface.get_rect(topleft=(WINDOW_WIDTH - 150, 20))
        screen.blit(mode_surface, mode_rect)
        
        # Indicador de velocidade
        speed_text = f"Velocidade: {int((1000 - self.speed) / 10)}"
        speed_surface = self.subtitle_font.render(speed_text, True, (56, 74, 12))
        speed_rect = speed_surface.get_rect(topleft=(WINDOW_WIDTH - 250, 60))
        screen.blit(speed_surface, speed_rect)
        
    def draw_grass(self, screen):
        grass_color = (167, 209, 61)
        for row in range(CELL_NUMBER_Y):
            if row % 2 == 0:
                for col in range(CELL_NUMBER_X):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(CELL_NUMBER_X):
                    if col % 2 == 1:
                        grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, grass_color, grass_rect)
                        
    def draw_score(self, screen):
        score_text = str(self.score)
        score_surface = self.font.render(score_text, True, (56, 74, 12))
        score_x = int(CELL_SIZE * 3)  # Movido mais para a direita
        score_y = int(CELL_SIZE)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        screen.blit(score_surface, score_rect)
        
    def draw_start_screen(self, screen):
        # Título
        title_surface = self.title_font.render('SNAKE GAME', True, (56, 74, 12))
        title_rect = title_surface.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 100))
        screen.blit(title_surface, title_rect)
        
        # Instruções
        start_surface = self.subtitle_font.render('Pressione QUALQUER TECLA para começar', True, (56, 74, 12))
        start_rect = start_surface.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
        screen.blit(start_surface, start_rect)
        
        # Controles
        controls_surface = self.subtitle_font.render('Use as setas para mover', True, (56, 74, 12))
        controls_rect = controls_surface.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 50))
        screen.blit(controls_surface, controls_rect)
        
        # Informação sobre wraparound
        wrap_surface = self.subtitle_font.render('A cobra atravessa as bordas!', True, (56, 74, 12))
        wrap_rect = wrap_surface.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100))
        screen.blit(wrap_surface, wrap_rect)
        
        # Informações sobre modo automático e controles de velocidade
        auto_surface = self.subtitle_font.render('Pressione A para modo automático', True, (56, 74, 12))
        auto_rect = auto_surface.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 150))
        screen.blit(auto_surface, auto_rect)
        
        speed_surface = self.subtitle_font.render('= acelerar | - desacelerar', True, (56, 74, 12))
        speed_rect = speed_surface.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 200))
        screen.blit(speed_surface, speed_rect)

def main():
    # Configurar a tela
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    
    # Criar instância do jogo
    game = Game()
    
    # Event personalizado para movimento da cobra
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, game.speed)
    
    # Loop principal do jogo
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == SCREEN_UPDATE:
                game.update()
                # Atualizar o timer com a nova velocidade
                pygame.time.set_timer(SCREEN_UPDATE, game.speed)
                
            if event.type == pygame.KEYDOWN:
                if not game.game_started:
                    game.start_game()
                else:
                    if event.key == pygame.K_a:
                        game.toggle_auto_mode()
                    elif event.key == pygame.K_EQUALS:  # Tecla =
                        game.increase_speed()
                    elif event.key == pygame.K_MINUS:  # Tecla -
                        game.decrease_speed()
                    elif not game.auto_mode:  # Só aceita controles manuais se não estiver no modo auto
                        if event.key == pygame.K_UP:
                            if game.snake.direction.y != 1:
                                game.snake.direction = pygame.Vector2(0, -1)
                        elif event.key == pygame.K_DOWN:
                            if game.snake.direction.y != -1:
                                game.snake.direction = pygame.Vector2(0, 1)
                        elif event.key == pygame.K_RIGHT:
                            if game.snake.direction.x != -1:
                                game.snake.direction = pygame.Vector2(1, 0)
                        elif event.key == pygame.K_LEFT:
                            if game.snake.direction.x != 1:
                                game.snake.direction = pygame.Vector2(-1, 0)
                        
        # Desenhar tudo
        screen.fill((175, 215, 70))
        game.draw_elements(screen)
        pygame.display.update()
        clock.tick(FPS)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()