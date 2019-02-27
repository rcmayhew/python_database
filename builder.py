import os


class Builder:
    def __init__(self, master_dir=os.getcwd(),
                 ):
        self.master_folder = master_dir
        self.loaded_databases =

    #def check database exist
    def database_exist(self, database_name):
        return database_name in database_names

    #edit __init.py__ list
    def edit_all(self, database_name):
        if self.database_exist(database_name):
            pass
    #make the weapon database
