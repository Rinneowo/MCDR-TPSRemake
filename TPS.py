# coding=utf-8
from time import sleep
import re

help_msg = '''------ §aMCDR TPS检测插件帮助信息 §f------
§b!!tps help §f- §c显示此帮助信息
§b!!tps §f- §c测试服务器tps
§b!!tps [秒] §f- §c测试服务器tps, [秒] 测试时间
--------------------------------'''


def on_info(server, info):
    if info.is_player == 1:
        if info.content.startswith('!!tps'):
            args = info.content.split(' ')
            if len(args) == 1:
                server.execute('debug start')
                sleep(1)
                server.execute('debug stop')
            elif args[1] == 'help':
                for line in help_msg.splitlines():
                    server.tell(info.player, line)
            elif len(args) == 2:
                time = int(args[1])
                server.execute('debug start')
                sleep(time)
                server.execute('debug stop')
    elif 'Stopped debug profiling after' in info.content:
        match = re.compile(r'[(](.*?)[)]', re.S)
        split = re.findall(match, info.content)[0].split(" ")[0]
        server.say("------ §a当前服务器TPS为 §e" + split + " §f------")

def on_load(server, info):
    server.add_help_message('!!tps help', 'TPS检测帮助')
© 2020 GitHub, Inc.