## v3说明

### list构造

```json
{
  "name": "app名称",
  "category":"类别",
  "next": "",
  "result":{
    "id": "当然item唯一标识符",
    "title": "标题",
    "forward": "概述",
    "author": "作者",
    "image": "图片url",
    "video": "视频url",
    "date": "日期，格式： 2017-09-20 12:12:12",
    "time_millis": "日期，格式： 1503231041",
    "age": "日期，格式： 一小时前",
    "original_url": "原始地址",
    "content": [],
    "type": "当前所属分类名称",
    "category_id": "在app内展示类型分类"，
    "other_info": "其他信息，以 | 为分隔符表示，如： 天气|晴|多云"
  }
}
```

### detail构造

```json
{
  "title": "标题",
  "subtitle": "副标题",
  "author": "作者",
  "date": "时间",
  "content": [文本列表],
  "serial_list": [如果是连载，则显示连载列表信息]
}
```

####文本列表说明

```json
{
  "type": "当前项的数据类型，对应下 type",
  "info": "数据内容，文本，链接等"
}

type{
  "text": "1",
  "image": "2",
  "video": "3",
  "h1": "4",
  "h2": '5',
  "li": "6",
  "text_cen": "7"
}
```

