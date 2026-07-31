import random
# snake.py - 贪吃蛇核心逻辑模块
# 实现蛇的移动、生长、碰撞检测和方向控制

import random

class Snake:
    """贪吃蛇类，管理蛇的移动、生长和碰撞检测
    
    属性:
        start_x (int): 初始水平位置
        start_y (int): 初始垂直位置
        length (int): 初始蛇身长度
        body (list): 蛇身坐标列表，列表头为蛇尾，列表尾为蛇头
        direction (tuple): 当前移动方向，如 (1, 0) 表示向右
        grow_flag (bool): 生长标志，为 True 时下一次移动蛇身长度+1
    """

    def __init__(self, start_x: int, start_y: int, length: int = 3):
        """初始化蛇，生成初始身体列表
        
        Args:
            start_x: 蛇头初始 x 坐标
            start_y: 蛇头初始 y 坐标
            length: 初始蛇身长度，默认 3
        """
        self.start_x = start_x
        self.start_y = start_y
        self.length = length
        # 初始化蛇身：从 start_x 开始向左延伸 length 个格子
        self.body = [(start_x - i, start_y) for i in range(length)]
        self.direction = (1, 0)  # 初始向右移动
        self.grow_flag = False

    def move(self):
        """根据当前方向移动蛇头，移除蛇尾；若生长标志为真，则不缩短蛇身
        
        无参数，无返回值。
        将蛇头向当前方向移动一个单位，并更新蛇身列表。
        若 grow_flag 为 False，移除蛇尾；否则保留蛇尾并重置 grow_flag。
        """
        head_x, head_y = self.body[-1]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body.append(new_head)
        # 根据生长标志决定是否移除蛇尾
        if not self.grow_flag:
            self.body.pop(0)          # 正常移动，移除蛇尾
        else:
            self.grow_flag = False     # 生长后重置标志，蛇身长度+1

    def grow(self):
        """设置生长标志，下一次移动时蛇身长度+1
        
        无参数，无返回值。
        """
        self.grow_flag = True

    def check_collision(self, width: int, height: int) -> bool:
        """检测是否撞墙或撞自身，若发生碰撞则返回 True
        
        Args:
            width: 游戏区域宽度（格子数）
            height: 游戏区域高度（格子数）
            
        Returns:
            bool: True 表示蛇与墙壁或自身发生碰撞，游戏应结束
        """
        head = self.body[-1]
        x, y = head
        # 判断蛇头是否超出边界
        if x < 0 or x >= width or y < 0 or y >= height:
            return True
        # 判断蛇头是否与身体其他部分重叠（排除蛇头自身）
        if head in self.body[:-1]:
            return True
        return False

    def change_direction(self, new_direction: tuple):
        """改变移动方向，不允许直接反向（180度掉头）
        
        Args:
            new_direction: 新的方向元组，如 (0, -1) 表示向上
        """
        dx, dy = new_direction
        # 防止玩家输入与当前方向完全相反的新方向
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)

    def get_head(self) -> tuple:
        """返回蛇头坐标
        
        Returns:
            tuple: (x, y) 蛇头位置
        """
        return self.body[-1]

    def get_body(self):
        """返回蛇身的完整列表
        
        Returns:
            list: 包含蛇身所有坐标的列表，从蛇尾到蛇头
        """
        return self.body
class Snake:
    """贪吃蛇类，管理蛇的移动、增长和碰撞检测"""

    def __init__(self, start_x: int, start_y: int, length: int = 3):
        """初始化蛇，蛇身用列表表示，蛇头在列表末尾"""
        self.start_x = start_x
        self.start_y = start_y
        self.length = length
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
        return self.body

    def reset(self):
        """重置蛇到初始状态"""
        self.body = [(self.start_x - i, self.start_y) for i in range(self.length)]
        self.direction = (1, 0)
        self.grow_flag = False
