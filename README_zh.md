
# 示例应用程序

一个带有分层入口点、CLI 参数解析和实用模块的 Python 示例应用程序。  
它展示了使用 Python 构建命令行工具的简单结构。

## 安装

1. 确保已安装 Python 3.8+。
2. 克隆仓库：
   ```bash
   git clone https://github.com/Chaistr/test.git
   cd test
   ```
3. （可选）创建并激活虚拟环境：
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows 环境: .venv\Scripts\activate
   ```
4. 无需外部依赖。本项目仅使用 Python 标准库。

## 使用

运行主入口点：
```bash
python main.py --name YourName
```

示例输出：
```
Running the application...
Received arguments: Namespace(name='YourName', verbose=False)
```

可用选项：
- `--name NAME`   要问候的名称（默认：World）
- `--verbose`     启用详细输出

你也可以使用 Python 的 `-m` 标志：
```bash
python -m __main__ --name Developer
```

## 模块

### `app.py`
核心应用模块。包含 `run_app(args)` 函数，用于打印欢迎信息和接收到的参数。

### `cli.py`
命令行接口模块，基于 `argparse`。提供 `parse_args(args=None)` 解析命令行参数，如 `--name` 和 `--verbose`。

### `math_utils.py`
数学工具模块。

#### `factorial(n)`
返回 `n` 的阶乘。若 `n` 不是整数则抛出 `TypeError`，若 `n` 为负数则抛出 `ValueError`。

示例：
```python
from math_utils import factorial

print(factorial(5))  # 输出: 120
print(factorial(0))  # 输出: 1
```

### `snake.py`
实现经典贪吃蛇游戏的 `Snake` 类。管理蛇身、移动、增长、碰撞检测和方向变更。

基本用法：
```python
from snake import Snake

snake = Snake(start_x=5, start_y=5, length=3)
snake.move()
snake.grow()
snake.change_direction((0, -1))
if snake.check_collision(width=20, height=20):
    print("游戏结束")
```

## 贡献

欢迎贡献！参与方式：

1. Fork the repository.
