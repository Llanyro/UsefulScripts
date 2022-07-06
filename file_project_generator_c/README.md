# How to use this script

You only need 3 thing to change to generate a header(*.h) and a source(*.c)
First, the name of the struct
Then the alias of the struct
And last, a list of the path that the file will be.

The next example will be:
Filename: (I recommend) ll_struct_name.h && ll_struct_name.c
Struct: ll_struct_name
Alias: AliasStruct
Path: ./anticheat/core

*** Remember to include the alias like this: ***
``` typedef struct ll_struct_name AliasStruct;  ```

```python3
from file_content_generator import generate_full

content: str = generate_full("ll_struct_name", "AliasStruct", ["anticheat", "core"])
print(content)
```

## How to modify the file "header.h" and "source.c"
Open it with any editor, remember that you can't modify any {?} character, because it will make the script stop working, or modify them carefully.
You can change, add, or remove the includes in both files

Remember this:
{0} is for the name__
{1} is fot he alias__
{2} is for the struct name as var__
