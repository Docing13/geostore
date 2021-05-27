from typing import List
import glob
import os

from geo_storer.settings.constants import DATA_PATH, GEOJSON


class FileManager:
    def __init__(self):
        self.f_names = self._names
        self.f_full_names = self._full_names

    @property
    def _full_names(self) -> List[str]:
        """
        :return: names with name and type
        """
        pattern = f"{DATA_PATH}*{GEOJSON}"
        names = [os.path.basename(f) for f in glob.glob(pattern)]

        return names

    @property
    def _names(self) -> List[str]:
        """
        :return: names without type
        """
        names = [n.split('.')[0] for n in self._full_names]
        return names
