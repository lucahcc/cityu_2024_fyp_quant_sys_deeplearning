# 量化交易系统与深度学习 | Quantitative Trading System with Deep Learning

![Language](https://img.shields.io/badge/Language-Python%203.11-blue)
![Framework](https://img.shields.io/badge/Framework-TensorFlow%2FKeras-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📋 项目概述 | Project Overview

本项目是一个**基于深度学习的智能量化交易系统**，融合了先进的神经网络架构与量化金融分析。通过多种深度学习模型预测金融资产价格，应用特征工程优化模型性能，并构建完整的交易回测框架。该系统演示了机器学习在金融时间序列预测中的应用，以及从数据获取、特征工程、模型训练到策略评估的完整工作流。

A comprehensive **intelligent quantitative trading system powered by deep learning**, integrating advanced neural network architectures with quantitative finance analysis. This system predicts financial asset prices using multiple deep learning models, optimizes model performance through feature engineering, and constructs a complete trading backtesting framework. It demonstrates the application of machine learning in financial time series forecasting and showcases a complete workflow from data acquisition, feature engineering, model training to strategy evaluation.

---

## 🎯 核心功能模块 | Core Functional Modules

### 1️⃣ 深度学习预测模型 | Deep Learning Prediction Models

#### **CNN+LSTM+Attention 架构 | Architecture**

**中文说明：**
- **模型架构**：卷积神经网络(CNN) + 双向长短期记忆网络(Bi-LSTM) + 注意力机制(Attention)
- **核心创新**：
  - 使用CNN捕捉时间序列的局部特征
  - MaxPooling降维处理高维数据
  - Bi-LSTM双向学习时间序列的长期依赖关系
  - 注意力机制自适应地权重不同时间步，增强预测精准度
- **应用场景**：实时黄金价格5分钟K线预测
- **模型参数**：83,137 (324.75 KB)
- **性能指标**：MSE损失函数监控，测试集实现显著预测精度

**English:**
- **Architecture**: Convolutional Neural Network (CNN) + Bidirectional LSTM (Bi-LSTM) + Attention Mechanism
- **Key Innovations**:
  - CNN captures local temporal features in time series
  - MaxPooling dimensionality reduction for high-dimensional data
  - Bi-LSTM learns long-term dependencies bidirectionally
  - Attention mechanism adaptively weights different timesteps, enhancing prediction accuracy
- **Application**: Real-time gold price 5-minute bar prediction
- **Total Parameters**: 83,137 (324.75 KB)
- **Performance**: Significant prediction accuracy on test dataset with optimized MSE loss

---

#### **Transformer 编码器 + 多头注意力 | Transformer Encoder + Multi-Head Attention**

**中文说明：**
- **模型架构**：采用Transformer编码器，融合多头注意力机制
- **创新亮点**：
  - 多头注意力机制(Multi-Head Attention)同时学习多个表示子空间
  - LayerNormalization确保训练稳定性
  - 完全并行化计算，相比RNN显著提升效率
- **优势**：更强的特征表示能力，更快的收敛速度
- **超参数配置**：600 epochs训练，MAE和MSE双重优化目标

**English:**
- **Architecture**: Transformer encoder with multi-head attention mechanism
- **Innovation Highlights**:
  - Multi-head attention learns multiple representation subspaces simultaneously
  - LayerNormalization ensures training stability
  - Fully parallelized computation significantly improves efficiency vs. RNN
- **Advantages**: Superior feature representation capability and faster convergence
- **Configuration**: 600 epochs training with dual MAE and MSE optimization objectives

---

#### **LSTM 基础模型 | LSTM Base Model**

- **中文**：PCA降维处理高维特征空间，TensorFlow原生实现，完整的数据预处理流程，支持多步时间序列预测
- **English**: PCA dimensionality reduction for high-dimensional feature spaces, native TensorFlow implementation with complete data preprocessing pipeline, supports multi-step time series forecasting

---

### 2️⃣ 智能特征工程模块 | Intelligent Feature Engineering Module

**项目路径 | Path**: `feature_selecter_lightgbm/`

#### **多维度特征筛选框架 | Multi-Dimensional Feature Selection Framework**

**中文说明：** 实现了企业级的特征选择工具类，包含5大特征选择方法

**English:** Enterprise-grade feature selection toolkit implementing 5 major methods

**📊 方法对比 | Method Comparison**

| 方法 / Method | 原理 / Principle | 适用场景 / Use Case | 优势 / Advantage |
|------|------|--------|------|
| **相关性分析 / Correlation Analysis** | Pearson相关系数 > 阈值 | 去除多重共线性 | 快速、可解释强 |
| **LightGBM特征重要性 / LightGBM Importance** | 基于梯度提升的特征贡献度 | 非线性关系识别 | 精准、处理复杂交互 |
| **单变量过滤 / SelectKBest** | 统计检验(卡方、F检验等) | 回归/分类任务 | 简单高效 |
| **递归特征消除 / RFE** | 递归训练模型去除不重要特征 | 保留顶级特征子集 | 考虑特征交互 |
| **PCA降维 / PCA** | 主成分分析 | 高维数据压缩 | 无信息损失的降维 |

#### **数据预处理管道 | Data Preprocessing Pipeline**

**中文：**
- **异常值处理**：基于分位数的Winsorize方法(保留5%-95%)
- **特征标准化**：Z-score标准化提升模型稳定性
- **缺失值处理**：智能填充与异常检测

**English:**
- **Outlier Handling**: Winsorize method based on quantiles (retain 5%-95%)
- **Feature Standardization**: Z-score normalization for model stability
- **Missing Value Treatment**: Intelligent imputation with anomaly detection

#### **可视化分析 | Visualization Analysis**
- 相关性热力图 / Correlation heatmaps
- 特征重要度条形图 / Feature importance bar charts
- 选择结果导出(Excel格式) / Results export in Excel format

---

### 3️⃣ 量化交易回测系统 | Quantitative Trading Backtesting System

**项目路径 | Path**: `trading system/`

#### **核心功能 | Core Capabilities**

**📈 数据获取与处理 | Data Acquisition & Processing**
- 支持多数据源：yfinance API、本地CSV文件 / Multi-source support: yfinance API, local CSV files
- 灵活的股票代码配置(纳斯达克100成分股列表) / Flexible ticker configuration (Nasdaq 100 constituents)
- K线重采样：支持5分钟、1小时、1天等多时间粒度 / K-line resampling: 5-min, hourly, daily and other timeframes

**🎲 策略执行框架 | Strategy Execution Framework**
- 面向对象的策略设计框架 / Object-oriented strategy design pattern
- 实时信号生成与执行 / Real-time signal generation and execution
- 支持多策略组合与参数优化 / Multi-strategy combination and parameter optimization support

**📊 回测与风险分析 | Backtesting & Risk Analysis**
- 历史数据完整回测 / Historical data comprehensive backtesting
- 损益(PnL)计算与可视化 / Profit & Loss (PnL) calculation and visualization
- 风险指标评估(Sharpe比率、最大回撤等) / Risk metric evaluation (Sharpe ratio, maximum drawdown, etc.)
- 交易可视化：价格走势 + 买卖信号 / Trade visualization: price trends + buy/sell signals

**🔧 高级特性 | Advanced Features**
- 支持单/多股票交易 / Single and multi-stock trading support
- 灵活的进场/出场条件 / Flexible entry/exit conditions
- 交易成本模拟(佣金、滑点) / Trading cost simulation (commissions, slippage)

---

## 📊 关键技术指标 | Key Technical Metrics

| 维度 / Dimension | 详情 / Details |
|------|------|
| **模型参数 / Model Parameters** | CNN: 64个过滤器 / 64 filters; Bi-LSTM: 128隐层 / 128 hidden units; 注意力 / Attention: 16,512参数 / params |
| **训练规模 / Training Scale** | 37,312训练样本 / training samples; 15,988测试样本 / test samples |
| **序列长度 / Sequence Length** | 5步时间序列 / 5-step time series (5 timesteps) |
| **输入维度 / Input Dimension** | 6维特征 / 6 features (OHLCV+技术指标 / technical indicators) |
| **批处理大小 / Batch Size** | 256 |
| **训练轮次 / Training Epochs** | 60-600 |
| **优化器 / Optimizer** | Adam(学习率 / learning rate: 1e-4) |
| **损失函数 / Loss Function** | 均方误差 / Mean Squared Error (MSE) |

---

## 🔧 技术栈 | Technology Stack

### 深度学习框架 | Deep Learning Frameworks
- **TensorFlow/Keras** - 神经网络构建与训练 / Neural network construction and training
- **NumPy/Pandas** - 数据处理与分析 / Data processing and analysis

### 机器学习库 | Machine Learning Libraries
- **LightGBM** - 梯度提升与特征重要性 / Gradient boosting and feature importance
- **Scikit-learn** - 特征选择、PCA、数据预处理 / Feature selection, PCA, data preprocessing

### 金融数据 | Financial Data Sources
- **yfinance** - 股票数据API / Stock market data API
- **jqdatasdk** - 中国A股/贵金属数据 / Chinese A-shares and precious metals data

### 可视化 | Visualization
- **Matplotlib/Seaborn** - 静态图表 / Static charts
- **Plotly** - 交互式可视化 / Interactive visualization

### 开发环境 | Development Environment
- **Jupyter Notebook** - 交互式开发与文档 / Interactive development and documentation
- **Python 3.11** - 编程语言 / Programming language

---

## 📁 项目结构 | Project Structure

```
quantitative_trading_system/
├── CNN+LSTM+Attention Mechanism to predict closing price.ipynb
│   └── 用于黄金价格5分钟预测的混合架构 / Hybrid architecture for 5-min gold price prediction
├── Transformer encoder (multi-attention) predicts gold closing prices.ipynb
│   └── Transformer编码器+多头注意力，600轮训练 / Transformer encoder + multi-head attention, 600 epochs training
├── LSTM.ipynb
│   └── 基础LSTM模型，采用PCA降维 / Baseline LSTM model with PCA dimensionality reduction
├── cnn_lstm_code.ipynb
│   └── CNN+LSTM完整实现示例 / Complete CNN+LSTM implementation example
├── feature_selecter_lightgbm/
│   ├── feature_selection.ipynb          [特征选择主程序 / Main program]
│   ├── feature_selector.py              [FeatureSelector类 / Class]
│   ├── technical_analysis.py            [技术指标计算 / Technical indicator calculation]
│   ├── selected_columns_data_*.csv      [筛选后的特征集 / Filtered feature sets]
│   └── heatmap.png                      [相关性可视化 / Correlation visualization]
├── trading system/
│   ├── trading_system.ipynb             [交易系统主程序 / Main program]
│   ├── stock_strategy_pnl.png           [收益曲线 / Profit curve visualization]
│   └── *_price.csv                      [多股票价格数据 / Multi-stock price data]
└── gold_data.csv                        [原始黄金5分钟K线数据 / Raw 5-min gold bar data]
```

---

## 🚀 核心成就与亮点 | Core Achievements & Highlights

✨ **算法创新 | Algorithm Innovation**
- 自主设计CNN+LSTM+Attention混合架构，融合卷积特征提取、循环序列建模、注意力权重机制三大创新 / Custom-designed CNN+LSTM+Attention hybrid architecture combining convolutional feature extraction, recurrent sequence modeling, and attention weighting
- 实现Transformer编码器的多头注意力机制，相比传统RNN获得显著性能提升 / Implemented Transformer encoder with multi-head attention mechanism, achieving significant performance improvements over traditional RNN

📈 **工程卓越 | Engineering Excellence**
- 完整的数据处理管道：数据获取 → 清洗 → 特征工程 → 模型训练 → 预测评估 / Complete end-to-end data pipeline: acquisition → cleaning → feature engineering → model training → prediction evaluation
- 企业级特征选择框架，支持5种特征筛选方法，处理参数>100维 / Enterprise-grade feature selection framework supporting 5 methods handling 100+ dimensional parameters
- 模块化设计，代码高度可复用与可维护 / Modular design with highly reusable and maintainable code

💼 **应用价值 | Practical Value**
- 从数据分析到策略执行的端到端解决方案 / End-to-end solution from data analysis to strategy execution
- 支持实时预测与回测验证，可直接应用于量化交易实践 / Real-time prediction with backtesting verification, directly applicable to quantitative trading practice
- 多时间粒度、多资产品种支持 / Multi-timeframe and multi-asset support

📊 **定量指标 | Quantitative Metrics**
- 模型总参数：83,137(CNN+LSTM+Attention), ~500K+(Transformer) / Total model parameters: 83,137 (CNN+LSTM+Attention), ~500K+ (Transformer)
- 特征筛选率：从100+维降至10-20维，信息保留率>95% / Feature selection compression: 100+ dimensions → 10-20 dimensions, >95% information retention
- 预测MSE测试集显著降低(相比基准模型) / Significant prediction MSE reduction on test set compared to baseline models

---

## 🎓 学习收获 | Learning Outcomes

### 深度学习 | Deep Learning
✓ 掌握RNN/LSTM/Transformer等序列模型的原理与实现 / Mastered principles and implementation of RNN/LSTM/Transformer sequence models  
✓ 理解注意力机制在金融时间序列中的作用 / Understood the role of attention mechanisms in financial time series  
✓ 熟悉TensorFlow/Keras的模型构建与训练流程 / Proficient in TensorFlow/Keras model building and training workflows  
✓ 学会处理金融时间序列的特殊性(非平稳性、异方差等) / Learned to handle peculiarities of financial time series (non-stationarity, heteroscedasticity)  

### 机器学习 | Machine Learning
✓ 系统学习特征工程的多种方法与取舍 / Systematic study of multiple feature engineering methods and trade-offs  
✓ 理解过拟合、欠拟合的诊断与解决方案 / Understanding of overfitting/underfitting diagnosis and solutions  
✓ 掌握模型评估指标的选择与应用 / Mastered model evaluation metrics selection and application  

### 金融工程 | Financial Engineering
✓ 理解量化交易的基本框架与回测流程 / Understand the basic framework and backtesting process of quantitative trading

---

## 📖 使用说明 | Usage Guide

### 安装依赖 | Installation

```bash
pip install tensorflow keras numpy pandas scikit-learn lightgbm yfinance matplotlib seaborn plotly jupyter
```

### 快速开始 | Quick Start

1. **特征工程 | Feature Engineering**
   ```bash
   # 打开Jupyter Notebook / Open Jupyter Notebook
   jupyter notebook feature_selecter_lightgbm/feature_selection.ipynb
   ```

2. **模型训练 | Model Training**
   ```bash
   # 选择以下任一模型 / Choose one of the models
   jupyter notebook "CNN+LSTM+Attention Mechanism to predict closing price.ipynb"
   ```

3. **交易回测 | Trading Backtesting**
   ```bash
   jupyter notebook trading\ system/trading_system.ipynb
   ```

---

## 📝 许可证 | License

MIT License - 详见LICENSE文件 / See LICENSE file for details

---

## 👤 作者 | Author

City University of Hong Kong - FYP Project 2024

---

## 🙏 致谢 | Acknowledgments

感谢深度学习、量化金融社区的启发与支持 / Thanks to the deep learning and quantitative finance community for inspiration and support.

---

**⭐ 如果这个项目对您有帮助，欢迎Star! | If this project helps you, please consider giving it a Star!**
