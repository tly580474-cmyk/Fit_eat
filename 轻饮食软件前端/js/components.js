/**
 * 轻饮食 - 可复用组件
 */

/**
 * 环形进度图组件
 */
const RingProgress = {
  /**
   * 渲染环形进度图
   * @param {Object} options - 配置选项
   * @returns {string} HTML字符串
   */
  render(options = {}) {
    const {
      size = 200,
      strokeWidth = 12,
      progress = 0,
      color = '#006e1c',
      bgColor = '#e2e2e2',
      label = '',
      sublabel = '',
      showCenter = true
    } = options;

    const radius = (size - strokeWidth) / 2;
    const circumference = 2 * Math.PI * radius;
    const offset = circumference - (progress / 100) * circumference;

    return `
      <div class="relative inline-flex items-center justify-center" style="width: ${size}px; height: ${size}px;">
        <svg class="ring-progress" width="${size}" height="${size}">
          <circle cx="${size/2}" cy="${size/2}" r="${radius}"
                  fill="none" stroke="${bgColor}" stroke-width="${strokeWidth}" />
          <circle cx="${size/2}" cy="${size/2}" r="${radius}"
                  fill="none" stroke="${color}" stroke-width="${strokeWidth}"
                  stroke-dasharray="${circumference}"
                  stroke-dashoffset="${offset}"
                  stroke-linecap="round"
                  style="transition: stroke-dashoffset 1s cubic-bezier(0.4, 0, 0.2, 1)" />
        </svg>
        ${showCenter ? `
          <div class="absolute inset-0 flex flex-col items-center justify-center">
            ${label ? `<span class="text-2xl font-bold text-gray-800">${label}</span>` : ''}
            ${sublabel ? `<span class="text-xs text-gray-500 mt-1">${sublabel}</span>` : ''}
          </div>
        ` : ''}
      </div>
    `;
  }
};

/**
 * 柱状图组件
 */
const BarChart = {
  /**
   * 渲染柱状图
   * @param {Object} options - 配置选项
   * @returns {string} HTML字符串
   */
  render(options = {}) {
    const {
      data = [],
      height = 200,
      barColor = '#4caf50',
      activeBarColor = '#006e1c',
      showLabels = true,
      showValues = false,
      activeIndex = -1
    } = options;

    const maxValue = Math.max(...data.map(d => d.value));

    return `
      <div class="flex items-end justify-between" style="height: ${height}px">
        ${data.map((item, index) => {
          const barHeight = maxValue > 0 ? Math.max((item.value / maxValue) * 100, 4) : 4;
          const isActive = index === activeIndex;

          return `
            <div class="flex flex-col items-center gap-2 flex-1 group">
              ${showValues ? `
                <span class="text-xs font-medium text-gray-600 opacity-0 group-hover:opacity-100 transition-opacity">
                  ${item.value}
                </span>
              ` : ''}
              <div class="w-8 rounded-t-lg transition-all group-hover:opacity-80"
                   style="height: ${barHeight}%; background: ${isActive ? activeBarColor : barColor}">
              </div>
              ${showLabels ? `
                <span class="text-xs ${isActive ? 'text-green-700 font-bold' : 'text-gray-500'}">
                  ${item.label}
                </span>
              ` : ''}
            </div>
          `;
        }).join('')}
      </div>
    `;
  }
};

/**
 * 雷达图组件
 */
