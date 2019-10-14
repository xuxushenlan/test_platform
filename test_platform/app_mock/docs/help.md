
该服务针对App自动化测试设计，目的是解决后端测试数据的构造问题。

##### 修改App，指定到该服务

1、开发klook App，```我的账户``` --> ```关于``` --> 三击版本号，打开隐藏设置。

2、添加并选择API， 设置为：```http://10.2.16.183:8001/api/```


##### 修改mock Server服务接口数据。

推荐使用Request库，调用接口并修改数据。

```python
import requests

base_url = "http://10.2.16.183:8001/api/"

r = requests.get(base_url + "v2/home")
result = r.json()

# 更新产品价格为 99999
result["result"]["groups"][1]["items"][0]["selling_price"] = 99999

# 重新将数据保存
result_json = json.dumps(result)
r = requests.put(base_url + "v2/home", data={"response": result_json})
ret = r.json()
print(ret)
```

__说明：__

* 通过```get/post```方法获取接口的数据。
* 通过```put```方法把修改的接口数据重新保存。


##### 测试App

重新开发App, 就可以看到修改后的数据在App上的展示了。