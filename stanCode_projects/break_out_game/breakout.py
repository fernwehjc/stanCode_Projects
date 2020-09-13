"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

This file delivers a game that the user can control the paddle
    to make the ball bounce in the window contains with bricks.
When the ball collides with a brick, the brick will be removed.
Once all bricks are removed or the user let the ball collide with the bottom of the window for certain times,
    the game is over.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.


def main():
    graphics = BreakoutGraphics()
    lives = graphics.get_lives()
    win = graphics.victory
    lose = graphics.fail
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    keep_break = 0  # The times that the user consistently clears a brick.
    while True:
        pause(FRAME_RATE)
        # Check if the user starts the game.
        while graphics.controller == 1:
            pause(FRAME_RATE)
            graphics.ball.move(dx, dy)
            # Check if the ball collides with the bottom of the window.
            if graphics.ball_hit_floor():
                lives -= 1
                graphics.controller = 0
                no_fall = 0
                # If the user still has chance to play, reset the ball.
                if lives > 0:
                    if lives == 2:
                        graphics.window.remove(graphics.heart_1)
                    elif lives == 1:
                        graphics.window.remove(graphics.heart_2)
                    graphics.reset_ball()
                    # Get the new velocity for the new play.
                    dx = graphics.get_dx()
                    dy = graphics.get_dy()
                # If the user has zero chance left to play, leave the loop.
                else:
                    # Switch off the game to wait for the user to click the mouse to start again.
                    graphics.controller = 0
                    graphics.window.remove(graphics.heart_3)
                    graphics.window.add(lose, x=(graphics.window.width - graphics.fail.width) / 2,
                                        y=graphics.window.height / 2)
                    break
            # Check if the ball collides with the paddle.
            if graphics.ball_hit_paddle():
                # Only change the direction once whenever the ball collides with the paddle.
                if dy > 0:
                    dy = -dy
            # Check if the ball collides with a brick.
            if graphics.ball_hit_brick():
                # Removes the brick with which the ball collides.
                graphics.remove_brick()
                dy = -dy
                keep_break += 1
                # Speed up the ball whenever the user consistently scores for 10 points.
                if keep_break == 10:
                    dx = 1.1 * dx
                    dy = 1.1 * dy
                    keep_break = 0
                # If all bricks are removed, leave the loop and wait for the user to click the mouse to start again.
                if graphics.num_bricks == 0:
                    graphics.controller = 0
                    graphics.window.add(win, x=(graphics.window.width - graphics.victory.width) / 2,
                                        y=graphics.window.height / 2)
                    break
            # Check if the ball collides with either left or right side of the window.
            if graphics.ball_hit_side_walls():
                # Only change the direction once whenever the ball collides with the wall.
                if graphics.ball.x < 0 and dx < 0:
                    dx = -dx
                elif graphics.ball.x + graphics.ball.width > graphics.window.width and dx > 0:
                    dx = -dx
            # Check if the ball collides with the top of the window.
            if graphics.ball_hit_ceiling():
                dy = -dy


if __name__ == '__main__':
    main()
