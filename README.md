1.依赖包
pip install PyExecJS 安装python转换js
pip install reportlib 生成pdf文档
pip intasll requests 
pip install flask        简单web应用
pip install jsonpath

2.实现方式
没有实现登录获取coockie，只能将coockie放入请求头
通过固定请求头请求网站，获取文章点赞数
获取top10点赞文章，记入list，目前只处理了前100个文章，需再改进
根据list中记录的url获取文章全文
解析html，目前处理欠缺，只能解析题目和正文
处理解析出来的每段文字，调用google翻译成中文
根据文字类别（题目、小标题、正文）组装pdf文件
保存pdf文件
从网页上处理生成pdf和下载pdf目前欠缺

运行
python requestweb.py