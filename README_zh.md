# 示例应用程序

一个具有分层入口点、CLI 参数解析和实用工具模块的 Python 示例应用程序。  
展示了使用 Python 构建命令行工具的简单结构，并包含经典贪吃蛇游戏。

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
   source .venv/bin/activate  # Windows 上: .venv\Scripts\activate
   ```
4. 无需外部依赖。本项目仅使用 Python 标准库。

## 使用方式

### 贪吃蛇游戏

运行经典贪吃蛇游戏：

```bash
python main.py
```

**操作说明：**
- **方向键**或 **WASD** 移动蛇
- **Q** 退出游戏

蛇在 20×15 的棋盘上移动。吃掉 `*`（食物）可增长身体并增加分数。撞墙或撞到自身则游戏结束。

### CLI 工具

运行命令行示例工具：

```bash
python app.py --name YourName
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

### `main.py`
贪吃蛇游戏的入口点。处理键盘输入、渲染和主游戏循环。

### `snake.py`
定义 `Snake` 类，包括移动、增长、碰撞检测和方向控制。

### `app.py`
核心应用程序模块。包含 `run_app(args)` 函数，打印欢迎消息和接收到的参数。

### `cli.py`
命令行接口模块，使用 `argparse`。提供 `parse_args(args=None)` 来解析 `--name` 和 `--verbose`。

### `__main__.py`
通过从 `main.py` 导入 `main` 并调用它来启用 `python -m` 执行。

### `math_utils.py`
实用工具模块，包含带类型和值检查的 `factorial(n)` 函数。