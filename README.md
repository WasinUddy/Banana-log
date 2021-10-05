# Bananalog

Create Log file in python easily with fancy Color !!!!

## Installation

```bash
pip install banana-log
```

## Usage

### 1. Import Banalog

```python
from bananalog.banana import Banana
```

### 2. Create logger object

```python
logger = Banana()
```

### 3. Modified logger object

3.1 Add logtype and defined color

```python
logger.type_color = {
  "Error": 'Red',
  "Warning": 'Yellow',
  "Assert": 'Magenta'
}
```

3.2 defined color for date and time

```python
logger.set_date_time_color_format(date_color='Green', time_color='Blue')
```

3.3 set time format

```python
logger.datetime_format = 'format_0' # 'format_0', 'format_1', ... , 'format_4'
```

Formats

- format_0 dd/mm/yy

- format_1 Textual month, day and year

- format_2 mm/dd/yy

- format_3 Month abbreviation, day and year

- format_4 dd/mm

  3.4 All done Lets start Logging!!!!

- Log with out log type

```python
logger.log("LOG MESSAGE")
```

- Log with log type

```python
logger.log("LOG MESSAGE", "LOG TYPE")
```

### Example OUTPUT

```
[24/12/2020][15:23:56][Warning]    FIRE!!!
```
