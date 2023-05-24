from typing import Union
from pyspark import SparkConf, SparkContext

my_li: list[int] = [1, 2, 3]
my_dic: dict[str, int] = {'edfe': 324}


def add(x: int, y: int) -> int:
    return x + y


dic: dict[str, Union[str, int]]

conf = SparkConf().setMaster('local[*]').setAppName('test_spark_app')

sc = SparkContext(conf=conf)
print(sc.version)
sc.stop()