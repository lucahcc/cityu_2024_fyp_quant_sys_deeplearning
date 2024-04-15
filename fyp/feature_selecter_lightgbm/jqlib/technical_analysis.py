{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6c7c44b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# coding=utf-8\n",
    "from typing import TypeVar, Tuple\n",
    "import datetime\n",
    "\n",
    "JQDate = TypeVar('JQDate', str, datetime.date, datetime.datetime)\n",
    "JQStkList = TypeVar('JQStkList', str, list, tuple)\n",
    "JQFields = TypeVar('JQStkList', str, list, tuple)\n",
    "\n",
    "\n",
    "def ATR(security_list, check_date, timeperiod=14):\n",
    "    # type: (JQStkList, JQDate, int) -> Tuple[dict, dict]\n",
    "    \"\"\"\n",
    "    ATR-真实波幅\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param timeperiod: 统计的天数\n",
    "    :return: MTR和ATR 的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "            ({'000001.XSHE': 0.080000000000000071, '603177.XSHG': np.nan},\n",
    "             {'000001.XSHE': 0.059999999999999866, '603177.XSHG': np.nan})\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def BIAS(security_list, check_date, N1=6, N2=12, N3=24):\n",
    "    # type: (JQStkList, JQDate, int, int, int) -> Tuple[dict, dict, dict]\n",
    "    \"\"\"\n",
    "    BIAS-乖离率\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N1: 统计的天数 N1\n",
    "    :param N2: 统计的天数 N2\n",
    "    :param N3: 统计的天数 N3\n",
    "    :return: BIAS1, BIAS2, BIAS3 的值。\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据。\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def CCI(security_list, check_date, N=14):\n",
    "    # type: (JQStkList, JQDate, int) -> dict\n",
    "    \"\"\"\n",
    "    CCI-商品路径指标\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N: 统计的天数 N\n",
    "    :return: CCI 的值。\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据。\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def KDJ(security_list, check_date, N=9, M1=3, M2=3):\n",
    "    # type: (JQStkList, JQDate, int, int, int) -> Tuple[dict, dict, dict]\n",
    "    \"\"\"\n",
    "    KDJ-随机指标\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N: 统计的天数 N\n",
    "    :param M1: 统计的天数 M1\n",
    "    :param M2: 统计的天数 M2\n",
    "    :return: K，D和J 的值。\n",
    "    :rtype: (dict): 键(key)为股票代码，值(value)为数据。\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def MFI(security_list, check_date, timeperiod=14):\n",
    "    # type: (JQStkList, JQDate, int) -> dict\n",
    "    \"\"\"\n",
    "    MFI-资金流量指标\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param timeperiod: 统计的天数 N\n",
    "    :return: MFI 的值。\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据。\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def MTM(security_list, check_date, timeperiod=14):\n",
    "    # type: (JQStkList, JQDate, int) -> dict\n",
    "    \"\"\"\n",
    "    MTM - 动量线\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param timeperiod: 统计的天数 N\n",
    "    :return:MTM的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def ROC(security_list, check_date, timeperiod=12):\n",
    "    # type: (JQStkList, JQDate, int) -> dict\n",
    "    \"\"\"\n",
    "    ROC-变动率指标\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param timeperiod: 统计的天数 N\n",
    "    :return:ROC的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def RSI(security_list, check_date, N1=6):\n",
    "    # type: (JQStkList, JQDate, int) -> dict\n",
    "    \"\"\"\n",
    "    RSI - 相对强弱指标\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N1: 统计的天数N1\n",
    "    :return:RSI 的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def CHO(security_list, check_date, N1=10, N2=20, M=6):\n",
    "    # type: (JQStkList, JQDate, int, int, int) -> dict\n",
    "    \"\"\"\n",
    "    CHO - 佳庆指标\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N1: 统计的天数 N1\n",
    "    :param N2: 统计的天数 N2\n",
    "    :param M: 统计的天数 M\n",
    "    :return:CHO 和 MACHO 的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def CYE(security_list, check_date):\n",
    "    # type: (JQStkList, JQDate) -> Tuple[dict, dict]\n",
    "    \"\"\"\n",
    "    CYE-市场趋势\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :return: CYEL和CYES的值\n",
    "    :rtype: (dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def DBQR(index_stock, security_list, check_date, N=5, M1=10, M2=20, M3=60):\n",
    "    # type: (str, JQStkList, JQDate, int, int, int, int) -> Tuple[dict, dict, dict, dict, dict]\n",
    "    \"\"\"\n",
    "    DBQR - 对比强弱\n",
    "    :param index_stock:大盘股票代码\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N: 统计的天数 N\n",
    "    :param M1: 统计的天数 M1\n",
    "    :param M2: 统计的天数 M2\n",
    "    :param M3: 统计的天数 M3\n",
    "    :return:ZS, GG, MADBQR1, MADBQR2和MADBQR3的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def DMA(security_list, check_date, N1=10, N2=50, M=10):\n",
    "    # type: (JQStkList, JQDate) -> Tuple[dict, dict]\n",
    "    \"\"\"\n",
    "    DMA-平均差\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N1: 统计的天数 N1\n",
    "    :param N2: 统计的天数 N2\n",
    "    :param M: 统计的天数 M\n",
    "    :return:DIF 和 DIFMA 的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def DMI(security_list, check_date, N=14, MM=6):\n",
    "    # type: (JQStkList, JQDate, int, int) -> Tuple[dict, dict, dict, dict]\n",
    "    \"\"\"\n",
    "    DMI - 趋向指标\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N: 统计的天数 N\n",
    "    :param MM :  统计的天数 MM\n",
    "    :return:PDI, MDI, ADX, ADXR的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def DMI(security_list, check_date, N=20, M=6):\n",
    "    # type: (JQStkList, JQDate, int, int) -> Tuple[dict, dict]\n",
    "    \"\"\"\n",
    "    DPO-区间震荡线\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N: 统计的天数 N\n",
    "    :param M :  统计的天数 M\n",
    "    :return:DPO 和 MADPO 的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def EMV(security_list, check_date, N=14, M=9):\n",
    "    # type: (JQStkList, JQDate, int, int) -> Tuple[dict, dict]\n",
    "    \"\"\"\n",
    "    EMV-简易波动指标\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N: 统计的天数 N\n",
    "    :param M: 统计的天数 M\n",
    "    :return:EMV和MAEMV的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def GDX(security_list, check_date, N=30, M=9):\n",
    "    # type: (JQStkList, JQDate, int, int) -> Tuple[dict, dict, dict]\n",
    "    \"\"\"\n",
    "    GDX-鬼道线\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N: 统计的天数 N\n",
    "    :param M: 统计的天数 M\n",
    "    :return: 济安线、压力线和支撑线的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def JLHB(security_list, check_date, N=7, M=5):\n",
    "    # type: (JQStkList, JQDate, int, int) -> Tuple[dict, dict, dict]\n",
    "    \"\"\"\n",
    "    JLHB-绝路航标\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N: 统计的天数 N\n",
    "    :param M: 统计的天数 M\n",
    "    :return:B, VAR2和绝路航标的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def JS(security_list, check_date, N=5, M1=5, M2=10, M3=20):\n",
    "    # type: (JQStkList, JQDate, int, int, int, int) -> Tuple[dict, dict, dict, dict]\n",
    "    \"\"\"\n",
    "    JS-加速线\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N: 统计的天数 N\n",
    "    :param M1: 统计的天数 M1\n",
    "    :param M2: 统计的天数 M2\n",
    "    :param M3: 统计的天数 M3\n",
    "    :return:JS, MAJS1, MAJS2和MAJS3 的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def MACD(security_list, check_date, SHORT=12, LONG=26, MID=9):\n",
    "    # type: (JQStkList, JQDate, int, int, int) -> Tuple[dict, dict, dict]\n",
    "    \"\"\"\n",
    "    MACD-平滑异同平均\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param SHORT: 统计的天数 SHORT\n",
    "    :param LONG: 统计的天数 LONG\n",
    "    :param MID: 统计的天数 MID\n",
    "    :return:DIF, DEA和MACD的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def QACD(security_list, check_date, N1=12, N2=26, M=9):\n",
    "    # type: (JQStkList, JQDate, int, int, int) -> Tuple[dict, dict, dict]\n",
    "    \"\"\"\n",
    "    QACD-快速异同平均\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N1: 统计的天数 N1\n",
    "    :param N2: 统计的天数 N2\n",
    "    :param M: 统计的天数 M\n",
    "    :return:DIF, MACD和DDIF的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def QR(index_stock, security_list, check_date, N=21):\n",
    "    # type: (JQStkList, JQDate, int) -> Tuple[dict, dict, dict]\n",
    "    \"\"\"\n",
    "    QR-强弱指标\n",
    "    :param index_stock:大盘股票代码\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N: 统计的天数 N\n",
    "    :return:个股，大盘和强弱指标的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def TRIX(security_list, check_date, N=12, M=9):\n",
    "    # type: (JQStkList, JQDate, int, int) -> Tuple[list, list]\n",
    "    \"\"\"\n",
    "    TRIX-终极指标\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N: 统计的天数 N\n",
    "    :param M: 统计的天数 M\n",
    "    :return:TRIX和MATRIX的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def UOS(security_list, check_date, N1=7, N2=14, N3=28, M=6):\n",
    "    # type: (JQStkList, JQDate, int, int, int, int) -> Tuple[dict, dict]\n",
    "    \"\"\"\n",
    "    UOS-终极指标\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N1: 统计的天数 N1\n",
    "    :param N2: 统计的天数 N2\n",
    "    :param N3: 统计的天数 N3\n",
    "    :param M: 统计的天数 M\n",
    "    :return:终极指标和MAUOS的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def VMACD(security_list, check_date, SHORT=12, LONG=26, MID=9):\n",
    "    # type: (JQStkList, JQDate, int, int, int) -> Tuple[dict, dict, dict]\n",
    "    \"\"\"\n",
    "    VMACD-量平滑移动平均\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param SHORT: 统计的天数 SHORT\n",
    "    :param LONG: 统计的天数 LONG\n",
    "    :param MID: 统计的天数 MID\n",
    "    :return:DIF, DEA和MACD 的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def VPT(security_list, check_date, N=51, M=6):\n",
    "    # type: (JQStkList, JQDate, int, int) -> Tuple[dict, dict]\n",
    "    \"\"\"\n",
    "    VPT-量价曲线\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N: 统计的天数 N\n",
    "    :param M: 统计的天数 M\n",
    "    :return:VPT 和 MAVPT 的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def WVAD(security_list, check_date, N=24, M=6):\n",
    "    # type: (JQStkList, JQDate, int, int) -> Tuple[dict, dict]\n",
    "    \"\"\"\n",
    "    WVAD-威廉变异离散量\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N: 统计的天数 N\n",
    "    :param M: 统计的天数 M\n",
    "    :return:WVAD 和 MAWVAD的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def PSY(security_list, check_date, timeperiod=12):\n",
    "    # type: (JQStkList, JQDate, int) -> dict\n",
    "    \"\"\"\n",
    "    PSY-心理线\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param timeperiod: 统计的天数 N\n",
    "    :return:PSY 的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def OBV(security_list, check_date, timeperiod=30):\n",
    "    # type: (JQStkList, JQDate, int) -> dict\n",
    "    \"\"\"\n",
    "    OBV-累积能量线\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param timeperiod: 统计的天数 N\n",
    "    :return:OBV 的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def BBI(security_list, check_date, timeperiod1=3, timeperiod2=6, timeperiod3=12, timeperiod4=24):\n",
    "    # type: (JQStkList, JQDate, int, int, int, int) -> dict\n",
    "    \"\"\"\n",
    "    BBI-多空均线\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param timeperiod1: 统计的天数 N1\n",
    "    :param timeperiod2: 统计的天数 N2\n",
    "    :param timeperiod3: 统计的天数 N3\n",
    "    :param timeperiod4: 统计的天数 N4\n",
    "    :return:BBI 的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def MA(security_list, check_date, timeperiod=5):\n",
    "    # type: (JQStkList, JQDate, int) -> dict\n",
    "    \"\"\"\n",
    "    MA-均线\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param timeperiod: 统计的天数timeperiod\n",
    "    :return:MA 的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def Bollinger_Bands(security_list, check_date, timeperiod=20, nbdevup=2, nbdevdn=2):\n",
    "    # type: (JQStkList, JQDate, int, int, int) -> Tuple[dict, dict, dict]\n",
    "    \"\"\"\n",
    "    BOLL-布林线\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param timeperiod: 统计的天数timeperiod\n",
    "    :param nbdevup: 统计的天数 nbdevup\n",
    "    :param nbdevdn: 统计的天数 nbdevdn\n",
    "    :return:上轨线UB 、中轨线MB、下轨线LB 的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def EMA(security_list, check_date, timeperiod=30):\n",
    "    # type: (JQStkList, JQDate, int) -> dict\n",
    "    \"\"\"\n",
    "    EMA-指数移动平均\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param timeperiod: 统计的天数timeperiod\n",
    "    :return:EMA 的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "def SMA(security_list, check_date, N=7, M=1):\n",
    "    # type: (JQStkList, JQDate, int, int) -> dict\n",
    "    \"\"\"\n",
    "    SMA-移动平均\n",
    "    :param security_list: 股票列表\n",
    "    :param check_date: 要查询数据的日期\n",
    "    :param N: 统计的天数 N\n",
    "    :param M: 权重 M\n",
    "    :return:SMA(X的 N 日移动平均) 的值\n",
    "    :rtype: 字典(dict): 键(key)为股票代码，值(value)为数据\n",
    "    \"\"\"\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0be4010",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
