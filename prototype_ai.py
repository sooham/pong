set_up = False

def reflect(a ,b):
  if a < 0:
    a = -a
  fdiv, rem = divmod(a, b)
  if fdiv % 2 == 0:
    return rem
  else:
    return b - rem

def chaser(paddle_frect, other_paddle_frect, ball_frect, table_size):
    global set_up
    if not set_up:
      chaser.ai = PongAI(paddle_frect, table_size)
      set_up = True

    vel = chaser.ai.get_vel(ball_frect)

    if vel[0] == 0:
      return 'nothing'

    if chaser.ai.ball_towards:
        intercept = (ball_frect.pos[1] + vel[1] * ((paddle_frect.pos[0] - ball_frect.pos[0]) / vel[0]))
        prediction = reflect(intercept, table_size[1])  
    else:
        prediction = chaser.ai.TABLE_CENTER

    chaser.ai.update_state(paddle_frect, ball_frect)

    if prediction < chaser.ai.TABLE_CENTER:
        paddle_hit_point = paddle_frect.pos[1] + 1 * paddle_frect.size[1] / 8
    elif prediction > chaser.ai.TABLE_CENTER:
        paddle_hit_point = (paddle_frect.pos[1] + 7 * paddle_frect.size[1] / 8) 
    else:
        paddle_hit_point = paddle_frect.pos[1] + paddle_frect.size[1] / 2
    

    if paddle_hit_point < prediction:
     return 'down'
    elif paddle_hit_point > prediction: 
     return 'up'
    else:
     return 'nothing'


class PongAI:
  def __init__(self, paddle, table_size,):
    self.ball_old_pos = (table_size[0] / 2, table_size[1] / 2)
    self.ball_old_vel = (0,0)
    self.ball_old_dist = abs(paddle.pos[0] - self.ball_old_pos[0])
    self.ball_towards = None
    self.TABLE_CENTER = table_size[1] / 2

  def get_vel(self, ball):
    ''' Returns the current velocity tuple of the ball'''
    return ball.pos[0] - self.ball_old_pos[0], ball.pos[1] - self.ball_old_pos[1]


  def towards(self, paddle, ball):
    ''' Changes the ball_direction'''
    current_dist = abs(paddle.pos[0] - ball.pos[0])
    if current_dist < self.ball_old_dist:
      self.ball_towards = True
    elif current_dist > self.ball_old_dist:
      self.ball_towards = False


  def update_state(self, paddle, ball):
    ''' updates the state of the AI'''
    self.ball_old_vel = self.get_vel(ball)
    self.ball_old_pos = ball.pos
    self.towards(paddle, ball)
    self.ball_old_dist = abs(paddle.pos[0] - ball.pos[0])