// awesome_c_driver.c
#include <stdio.h>
#include <stdbool.h>


/**
# -shared: 创建共享库
# -o: 输出文件名
# -fPIC: 允许代码独立于位置

gcc -shared -o awesome_c_driver.so awesome_c_driver.c -fPIC
 */


// 模拟灯光状态的全局变量
static bool is_on = false;
static int brightness = 0; // 0-255

// 暴露给 Python 的函数：获取状态
// 返回 1 (True) 或 0 (False)
int get_state() {
    return is_on;
}

// 暴露给 Python 的函数：获取亮度
// 返回 0-255
int get_brightness() {
    return brightness;
}

// 暴露给 Python 的函数：设置状态为 ON
void turn_on() {
    is_on = true;
    if (brightness == 0) {
        brightness = 255; // 默认亮度
    }
    printf("C Driver: Light turned ON. Brightness: %d\n", brightness);
}

// 暴露给 Python 的函数：设置状态为 OFF
void turn_off() {
    is_on = false;
    brightness = 0;
    printf("C Driver: Light turned OFF.\n");
}

// 暴露给 Python 的函数：设置亮度
// 接受一个 0-255 的整数
void set_brightness(int value) {
    if (value > 0) {
        is_on = true;
        brightness = value;
        printf("C Driver: Brightness set to %d.\n", brightness);
    } else {
        turn_off();
    }
}

