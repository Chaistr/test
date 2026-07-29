import random


class Snake:
    """贪吃蛇类，管理蛇的移动、增长和碰撞检测"""

    def __init__(self, start_x: int, start_y: int, length: int = 3):
        """初始化蛇，蛇身用列表表示，蛇头在列表末尾"""
        self.body = [(start_x - i, start_y) for i in range(length)]
        self.direction = (1, 0)  # 初始向右
        self.grow_flag = False

    def move(self):
        """根据当前方向移动蛇头，移除蛇尾（除非设置了增长标志）"""
        head_x, head_y = self.body[-1]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body.append(new_head)
        if not self.grow_flag:
            self.body.pop(0)
        else:
            self.grow_flag = False

    def grow(self):
        """设置增长标志，下次移动时蛇身长度+1"""
        self.grow_flag = True

    def check_collision(self, width: int, height: int) -> bool:
        """检测是否撞墙或撞自身，返回 True 表示发生碰撞"""
        head = self.body[-1]
        x, y = head
        # 撞墙检测
        if x < 0 or x >= width or y < 0 or y >= height:
            return True
        # 撞自身检测（排除蛇头自身）
        if head in self.body[:-1]:
            return True
        return False

    def change_direction(self, new_direction: tuple):
        """改变方向，不允许直接反向"""
        dx, dy = new_direction
        # 不允许 180 度转向
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)

    def get_head(self) -> tuple:
        """返回蛇头坐标"""
        return self.body[-1]

    def get_body(self) -> list:
        """返回蛇身坐标列表"""
