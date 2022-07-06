# How to use this script

You only need 3 thing to change to generate a header(*.h) and a source(*.c)
First, the name of the strcut
Then the alias of the struct
And last, a list of the path that the file will be

The next example will be:
Filename: (I recommend) ll_struct_name.h && ll_struct_name.c
Struct: ll_struct_name
Alias: AliasStruct
Path: ./anticheat/core

```python3
content: str = generate_full("ll_struct_name", "AliasStruct", ["anticheat", "core"])
print(content)
```
