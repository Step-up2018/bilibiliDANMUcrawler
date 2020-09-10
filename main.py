import easygui as g

import spid
from MakeCloud import makecloud

while 1:
    ch1 = g.buttonbox(msg="输入AV号还是BV号", title="弹幕爬取器", choices=("AV号", "BV号"))
    id = " "
    if ch1=="AV号":
        id = g.enterbox(msg="输入AV号", title="弹幕爬取器")
        spid.spidera(id)
    else:
        id = g.enterbox(msg="输入BV号", title="弹幕爬取器")
        spid.spiderb(id)
    title = g.msgbox(msg="弹幕信息已保存", title="弹幕爬取器", ok_button="生成词云")
    makecloud(ch1, id)
    break