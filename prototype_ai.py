set_up = False
def chaser(paddle_frect, other_paddle_frect, ball_frect, table_size):
    '''return "up" or "down", by predicting the future landing position of the
    ball (given that it never bounces) and goes there.

    Arguments:
    paddle_frect: a rectangle representing the coordinates of the paddle
                  paddle_frect.pos[0], paddle_frect.pos[1] is the top-left
                  corner of the rectangle.
                  paddle_frect.size[0], paddle_frect.size[1] are the dimensions
                  of the paddle along the x and y axis, respectively

    other_paddle_frect:
                  a rectangle representing the opponent paddle. It is formatted
                  in the same way as paddle_frect
    ball_frect:   a rectangle representing the ball. It is formatted in the
                  same way as paddle_frect
    table_size:   table_size[0], table_size[1] are the dimensions of the table,
                  along the x and the y axis respectively

    The coordinates look as follows:

     0             x
     |------------->
     |
     |
     |
 y   v
    '''
    global set_up
    if not set_up:
      print('setting up ai')
      chaser.ai = PongAI(table_size)
      set_up = True
    chaser.ai.detect_wall_bounce(ball_frect)
    chaser.ai.detect_paddle_bounce(ball_frect, paddle_frect)
    chaser.ai.detect_paddle_bounce(ball_frect, other_paddle_frect)
    return 'nothing'


class PongAI:
  ''' Represents a pong player's mind'''
  
  def __init__(self, table_size):
    self.old_pos = (table_size[0] / 2) , (table_size[1] / 2)
    self.old_vel = (0,0)


  def move_predicted_pt(ball_frect):
    ''' moves the paddle to the predicted ball hit y point.'''
    pass

  def get_vel(self, ball_frect):
    ''' Returns the current velocity tuple of the ball'''
    dxdy = (ball_frect.pos[0] - self.old_pos[0]), (ball_frect.pos[1] - self.old_pos[1])
    self.old_pos = ball_frect.pos
    return dxdy

  def detect_wall_bounce(self, ball_frect):
    dxdy = self.get_vel(ball_frect)
    result = abs(self.old_vel[0] - dxdy[0]) < 1e-12 and abs(self.old_vel[0] - dxdy[0]) < 1e-12 and dxdy != (0, 0)
    if result:
      print('bounce')
      'does not detect paddle bounces for some reason'
      self.old_vel = dxdy
    return result

  def detect_paddle_bounce(self, ball_frect, paddle_frect):
    ''' Returns true if the ball is sufficiently close enough to paddle to bounce'''
    if abs(ball_frect.pos[0] - paddle_frect.pos[0]) < (paddle_frect.size[0] + ball_frect.size[0] / 3.5) and (paddle_frect.pos[1] < ball_frect.pos[1] < (paddle_frect.pos[1] + paddle_frect.size[1])):
      print('paddle bounce')




    

class BallPath:
  ''' Represents a ball path object'''

  def __init__(self, start_coords, vel):
    ''' A ball path has a direction and starting point'''
    self.start = start_coords
    self.direction = vel

  def check_path_collision_wall(self, paddle, table_size):
    ''' Returns true iff the ball path will exceed the wall's y coordinate
    range [0, table_size[1]] before it reaches the paddle's x axis point.
    '''
    # check path direction to left or right
    if self.direction[0] < 0: # to left
      return ((table_size[1] - self.start[1])/ self.start[0]) < (self.direction[1] / self.direction[0]) < (self.start[1] / self.start[0])
    else: # to right
      return (self.start[1] / (table_size[0] - self.start[0]))<(self.direction[1] / self.direction[0]) < ((table_size[1] - self.start[1])/ (table_size[0] - self.start[0]))








