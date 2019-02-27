import os
#need to add database meta data to file

class Builder:
    def __init__(self, master_dir=os.getcwd(),
                 prior_database_file=None):
        self.master_folder = master_dir
        self.loaded_databases = prior_database_file
        self.databases = {}
        self.load_databases()

    #finds the list of databases in list_of_db.py
    #it should be in the main folder of the database
    def load_databases(self):
        if self.loaded_databases is None:
            self.databases = {}
        else:
            try:
                import list_of_db as valid_dbs
                self.databases = valid_dbs.db
            except ImportError:
                print("No valid databases at %s" %
                      self.loaded_databases)
                self.databases = {}

    #def check database exist
    def database_exist(self, database_name):
        return database_name in self.databases

    #edit __init.py__ list
    def edit_database_list(self, database_name):
        if self.database_exist(database_name):
            pass
        else:
            #will remove the closing bracket and then add the
            #needed info
            pass

    #add data to the list
    #can pull data, amend, then reprint
    #would rather amend the print, but error checking will be hard
    def amend_database(self):
        #need to pull the prior database or atleast pull the shape
        pass
