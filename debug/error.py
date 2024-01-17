# 1.AttributeError

# 属性の参照や代入が失敗した場合のエラー

a = 12
a.replace(1, 2)

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Input In [1], in <cell line: 2>()
      1 a = 12
----> 2 a.replace(1, 2)

AttributeError: 'int' object has no attribute 'replace'