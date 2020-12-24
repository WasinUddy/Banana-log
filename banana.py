import colorama
from colorama import Fore
import datetime


class Banana:

    def __init__(self):
        colorama.init()
        self.datetime_format = 'format_0'

        # Log type color
        self.type_color = {
            "Error": 'Red',
            "Assert": 'Red',
            "Warning": 'Red',
            "Log": 'No_color',
            "Exception": 'Yellow'
        }

        # default date time color
        self.__static_color_format = {
            'date': Fore.RESET,
            'time': Fore.RESET,
        }

        # map color name to colorama color code
        self.__color_variable_map = {
            'Black': Fore.BLACK,
            'Red': Fore.RED,
            'Green': Fore.GREEN,
            'Yellow': Fore.YELLOW,
            'Blue': Fore.BLUE,
            'Magenta': Fore.MAGENTA,
            'Cyan': Fore.CYAN,
            'White': Fore.WHITE,
            'No_color': Fore.RESET

        }

    # print log
    def log(self, log_text, log_type=None):

        # adding bracket to date and time
        print_date = f'[{self.__static_color_format["date"] + self.__get_current_date() + Fore.RESET}]'
        print_time = f'[{self.__static_color_format["time"] + self.__get_curent_time() + Fore.RESET}]'

        # log message
        print_text = f'   {log_text}'

        # if log type is assigned add log type bracket as well
        if log_type is not None:
            print_type = f'[{self.__color_variable_map[self.type_color[log_type]] + log_type + Fore.RESET}]'
            print(print_date + print_time + print_type, print_text)
        else:
            print(print_date + print_time, print_text)

    # set date and time color in log
    def set_date_time_color_format(self, date_color, time_color):
        self.__static_color_format['date'] = self.__color_variable_map[date_color]
        self.__static_color_format['time'] = self.__color_variable_map[time_color]

    # get current date
    def __get_current_date(self):
        today = datetime.date.today()

        # format_0 dd/mm/YY
        if self.datetime_format == 'format_0':
            return today.strftime("%d/%m/%Y")

        # format_1 Textual month, day and year
        if self.datetime_format == 'format_1':
            return today.strftime("%B %d, %Y")

        # format_2 mm/dd/y
        if self.datetime_format == 'format_2':
            return today.strftime("%m/%d/%y")

        # format_3 Month abbreviation, day and year
        if self.datetime_format == 'format_3':
            return today.strftime("%b-%d-%Y")

        # format_4 dd/mm
        if self.datetime_format == 'format_4':
            return today.strftime("%d/%m")

    # get Current time
    def __get_curent_time(self):
        return datetime.datetime.now().strftime("%H:%M:%S")
