# CMake 学习指南

## 简介

CMake 是一个跨平台的自动化构建系统，它使用配置文件（`CMakeLists.txt`）来生成标准的构建文件，如 Unix 的 Makefile 或 Windows 的 Visual Studio 项目文件。CMake 不依赖于某个具体的编译器，可以支持多种编译环境。

## 安装 CMake

CMake 可以从其[官方网站](https://cmake.org/download/)下载并安装。支持 Windows、Linux 和 macOS 等多个平台。

## 基本概念

- **CMakeLists.txt**：项目根目录下的配置文件，定义了如何编译和链接程序。
- **目标（Target）**：通常指可执行文件或库。
- **源文件（Source Files）**：项目中的源代码文件。

## 创建一个简单的 CMakeLists.txt

例如，为 `main.c` 和 `hello.c` 文件创建一个简单的项目。

```cmake
cmake_minimum_required(VERSION 3.10)  # 指定 CMake 的最低版本
project(HelloWorld)                   # 定义项目名称

add_executable(HelloWorld main.c hello.c)  # 添加可执行文件
```

## 编译项目

1. **创建构建目录**：在项目根目录下创建一个名为 `build` 的目录。

   ```bash
   mkdir build && cd build
   ```

2. **运行 CMake 配置项目**：

   ```bash
   cmake ..
   ```

3. **构建项目**：使用生成的构建系统（如 Makefile）构建项目。

   ```bash
   make
   ```

## 在 Windows 上使用 CMake

如果你使用的是 Windows 系统，有以下几个选项来编译你的项目：

### 1. 使用 Visual Studio

CMake 可以生成 Visual Studio 解决方案文件。使用以下命令：

```bash
cmake -G "Visual Studio 16 2019" ..
```

然后在 Visual Studio 中打开生成的 `.sln` 文件。

### 2. 使用 MSBuild

如果你安装了 MSBuild，可以直接在命令行中构建 Visual Studio 项目：

```bash
cmake ..
msbuild HelloWorld.sln
```

### 3. 使用 MinGW 或 Cygwin

你也可以在 Windows 上安装 MinGW 或 Cygwin 来使用 Unix 风格的 Makefile。

## 高级特性

- **模式规则**：使用通配符定义通用的构建规则。
- **自动变量**：如 `$@`（目标名）、`$^`（所有依赖项）。
- **条件判断**：使用 `if`、`else` 等语句根据不同条件执行不同命令。
- **自定义函数**：定义复用的逻辑。

## 使用 WSL

在 Windows Subsystem for Linux (WSL) 中，你可以像在 Linux 环境下一样使用 CMake 和 Make。安装 WSL，并在其中安装必要的编译工具。

## 结论

CMake 是一个功能强大的构建系统，它可以简化跨平台项目的构建过程。通过学习 CMake，你可以更高效地管理复杂的构建任务，并确保你的项目可以在多种不同的环境中轻松构建。
