>>>from sklearn import datasets ##导入包中的数据
>>> iris=datasets.load_iris() ##加载数据
>>> iris.feature_names  ##显示特征名字
 ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
>>> iris.data   ##显示数据
 array([[ 5.1, 3.5, 1.4, 0.2],[ 4.9, 3. , 1.4, 0.2],[ 4.7, 3.2, 1.3, 0.2]............
>>> iris.data.size  ##数据大小 ---600个
>>> iris.target_names  ##显示分类的名字 
 array(['setosa', 'versicolor', 'virginica'], dtype='<U10')
>>> from sklearn.naive_bayes import GaussianNB ##导入高斯朴素贝叶斯算法
>>> clf = GaussianNB()    ##给算法赋一个变量，主要是为了方便使用
>>> clf.fit(iris.data, iris.target)  ##开始分类。对于量特别大的样本，可以使用函数partial_fit分类，避免一次加载过多数据到内存

>>> clf.predict(iris.data[0].reshape(1,-1)) ##验证分类。标红部分特别说明：因为predict的参数是数组，data[0]是列表，所以需要转换一下
array([0])
>>> data=np.array([6,4,6,2])   ##验证分类
>>> clf.predict(data.reshape(1,-1))
array([2])