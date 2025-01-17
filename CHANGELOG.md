## 0.3.1 - Unreleased

### Added
* Add alpha to rolling mean ([#225](https://github.com/KIT-IAI/pyWATTS/issues/225))
* RiverDriftDetectionCondition for wrapping the river drift detection algorithms ([#221](https://github.com/KIT-IAI/pyWATTS/issues/221))
* Add a module for merging shifted time series ([#2179](https://github.com/KIT-IAI/pyWATTS/issues/219))
* Add a module for statistic feature extraction ([#217](https://github.com/KIT-IAI/pyWATTS/issues/217))
* Add a tsne summary module ([#229](https://github.com/KIT-IAI/pyWATTS/issues/229))
* Add a module for inserting synthetic concept drift ([#226](https://github.com/KIT-IAI/pyWATTS/issues/226))
* Add a TSTR Summary ([#232](https://github.com/KIT-IAI/pyWATTS/issues/232))
* Add a confusion matrix summary ([#236](https://github.com/KIT-IAI/pyWATTS/issues/236))
* Add a module to insert unusual behaviour into a time series ([#240](https://github.com/KIT-IAI/pyWATTS/issues/240))
* Add F1Score Summary ([#234](https://github.com/KIT-IAI/pyWATTS/issues/234))
* Add a discriminative score summary ([#238](https://github.com/KIT-IAI/pyWATTS/issues/238))
* Add NPY Callback ([#247](https://github.com/KIT-IAI/pyWATTS/issues/247))

### Changed
* Make the inputs of the PNN more flexible ([#228](https://github.com/KIT-IAI/pyWATTS/issues/228))


### Fixed
* Enabled installation for macOS([#241](https://github.com/KIT-IAI/pyWATTS/issues/241))
* Adapt CD Condition to new river api ([#249](https://github.com/KIT-IAI/pyWATTS/issues/249))

## 0.3.0 - 2022-31-03

### Added
* Add average module for pre-processing ([#166](https://github.com/KIT-IAI/pyWATTS/issues/166))
* Metric can be calculated on cutouts ([#149](https://github.com/KIT-IAI/pyWATTS/issues/149))
* Add custom scaler module for pre-processing ([#167](https://github.com/KIT-IAI/pyWATTS/issues/167))
* Add a MASE Summary ([#148](https://github.com/KIT-IAI/pyWATTS/issues/148))
* Add ensemble module for post-processing ([#165](https://github.com/KIT-IAI/pyWATTS/issues/165))
* Online Start Feature ([#189](https://github.com/KIT-IAI/pyWATTS/issues/189))
* Enable Multiple RefitConditions ([#192](https://github.com/KIT-IAI/pyWATTS/issues/192))
* Periodic Refit Condition ([#192](https://github.com/KIT-IAI/pyWATTS/issues/192))
* Add AnomalyGeneration modules ([#195](https://github.com/KIT-IAI/pyWATTS/issues/195))
* Add get_min_data method in modules to enable them to specify how much data they need. ([#147](https://github.com/KIT-IAI/pyWATTS/issues/147))

### Changed
* Retraining is triggered after all steps are transformed ([#117](https://github.com/KIT-IAI/pyWATTS/issues/117))
* The sklean-wrapper includes now methods based on the SelectorMixin ([#185](https://github.com/KIT-IAI/pyWATTS/issues/185))


### Fixed
* Try to handle non matching shapes in metrics. If not possible raise an exception.  ([#154](https://github.com/KIT-IAI/pyWATTS/issues/154))
* Fixed Sampler-module, samples now in forwarding direction ([#174](https://github.com/KIT-IAI/pyWATTS/issues/174))
* Fixed wrong check of if summary should be returned in _run method of pipeline ([#157](https://github.com/KIT-IAI/pyWATTS/issues/157))
* Fixed Pipeline.to_folder() for modules that store parameters in numpy format by adding a special JSON-encoder for types that are not json-serializable by default ([#175](https://github.com/KIT-IAI/pyWATTS/issues/175))
* Added missing summaries to pywatts.summaries.__init__.py ([#183](https://github.com/KIT-IAI/pyWATTS/issues/183))
* Naming in the Metric Summaries  ([#193](https://github.com/KIT-IAI/pyWATTS/issues/193))
* Fixed wrong time dimension name in ComputationMode.Transform ([#199](https://github.com/KIT-IAI/pyWATTS/issues/199))
* Fixed online execution of subpipeline ([#203](https://github.com/KIT-IAI/pyWATTS/issues/203))
* Enable to store a Keras Model with custom objects as custom loss functions ([#17](https://github.com/KIT-IAI/pyWATTS/issues/17))
* Fixed online execution of stacked pipelines ([#213](https://github.com/KIT-IAI/pyWATTS/issues/213))

### Deprecated

### Removed
* MAECalculator and RMSECalculator.

## 0.2.0 - 2021-30-09

### Added
* Logger for modules is defined in Base  ([#77](https://github.com/KIT-IAI/pyWATTS/issues/77))
* Add parameters to RMSECalculator so that it can caluclate a sliding rmse too. ([#23](https://github.com/KIT-IAI/pyWATTS/issues/23))
* StatsmodelTimeSeriesModelWrapper.  ([#29](https://github.com/KIT-IAI/pyWATTS/issues/29))
* Optional pipeline path and less aggressive FileManager directory creation ([#94](https://github.com/KIT-IAI/pyWATTS/issues/94)) 
* Add fit_method parameter to FunctionModule ([#93](https://github.com/KIT-IAI/pyWATTS/issues/93))
* SummaryFunctionality ([#34](https://github.com/KIT-IAI/pyWATTS/issues/34))
  * BaseSummary Module, from which summary module should inherit.
  * SummaryStep, which handles the execution of the summary module.
  * RMSESummary and RollingRMSE as consequence of the usage of summary modules.
  * Time needed by the fit method is recorded by the summary. (Part of the summary.md)
  * Section about how to get results of a pyWATTS pipeline.
  * Enable more generic usage of summaries, including different output formats ([#129](https://github.com/KIT-IAI/pyWATTS/issues/129))
* Add MAE as another summary. ([#99](https://github.com/KIT-IAI/pyWATTS/issues/99))
* Add summary parameter to train and test to ensure backward compatibility. ([#127](https://github.com/KIT-IAI/pyWATTS/issues/127))
* Add Min amd Max as new summaries ([#105](https://github.com/KIT-IAI/pyWATTS/issues/105))
* Add MAPE as new summary ([#104](https://github.com/KIT-IAI/pyWATTS/issues/104))
* Add a RunSetting for setting run specific settings in the steps ([#150](https://github.com/KIT-IAI/pyWATTS/issues/150))
* Add Slicer to slice data in a numpy like manner, i.e. a[start:end] ([#152](https://github.com/KIT-IAI/pyWATTS/issues/152))

### Changed
* Remove parameter step.stop. Instead we call the method _should_stop on the previous steps. ([#25](https://github.com/KIT-IAI/pyWATTS/issues/25))
* Change metrics to summaries ([#115](https://github.com/KIT-IAI/pyWATTS/issues/115))
* Change indeces and indices to indexes  ([#102](https://github.com/KIT-IAI/pyWATTS/issues/102))
* Restructure the modules folder  ([#114](https://github.com/KIT-IAI/pyWATTS/issues/114))

### Deprecated
* Usage of RMSECalculator. Will be removed in version 0.3. Calculation of metrics should be a summary and not a module. ([#34](https://github.com/KIT-IAI/pyWATTS/issues/34))
* Usage of MAECalculator. Will be removed in version 0.3. Calculation of metrics should be a summary and not a module. ([#115](https://github.com/KIT-IAI/pyWATTS/issues/115))

### Fixed
* Converts the input for the keras model in the kerasWrapper from xr.Dataarray to np.array ([#97](https://github.com/KIT-IAI/pyWATTS/issues/97))
* Missing call of _get_rolling in Rolling Base  ([#76](https://github.com/KIT-IAI/pyWATTS/issues/76))
* Fix save and load of keras Wrapper  ([#91](https://github.com/KIT-IAI/pyWATTS/issues/91))
* Import of pytorchWrapper via wrapper.__init__
* Fix the mask for weekends and public holidays in rolling_base  ([#107](https://github.com/KIT-IAI/pyWATTS/issues/107))
* Improved Online Learning Performance  ([#18](https://github.com/KIT-IAI/pyWATTS/issues/18))
  * Add a cache for the most recent value, since this value is often requested by successing modules.
  * Remove unecessary copies
  * Avoid uncessary execution in should_stop 
  * Improve performance in sample_module
  * Improve performance in trend_extraction
  * Callbacks are only executed if the step is finished. No intermediate results are plotted.
* Fix the extracted time index in rolling RMSE  ([#124](https://github.com/KIT-IAI/pyWATTS/issues/124))
* Use raise from if an exception is raise because an other is raised before for retaining the original stack trace  ([#123](https://github.com/KIT-IAI/pyWATTS/issues/123))
* Function module crashed because of missing is_fitted = True ([#144](https://github.com/KIT-IAI/pyWATTS/issues/144))



## 0.1.0 - 2021-25-03

### Added

  * Added integration tests to github actions by executing the examples in root directory ([#47](https://github.com/KIT-IAI/pyWATTS/issues/47))
  * Implementation of the profile neural network ([#71](https://github.com/KIT-IAI/pyWATTS/issues/47))
  * Imports from the init files for exception, modules, and wrapper. ([#27](https://github.com/KIT-IAI/pyWATTS/issues/27))
  * Add rolling_variance, rolling_kurtosis, rolling_skewness. ([#28](https://github.com/KIT-IAI/pyWATTS/issues/28))
  * Select the kind of groupby in the rolling function by an enum ([#28](https://github.com/KIT-IAI/pyWATTS/issues/28))

### Changed

  * Remove plot, to_csv, summary. Instead we add a callback functionality. Additional, we provide some basic callbacks. ([#16](https://github.com/KIT-IAI/pyWATTS/issues/16))
  * Change of the API  ([#16](https://github.com/KIT-IAI/pyWATTS/issues/16))
    * Use keyword arguments instead of list for determining the input of modules. keyword that start with target are only fed into the fit function.
    * Adapt the modules, so that they are compatible with the new API
    * Use xarray DataArray instead of xr.DataSets for exchaning the data
    * Remove collect step, since through the new API they are not necessary any more
    * Add ResultStep, for selecting the desired result if a moudule provides multiple ones.
    * Remove whitelister, instead columns can be selected via square brackets.
  * CalendarExtraction: Remove encoding, for each encoding and suitable feature a new feature is created. 
    E.g. month_sine. Additionally further calendar features are added. E.g. monday, tuesday, .. and cos encodings. For 
    the different features, a enum type is defined.


### Deprecated

### Fixed

  * Fixed pipeline crashing in RMSE module because of wrong time index ([#39](https://github.com/KIT-IAI/pyWATTS/issues/39))
  * Fixed bracket operator not working for steps within the pipeline ([#42](https://github.com/KIT-IAI/pyWATTS/issues/42))
  * Fixed dict objects could not be passed to pipeline ([#43](https://github.com/KIT-IAI/pyWATTS/issues/43))
  * Fixed old parameter in sample_module  ([#67](https://github.com/KIT-IAI/pyWATTS/issues/67))
  * Fixed array creation in trend extraciont ([#69](https://github.com/KIT-IAI/pyWATTS/issues/69))

## [0.0.1] - 2021-MM-DD

  * Train and test methods of pipeline returns data
  * Add PipelineStep for better management of Subpipelining
  * Replace pipeline.run with pipeline.train and pipeline.test
  * Remove CSVReader and add a parameter data to pipeline.run() method. 
    Data can either be a pandas dataframe or an xarray dataset.
