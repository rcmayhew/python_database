import os
# need to add database meta data to file


class Builder:
    def __init__(self):
        """
        make files
        database
            Tables
                __init__.py
                list1.py
            __init__.py
            Tables_list.py
        """
        """
        base_Tables_lists = 
        "addTables_list = {"__init__": ("from Database.Tables import __init__", "__init__.__all__")}"
        base_Tables_init = "__all__ = []"
        base_Database_init = "__all__ = ['Tables_list', 'Tables']"
        """
        pass

    @staticmethod
    def amend_database(table_name, extra_data):
        # will need to check the shape to make sure that they can be combined
        prior_list = Builder.load_table(table_name)
        Builder.__write_table__(prior_list + extra_data, table_name)

    @staticmethod
    def __write_table__(data, table_name):
        # need to check that the file is not already
        full_text = table_name + " = " + str(data)
        path = "Database\\Tables\\" + table_name
        file = open(path, 'w')
        file.write(full_text)
        file.close()

    @staticmethod
    def __write_Table_list__(text):
        path = "Database\\Tables\\Tables_list"
        file = open(path, 'w')
        file.write(text)
        file.close()

    @staticmethod
    def __add_to_table_list__(table_name):
        prior_list = Builder.__load_table_list__()
        prior_list.update({table_name: ("from Database.Tables import " + table_name,
                                        table_name + "." + table_name)})
        full_text = str(prior_list)
        Builder.__write_Table_list__(full_text)

    @staticmethod
    def __load_table_list__():
        # This import statements is relative to runtime location
        from Database import Tables_list
        return Tables_list.Tables_list

    @staticmethod
    def load_table(table_name):
        tables = Builder.__load_table_list__()
        exe, eva = tables[table_name]
        exec(exe)
        return eval(eva)

    @staticmethod
    def __add_to_init__(table_name):
        prior_data = Builder.load_table("__init__.py")
        prior_data.append(table_name)
        Builder.__write_Table_list__(prior_data)

    @staticmethod
    def create_table(table_name, data):
        # assume that the table does not exist
        Builder.__add_to_table_list__(table_name)
        Builder.__add_to_init__(table_name)
        Builder.__write_table__(data, table_name)

if __name__ == "__main__":
    pass


"""
to do
check table exist
load table
amend table
write to file
add to dict table
add to init table
"""

"""
error handling
when loading to table already made, ask to create a table with a different name
replace file when the file doesn't exist.
table to load is not in the list of tables
"""


