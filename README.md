# NcatBot Modular Plugins | 模块化插件合集

基于 [NcatBot](https://github.com/liyihao1110/ncatbot) 框架开发的 QQ 机器人插件合集。

> ✨ **核心设计理念：高度解耦**
> 本项目中的每一个插件 (`plugins/` 目录下的文件夹) 均设计为**独立模块**。您可以根据需求仅选择安装其中某一个插件，而无需加载整个项目。互不依赖，即插即用。

## 🧩 插件列表与介绍

### 1. Pixiv 综合助手 (`UnnamedPixivIntegrate`)

功能最强大的 Pixiv 集成插件，支持搜图、下载、每日推送及画师更新检测。

* **独立性**：仅依赖 `ncatbot` 及 `BetterPixiv` 逻辑，可单独部署。
* **主要功能**：
* **作品查询**：通过 ID 获取插画详情及原图下载。
* **每日插画推送**：定时推送每日随机涩图（支持来源：用户收藏夹 / 本地磁盘）。
* **画师更新检测**：监控指定画师，一旦有新作品发布自动推送到群。
* **Docker 优化**：内置 Docker 路径映射逻辑，支持容器化部署时的文件发送。


* **指令**：
* `p <id>` 或 `pixiv <id>`：下载并发送指定 ID 的作品（自动检测 R18）。
* `pi <id>` 或 `pixiv_info <id>`：仅查看作品信息。
* `uis`：手动触发每日插画源的更新。


* **核心配置** (`config/UnnamedPixivIntegrate.json`)：
* `refresh_token`: 必填，Pixiv Refresh Token。
* `proxy_server`: 代理地址 (如 `http://127.0.0.1:7890`)。
* `daily_illust_config`: 每日推送的时间、来源配置。



### 2. 全能搜图 (`UnnamedImageSearchIntegrate`)

集成多引擎的反向搜图插件，目前核心支持 **SauceNAO**。

* **独立性**：完全独立，仅需配置 API Key。
* **主要功能**：
* **统一结果模型**：自动解析 SauceNAO 复杂的返回结果，提取标题、作者、相似度和来源链接。
* **智能限流**：内置速率限制处理，防止 API 配额耗尽。
* **引用搜图**：通过回复图片触发，交互自然。


* **使用方法**：
* 在群聊中**回复**一张图片，并发送文本 `si` (Search Image)。


* **核心配置** (`config/UnnamedImageSearchIntegrate.json`)：
* `api_token`: SauceNAO API Key。
* `min_similarity`: 最低相似度阈值 (默认 70.0)。



### 3. JMComic 解析 (`UnnamedJmComicIntegrate`)

简单高效的 JMComic 禁漫天堂 ID 解析工具。

* **独立性**：依赖 `jmcomic` 库。
* **主要功能**：
* 根据 JM ID 解析本子标题、Tag 等信息。
* 支持代理配置以绕过网络限制。


* **指令**：
* `jm <id>`：解析指定 ID 的本子信息。


* **核心配置** (`config/UnnamedJmComicIntegrate.json`)：
* `proxy_server`: 代理服务器地址。



### 4. CM / Hitomi 集成 (`UnnamedCmIntegrate`)

针对特定后端（色孽神选/Hitomi）的下载与管理集成插件。

* **独立性**：需要配合特定的后端服务运行。
* **主要功能**：
* 解析 Hitomi ID 或 URL。
* 后端连通性测试。
* 自动检查 Tag 缺失并引导补全。
* 提交下载/录入任务。


* **指令**：
* `cm <id/url>`：提交下载任务或查询状态。


* **核心配置** (`config/UnnamedCmIntegrate.json`)：
* `base_url`: 后端 API 地址。
* `auth_token`: 鉴权 Token。



---

## 🚀 快速开始

### 环境要求

* Python 3.13+
* NcatBot
* NapCat (作为 OneBot11 客户端)

### 安装步骤

1. **克隆项目**
    ```bash
    git clone https://github.com/ACBAD/qqbot-napcat
    cd qqbot-napcat
    ```
2. **安装依赖**
    各个插件目录下的 `requirements.txt` (如果有) 需要分别安装，或者安装项目根目录的依赖：
    ```bash
    pip install ncatbot httpx pydantic aiofiles jmcomic
    ```
3. **配置 NapCat**

    确保你的 NapCat 客户端已启动，并且 HTTP/WebSocket 配置与 `ncatbot` 默认配置一致。
4. **先运行一次机器人, 待插件全部加载后关闭, 以创建默认配置文件**
    ```bash
    python main.py
    ```
5. **填写配置文件等, 开始使用**

### 独立使用指南

如果您只需要其中某一个功能（例如只想要搜图功能）：

1. 建立一个新的文件夹。
2. 创建一个 `main.py` 写入基本的 Bot 启动代码。
3. 引用代码内容
    - **强烈推荐**: Linux使用软链接方式链接, Windows可使用管理员权限创建链接, 此时拉取更新只需进入源仓库`git pull`即可
    - 将 `plugins/UnnamedImageSearchIntegrate` 文件夹完整复制到新项目的 `plugins/` 目录下。若项目更新需要手动复制
4. 运行即可。

---

## 📂 目录结构

```text
qqbot-napcat/
├── main.py                     # 机器人入口
├── what.jpg                    # 戳一戳彩蛋资源
├── plugins/                    # 插件目录
│   ├── unnamed_pixiv_integrate/        # Pixiv 插件
│   ├── unnamed_image_search_integrate/ # 搜图插件
│   ├── unnamed_jmcomic_integrate/      # JMComic 插件
│   └── unnamed_cm_integrate/           # CM 集成插件
└── ...

```

## ⚠️ 免责声明

本项目的插件功能（如 Pixiv 下载、JMComic 解析等）仅供学习交流使用。

* 请勿用于商业用途。
* 请勿在公共场合传播违反法律法规的内容。
* 开发者不对使用本插件导致的封号、网络风险负责。