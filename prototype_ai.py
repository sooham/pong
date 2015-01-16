old_position = (0, 0)
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
    global old_position

    old_position = table_size[0]/2, table_size[1]/2
    new_position = ball_frect.pos

    dx = abs(paddle_frect.pos[0] - ball_frect.pos[0])
    # find the velocity of the ball
    ball_v = (new_position[0] - old_position[0]), (new_position[1] - old_position[1])
    old_position = new_position
    ball_frect_future_y = ball_frect.pos[1] + ball_v[1]*dx

    if paddle_frect.pos[1] < ball_frect_future_y:
      return 'down'
    else:
      return 'up'

