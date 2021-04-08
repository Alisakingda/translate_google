#!/usr/bin/python
# -*- coding:utf-8 -*-
from translate_google import get_translate
import asyncio
import re
import time

def main():
    print('start')
    tl = 'en_us'
    # 创建一个event_loop
    tasks = []
    loop = asyncio.get_event_loop()

    async def do_work(text):
        translate_text = get_translate(text, tl)
        # print(translate_text)
        return translate_text

    with open('app.txt', 'r', encoding='utf-8') as fp:
        now = lambda: time.time()
        start = now()

        for line in fp:
            ex = '.*?"(.*?)": .*?'
            l = re.findall(ex, line)
            # print(line)
            if len(l)!= 0:
                text = l[0]
                translate_text = get_translate(text, tl)[0][0]
                line = '"%s": "%s",\n' %(text, translate_text)
                # current_line = line
                # # print(text)
                # def callback(future):
                #     print(future.result()[0][0])
                #     print(current_line)
                #
                # task = loop.create_task(do_work(text))
                # task.add_done_callback(callback,)
                # tasks.append(task)
                # task.add_done_callback(callback)
            with open('%s.js'%(tl), 'a', encoding="utf-8") as fp:
                fp.write(line)
        # loop.run_until_complete(asyncio.wait(tasks))
        end = now()
        print('总计用时:', end - start)

if __name__ == "__main__":
    main()
