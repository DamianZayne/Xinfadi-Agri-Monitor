# 新发地蔬菜价格监测系统

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Scraping Success](https://img.shields.io/badge/success_rate-98%25-brightgreen.svg)]()

逆向分析前端分页组件通信协议，实现自动化数据采集管道，支撑市场价格分析报告生成

## ✨ 核心功能

- 🕵️ 逆向分析 jQuery + layPage 分页加载机制
- ⚡ 自动化模拟 POST 分页请求链（current/page + limit 参数维护）
- 🛡️ 反反爬措施（随机延迟 + 请求头伪装）
- 📊 累计采集蔬菜价格数据 573,046 条

## 🚀 快速启动

### 环境安装

```bash
pip install requests fake-useragent pandas
