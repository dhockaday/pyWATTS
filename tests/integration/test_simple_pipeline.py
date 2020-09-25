import os
import unittest
from time import sleep

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

from pywatts.core.pipeline import Pipeline
from pywatts.core.step import Step
from pywatts.modules.linear_interpolation import LinearInterpolater
from pywatts.modules.missing_value_detection import MissingValueDetector
from pywatts.modules.whitelister import WhiteLister
from pywatts.wrapper.sklearn_wrapper import SKLearnWrapper

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "../..",
    'data',
)


class TestSimplePipeline(unittest.TestCase):

    def setUp(self) -> None:
        # TODO: Look for better solution... This fails since the tests are faster than one second. Consequently all directory have the same timestamp
        sleep(1)

    def test_create_and_run_simple_pipeline(self):
        pipeline = Pipeline()
        white_lister_price = WhiteLister("price_day_ahead")(pipeline)
        white_lister = WhiteLister("load_power_statistics")(pipeline)
        imputer_power_statistics = LinearInterpolater(method="nearest", dim="time",
                                                      name="imputer_power")([white_lister])
        imputer_price = LinearInterpolater(method="nearest", dim="time",
                                           name="imputer_price")([white_lister_price])
        scaler = SKLearnWrapper(StandardScaler())([imputer_price])
        SKLearnWrapper(LinearRegression())([scaler], targets=[imputer_power_statistics, imputer_price], plot=True)
        df = pd.read_csv("data/getting_started_data.csv", index_col="time", sep=",", parse_dates=["time"],
                         infer_datetime_format=True)
        data = pd.read_csv("data/getting_started_data.csv", index_col="time", sep=",", parse_dates=["time"],
                           infer_datetime_format=True)
        train = data[6000:]
        test = data[:6000]
        pipeline.train(train)
        pipeline.test(test)

    def test_run_reloaded_simple_pipeline(self):
        pipeline = Pipeline()

        white_lister_price = WhiteLister("price_day_ahead")(pipeline)
        white_lister = WhiteLister("load_power_statistics")(pipeline)
        imputer_power_statistics = LinearInterpolater(method="nearest", dim="time",
                                                      name="imputer_power")([white_lister])
        imputer_price = LinearInterpolater(method="nearest", dim="time",
                                           name="imputer_price")([white_lister_price])
        scaler = SKLearnWrapper(StandardScaler())([imputer_price])
        SKLearnWrapper(LinearRegression())([scaler], targets=[imputer_price, imputer_power_statistics])

        pipeline.to_folder("./pipe1")
        sleep(1)

        pipeline2 = Pipeline()
        pipeline2.from_folder("./pipe1")
        df = pd.read_csv("data/getting_started_data.csv", index_col="time", sep=",", parse_dates=["time"],
                         infer_datetime_format=True)
        data = pd.read_csv("data/getting_started_data.csv", index_col="time", sep=",", parse_dates=["time"],
                           infer_datetime_format=True)
        train = data[6000:]
        test = data[:6000]
        pipeline2.train(train)
        pipeline2.test(test)

    def test_multiple_same_module_save_load(self):
        pipeline = Pipeline()
        whitelister = WhiteLister(target="price_day_ahead")(pipeline)
        detector = MissingValueDetector()
        detector(pipeline)
        detector([whitelister])

        pipeline.to_folder("./pipe1")
        sleep(1)

        pipeline2 = Pipeline()
        pipeline2.from_folder("./pipe1")

        self.assertEqual(4, pipeline2.computational_graph.number_of_nodes())
        modules = []
        for element in pipeline2.id_to_step.values():
            if isinstance(element, Step) and not element.module in modules:
                modules.append(element.module)
        self.assertEqual(2, len(modules))
        self.assertEqual(4, pipeline2.target_graph.number_of_nodes())
        self.assertEqual(3, pipeline2.computational_graph.number_of_edges())
        self.assertEqual(0, pipeline2.target_graph.number_of_edges())

        data = pd.read_csv("data/getting_started_data.csv", index_col="time", sep=",", parse_dates=["time"],
                           infer_datetime_format=True)
        train = data[6000:]
        test = data[:6000]
        pipeline2.train(train)
        pipeline2.test(test)
