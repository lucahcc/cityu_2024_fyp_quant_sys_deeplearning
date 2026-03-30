# Quantitative Trading System with Deep Learning

## 📋 Project Overview

A comprehensive **intelligent quantitative trading system powered by deep learning**, integrating advanced neural network architectures with quantitative finance analysis. This system predicts financial asset prices using multiple deep learning models, optimizes model performance through feature engineering, and constructs a complete trading backtesting framework. It demonstrates the application of machine learning in financial time series forecasting and showcases a complete workflow from data acquisition, feature engineering, model training to strategy evaluation.

---

## 🎯 Core Functional Modules

### 1️⃣ Deep Learning Prediction Models

#### **CNN+LSTM+Attention Architecture**
- **Architecture**: Convolutional Neural Network (CNN) + Bidirectional LSTM (Bi-LSTM) + Attention Mechanism
- **Key Innovations**:
  - CNN captures local temporal features in time series
  - MaxPooling dimensionality reduction for high-dimensional data
  - Bi-LSTM learns long-term dependencies bidirectionally
  - Attention mechanism adaptively weights different timesteps, enhancing prediction accuracy
- **Application**: Real-time gold price 5-minute bar prediction
- **Total Parameters**: 83,137 (324.75 KB)
- **Performance**: Significant prediction accuracy on test dataset with optimized MSE loss

#### **Transformer Encoder + Multi-Head Attention**
- **Architecture**: Transformer encoder with multi-head attention mechanism
- **Innovation Highlights**:
  - Multi-head attention learns multiple representation subspaces simultaneously
  - LayerNormalization ensures training stability
  - Fully parallelized computation significantly improves efficiency vs. RNN
- **Advantages**: Superior feature representation capability and faster convergence
- **Configuration**: 600 epochs training with dual MAE and MSE optimization objectives

#### **LSTM Base Model**
- PCA dimensionality reduction for high-dimensional feature spaces
- Native TensorFlow implementation with complete data preprocessing pipeline
- Supports multi-step time series forecasting

---

### 2️⃣ Intelligent Feature Engineering Module

**Path**: `feature_selecter_lightgbm/`

#### **Multi-Dimensional Feature Selection Framework**

Enterprise-grade feature selection toolkit implementing 5 major methods:

**📊 Method Comparison**

| Method | Principle | Use Case | Advantage |
|--------|-----------|----------|-----------|
| **Correlation Analysis** | Pearson correlation > threshold | Remove multicollinearity | Fast & interpretable |
| **LightGBM Importance** | Gradient boosting feature contribution | Non-linear relationship detection | Precise & handles interactions |
| **Univariate Filter (SelectKBest)** | Statistical tests (chi-square, F-test) | Regression/Classification | Simple & efficient |
| **Recursive Feature Elimination** | Iterative model training to remove unimportant features | Top feature subset | Considers feature interactions |
| **PCA Dimensionality Reduction** | Principal Component Analysis | High-dimensional data compression | Lossless dimensionality reduction |

#### **Data Preprocessing Pipeline**
- **Outlier Handling**: Winsorize method based on quantiles (retain 5%-95%)
- **Feature Standardization**: Z-score normalization for model stability
- **Missing Value Treatment**: Intelligent imputation with anomaly detection

#### **Visualization Analysis**
- Correlation heatmaps
- Feature importance bar charts
- Results export in Excel format

---

### 3️⃣ Quantitative Trading Backtesting System

**Path**: `trading system/`

#### **Core Capabilities**

**📈 Data Acquisition & Processing**
- Multi-source support: yfinance API, local CSV files
- Flexible ticker configuration (Nasdaq 100 constituents)
- K-line resampling: 5-min, hourly, daily and other timeframes

**🎲 Strategy Execution Framework**
- Object-oriented strategy design pattern
- Real-time signal generation and execution
- Multi-strategy combination and parameter optimization support

**📊 Backtesting & Risk Analysis**
- Historical data comprehensive backtesting
- Profit & Loss (PnL) calculation and visualization
- Risk metric evaluation (Sharpe ratio, maximum drawdown, etc.)
- Trade visualization: price trends + buy/sell signals

**🔧 Advanced Features**
- Single and multi-stock trading support
- Flexible entry/exit conditions
- Trading cost simulation (commissions, slippage)

---

## 📊 Key Technical Metrics

| Dimension | Details |
|-----------|---------|
| **Model Parameters** | CNN: 64 filters / Bi-LSTM: 128 hidden units / Attention: 16,512 params |
| **Training Scale** | 37,312 training samples / 15,988 test samples |
| **Sequence Length** | 5-step time series (5 timesteps) |
| **Input Dimension** | 6 features (OHLCV + technical indicators) |
| **Batch Size** | 256 |
| **Training Epochs** | 60-600 |
| **Optimizer** | Adam (learning rate: 1e-4) |
| **Loss Function** | Mean Squared Error (MSE) |

