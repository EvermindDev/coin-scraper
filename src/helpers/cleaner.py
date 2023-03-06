import os


class Cleaner:
    @staticmethod
    def remove_files_in_directory(directory):
        """Remove all files in the given directory except .gitkeep"""
        for filename in os.listdir(directory):
            if filename != '.gitkeep':
                os.remove(os.path.join(directory, filename))

    @staticmethod
    def remove_data_file(config):
        """Remove the data file if it exists"""
        filepath = os.path.join(config.DATA_DIRECTORY, config.DATA_FILE_NAME + '.' + config.DATA_FILE_FORMAT)
        if os.path.exists(filepath):
            os.remove(filepath)

    @staticmethod
    def data_cleanup(config):
        data_dir = config.DATA_DIRECTORY
        Cleaner.remove_files_in_directory(os.path.join(data_dir, 'historical'))
        Cleaner.remove_files_in_directory(os.path.join(data_dir, 'logo'))
        Cleaner.remove_data_file(config)
