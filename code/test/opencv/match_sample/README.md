


https://www.freesion.com/article/85171339454/#%EF%BC%883%EF%BC%89%E5%90%84%E7%A7%8D%E7%89%B9%E5%BE%81%E6%A3%80%E6%B5%8B%E7%AE%97%E6%B3%95%E7%9A%84%E6%AF%94%E8%BE%83
（1）特征检测算法
Harris：该算法用于检测角点；
SIFT：该算法用于检测斑点；https://blog.csdn.net/qq_40369926/article/details/88597406
SURF：该算法用于检测角点；
FAST：该算法用于检测角点；
BRIEF：该算法用于检测斑点；
ORB：该算法代表带方向的FAST算法与具有旋转不变性的BRIEF算法；
（2）特征匹配算法
暴力(Brute-Force)匹配法；
基于FLANN匹配法；
可以采用单应性进行空间验证。
（3）各种特征检测算法的比较
参考：https://www.cnblogs.com/jsxyhelu/p/7834416.html

计算速度： ORB>>SURF>>SIFT（各差一个量级）
旋转鲁棒性： SURF>ORB~SIFT（表示差不多）
模糊鲁棒性： SURF>ORB~SIFT
尺度变换鲁棒性： SURF>SIFT>ORB（ORB并不具备尺度变换性）
