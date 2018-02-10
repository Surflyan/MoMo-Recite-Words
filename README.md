# 墨墨背单词每日分享脚本

![](https://img.shields.io/badge/language-python-orange.svg) ![](https://img.shields.io/badge/platform-linux\windows-lightgrey.svg)  ![](https://img.shields.io/badge/license-MIT-000000.svg)
--------------------------------------------------------------------------------

## Why ？

墨墨背单词是一款非常受欢迎的单词记忆APP。个人喜欢它的地方有三点：
* 助记向用户开发。形成了活跃的单词助记社区；
* 单词记忆周期长。对于每个单词都有个人的记忆周期，一个熟悉的单词也可能在很久以后再次复习出现；
* 词库共有6万余单词，单词书起到分类作用，同一个单词不会重复记忆。

相较其他同类软件在助记的使用上盈利，而墨墨换个思路，设置用户记忆单词上限，初始用户有600个单词额度，可通过每日打卡、分享等手段获得免费单词上限增长。也可选择付费购买单次上限，这也是墨墨的盈利模式。

--------------------------------------------------------------------------------

## Implement

本脚本主要着眼于用户每日分享最高可获得的20个单词上限。墨墨规定，每个分享页获得20次点击（墨墨用户除外、同一用户只记一次），可获得20个单词上限。
分享到票圈、朋友们，这一点也不`Geek`!

观察墨墨每日分享链接 [https://www.maimemo.com/share/page/?uid=2369398&pid=1136](https://www.maimemo.com/share/page/?uid=2369398&pid=1136)

* uid = 用户ID

* pid = 每日分享页面ID

* 最让人意外的是 **pid 数值，每日++**！

ok！一个python脚本，搞定一切。

不同用户，可通过IP代理完成；pid每日增1，可每次 crawl 之后，将 pid ++ 写回到 config.txt

### File

**ProxyCrawler.py**: 代理IP获取，代理来源 [http://www.xicidaili.com/wt](http://www.xicidaili.com/wt/)

**VisitLink.py**: 读取config.txt, 生成MomoSharePageUrl, 利用requests.get 访问之

**Scheduler.py**: 设置定时任务，每日定时启动

**config.txt**: 用户个人信息配置，uid，今日 pid



--------------------------------------------------------------------------------

## INSTALL & USE
```
git clone https://github.com/Surflyan/MoMo-Recite-Words.git
cd Momo-Recite-Words
pip install -r requirments.txt

# 修改config.txt
uid
today-pid

python Scheduker.py
```

若部署到Linux服务器，可将启动命令写到`/etc/rc.local` Exit 之前。

每日定时爬取时间设置在 `Scheduler.py`：
```python
scheduler.add_job(MyJob,'cron',hour = '23',minute = '00')
```
--------------------------------------------------------------------------------

## LICENSE
[MIT](https://github.com/nishanths/license/blob/master/LICENSE)
