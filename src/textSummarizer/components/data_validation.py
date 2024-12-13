from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml,create_directory

import os

class DataValidation:
    def __init__(self, config):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            missing_files = []

            for required_file in self.config.ALL_REQUIRED_FILES:
                if required_file not in all_files:
                    missing_files.append(required_file)

            if missing_files:
                with open(self.config.STATUS_FILE, "w") as f:
                    f.write("The following required files are missing:\n")
                    f.writelines(f"- {file}\n" for file in missing_files)
                return False
            else:
                with open(self.config.STATUS_FILE, "w") as f:
                    f.write("All required files are present.")
                return True

        except Exception as e:
            raise e
