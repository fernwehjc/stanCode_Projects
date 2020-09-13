"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This file creates all graphic objects and the critical function for the Breakout Game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gimage import GImage
import random

# Constants
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.
NUM_LIVES = 3          # Chances for a play.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        self.paddle_offset = paddle_offset
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.brick_offset = brick_offset
        self.brick_rows = brick_rows
        self.brick_height = brick_height
        self.brick_spacing = brick_spacing
        self.controller = 0  # 0: game off; 1: game on
        self.num_bricks = brick_cols * brick_rows  # The number of bricks in a game.
        self.score = 0  # The number of points that the user wins.
        self.__lives = NUM_LIVES  # The number of chances that the user has to play.

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width) / 2,
                        y=self.window.height - self.paddle_offset - self.paddle.height)

        self.half_paddle = GRect(width=0.5 * self.paddle_width, height=self.paddle_height)
        self.half_paddle.filled = True

        # Create a filled ball.
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0

        # Center a filled ball in the graphical window and set up an initial moving direction & velocity.
        self.reset_ball()

        # Draw bricks.
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(width=brick_width, height=brick_height, x=j * (brick_width + brick_spacing),
                              y=brick_offset + i * (brick_height + brick_spacing))
                # Colors the bricks from the top row of bricks based on the remainder of "row_order divides 10".
                if (i + 1) % 10 == 1 or (i + 1) % 10 == 2:
                    brick.filled = True
                    brick.color = 'red'
                    brick.fill_color = 'red'
                elif (i + 1) % 10 == 3 or (i + 1) % 10 == 4:
                    brick.filled = True
                    brick.color = 'orange'
                    brick.fill_color = 'orange'
                elif (i + 1) % 10 == 5 or (i + 1) % 10 == 6:
                    brick.filled = True
                    brick.color = 'yellow'
                    brick.fill_color = 'yellow'
                elif (i + 1) % 10 == 7 or (i + 1) % 10 == 8:
                    brick.filled = True
                    brick.color = 'green'
                    brick.fill_color = 'green'
                elif (i + 1) % 10 == 9 or (i + 1) % 10 == 0:
                    brick.filled = True
                    brick.color = 'blue'
                    brick.fill_color = 'blue'
                self.window.add(brick)

        # Create a score board.
        self.score_board = GLabel(f'Score: {self.score}')
        self.score_board.font = 'nevada-20-bold'
        self.score_board.color = 'forestgreen'
        self.window.add(self.score_board, 5, self.window.height - 3)

        # Create a lives indicator.
        self.heart_1 = GImage('heart.jpg')
        self.window.add(self.heart_1, x=self.window.width - (NUM_LIVES - 0) * (self.heart_1.width + 1),
                        y=self.window.height - self.heart_1.height)
        self.heart_2 = GImage('heart.jpg')
        self.window.add(self.heart_2, x=self.window.width - (NUM_LIVES - 1) * (self.heart_2.width + 1),
                        y=self.window.height - self.heart_2.height)
        self.heart_3 = GImage('heart.jpg')
        self.window.add(self.heart_3, x=self.window.width - (NUM_LIVES - 2) * (self.heart_3.width + 1),
                        y=self.window.height - self.heart_3.height)

        # Create a message for the user who clears all bricks.
        self.victory = GLabel('VICTORY!')
        self.victory.font = 'Bradley Hand-60-bold'

        # Create a message for the user who fails the game.
        self.fail = GLabel('GAME OVER!')
        self.fail.font = 'Bradley Hand-60-bold'

        self.empty = GOval(0, 0)
        self.blue = GRect(30, 30)
        self.blue.filled = True
        self.blue.color = 'navy'
        self.blue.fill_color = 'navy'

        # Initialize our mouse listeners.
        onmousemoved(self.move_paddle)
        onmouseclicked(self.game_start)

    def move_paddle(self, event):
        """
        When the user moves the mouse, the paddle will follow the move but always stays within the window.
        :param event: MouseEvent
        """
        if event.x < self.paddle.width:
            self.paddle.x = 0
        elif event.x > self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width / 2

    def game_start(self, event):
        """
        When the user clicks the mouse, the game starts.
        :param event: MouseEvent
        """
        self.controller = 1

    def reset_ball(self):
        """
        Centered the ball in the window and set the initial moving direction and velocity.
        """
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height-self.ball.height)/2
        self.set_ball_velocity()
        self.window.add(self.ball)

    def set_ball_velocity(self):
        """
        Randomly assign a horizontal velocity and set the vertical velocity as the constant "INITIAL_Y_SPEED".
        """
        self.__dx = random.randint(2, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    def ball_hit_floor(self):
        """
        Determine whether the ball exceeds the bottom of the window.
        :return: boolean, True stands for the situation of the ball exceeding the window.
        """
        is_ball_hit_floor = (self.ball.y + self.ball.height >= self.window.height)
        return is_ball_hit_floor

    def ball_hit_paddle(self):
        """
        Determine whether any of the four vertices of the ball object touches the paddle object.
        :return: boolean, True stands for the situation of part of the ball overlapping the paddle.
        """
        obj_tl = self.window.get_object_at(self.ball.x, self.ball.y)
        obj_tr = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        obj_bl = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        obj_br = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        is_hit_paddle = (obj_tl is self.paddle or obj_tr is self.paddle
                         or obj_bl is self.paddle or obj_br is self.paddle)
        return is_hit_paddle

    def ball_hit_brick(self):
        """
        Determine whether any of the four vertices of the ball object touches a brick object.
        :return: boolean, True stands for the situation of part of the ball overlapping a brick.
        """
        obj_tl = self.window.get_object_at(self.ball.x, self.ball.y)
        obj_tr = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        obj_bl = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        obj_br = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        is_hit_obj = (obj_tl is not None or obj_tr is not None or obj_bl is not None or obj_br is not None)
        is_beyond_paddle = (self.ball.y + self.ball.height) < self.paddle.y
        return is_hit_obj and is_beyond_paddle

    def remove_brick(self):
        """
        Removes a brick once any of the four vertices of the ball object touches a brick object.
        Counts the number of the remain bricks.
        Revise the score board in the window.
        """
        obj_tl = self.window.get_object_at(self.ball.x, self.ball.y)
        obj_tr = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        obj_bl = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        obj_br = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if obj_tl is not None:
            self.window.remove(obj_tl)
            self.score += 1
            self.num_bricks -= 1
            self.score_board.text = f'Score: {self.score}'
        elif obj_tr is not None:
            self.window.remove(obj_tr)
            self.score += 1
            self.num_bricks -= 1
            self.score_board.text = f'Score: {self.score}'
        elif obj_bl is not None:
            self.window.remove(obj_bl)
            self.score += 1
            self.num_bricks -= 1
            self.score_board.text = f'Score: {self.score}'
        elif obj_br is not None:
            self.window.remove(obj_br)
            self.score += 1
            self.num_bricks -= 1
            self.score_board.text = f'Score: {self.score}'

    def ball_hit_side_walls(self):
        """
        Determine whether any of the four vertices of the ball object touches either the left and the right side of
        the window.
        :return: boolean, True stands for the situation of part of the ball exceeding the window.
        """
        is_ball_in_window = 0 < self.ball.x < (self.window.width - self.ball.width)
        return is_ball_in_window is not True

    def ball_hit_ceiling(self):
        """
        Determine whether the ball exceeds the top of the window.
        :return: boolean, True stands for the situation of the ball exceeding the window.
        """
        is_ball_hit_ceiling = self.ball.y <= 0
        return is_ball_hit_ceiling

    # Getter.
    def get_dx(self):
        """
        Get the value of horizontal velocity.
        :return: int, horizontal velocity of the ball
        """
        return self.__dx

    def get_dy(self):
        """
        Get the value of vertical velocity.
        :return: int, vertical velocity of the ball
        """
        return self.__dy

    def get_lives(self):
        """
        Get the value of the total lives of the game.
        :return: int, chances for a user to play
        """
        return self.__lives
