# Bananalog
Create Log file in python easily with fancy Color !!!!

## Installation
```Bash
pip install banana-log
```

## Usage
1 Import Banalog
```Python
from banana import Banana
```
2 Create logger object
```Python
logger = Banana()
```
3 Modified logger object

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1 Add logtype and defined color

```Python
logger.type_color = {
  "Error": 'Red',
  "Warning": 'Yellow',
  "Assert": 'Magenta'
}
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.2 defined color for date and time

```Python
logger.set_date_time_color_format(date_color='Green', time_color='Blue')
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.3 set time format

```Python
logger.datetime_format = 'format_0' # 'format_0', 'format_1', ... , 'format_4'
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; format_0 dd/mm/yy

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; format_1 Textual month, day and year

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; format_2 mm/dd/yy

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; format_3 Month abbreviation, day and year

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; format_4 dd/mm

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.4 All done Lets start Logging!!!!

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.4.1 Log with out log type
```Python
logger.log("LOG MESSAGE")
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.4.2 Log with log type
```Python
logger.log("LOG MESSAGE", "LOG TYPE")
```


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Example OUTPUT
```Bash
[24/12/2020][15:23:56][Warning]    FIRE!!!
```
sorry I do not know how to add color in github LOL.
