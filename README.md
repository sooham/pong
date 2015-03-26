# BallNet - The Intelligent Pong player

### (3rd place winner)[http://www.cs.toronto.edu/~guerzhoy/pong2015/] for the U of T wide PongAI competition!

##Made by Juan Camilo Osorio and Sooham Rafiz. 

Our submission for the Pong Artificial Intelligence competition
hosted by U of T professor [Michael Guerzhoy](http://www.cs.toronto.edu/~guerzhoy/)

##Specifics of the program
The main Pong Artifical intelligence program is sparsely documented.
Instead documentation on the code is provided here.

The program is written in Python and relies on the PyGame library to work
properly. To use the AI, you **must** call the function `pong_ai()`.

`pong_ai` function relies on the `object.AI` class to calculate the velcoity
of the ball and it's future trajectory.

What makes the AI truly intelligent is it's ability to agressively hit the
corners of the opposition's side yet catch extremely fast balls directed at itself.

##Bugs and issues:
Ball passes through paddle when ball reaches maximum velocity.

##LICENSE
This code can be used under the terms of the creative commons
CC 1.0 Universal license, hence this code and its derivatives cannot be used
without reference to the original authors.

Thank you U of T professor Michael Guerzhoy for hosting the competition.
