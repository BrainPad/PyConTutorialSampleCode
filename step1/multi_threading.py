# -*- coding: utf-8 -*-

import logging
from logging import getLogger, StreamHandler, Formatter
import threading


logger = getLogger("app")
EXECUTE_FUNCTION_COUNT = 5


def do_something(what):
    whoami(what)


def whoami(what):
    logger.debug(f"Thread says: {what}")


def init_logger():
    # loggerのログレベル設定(ハンドラに渡すエラーメッセージのレベル)
    logger.setLevel(logging.DEBUG)
    # handlerの生成
    handler = StreamHandler()
    # handlerのログレベル設定(ハンドラが出力するエラーメッセージのレベル)
    handler.setLevel(logging.DEBUG)
    # ログ出力フォーマット設定
    formatter = Formatter(
        '%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)d'
        ' %(thread)d %(threadName)s %(name)s -'
        ' %(message)s')
    handler.setFormatter(formatter)
    # loggerにhandlerをセット
    logger.addHandler(handler)


if __name__ == '__main__':
    init_logger()
    whoami("I'm the main program")
    for n in range(EXECUTE_FUNCTION_COUNT):
        p = threading.Thread(
            target=do_something,
            args=(f"I'm function {n}",)
        )
        p.start()
