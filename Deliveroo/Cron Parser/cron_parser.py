
import sys


class CronParser:

    def __init__(self, minute, hour, week_day, month, month_day, exec_command):
        self.invalid_command = False
        self.invalid_command_msg = "INVALID COMMAND"
        self.parsed_minute = self.parse_minute(minute)
        self.parsed_hour = self.parse_hour(hour)
        self.parsed_month_day = self.parse_month_day(month_day)
        self.parsed_month = self.parse_month(month)
        self.parsed_week_day = self.parse_week_day(week_day)
        self.exec_command = exec_command
    
    def get_min_max_for_field(self, field_type):
        if field_type == "minute":
            return 0, 59
        
        elif field_type == "hour":
            return 0, 23
        
        elif field_type == "month_day":
            return 1, 31
        
        elif field_type == "month":
            return 1, 12
        
        elif field_type == "week_day":
            return 0,7
    

    def parse_field(self, field, field_type):

        if self.invalid_command:
            return self.invalid_command_msg

        MIN_FIELD_VAL , MAX_FIELD_VAL = self.get_min_max_for_field(field_type)

        # Check if its valid field range
        field_values = set()

        if field.isdigit():
            if not (MIN_FIELD_VAL <= int(field) <= MAX_FIELD_VAL):
                self.invalid_command = True
                return self.invalid_command_msg
            else:
                self.parsed_field = int(field)
        

        if field[0] != "*":
            # check for list separator
            fields_list = field.split(',')

            for field_ele in fields_list:
                if field_ele.isdigit():
                    if int(field_ele) < MIN_FIELD_VAL or int(field_ele) > MAX_FIELD_VAL:
                        self.invalid_command = True
                        return self.invalid_command_msg
                    else:
                        field_values.add(field_ele)
                
                else:
                    # check for range_values
                    if "-" in field_ele:
                        start, end = map(int, field_ele.split('-'))
                        for val in range(start, end+1):
                            if val < MIN_FIELD_VAL or val > MAX_FIELD_VAL:
                                self.invalid_command = True
                                return self.invalid_command_msg
                            else:
                                field_values.add(val)
        
        else:
            if len(field) == 1:
                for val in range(MAX_FIELD_VAL+1):
                    field_values.add(val)
            
            else:
                if field[1] != '/' or len(field) < 3:
                    self.invalid_command = True
                    return self.invalid_command_msg

                # Only single value after step
                field = field[2:]
                
                if field.isdigit():
                    for val in range(MIN_FIELD_VAL, MAX_FIELD_VAL, int(field)):
                        field_values.add(val)
                
                else:
                    fields_list = field.split(',')
                    if len(fields_list) == 1 or '-' in fields_list[0]:
                        self.invalid_command = True
                        return self.invalid_command_msg
                    
                    for index, field_ele in enumerate(fields_list):
                        if field_ele.isdigit():
                            if index == 0:
                                field_values.add(field_ele)
                            else:
                                if MIN_FIELD_VAL <= int(field_ele) <= MAX_FIELD_VAL:
                                    field_values.add(field_ele)
                                else:
                                    self.invalid_command = True
                                    return self.invalid_command_msg
                        else:
                            # check for range_values
                            if "-" in field_ele:
                                start, end = map(int, field_ele.split('-'))
                                if end < start:
                                    self.invalid_command = True
                                    return self.invalid_command_msg
                                
                                for val in range(start, end+1):
                                    if val < MIN_FIELD_VAL or val > MAX_FIELD_VAL:
                                        self.invalid_command = True
                                        return self.invalid_command_msg
                                    else:
                                        field_values.add(val)

        return sorted(map(int, field_values))
    

    def parse_minute(self, minute):
        if self.invalid_command:
            return self.invalid_command_msg
        
        self.parsed_minute_values = self.parse_field(minute, "minute")

        return self.parsed_minute_values
                

    def parse_hour(self, hour):
        if self.invalid_command:
            return self.invalid_command_msg

        self.parsed_hour_values = self.parse_field(hour, "hour")

        return self.parsed_hour_values
    

    def parse_month_day(self, month_day):
        if self.invalid_command:
            return self.invalid_command_msg
        
        self.parsed_month_day_values = self.parse_field(month_day, "month_day")

        return self.parsed_month_day_values
        

    def parse_month(self, month):
        if self.invalid_command:
            return self.invalid_command_msg
        
        self.parsed_month_values = self.parse_field(month, "month")

        return self.parsed_month_values


    def parse_week_day(self, week_day):
        if self.invalid_command:
            return self.invalid_command_msg
        
        self.parsed_week_day_values = self.parse_field(week_day, "week_day")

        return self.parsed_week_day_values
    

    def print_output(self):
        if self.invalid_command:
            print("Given string is not a valid cron expression.")
            return self.invalid_command_msg

        print(f"{'minute':<14}", end="")
        print(*self.parsed_minute_values)

        print(f"{'hour':<14}", end="")
        print(*self.parsed_hour_values)

        print(f"{'day of month':<14}", end="")
        print(*self.parsed_month_day_values)

        print(f"{'month':<14}", end="")
        print(*self.parsed_month_values)

        print(f"{'day of week':<14}", end="")
        print(*self.parsed_week_day_values)

        print(f"{'command':<14}", end="")
        print(self.exec_command)



if __name__ == "__main__":
    arguments = sys.argv
    cron_command = arguments[1]
    minute, hour, month_day, month, week_day, exec_command = cron_command.split()
    cron_parser = CronParser(minute=minute, hour=hour, week_day=week_day, month=month, month_day=month_day, exec_command=exec_command)
    cron_parser.print_output()
    
