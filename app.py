import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 模拟数据生成函数
def generate_mock_data(size=5):
    keywords = ["阿里云", "云服务器", "云数据库", "对象存储", "负载均衡"] * (size // 5 + 1)
    keywords = keywords[:size]
    data = {
        "关键词": keywords,
        "搜索量": np.random.randint(1000, 10000, size),
        "点击量": np.random.randint(100, 1000, size),
        "转化率": np.random.uniform(0.01, 0.1, size),
        "排名": np.random.randint(1, 50, size),
        "CPC": np.random.uniform(1, 10, size),
        "状态": np.random.choice(["启用", "暂停", "删除"], size),
        "优先级": np.random.choice(["高", "中", "低"], size),
        "更新时间": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")] * size
    }
    return pd.DataFrame(data)

def main():
    # 设置页面配置
    st.set_page_config(
        page_title="阿里云 SEO/SEM 关键词管理系统",
        page_icon="🔍",
        layout="wide"
    )

    # 初始化session state
    if 'keywords_data' not in st.session_state:
        st.session_state.keywords_data = generate_mock_data(20)
    if 'show_add_form' not in st.session_state:
        st.session_state.show_add_form = False

    # 侧边栏导航
    st.sidebar.title("功能导航")
    page = st.sidebar.radio(
        "选择功能模块",
        ["词库管理", "数据监控", "智能扩充", "查询分析", "数据报告"]
    )

    # 主页面内容
    st.title("阿里云 SEO/SEM 关键词管理系统")

    if page == "查询分析":
        st.header("关键词查询分析")
        
        # 查询输入
        search_keyword = st.text_input("输入要查询的关键词")
        
        if search_keyword:
            # 创建两列布局
            col_seo, col_sem = st.columns(2)
            
            with col_seo:
                st.markdown("### SEO 数据")
                # SEO核心指标
                st.markdown("#### 核心指标")
                metric_cols = st.columns(2)
                with metric_cols[0]:
                    st.metric("自然排名", "5", "-2")
                    st.metric("日均流量", "1,234", "+15%")
                with metric_cols[1]:
                    st.metric("跳出率", "35.5%", "-2.1%")
                    st.metric("平均停留时间", "2:45", "+0:15")
                
                # SEO趋势图
                st.markdown("#### 流量趋势")
                dates = pd.date_range(start='2024-01-01', end='2024-03-20', freq='D')
                seo_data = pd.DataFrame({
                    '日期': dates,
                    '流量': np.random.randint(100, 500, len(dates))
                })
                fig = px.line(seo_data, x='日期', y='流量', title='SEO流量趋势')
                st.plotly_chart(fig, use_container_width=True)
                
                # SEO页面分布
                st.markdown("#### 收录页面分布")
                pages_df = pd.DataFrame({
                    "页面URL": [f"https://example.com/page{i}" for i in range(1, 6)],
                    "排名": np.random.randint(1, 50, 5),
                    "流量占比": [f"{x:.1f}%" for x in np.random.uniform(10, 30, 5)]
                })
                st.dataframe(pages_df, use_container_width=True)
            
            with col_sem:
                st.markdown("### SEM 数据")
                # SEM核心指标
                st.markdown("#### 核心指标")
                metric_cols = st.columns(2)
                with metric_cols[0]:
                    st.metric("广告排名", "2.3", "+1")
                    st.metric("点击量", "856", "+12%")
                with metric_cols[1]:
                    st.metric("点击率", "4.5%", "+0.8%")
                    st.metric("平均点击成本", "￥2.34", "-￥0.21")
                
                # SEM趋势图
                st.markdown("#### 投放趋势")
                sem_data = pd.DataFrame({
                    '日期': dates,
                    '点击量': np.random.randint(200, 800, len(dates))
                })
                fig = px.line(sem_data, x='日期', y='点击量', title='SEM点击趋势')
                st.plotly_chart(fig, use_container_width=True)
                
                # SEM投放位置
                st.markdown("#### 投放位置分布")
                position_df = pd.DataFrame({
                    "位置": ["Top1", "Top2", "Top3", "侧边栏"],
                    "展现占比": [f"{x:.1f}%" for x in np.random.uniform(10, 40, 4)],
                    "点击率": [f"{x:.1f}%" for x in np.random.uniform(2, 8, 4)]
                })
                st.dataframe(position_df, use_container_width=True)

    elif page == "词库管理":
        st.header("词库管理")
        
        # 添加功能按钮
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("➕ 添加关键词"):
                st.session_state.show_add_form = True
        with col2:
            st.download_button(
                label="📥 导出数据",
                data=st.session_state.keywords_data.to_csv(index=False).encode('utf-8'),
                file_name='keywords_data.csv',
                mime='text/csv'
            )
        with col3:
            st.button("📤 批量导入")
        with col4:
            st.button("🏷️ 标签管理")
            
        # 添加关键词表单
        if st.session_state.show_add_form:
            with st.form("add_keyword_form"):
                st.subheader("添加新关键词")
                new_keyword = st.text_input("关键词")
                col1, col2 = st.columns(2)
                with col1:
                    status = st.selectbox("状态", ["启用", "暂停", "删除"])
                    search_volume = st.number_input("搜索量", min_value=0, value=1000)
                    conversion_rate = st.number_input("转化率", min_value=0.0, max_value=1.0, value=0.05, format="%.3f")
                with col2:
                    priority = st.selectbox("优先级", ["高", "中", "低"])
                    clicks = st.number_input("点击量", min_value=0, value=100)
                    cpc = st.number_input("CPC", min_value=0.0, value=1.0, format="%.2f")
                
                submitted = st.form_submit_button("提交")
                
                if submitted:
                    # 检查关键词是否已存在
                    if new_keyword in st.session_state.keywords_data["关键词"].values:
                        st.error(f"关键词 '{new_keyword}' 已存在！")
                    elif not new_keyword:
                        st.error("请输入关键词！")
                    else:
                        # 添加新关键词
                        new_data = pd.DataFrame([{
                            "关键词": new_keyword,
                            "搜索量": search_volume,
                            "点击量": clicks,
                            "转化率": conversion_rate,
                            "排名": np.random.randint(1, 50),
                            "CPC": cpc,
                            "状态": status,
                            "优先级": priority,
                            "更新时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }])
                        st.session_state.keywords_data = pd.concat([st.session_state.keywords_data, new_data], ignore_index=True)
                        st.success(f"关键词 '{new_keyword}' 添加成功！")
                        st.session_state.show_add_form = False
                        st.rerun()
            
            if st.button("取消"):
                st.session_state.show_add_form = False
                st.rerun()
            
        # 筛选条件
        col1, col2, col3 = st.columns(3)
        with col1:
            status_filter = st.multiselect("状态", ["启用", "暂停", "删除"])
        with col2:
            priority_filter = st.multiselect("优先级", ["高", "中", "低"])
        with col3:
            search_keyword = st.text_input("搜索关键词")
            
        # 应用筛选
        df = st.session_state.keywords_data.copy()
        if status_filter:
            df = df[df["状态"].isin(status_filter)]
        if priority_filter:
            df = df[df["优先级"].isin(priority_filter)]
        if search_keyword:
            df = df[df["关键词"].str.contains(search_keyword, case=False)]
            
        # 展示数据表格
        st.dataframe(
            df,
            column_config={
                "状态": st.column_config.SelectboxColumn(
                    "状态",
                    options=["启用", "暂停", "删除"],
                    required=True
                ),
                "优先级": st.column_config.SelectboxColumn(
                    "优先级",
                    options=["高", "中", "低"],
                    required=True
                )
            },
            hide_index=True,
            use_container_width=True
        )

    elif page == "数据监控":
        st.header("数据监控")
        
        # 时间范围选择
        col1, col2 = st.columns(2)
        with col1:
            date_range = st.date_input(
                "选择时间范围",
                value=(datetime.now() - timedelta(days=30), datetime.now())
            )
        with col2:
            data_type = st.selectbox(
                "数据类型",
                ["整体趋势", "搜索引擎分布", "设备分布", "地域分布"]
            )
        
        # 分别创建四个图表
        col1, col2 = st.columns(2)
        
        with col1:
            # 流量趋势
            dates = pd.date_range(start='2024-01-01', end='2024-03-20', freq='D')
            traffic_data = pd.DataFrame({
                '日期': dates,
                '流量': np.random.randint(1000, 5000, len(dates))
            })
            fig1 = px.line(traffic_data, x='日期', y='流量', title='流量趋势')
            st.plotly_chart(fig1, use_container_width=True)
            
            # 排名分布
            ranking_data = pd.DataFrame({
                '排名区间': ['1-3名', '4-10名', '11-30名', '30名以后'],
                '关键词数量': [30, 45, 15, 10]
            })
            fig2 = px.bar(ranking_data, x='排名区间', y='关键词数量', title='排名分布')
            st.plotly_chart(fig2, use_container_width=True)
            
        with col2:
            # 转化趋势
            conversion_data = pd.DataFrame({
                '日期': dates,
                '转化量': np.random.randint(100, 500, len(dates))
            })
            fig3 = px.line(conversion_data, x='日期', y='转化量', title='转化趋势')
            st.plotly_chart(fig3, use_container_width=True)
            
            # 来源分布
            source_data = pd.DataFrame({
                '来源': ['百度', '360', '搜狗', '其他'],
                '占比': [60, 20, 15, 5]
            })
            fig4 = px.pie(source_data, values='占比', names='来源', title='来源分布')
            st.plotly_chart(fig4, use_container_width=True)

    elif page == "智能扩充":
        st.header("智能词库扩充")
        
        # 输入区域
        col1, col2 = st.columns([2, 1])
        with col1:
            input_keyword = st.text_input("输入关键词", "阿里云")
            expansion_type = st.selectbox(
                "扩充方式",
                ["相关词推荐", "长尾词发现", "竞品词发现", "同义词推荐"]
            )
        with col2:
            min_search_volume = st.slider("最小搜索量", 0, 10000, 100)
            max_keywords = st.number_input("最大扩充数量", 10, 100, 50)
            
        if st.button("开始扩充"):
            with st.spinner("正在分析关键词..."):
                # 模拟加载过程
                st.progress(100)
                
                # 推荐关键词表格
                st.markdown("### 推荐关键词")
                recommended_df = pd.DataFrame({
                    "关键词": [f"{input_keyword}{suffix}" for suffix in ["价格", "教程", "配置", "优惠", "对比", "入门", "使用", "案例", "文档", "问题"]],
                    "搜索量": np.random.randint(100, 1000, 10),
                    "竞争度": np.random.uniform(0.1, 0.9, 10),
                    "预估点击价格": np.random.uniform(1, 10, 10),
                    "相关度": np.random.uniform(0.5, 1.0, 10)
                })
                st.dataframe(recommended_df, use_container_width=True)
                
                # 关键词分析可视化
                st.markdown("### 关键词分析")
                
                # 1. 关键词权重分布
                words_data = pd.DataFrame({
                    "关键词": recommended_df["关键词"],
                    "权重": np.random.randint(10, 100, len(recommended_df))
                })
                
                fig1 = px.bar(
                    words_data,
                    x="关键词",
                    y="权重",
                    title="关键词权重分布",
                    color="权重"
                )
                fig1.update_layout(
                    xaxis_tickangle=45,
                    height=400
                )
                st.plotly_chart(fig1, use_container_width=True)
                
                # 2. 搜索量与竞争度散点图
                fig2 = px.scatter(
                    recommended_df,
                    x="搜索量",
                    y="竞争度",
                    size="预估点击价格",
                    color="相关度",
                    hover_name="关键词",
                    title="搜索量与竞争度分析"
                )
                st.plotly_chart(fig2, use_container_width=True)
                
                # 3. 关键词特征雷达图
                # 为每个关键词生成多维特征
                features = ["相关度", "搜索潜力", "转化价值", "竞争难度", "投资回报"]
                radar_data = pd.DataFrame({
                    "关键词": recommended_df["关键词"][:5],  # 只取前5个关键词避免图表过于复杂
                    **{feature: np.random.uniform(0, 100, 5) for feature in features}
                })
                
                fig3 = go.Figure()
                for idx, row in radar_data.iterrows():
                    fig3.add_trace(go.Scatterpolar(
                        r=row[features].values,
                        theta=features,
                        fill='toself',
                        name=row['关键词']
                    ))
                
                fig3.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                    showlegend=True,
                    title="关键词特征分析"
                )
                st.plotly_chart(fig3, use_container_width=True)
                
                # 4. 预估效果趋势
                dates = pd.date_range(start='2024-01-01', end='2024-03-31', freq='D')
                trend_data = pd.DataFrame({
                    '日期': dates,
                    '预估流量': np.random.randint(100, 1000, len(dates)),
                    '预估转化': np.random.randint(10, 100, len(dates))
                })
                
                fig4 = px.line(
                    trend_data,
                    x='日期',
                    y=['预估流量', '预估转化'],
                    title="关键词效果预估趋势"
                )
                st.plotly_chart(fig4, use_container_width=True)

    elif page == "数据报告":
        st.header("数据分析与报告")
        
        # 报告类型选择
        report_type = st.selectbox(
            "报告类型",
            ["实时监控", "周报", "月报", "竞品分析", "自定义报告"]
        )
        
        # 核心指标展示
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                label="平均排名",
                value="5.2",
                delta="-0.8"
            )
        with col2:
            st.metric(
                label="整体流量",
                value="12,345",
                delta="15%"
            )
        with col3:
            st.metric(
                label="转化率",
                value="3.4%",
                delta="0.5%"
            )
            
        # 添加详细报告内容
        tabs = st.tabs(["流量分析", "转化分析", "竞品分析", "投放建议"])
        
        with tabs[0]:
            st.markdown("### 流量分析")
            
            # 1. 流量来源分布（改用堆积柱状图）
            st.markdown("#### 流量来源分布")
            # 准备按时间的流量来源数据
            dates = pd.date_range(start='2024-03-01', end='2024-03-07', freq='D')
            source_data = pd.DataFrame({
                '日期': dates.repeat(6),
                '来源': ['自然搜索', '付费搜索', '直接访问', '社交媒体', '邮件营销', '其他'] * len(dates),
                '流量': [
                    *np.random.randint(4000, 6000, len(dates)),  # 自然搜索
                    *np.random.randint(2000, 4000, len(dates)),  # 付费搜索
                    *np.random.randint(1000, 2000, len(dates)),  # 直接访问
                    *np.random.randint(500, 1000, len(dates)),   # 社交媒体
                    *np.random.randint(300, 700, len(dates)),    # 邮件营销
                    *np.random.randint(100, 300, len(dates))     # 其他
                ]
            })
            
            fig = px.bar(source_data, 
                        x='日期', 
                        y='流量',
                        color='来源',
                        title='流量来源分布趋势',
                        color_discrete_sequence=px.colors.qualitative.Set3)
            
            fig.update_layout(
                barmode='relative',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                yaxis_title='流量占比',
                xaxis_title='日期',
                legend_title='流量来源',
                title_x=0.5
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # 2. 流量落地页分布（改进可视化）
            st.markdown("#### 流量落地页分布")
            landing_data = pd.DataFrame({
                "页面": ["首页", "产品详情", "解决方案", "定价页", "文档中心"],
                "访问量": [8000, 5000, 3000, 2000, 1500],
                "跳出率": [0.25, 0.35, 0.4, 0.3, 0.45],
                "平均停留时间": ["2:30", "3:45", "1:50", "2:15", "4:20"]
            })
            
            # 创建两列布局
            col1, col2 = st.columns(2)
            
            with col1:
                # 访问量和跳出率对比图
                fig = make_subplots(specs=[[{"secondary_y": True}]])
                
                fig.add_trace(
                    go.Bar(
                        name="访问量",
                        x=landing_data["页面"],
                        y=landing_data["访问量"],
                        marker_color='rgb(158,202,225)'
                    ),
                    secondary_y=False
                )
                
                fig.add_trace(
                    go.Scatter(
                        name="跳出率",
                        x=landing_data["页面"],
                        y=landing_data["跳出率"],
                        mode='lines+markers',
                        marker_color='rgb(94,94,94)',
                        line=dict(color='rgb(94,94,94)')
                    ),
                    secondary_y=True
                )
                
                fig.update_layout(
                    title="页面访问量与跳出率",
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    title_x=0.5
                )
                
                fig.update_yaxes(title_text="访问量", secondary_y=False)
                fig.update_yaxes(title_text="跳出率", secondary_y=True)
                
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # 平均停留时间图
                time_in_seconds = [int(t.split(':')[0]) * 60 + int(t.split(':')[1]) for t in landing_data["平均停留时间"]]
                
                fig = go.Figure(data=[
                    go.Bar(
                        name="平均停留时间",
                        x=landing_data["页面"],
                        y=time_in_seconds,
                        text=[f"{t}" for t in landing_data["平均停留时间"]],
                        textposition='auto',
                        marker_color='rgb(142,202,230)'
                    )
                ])
                
                fig.update_layout(
                    title="页面平均停留时间",
                    yaxis_title="时间（秒）",
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    title_x=0.5
                )
                
                st.plotly_chart(fig, use_container_width=True)
            
            # 3. 流量转化路径（优化桑基图）
            st.markdown("#### 流量转化路径")
            fig = go.Figure(data=[go.Sankey(
                node = dict(
                    pad = 15,
                    thickness = 20,
                    line = dict(color = "rgba(0,0,0,0)", width = 0.5),
                    label = ["访问", "搜索", "浏览产品", "加入购物车", "注册", "购买"],
                    color = ["#FFB6C1", "#87CEEB", "#98FB98", "#DDA0DD", "#F0E68C", "#E6E6FA"]  # 柔和的配色方案
                ),
                link = dict(
                    source = [0, 0, 1, 1, 2, 2, 3, 4],
                    target = [1, 2, 3, 4, 4, 5, 5, 5],
                    value = [8000, 4000, 3000, 2000, 1500, 1000, 800, 500],
                    color = ["rgba(255,182,193,0.3)", "rgba(135,206,235,0.3)", 
                            "rgba(152,251,152,0.3)", "rgba(221,160,221,0.3)", 
                            "rgba(240,230,140,0.3)", "rgba(230,230,250,0.3)",
                            "rgba(255,182,193,0.3)", "rgba(135,206,235,0.3)"]  # 半透明的连接颜色
                )
            )])
            
            fig.update_layout(
                title_text="用户转化路径分析",
                font_size=12,
                height=400,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                title_x=0.5
            )
            
            st.plotly_chart(fig, use_container_width=True)

        with tabs[1]:
            st.markdown("### 转化分析")
            
            # 1. 转化漏斗
            st.markdown("#### 整体转化漏斗")
            funnel_data = pd.DataFrame({
                "阶段": ["访问", "点击", "注册", "购买"],
                "数量": [10000, 5000, 1000, 200]
            })
            fig = go.Figure(go.Funnel(y=funnel_data["阶段"], x=funnel_data["数量"]))
            st.plotly_chart(fig, use_container_width=True)
            
            # 2. 产品转化分布
            st.markdown("#### 产品转化分布")
            product_data = pd.DataFrame({
                "产品": ["ECS云服务器", "OSS对象存储", "RDS云数据库", "CDN", "负载均衡", 
                        "云监控", "容器服务", "弹性公网IP", "NAT网关", "SSL证书"],
                "销量": np.random.randint(100, 1000, 10),
                "收入": np.random.randint(10000, 100000, 10),
                "同比增长": np.random.uniform(-0.3, 0.5, 10)
            })
            
            # 产品销量对比
            fig = px.bar(product_data, x="产品", y="销量", 
                        text=product_data["销量"].apply(str),
                        title="各产品销量分布")
            fig.update_layout(xaxis_tickangle=45)
            st.plotly_chart(fig, use_container_width=True)
            
            # 产品收入热力图
            product_channel = pd.DataFrame(
                np.random.randint(1000, 10000, size=(10, 4)),
                columns=["自然搜索", "付费搜索", "直接访问", "其他"],
                index=product_data["产品"]
            )
            fig = px.imshow(product_channel, 
                          title="产品-渠道收入分布",
                          aspect="auto")
            st.plotly_chart(fig, use_container_width=True)
            
        with tabs[2]:
            st.markdown("### 竞品分析")
            
            # 1. 关键词覆盖对比
            st.markdown("#### 关键词覆盖对比")
            competitors = ["阿里云", "腾讯云", "华为云", "火山云"]
            coverage_data = pd.DataFrame({
                "品牌": competitors * 3,
                "关键词类型": ["产品词"] * 4 + ["品牌词"] * 4 + ["解决方案词"] * 4,
                "覆盖率": np.random.uniform(0.3, 0.9, 12)
            })
            fig = px.bar(coverage_data, x="品牌", y="覆盖率", color="关键词类型", 
                        barmode="group", title="关键词覆盖率对比")
            st.plotly_chart(fig, use_container_width=True)
            
            # 2. 多维度竞争力分析
            st.markdown("#### 多维度竞争力分析")
            metrics = ["搜索排名", "广告投放", "品牌知名度", "产品完整度", "价格优势"]
            radar_data = pd.DataFrame({
                "指标": metrics * len(competitors),
                "品牌": [comp for comp in competitors for _ in metrics],
                "得分": np.random.uniform(60, 100, len(metrics) * len(competitors))
            })
            fig = px.line_polar(radar_data, r="得分", theta="指标", color="品牌", 
                              line_close=True, title="竞争力雷达图")
            st.plotly_chart(fig, use_container_width=True)
            
        with tabs[3]:
            st.markdown("### 投放建议")
            
            # 场景选择
            scenario = st.selectbox(
                "选择分析场景",
                ["整体优化建议", "预算分配建议", "竞价策略建议", "创意优化建议"]
            )
            
            # 总结性建议
            st.markdown("#### 核心建议")
            if scenario == "整体优化建议":
                st.info("""
                ### 核心发现
                1. 当前广告投放ROI为2.8，高于行业平均水平
                2. 长尾关键词的转化率比核心词高出35%
                3. 移动端流量占比达70%，但转化率低于PC端
                
                ### 优化建议
                1. 建议增加长尾词的投放预算，预计可提升ROI 15%
                2. 优化移动端转化路径，重点优化产品详情页
                3. 调整投放时段，将预算集中在转化率高的时段
                
                ### 预期效果
                - 预计可提升整体转化率20%
                - 预计可降低获客成本15%
                - 预计可提升ROI至3.2以上
                """)
                
                # 数据支撑
                col1, col2 = st.columns(2)
                with col1:
                    # ROI趋势
                    dates = pd.date_range(start='2024-01-01', end='2024-03-31', freq='D')
                    roi_data = pd.DataFrame({
                        '日期': dates,
                        'ROI': np.random.uniform(2.5, 3.5, len(dates))
                    })
                    fig = px.line(roi_data, x='日期', y='ROI', title='ROI趋势分析')
                    st.plotly_chart(fig, use_container_width=True)
                
                with col2:
                    # 长尾词vs核心词对比
                    keyword_type_data = pd.DataFrame({
                        '指标': ['展现量', '点击率', '转化率', '获客成本'],
                        '长尾词': [15000, 0.035, 0.028, 35],
                        '核心词': [50000, 0.025, 0.018, 55]
                    })
                    fig = go.Figure(data=[
                        go.Bar(name='长尾词', x=keyword_type_data['指标'], y=keyword_type_data['长尾词']),
                        go.Bar(name='核心词', x=keyword_type_data['指标'], y=keyword_type_data['核心词'])
                    ])
                    fig.update_layout(title='长尾词vs核心词效果对比', barmode='group')
                    st.plotly_chart(fig, use_container_width=True)
                
                # 时段转化率热力图
                hours = list(range(24))
                days = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
                conversion_matrix = np.random.uniform(0.01, 0.05, (len(days), len(hours)))
                fig = px.imshow(conversion_matrix,
                              labels=dict(x="小时", y="星期", color="转化率"),
                              x=hours,
                              y=days,
                              title="时段转化率分布")
                st.plotly_chart(fig, use_container_width=True)

            elif scenario == "预算分配建议":
                st.info("""
                ### 核心发现
                1. 当前预算分配过于集中在核心词，占比达75%，导致长尾词机会流失
                2. 部分长尾词ROI超过5.0，但预算投入不足
                3. 不同时段转化效果差异显著，最高时段是最低时段的3倍
                4. 移动端流量占比70%，但预算分配仅占40%
                5. 部分高ROI词组预算用尽，错失转化机会
                
                ### 优化建议
                1. 预算结构优化
                   - 核心词预算占比由75%降至60%
                   - 长尾词预算占比由20%提升至30%
                   - 新词测试预算保持10%不变
                
                2. 分时段预算调整
                   - 工作日9-11点、14-17点预算提升30%
                   - 周末13-15点、19-22点预算提升20%
                   - 低效时段（凌晨3-6点）暂停投放
                
                3. 设备预算优化
                   - 移动端预算占比提升至65%
                   - PC端预算向高转化率时段倾斜
                
                4. 智能放量策略
                   - 对ROI>4的词组取消预算上限
                   - 新词测试周期缩短为3天
                   - 引入智能竞价，动态调整预算
                
                ### 预期效果
                1. 效率提升
                   - 整体ROI提升25%
                   - 获客成本降低20%
                   - 预算利用率提升30%
                
                2. 流量质量
                   - 有效流量提升35%
                   - 转化率提升15%
                   - 无效点击减少25%
                
                3. 长期收益
                   - 新词储备增加200个
                   - 长尾词贡献提升40%
                   - 品牌词成本降低15%
                """)

            elif scenario == "竞价策略建议":
                st.info("""
                ### 核心发现
                1. 竞价效率问题
                   - 30%关键词出价过高，ROI低于行业均值
                   - 15%高潜力词排名不足第3位
                   - 竞争对手在核心词上出价高出20-30%
                
                2. 排名分布问题
                   - 核心词组排名波动较大
                   - 品牌词排名存在被竞争对手干扰
                   - 长尾词排名普遍不足
                
                3. 质量度问题
                   - 25%关键词质量度低于6分
                   - 创意相关性评分普遍偏低
                   - 落地页体验分数有提升空间
                
                ### 优化建议
                1. 分层竞价策略
                   - 核心产品词：保持前3位排名
                   - 品牌词：保持首位排名
                   - 长尾词：控制在4-8位
                   - 测试词：控制成本优先
                
                2. 智能调价方案
                   - 高ROI词组：提升出价10-20%
                   - 低效词组：降低出价20-30%
                   - 新词测试：设置最高出价上限
                
                3. 竞争策略调整
                   - 避开竞争对手高峰时段
                   - 差异化出价策略
                   - 关注竞争对手动态
                
                4. 质量度优化
                   - 优化创意相关性
                   - 改善落地页体验
                   - 提升点击率
                
                ### 预期效果
                1. 排名效果
                   - 核心词平均排名提升2位
                   - 品牌词稳定保持首位
                   - 长尾词排名提升3-5位
                
                2. 成本控制
                   - 整体CPC降低15%
                   - 优质流量成本降低20%
                   - 预算使用效率提升25%
                
                3. 质量提升
                   - 平均质量度提升2分
                   - 创意相关性提升30%
                   - 无效点击减少20%
                """)

            elif scenario == "创意优化建议":
                st.info("""
                ### 核心发现
                1. 创意表现问题
                   - 创意文案点击率差异达300%
                   - 高展现量创意转化率低
                   - 移动端创意表现低于PC端
                   - 创意素材同质化严重
                
                2. 设备分布问题
                   - 移动端占比70%但效果不佳
                   - PC端创意与移动端未差异化
                   - 不同设备用户行为差异大
                
                3. 素材效果问题
                   - 主图点击率普遍偏低
                   - 创意文案缺乏卖点
                   - A/B测试覆盖率不足
                
                ### 优化建议
                1. 创意结构优化
                   - 突出核心卖点和优势
                   - 强化品牌信任背书
                   - 加入行业热点元素
                   - 突出性价比优势
                
                2. 差异化策略
                   - PC端：详细技术参数
                   - 移动端：简洁直观展示
                   - 新客户：突出优惠力度
                   - 老客户：突出升级价值
                
                3. 测试与优化
                   - 扩大A/B测试覆盖
                   - 建立创意迭代机制
                   - 引入竞品创意分析
                   - 建立创意素材库
                
                4. 展现策略
                   - 基于时段调整创意
                   - 根据用户特征匹配
                   - 动态创意优化
                   - 智能轮换机制
                
                ### 预期效果
                1. 效率提效
                   - 点击率提升15%
                   - 转化率提升20%
                   - 创意质量度提升25%
                
                2. 成本优化
                   - 点击成本降低10%
                   - 获客成本降低15%
                   - 创意制作效率提升30%
                
                3. 长期价值
                   - 品牌认知度提升
                   - 用户体验改善
                   - 创意资产积累
                """)

    # 页面底部
    st.markdown("---")
    st.markdown("© 2024 阿里云 SEO/SEM 关键词管理系统")

if __name__ == '__main__':
    main()