cmake_minimum_required(VERSION 3.10)  # 指定 CMake 的最低版本要求
project(HelloWorld)                   # 定义项目名称

# 添加 src 目录下的所有源文件到变量 SRC_FILES
file(GLOB SRC_FILES "src/*.c")

# 指定生成可执行文件
add_executable(HelloWorld ${SRC_FILES})
