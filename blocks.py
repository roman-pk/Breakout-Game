from turtle import Turtle

COLORS = {'Yellow': 1,
          'Green': 3,
          'Orange': 5,
          'Red': 7
          }


class BlockManager:
    def __init__(self):
        self.all_blocks = []
        self.y_pos = 100

        for color in COLORS:
            self.x_pos = -425
            for i in range(9):
                new_block = Turtle("square")
                # 40px tall by 100px
                new_block.shapesize(2, 5)
                new_block.color(color)
                new_block.penup()
                new_block.goto(self.x_pos, self.y_pos)
                self.all_blocks.append(new_block)
                self.x_pos += 105
                new_block.point = COLORS[color]
            self.y_pos += 45

    def break_block(self, block):
        # Remove the blocks from the list and hide it from the screen
        block.hideturtle()
        self.all_blocks.remove(block)