const RadarChart = {
  /**
   * 渲染雷达图
   * @param {Object} options - 配置选项
   * @returns {string} HTML字符串
   */
  render(options = {}) {
    const {
      data = {},
      size = 280,
      color = '#4caf50',
      bgColor = '#e2e2e2'
    } = options;

    const center = size / 2;
    const radius = size / 2 - 40;
    const labels = Object.keys(data);
    const values = Object.values(data);
    const angleStep = (2 * Math.PI) / labels.length;

    // 计算多边形点
    const points = values.map((value, i) => {
      const angle = i * angleStep - Math.PI / 2;
      const r = (value / 100) * radius;
      return `${center + r * Math.cos(angle)},${center + r * Math.sin(angle)}`;
    }).join(' ');

    // 网格线点
    const gridLevels = [0.2, 0.4, 0.6, 0.8, 1.0];
    const gridPolygons = gridLevels.map(level => {
      const gridPoints = labels.map((_, i) => {
        const angle = i * angleStep - Math.PI / 2;
        const r = level * radius;
        return `${center + r * Math.cos(angle)},${center + r * Math.sin(angle)}`;
      }).join(' ');
      return `<polygon points="${gridPoints}" fill="none" stroke="${bgColor}" stroke-width="1" />`;
    }).join('');

    // 轴线
    const axisLines = labels.map((_, i) => {
      const angle = i * angleStep - Math.PI / 2;
      return `<line x1="${center}" y1="${center}" x2="${center + radius * Math.cos(angle)}" y2="${center + radius * Math.sin(angle)}" stroke="${bgColor}" stroke-width="1" />`;
    }).join('');

    // 标签
    const labelElements = labels.map((label, i) => {
      const angle = i * angleStep - Math.PI / 2;
      const labelRadius = radius + 25;
      const x = center + labelRadius * Math.cos(angle);
      const y = center + labelRadius * Math.sin(angle);
      return `<text x="${x}" y="${y}" text-anchor="middle" dominant-baseline="middle" class="text-xs font-medium fill-gray-600">${label}</text>`;
    }).join('');

    return `
      <div class="flex items-center justify-center">
        <svg width="${size}" height="${size}" viewBox="0 0 ${size} ${size}">
          ${gridPolygons}
          ${axisLines}
          <polygon points="${points}" fill="${color}" fill-opacity="0.2" stroke="${color}" stroke-width="2" />
          ${values.map((value, i) => {
            const angle = i * angleStep - Math.PI / 2;
            const r = (value / 100) * radius;
            return `<circle cx="${center + r * Math.cos(angle)}" cy="${center + r * Math.sin(angle)}" r="4" fill="${color}" />`;
          }).join('')}
          ${labelElements}
        </svg>
      </div>
    `;
  }
};

/**
 * 进度条组件
 */
const ProgressBar = {
  /**
   * 渲染进度条
   * @param {Object} options - 配置选项
   * @returns {string} HTML字符串
   */
  render(options = {}) {
    const {
      current = 0,
      target = 100,
      color = '#006e1c',
      height = 8,
      showLabel = true,
      label = '',
      unit = ''
    } = options;

    const progress = Math.min((current / target) * 100, 100);

    return `
      <div>
        ${showLabel || label ? `
          <div class="flex justify-between items-center mb-2">
            <span class="text-sm font-medium text-gray-700">${label}</span>
            <span class="text-sm text-gray-500">${current}${unit} / ${target}${unit}</span>
          </div>
        ` : ''}
        <div class="progress-bar" style="height: ${height}px">
          <div class="progress-bar-fill" style="width: ${progress}%; background: ${color}"></div>
        </div>
      </div>
    `;
  }
};

/**
 * 日期选择器组件
 */
const DatePicker = {
  /**
   * 渲染横向日期选择器
   * @param {Object} options - 配置选项
   * @returns {string} HTML字符串
   */
  render(options = {}) {
    const {
      days = [],
      activeIndex = 0,
      onSelect = ''
    } = options;

    return `
      <div class="horizontal-scroll py-2">
        ${days.map((day, index) => `
          <button class="flex-shrink-0 w-14 py-3 rounded-xl flex flex-col items-center justify-center transition-all ${
            index === activeIndex
              ? 'bg-green-600 text-white shadow-md shadow-green-200'
              : 'bg-white text-gray-600 hover:bg-gray-50'
          }" onclick="${onSelect}(${index})">
            <span class="text-xs opacity-70">${day.weekday}</span>
            <span class="text-lg font-bold">${day.date}</span>
          </button>
        `).join('')}
      </div>
    `;
  }
};

/**
 * 食谱卡片组件
 */
