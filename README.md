# SSXSwitcher
Mac 版本 ShadowsocksX.app 网络选择工具
###SSX 网络切换工具
VPN在Win上很给力，但是在Mac上很废，经常连接失败或者连接不上。后来发现SSX，感觉不错，但是也不稳定，需要切换。
切换网络添加网络的时候经常需要点好几下。感觉好麻烦。

最近在学python。想着试试能不能用python写个工具。解决下切换网络的问题。
经过几天的努力，结果还算满意。编码没用多久。但是找plist找了许久。
本以为SSX会有存储地址的plist或者其他文件。结果找了好久没找到。Git上的SSX源码也没了。

后来各种搜索。终于找到了``clowwindy.ShadowsocksX.plist``。
经过多次修改，测试，确定了``clowwindy.ShadowsocksX.plist``的作用。

把py放到``~``用户目录下，每次打开shell直接命令走起。方便了不少。自己用的还不错。

目前只添加了2个获取免费代理网站。满足日常所需。