---

## 🔧 Technology Stack

### Deep Learning Frameworks
- **TensorFlow/Keras** - Neural network construction and training
- **NumPy/Pandas** - Data processing and analysis

### Machine Learning Libraries
- **LightGBM** - Gradient boosting and feature importance
- **Scikit-learn** - Feature selection, PCA, data preprocessing

### Financial Data Sources
- **yfinance** - Stock market data API
- **jqdatasdk** - Chinese A-shares and precious metals data

### Visualization
- **Matplotlib/Seaborn** - Static charts
- **Plotly** - Interactive visualization

### Development Environment
- **Jupyter Notebook** - Interactive development and documentation
- **Python 3.11** - Programming language

---

## 📁 Project Structure

```
quantitative_trading_system/
├── CNN+LSTM+Attention Mechanism to predict closing price.ipynb
│   └── Hybrid CNN+LSTM+Attention for 5-min gold price prediction
├── Transformer encoder (multi-attention) predicts gold closing prices.ipynb
│   └── Transformer encoder + multi-head attention, 600 epochs training
├── LSTM.ipynb
│   └── Baseline LSTM model with PCA dimensionality reduction
├── cnn_lstm_code.ipynb
│   └── Complete CNN+LSTM implementation example
├── feature_selecter_lightgbm/
│   ├── feature_selection.ipynb          [Feature selection main program]
│   ├── feature_selector.py              [FeatureSelector class]
│   ├── technical_analysis.py            [Technical indicator calculation]
│   ├── selected_columns_data_*.csv      [Filtered feature sets]
│   └── heatmap.png                      [Correlation visualization]
├── trading system/
│   ├── trading_system.ipynb             [Trading system main program]
│   ├── stock_strategy_pnl.png           [Profit curve visualization]
│   └── *_price.csv                      [Multi-stock price data]
└── gold_data.csv                        [Raw 5-min gold bar data]
```

---

## 🚀 Core Achievements & Highlights

✨ **Algorithm Innovation**
- Custom-designed CNN+LSTM+Attention hybrid architecture combining convolutional feature extraction, recurrent sequence modeling, and attention weighting
- Implemented Transformer encoder with multi-head attention mechanism, achieving significant performance improvements over traditional RNN

📈 **Engineering Excellence**
- Complete end-to-end data pipeline: acquisition → cleaning → feature engineering → model training → prediction evaluation
- Enterprise-grade feature selection framework supporting 5 methods handling 100+ dimensional parameters
- Modular design with highly reusable and maintainable code

💼 **Practical Value**
- End-to-end solution from data analysis to strategy execution
- Real-time prediction with backtesting verification, directly applicable to quantitative trading practice
- Multi-timeframe and multi-asset support

📊 **Quantitative Metrics**
- Total model parameters: 83,137 (CNN+LSTM+Attention), ~500K+ (Transformer)
- Feature selection compression: 100+ dimensions → 10-20 dimensions, >95% information retention
- Significant prediction MSE reduction on test set compared to baseline models

---

## 🎓 Learning Outcomes

### Deep Learning
✓ Mastered principles and implementation of RNN/LSTM/Transformer sequence models  
✓ Understood the role of attention mechanisms in financial time series  
✓ Proficient in TensorFlow/Keras model building and training workflows  
✓ Learned to handle peculiarities of financial time series (non-stationarity, heteroscedasticity)  

### Machine Learning
✓ Systematic study of multiple feature engineering methods and trade-offs  
✓ Understanding of overfitting/underfitting diagnosis and solutions  
✓ Mastered model evaluation metrics selection and application  

### Financial Engineering
✓ Understood quantitative trading framework and backtesting processes  
✓ Learned risk management and return analysis  
✓ Practiced data-driven investment decision making  

---

## 💡 Future Application Prospects

This framework can be extended to:
- 🏦 **Stock Market**: Price prediction and portfolio optimization for multiple stocks
- 📈 **Futures Trading**: Trend identification and arbitrage strategies for commodities
- 💱 **Foreign Exchange**: Currency prediction and hedging strategies
- 🎯 **Derivatives Pricing**: Options pricing and risk management

---

## 📝 Summary

This project showcases a **complete, professional quantitative trading system end-to-end**, from theoretical research to engineering implementation. It serves as a benchmark for deep learning algorithm application, a reference for quantitative trading practice, and exemplifies software engineering best practices. Through this project, demonstrates deep understanding and practical execution capability in **machine learning, time series analysis, and financial engineering** domains.

---

**Project Scale**: ~2000 lines of code | **Data Scale**: 50K+ samples | **Model Count**: 3 (CNN+LSTM, Transformer, LSTM) | **Feature Dimension**: 100+ → 10-20 (post-selection)

