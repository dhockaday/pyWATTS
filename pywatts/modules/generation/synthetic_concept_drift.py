from typing import List, Dict, Callable

import cloudpickle
import numpy as np
import pandas as pd
import xarray as xr

from pywatts_pipeline.core.transformer.base import BaseTransformer
from pywatts_pipeline.core.util.filemanager import FileManager
from pywatts_pipeline.utils._xarray_time_series_utils import numpy_to_xarray, _get_time_indexes


class DriftInformation:
    """
    The drift information describe one concept drift.
    :param manipulator: A callable that returns a one-dimensional numpy array which is added on the time series.
    :type manipulator: Callable[[int], np.array]
    :param position: The start position of the concept drift.
    :type position: pd.Timestamp
    :param length: The length of the inserted concept drift.
    :type length: int
    """

    def __init__(self, manipulator: Callable[[int], np.array], position: pd.Timestamp, length: int):
        self.manipulator = manipulator
        self.position = position
        self.length = length

    def get_drift(self):
        """
        This function returns the array that contains the concept drift.
        :return: The array containing the data for inserting a concept drift.
        :rtype: np.array
        """
        return self.manipulator(self.length).reshape(
            (self.length,))


class SyntheticConcecptDriftInsertion(BaseTransformer):
    """
    Module for inserting synthetic concept drifts in the input time series. The inserted concept drifts are specified by
    the drift information.
    :param drift_information: A list of drift information. Each drift information specifies the position, the kind, and
        the length of a concept drift.
    :type drift_information: List[DriftInformation]
    """

    def __init__(self, drift_information: List[DriftInformation], name: str = "Concept Drift Generation"):
        super().__init__(name)
        self.drift_information = drift_information

    def get_params(self) -> Dict[str, object]:
        """
        Get parameters of the SyntheticConceptDriftGeneration module
        :return: Dict containing all parameters.
        :rtype: Dict[str, object]
        """
        return {
            "drift_information": self.drift_information
        }

    def set_params(self, drift_information: List[DriftInformation] = None):
        """
        Set parameters of the SyntheticConcecptDriftGeneration module
        :param drift_information: A list of drift information. Each drift information specifies the position, the kind,
         and the length of a concept drift.
        :type drift_information: List[DriftInformation]
        """
        if drift_information is not None:
            self.drift_information = drift_information

    def transform(self, x: xr.DataArray) -> xr.DataArray:
        """
        This method inserts the concept drift in the input time series.
        :param x: Array to be transformed.
        :type x: xr.DataArray
        :return: Transformed array.
        :rtype: Dict[str, xr.DataArray]
        """
        seq = x.values
        index = x[_get_time_indexes(x)[0]]
        freq = pd.Timestamp(index.values[1]) - pd.Timestamp(index.values[0])

        drift_seq = np.zeros(seq.shape)
        for drift in self.drift_information:
            end_drift = drift.position + freq * (drift.length - 1)
            if index.values[0] > end_drift:
                # Add the last value to the drift_seq
                pass
            elif index.values[-1] < drift.position:
                # Drift has not started yet
                pass
            else:
                # This mask indicates the values that should be updated
                change_mask_input = (index.values >= drift.position) & (index.values <= end_drift)
                d_seq = pd.Series(drift.get_drift(), index=pd.date_range(drift.position, end_drift, freq=freq))
                mask_drift = ((d_seq.index.values >= index.values[0]) & (d_seq.index.values <= index.values[-1]))
                drift_seq[change_mask_input] += d_seq[mask_drift]
                drift_seq[index.values > end_drift] += d_seq.values[-1]
        result = drift_seq + seq
        return numpy_to_xarray(result, x)

    def save(self, fm: FileManager) -> Dict:
        json = {"params": {},
                "name": self.name,
                "class": self.__class__.__name__,
                "module": self.__module__}

        file_path = fm.get_path(f'{self.name}_drift_information.pickle')
        with open(file_path, 'wb') as outfile:
            cloudpickle.dump(self, file=outfile)
        json["drift_information"] = file_path
        return json

    @classmethod
    def load(cls, load_information: Dict):
        name = load_information["name"]
        with open(load_information[f"drift_information"], 'rb') as pickle_file:
            drift_information = cloudpickle.load(pickle_file)
        return cls(name=name, drift_information=drift_information)
