def chaser(paddle_frect, other_paddle_frect, ball_frect, table_size):
    if paddle_frect.pos[1]+paddle_frect.size[1]/2 < ball_frect.pos[1]+ball_frect.size[1]/2:
        return "down"
    else:
        return "up"