const MealCard = {
  /**
   * 渲染餐单卡片
   * @param {Object} options - 配置选项
   * @returns {string} HTML字符串
   */
  render(options = {}) {
    const {
      image = '',
      name = '',
      calories = 0,
      protein = 0,
      type = '',
      tags = [],
      onClick = ''
    } = options;

    const typeColors = {
      breakfast: 'bg-orange-500',
      lunch: 'bg-green-600',
      dinner: 'bg-blue-500',
      snack: 'bg-gray-500'
    };

    const typeNames = {
      breakfast: '早餐',
      lunch: '午餐',
      dinner: '晚餐',
      snack: '加餐'
    };

    return `
      <div class="min-w-[260px] lg:min-w-0 snap-start cursor-pointer group" onclick="${onClick}">
        <div class="relative h-48 rounded-2xl overflow-hidden shadow-lg transition-transform active:scale-[0.98]">
          <img src="${image}" alt="${name}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
               onerror="this.src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNjAiIGhlaWdodD0iMTkyIiB2aWV3Qm94PSIwMCAwIDI2MCAxOTIiPjxyZWN0IHdpZHRoPSIyNjAiIGhlaWdodD0iMTkyIiBmaWxsPSIjZTJlMmUyIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtc2l6ZT0iMTQiIGZpbGw9IiM2ZjdhNmIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGR5PSIuM2VtIj7pmL4g6YOo5paH5Lu2PC90ZXh0Pjwvc3ZnPg=='">
          <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent"></div>
          <div class="absolute bottom-4 left-4 right-4 text-white">
            <span class="${typeColors[type] || 'bg-gray-500'} px-2 py-0.5 rounded text-xs font-bold uppercase mb-1 inline-block">
              ${typeNames[type] || type}
            </span>
            <h3 class="font-bold text-lg">${name}</h3>
            <div class="flex items-center gap-3 mt-1 opacity-90">
              <span class="flex items-center gap-1 text-sm">
                <span class="material-symbols-outlined text-sm">bolt</span>
                ${calories} kcal
              </span>
              ${protein ? `
                <span class="text-sm">蛋白 ${protein}g</span>
              ` : ''}
            </div>
          </div>
        </div>
      </div>
    `;
  }
};

/**
 * 社区动态卡片组件
 */
const PostCard = {
  /**
   * 渲染动态卡片
   * @param {Object} options - 配置选项
   * @returns {string} HTML字符串
   */
  render(options = {}) {
    const {
      user = {},
      content = '',
      image = '',
      likes = 0,
      comments = 0,
      time = '',
      location = '',
      onLike = '',
      onComment = '',
      onShare = ''
    } = options;

    return `
      <article class="bg-white rounded-xl overflow-hidden shadow-sm transition-transform active:scale-[0.99]">
        <div class="p-4 flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-full overflow-hidden bg-gray-100">
              <img src="${user.avatar}" alt="${user.name}" class="w-full h-full object-cover"
                   onerror="this.src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCIgdmlld0JveD0iMCAwIDQwIDQwIj48cmVjdCB3aWR0aD0iNDAiIGhlaWdodD0iNDAiIGZpbGw9IiNlMmUyZTIiLz48dGV4dCB4PSI1MCUiIHk9IjUwJSIgZm9udC1zaXplPSIxNiIgZmlsbD0iIzZmN2E2YiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPlU8L3RleHQ+PC9zdmc+'">
            </div>
            <div>
              <p class="font-bold text-sm">${user.name}</p>
              <p class="text-xs text-gray-500">${time}${location ? ` · ${location}` : ''}</p>
            </div>
          </div>
          <button class="text-green-600 text-sm font-bold">+ 关注</button>
        </div>

        ${image ? `
          <div class="aspect-square w-full bg-gray-100">
            <img src="${image}" alt="" class="w-full h-full object-cover"
                 onerror="this.src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MDAiIGhlaWdodD0iNDAiIHZpZXdCb3g9IjAgMCA0MDAgNDAwIj48cmVjdCB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQwMCIgZmlsbD0iI2UyZTJlMiIvPjx0ZXh0IHg9IjUwJSIgeT0iNTAlIiBmb250LXNpemU9IjE4IiBmaWxsPSIjNmY3YTZiIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBkeT0iLjNlbSI+6Zm254mH5Zu+54mHPC90ZXh0Pjwvc3ZnPg=='">
          </div>
        ` : ''}

        <div class="p-4 space-y-3">
          <p class="text-sm leading-relaxed">${content}</p>
          <div class="flex items-center gap-4 pt-2">
            <button class="flex items-center gap-1 text-gray-500 hover:text-green-600 transition-colors" onclick="${onLike}">
              <span class="material-symbols-outlined text-xl">favorite</span>
              <span class="text-sm">${Utils.formatNumber(likes)}</span>
            </button>
            <button class="flex items-center gap-1 text-gray-500 hover:text-green-600 transition-colors" onclick="${onComment}">
              <span class="material-symbols-outlined text-xl">chat_bubble</span>
              <span class="text-sm">${comments}</span>
            </button>
            <button class="flex items-center gap-1 text-gray-500 hover:text-green-600 transition-colors ml-auto" onclick="${onShare}">
              <span class="material-symbols-outlined text-xl">share</span>
            </button>
          </div>
        </div>
      </article>
    `;
  }
};

