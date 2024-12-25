# 阿里云 SEO/SEM 关键词管理系统

基于 Streamlit 开发的一站式 SEO/SEM 关键词管理平台，实现了站内外数据的整合分析，并通过智能化手段扩充词库，为 SEO 和 SEM 运营提供数据支持。

## 功能特性

### 1. 词库管理
- 关键词列表管理（支持多维度筛选和排序）
- 批量导入/导出功能（支持 Excel、CSV 格式）
- 关键词状态管理（启用/暂停/删除）
- 关键词优先级设置

### 2. 数据监控
- 流量趋势分析
- 排名分布统计
- 转化趋势追踪
- 来源分布分析

### 3. 智能扩充
- 相关词推荐
- 长尾词发现
- 竞品词发现
- 同义词推荐
- 关键词权重分析
- 搜索量与竞争度分析

### 4. 查询分析
- SEO数据分析（排名、流量、用户行为等）
- SEM数据分析（广告效果、投放位置等）
- 一站式查询面板
- 可视化数据展示

### 5. 数据报告
- 流量分析（来源分布、落地页分析、转化路径）
- 转化分析（漏斗分析、产品转化分布）
- 竞品分析（关键词覆盖对比、竞争力分析）
- 投放建议（多场景优化建议）

## 技术栈

- Python 3.9
- Streamlit 1.32.0
- Pandas 2.2.0
- Plotly 5.18.0
- NumPy 1.26.0
- WordCloud 1.9.3

## 快速开始

### 方式一：本地运行

1. 克隆项目
```bash
git clone <repository_url>
cd sem-seo-app
```

2. 创建虚拟环境（可选）
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 运行应用
```bash
streamlit run app.py
```

### 方式二：Docker部署

1. 构建镜像
```bash
docker-compose build
```

2. 启动服务
```bash
docker-compose up -d
```

访问 http://localhost:8501 即可使用系统。

## 目录结构

```
sem-seo-app/
├── app.py              # 主应用程序
├── requirements.txt    # 项目依赖
├── Dockerfile         # Docker配置文件
├── docker-compose.yml # Docker编排文件
├── .dockerignore     # Docker忽略文件
└── README.md         # 项目说明文档
```

## 使用说明

1. **词库管理**
   - 点击"➕ 添加关键词"添加新的关键词
   - 使用筛选条件过滤关键词列表
   - 可导出数据为CSV格式

2. **数据监控**
   - 选择时间范围查看数据趋势
   - 查看不同维度的数据分布
   - 实时监控关键指标变化

3. **智能扩充**
   - 输入种子关键词获取相关推荐
   - 设置最小搜索量和最大扩充数量
   - 查看关键词分析可视化结果

4. **查询分析**
   - 输入关键词查看SEO和SEM数据
   - 对比分析不同维度的数据
   - 查看历史趋势和分布情况

5. **数据报告**
   - 选择报告类型查看详细分析
   - 查看多维度的数据可视化
   - 获取优化建议和策略指导

## 注意事项

1. 当前版本使用模拟数据进行展示
2. 建议使用Chrome或Firefox浏览器访问
3. 推荐屏幕分辨率1920x1080或以上

## 后续规划

1. 接入真实数据源
2. 添加用户权限管理
3. 优化数据分析算法
4. 增加更多自动化功能
5. 提供API接口服务

## 贡献指南

欢迎提交Issue和Pull Request。

## 许可证

MIT License 