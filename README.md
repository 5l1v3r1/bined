
***

**Module**: Bined

   **JOB**: Encode/Decode Binary Bits
***

# install:
   - pip install bined
***
# usage:

```python
>>>
>>> from bined.bined import *
>>>
>>>
>>> encodeSTR('hello')
'0110100001100101011011000110110001101111'
>>>
>>> encodeSTR(['python','love'])
['011100000111100101110100011010000110111101101110', '01101100011011110111011001100101']
>>>
>>> decodeSTR('011100000111100101110100011010000110111101101110')
'python'
>>>
>>> encodeINT(255)
'11111111'
>>>
>>> encodeINT([255,'100'])
['11111111', '1100100']
>>>
>>> decodeINT(['11111111', '1100100'])
[255, 100]
>>>
>>>
>>> encodeIP('192.168.1.92')
'11000000.10101000.00000001.01011100'
>>>
>>>
>>> decodeIP('11000000.10101000.00000001.01011100')
'192.168.1.92'
>>>
>>>
```
***
# That's All :)
   * This Module By Oseid Aldary
   * Thanks For Usage
   * Have A Nice Day...GoodBye :)