/**
 * 成就徽章组件
 */
const AchievementBadge = {
  /**
   * 渲染成就徽章
   * @param {Object} options - 配置选项
   * @returns {string} HTML字符串
   */
  render(options = {}) {
    const {
      icon = 'star',
      name = '',
      desc = '',
      unlocked = false,
      color = 'green'
    } = options;

    const colors = {
      green: 'bg-green-100 text-green-600',
      orange: 'bg-orange-100 text-orange-600',
      blue: 'bg-blue-100 text-blue-600',
      purple: 'bg-purple-100 text-purple-600'
    };

    return `
      <div class="flex flex-col items-center gap-2 ${unlocked ? '' : 'opacity-30 grayscale'}">
        <div class="w-16 h-16 rounded-full ${unlocked ? colors[color] : 'bg-gray-200 text-gray-400'} flex items-center justify-center">
          <span class="material-symbols-outlined text-3xl ${unlocked ? 'filled' : ''}">${icon}</span>
        </div>
        <span class="text-xs font-medium text-gray-600">${name}</span>
        ${desc ? `<span class="text-[10px] text-gray-400">${desc}</span>` : ''}
      </div>
    `;
  }
};

/**
 * 营养数据卡片组件
 */
const NutritionCard = {
  /**
   * 渲染营养数据卡片
   * @param {Object} options - 配置选项
   * @returns {string} HTML字符串
   */
  render(options = {}) {
    const {
      label = '',
      value = 0,
      target = 100,
      unit = 'g',
      color = '#006e1c',
      icon = ''
    } = options;

    const progress = Math.min((value / target) * 100, 100);

    return `
      <div class="bg-white rounded-2xl p-4 border border-gray-100">
        <div class="flex justify-between items-center mb-3">
          <div class="flex items-center gap-2">
            <span class="w-2 h-6 rounded-full" style="background: ${color}"></span>
            <span class="font-medium">${label}</span>
          </div>
          <span class="text-sm text-gray-500">${value}${unit} / ${target}${unit}</span>
        </div>
        <div class="h-2 bg-gray-100 rounded-full overflow-hidden">
          <div class="h-full rounded-full transition-all duration-600" style="width: ${progress}%; background: ${color}"></div>
        </div>
      </div>
    `;
  }
};

// 导出组件
window.Components.RingProgress = RingProgress;
window.Components.BarChart = BarChart;
window.Components.RadarChart = RadarChart;
window.Components.ProgressBar = ProgressBar;
window.Components.DatePicker = DatePicker;
window.Components.MealCard = MealCard;
window.Components.PostCard = PostCard;
window.Components.AchievementBadge = AchievementBadge;
window.Components.NutritionCard = NutritionCard;
