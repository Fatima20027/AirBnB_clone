import os
import json
import datetime


class FileStorage:
    """A class for storing and loading objects to/from a JSON file."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns:
            dict: A dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes stored objects to the JSON file.
        """
        jso_dict = {}

        for ky in FileStorage.__objects:
            jso_dict[ky] = FileStorage.__objects[ky].to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(jso_dict, f)

    def reload(self):
        """
        Deserializes objects from the JSON file into storage.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                for line in file:
                    try:
                        json_data = json.loads(line)
                        for key, value in json_data.items():
                            clas_nm, obj_id = key.split('.')
                            modl = __import__(
                                'models.' + clas_nm, fromlist=[clas_nm])
                            cls = getattr(modl, clas_nm)
                            value["created_at"] = datetime.datetime.strptime(
                                value["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                            value["updated_at"] = datetime.datetime.strptime(
                                value["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                            self.__objects[key] = cls(**value)
                    except Exception as e:
                        print(f"Error loading object: {e}")
