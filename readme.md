## 后台服务

基于 python 的 flask 框架，制作的简易后台功能。

### 包含内容

####v2 文件夹

通过抓取一些应用的api，以及提取的网页的数据，构成了一个新的数据构成，以json方式返回。

##### 获取列表的方式

`{hostIp}/v2/list/{name}/{category}/{page|nextId}`

这是获取文章列表的基本方法，例如`http://all.wuruoye.com/v2/list/ifan/home/0`，返回一个数据列表

##### 获取详情

`{hostIp}/v2/detail/{name}/{category}/{id}`

获取文章详情的方法，如`http://all.wuruoye.com/v2/detail/ifan/home/12345`

####v3文件夹

