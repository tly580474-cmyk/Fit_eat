---
name: 轻食刻 Fresh & Vitality
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#3f4a3c'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#6f7a6b'
  outline-variant: '#becab9'
  surface-tint: '#006e1c'
  primary: '#006e1c'
  on-primary: '#ffffff'
  primary-container: '#4caf50'
  on-primary-container: '#003c0b'
  inverse-primary: '#78dc77'
  secondary: '#8b5000'
  on-secondary: '#ffffff'
  secondary-container: '#ff9800'
  on-secondary-container: '#653900'
  tertiary: '#556158'
  on-tertiary: '#ffffff'
  tertiary-container: '#929e94'
  on-tertiary-container: '#2a352d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#94f990'
  primary-fixed-dim: '#78dc77'
  on-primary-fixed: '#002204'
  on-primary-fixed-variant: '#005313'
  secondary-fixed: '#ffdcbe'
  secondary-fixed-dim: '#ffb870'
  on-secondary-fixed: '#2c1600'
  on-secondary-fixed-variant: '#693c00'
  tertiary-fixed: '#d9e6da'
  tertiary-fixed-dim: '#bdcabe'
  on-tertiary-fixed: '#131e17'
  on-tertiary-fixed-variant: '#3e4a41'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 30px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.5px
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 26px
    fontWeight: '700'
    lineHeight: 34px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  container-margin: 1.25rem
  gutter-base: 1rem
  stack-sm: 0.5rem
  stack-md: 1rem
  stack-lg: 1.5rem
  card-padding: 1rem
---

## 品牌与风格

本设计系统以"轻食刻"（Fresh & Vitality）为核心叙事，专为注重健康、追求清晰与动力的用户量身打造。整体风格亲切、积极、干净，弥合了临床营养工具与活力生活方式之间的差距。

美学上融合了**现代极简主义**与**柔和触感**元素。优先使用高质量食物摄影和充足的留白，以降低膳食规划时的认知负担。用户应感受到"轻松健康"的体验——饮食追踪应像均衡生活的自然延伸，而非负担。视觉重心由卡片和鲜活的数据可视化承载，确保中文排版在界面中保持清晰、醒目。

## 色彩体系

色彩灵感源于自然与活力。

- **主色·绿（#006e1c）：** 代表成长、健康与新鲜食材。用于主要操作按钮、进度指示器及"成功"状态。
- **辅色·橙（#8b5000）：** 象征代谢能量与食欲。少量用于高亮、警告或"活跃"状态（如运动按钮），为绿色提供温暖对比。
- **中性·奶油（#f9f9f9）：** 主背景色。比纯白更柔和、更有质感，减少夜间记录饮食时的视觉疲劳。
- **点缀·薄荷（#e2e2e2）：** 用于大面积表面区域（如卡片背景、标签容器），营造层次分明的"色调"效果，避免高对比度。

## 字体规范

设计系统采用 **Plus Jakarta Sans**，其圆润的字形末端与柔和的 UI 形态相得益彰。中文字符默认使用系统高质量无衬线字体（苹方或思源黑体），确保各字重下的最大可读性。

字体层级清晰：

- **标题：** 粗体且富有表现力，用于食谱名称和每日摘要。
- **正文：** 中文文本使用充足行高（1.5 倍），防止文字过于密集，确保食材清单和烹饪说明易于浏览。
- **数据标签：** 用于营养成分（热量、宏量营养素）；通常使用略重的字重，使数字更加突出。

## 布局与间距

设计系统遵循**移动优先、固定-流式**混合模型。移动端使用 1.25rem（20px）侧边距，为卡片式布局提供呼吸空间。

布局逻辑：

- **垂直节奏：** 内容遵循严格的 4px/8px 基线网格，保持元素对齐。
- **卡片间距：** 卡片内部元素使用 1rem（16px）间距。
- **板块分隔：** 不同内容区块（如"早餐"与"午餐"）之间使用 1.5rem（24px）间距，清晰标示每日时间线的过渡。
- **安全区域：** 底部导航栏和浮动操作按钮（FAB）的"记录饮食"需考虑设备特定的主页指示器区域。

## 阴影与层次

深度效果通过**色调分层**和**环境阴影**实现。系统不使用生硬的黑色阴影，而是采用带有主色调的"柔焦"阴影，保持"清新"观感。

- **层级 0（背景）：** 柔和的奶油色（#f9f9f9）底色。
- **层级 1（卡片）：** 通过 10% 透明度的主绿色阴影（0px 4px 20px）提升，使食谱卡片感觉从背景中"浮起"。
- **层级 2（交互）：** 浮动按钮或活跃选中状态使用更明显的阴影，引导用户交互。
- **遮罩层：** 使用 40% 背景模糊（毛玻璃效果）作为模态框背景，在聚焦特定任务（如添加食材）的同时保持上下文。

## 形状语言

形状语言整体偏**圆润与有机**。

- **标准卡片：** 使用 1rem（16px）圆角，营造亲切、现代的感觉。
- **特色卡片：** 大型主视觉卡片（如"每日目标"）可使用 1.5rem（24px）圆角，柔化视觉冲击。
- **按钮与标签：** 遵循"半胶囊"风格，最小圆角 0.5rem（8px），确保触感柔软、"弹润"，除非是纯图标浮动按钮，否则不使用完全圆形。
- **图片：** 食物摄影的圆角应始终与容器卡片保持一致，维护整体协调感。

## 组件定义

- **食谱卡片：** 全宽图片，底部文字叠加。使用从暗到透明的渐变，确保在明亮食物照片上的文字可读性。
- **营养仪表盘：** 宏量营养素（蛋白质、碳水、脂肪）使用环形进度条，在奶油色背景上呈现高对比度色彩。
- **按钮：**
  - *主按钮：* 实底 #006e1c，白色文字，16px 圆角。
  - *辅按钮：* 描边 #006e1c 或实底 #8b5000，用于"消耗"或"能量"操作。
- **输入框：** 简洁、极简的字段，1px 边框在聚焦时加粗并变为主绿色。标签应始终保持在输入框上方可见。
- **时间线列表：** 用于每日体重追踪或饮食日志。使用竖向"主干"配合圆点指示器，展示一天中的进度。
- **标签：** 小巧的圆角指示器，用于饮食标签（如"素食"、"高蛋白"）。使用薄荷色背景搭配主绿色文字。
