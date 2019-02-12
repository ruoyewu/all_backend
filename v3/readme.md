## v3说明

### AppInfo 构造

```json
{
  "name": "",
  "title": "",
  "icon": "",
  "category_name": [],
  "category_title": []
}
```



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
    "other_info": "其他信息，以 | 为分隔符表示，如： 天气|晴|多云",
    "open_type": ""
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
  "text_cen": "7",
  "quote": "8"
}
```

```
{"age":"","author":"沈星佑","category_id":"","content":[{"info":"https://s3.ifanr.com/wp-content/uploads/2019/02/emoji-2019.jpg","type":"2"},{"info":"2019 年最新一批 emoji 表情包公布了，这次的 emoji v12 版本中加入 59 个新成员，其中包括机械臂、冰块、血滴、华夫饼、盲人、水獭、连体泳衣......","type":"1"},{"info":"https://s3.ifanr.com/wp-content/uploads/2019/02/WechatIMG35.jpeg","type":"2"},{"info":"这次新增的其中一个 emoji 为 「两人手牵手」，通过不同性别、肤色的的组合，可以衍生出 71 个新变种。","type":"1"},{"info":"近些年来，emoji 在互联网巨头和网友的努力下变得越来越多元化。比如加入了中性性别的人像，人像 emoji 加入不同肤色的选项，以及父母、恋人之类的组合不仅是一男一女的搭配。","type":"1"},{"info":"https://s3.ifanr.com/wp-content/uploads/2018/03/apple-accessible-emoji-proposed-2018-emojipedia-1024x1024.jpg","type":"2"},{"info":"这次更新有一个显著的特点就是是加入了不少与残障人士有关的 emoji，比如导盲犬 / 服务犬，自动 / 手动轮椅，带着助听器的耳朵，一个在做手语的聋人，男 / 女在自动 / 手动轮椅上，男 / 女拿着盲杖走路等等。","type":"1"},{"info":"这类 emoji 被统一码联盟收录，离不开苹果的推动。2018 年 3 月，苹果与美国盲人协会、美国聋人协会和脑性麻痹基金会联手，向统一码联盟提交了包括机械臂（义肢）、助听器、导盲犬、拄杖走路、轮椅等 13 个 emoji。这些 emoji 大部分都通过了审核，加入到 Unicode 12.0 中。","type":"1"},{"info":"统一码联盟（The Unicode Consortium）每年会对来自全球的 emoji 提案进行选拔和投票，定期公布新的 emoji。每一个 emoji，就是一个 Unicode 字符。","type":"1"},{"info":"这次公布的 59 个新 emoji 已经加入 Unicode 12.0 ，不过全都是样本而已，接下来，像 Google、苹果、三星、Facebook 这些软件和硬件提供商的设计师，会将这些 emoji 进行改造，变成适应自家平台风格的表情包。通常要等到 9 月、10 月我们才能用上最新的表情包。","type":"1"},{"info":"https://s3.ifanr.com/wp-content/uploads/2018/11/aojipedia-2017.jpg","type":"2"},{"info":"emoji 已经成为人们在互联网世界表达和沟通的常用符号。它使用图形、图像和颜色来表达含义，比图片、视频这些载体要简单，也比文字能够传达更丰富的含义。","type":"1"},{"info":"当然 emoji 这套符号本身在日渐变得更加多元和复杂。其一是 emoji 数量越来越多，使用场景越来越复杂。用 emoji 写歌写书不是什么新鲜事了。","type":"1"},{"info":"https://s3.ifanr.com/wp-content/uploads/2017/08/IMG_4283.jpg","type":"2"},{"info":"▲ 烂番茄 0 分电影《The Emoji Movie》","type":"1"},{"info":"其二是不同的平台对同一个编码的 emoji 重新设计，融入了自身的价值观和设计风格后，产生了跨平台的沟通障碍。","type":"1"},{"info":"Android 平台表情包设计总监珍妮弗 · 丹尼尔（Jennifer Daniel）曾经解释了各个平台的 emoji 风格。","type":"1"},{"info":"https://s3.ifanr.com/wp-content/uploads/2018/07/emoji-2018-07-09-16.18.57.jpg","type":"2"},{"info":"▲ 图片来自：Emojipedia","type":"1"},{"info":"苹果沉迷设计，因此他们的版本更加立体，渐变和阴影的细节非常考究；微软的版本有着又黑又粗的边框，怕是要跟文字明显区分开来；Twitter 是发短消息起家的社交平台，因此他们的 emoji 非常简洁，基本没有阴影渐变这些细节；Google 则是更加轻松和卡通化。","type":"1"},{"info":"其三，emoji 的版权细节涉及多方利益，也在让它变得更加复杂。因为 emoji 的官方名字版权属于 Unicode 规范，即统一码联盟；描述文字版权属于网站 emojipedia.org；对应的图形设计版权，属于它的创作者或公司。","type":"1"},{"info":"因此，「Apple Color Emoji」，版权属于苹果，Google 的 Android Emoji 遵守 Apache Licene 2.0 的开源协议。","type":"1"},{"info":"https://s3.ifanr.com/wp-content/uploads/2018/07/emoji-1.jpg","type":"2"},{"info":"更加值得注意的是，同一个 emoji 在不同群体、不同时期都被产生不同的解读。","type":"1"},{"info":"emoji 作为一种沟通符号，在变得流行，却又相当语义不明，这让律师这个群体相当恼火。","type":"1"},{"info":"《华尔街日报》的数据显示，从 2015 年开始与 emoji 表情包有关的案件在明显增加。这些 emoji 作为诽谤、骚扰、商业纠纷等案件的证据，如何解读 emoji 已经开始影响案件审判的走向。","type":"1"},{"info":"美国律师 Morgan Clemons 发起了一个名为「Emoji Law 101」的行动，讨论法律视角中的各种 emoji 和表情文字。","type":"1"},{"info":"律师们面对 emoji 和 表情文字的心情，估计可以用这个颜文字来表达：¯\_(ツ)_/¯","type":"1"}],"date":"2019-02-12 19:01:43","forward":"emoji 是一种语义不明的沟通符号。¯\_(ツ)_/¯","id":"1171732","image":"https://s3.ifanr.com/wp-content/uploads/2019/02/emoji-2019.jpg","img_list":[],"open_type":"1","original_url":"https://www.ifanr.com/1171732","other_info":"","time_millis":"","title":"2019 年最新 Emoji 来了，对残障人士有更多关注","type":"公司","video":""}
```

