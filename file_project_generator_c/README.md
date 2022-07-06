# How to use this script

You only need 3 thing to change to generate a header(*.h) and a source(*.c) <br/>
First, the name of the struct <br/>
Then the alias of the struct <br/>
And last, a list of the path that the file will be. <br/>

The next example will be: <br/>
Filename: (I recommend) ll_struct_name.h && ll_struct_name.c <br/>
Struct: ll_struct_name <br/>
Alias: AliasStruct <br/>
Path: ./anticheat/core <br/>

*** Remember to include the alias like this: ***
``` typedef struct ll_struct_name AliasStruct;  ```

```python3
from file_content_generator import generate_full

content: str = generate_full("ll_struct_name", "AliasStruct", ["anticheat", "core"])
print(content)
```

## How to modify the file "header.h" and "source.c"
Open it with any editor, remember that you can't modify any {?} character, because it will make the script stop working, or modify them carefully. <br/>
You can change, add, or remove the includes in both files

Remember this: <br/>
{0} is for the name <br/>
{1} is fot he alias <br/>
{2} is for the struct name as var <br/>
