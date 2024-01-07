# Banker's Algorithm

## 算法介绍

银行家算法是最著名的死锁避免算法。当进程首次申请资源时，要测试该进程对资源的最大需求量，如果系统现存的资源可以满足它的最大需求量时，则按当前的申请量分配资源，否则，推迟分配。  

## 数据结构描述

1. 可利用资源矢量Avaiable

    含有m个元素的数组，其中的每一个元素代表一类可用的资源数目。Available[j]=k，则表示系统中现有Rj类资源K个。

2. 最大需求矩阵Max

    为nxm矩阵，定义了系统中n个进程中的每一个进程对m类资源的最大需求。Max[i,j]=K，则表示进程i需要Rj类资源最大数目为K

3. 分配矩阵Allocation

    为n×m矩阵，定义了系统中每一类资源当前已分配给每一进程的资源数。Allocation[i,j]=K，则表示进程i当前已分配得Rj类资源的数目为K。

4. 需求矩阵Need

    为n×m矩阵，表示每个进程尚需的各类资源数，Need[i,j]=K，则表示进程i还需要Rj类资源数目为K

## 银行家算法描述

### 银行家算法

设Request i是进程Pi的请求矢量，如果Request i[j]=K，表示进程Pi需要Rj类资源K个。当Pi发出资源请求后，系统按下述步骤进行检测：

1. 如果Request i[j] ≤Need[i，j]，便转向步骤2，否则认为出错，因为它所需的资源数超过了它所宣布的最大值。
2. 如果Request i[j] ≤Available[i，j]，便转向步骤3，否则，表示尚无足够资源，Pi须等待
3. 系统试探着把资源分配给进程Pi，并修改下面数据结构中的数值：
    Available[j]=Availabe[j]-Request i[j]  
    Allocation[i,j]=Allocation[i,j]+Request i[j]  
    Need[i,j]=Need[i,j]-Request i[j]  
4、系统执行安全性算法，检查此次资源分配后，系统是否处于安全状态。若安全，才正式将资源分配给进程Pi，以完成本次分配；否则，将本次试探分配作废，恢复原来的资源分配状态，让进程Pi等待。

### 安全性算法

1. 设置两个矢量。

    - 工作矢量Work；它表示系统可提供给进程继续运行所需的各类资源数目，它含有m个元素，在执行安全算法开始时，Work=Available；
    - Finish：它表示系统是否有足够的资源分配给进程，使之运行完成。开始时Finish[i]=false；当有足够资源分配给进程Pi时，再令Finish[i]=true;

2. 从进程集合中找到一个能满足下述条件的进程：
    Finish[i]=false;
    Need[i,j]=Work[j];
    若找到，执行下一步骤，否则，执行步骤4

3. 当进程Pi获得资源后，可顺利执行，直至完成，并释放分配给它的资源，共应执行：
    Work[j]=Work[j]+Allocation[i,j];  
    Finish[i]=true;  
    go to step (2)  

4. 如果所有进程的Finish[i]=true满足，则表示系统处于安全状态；否则系统将处于不安全状态
