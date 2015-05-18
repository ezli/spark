#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# DO NOT MODIFY THIS FILE! It was generated by _shared_params_code_gen.py.

from pyspark.ml.param import Param, Params


class HasMaxIter(Params):
    """
    Mixin for param maxIter: max number of iterations (>= 0).
    """

    # a placeholder to make it appear in the generated doc
    maxIter = Param(Params._dummy(), "maxIter", "max number of iterations (>= 0)")

    def __init__(self):
        super(HasMaxIter, self).__init__()
        #: param for max number of iterations (>= 0)
        self.maxIter = Param(self, "maxIter", "max number of iterations (>= 0)")
        if None is not None:
            self._setDefault(maxIter=None)

    def setMaxIter(self, value):
        """
        Sets the value of :py:attr:`maxIter`.
        """
        self._paramMap[self.maxIter] = value
        return self

    def getMaxIter(self):
        """
        Gets the value of maxIter or its default value.
        """
        return self.getOrDefault(self.maxIter)


class HasRegParam(Params):
    """
    Mixin for param regParam: regularization parameter (>= 0).
    """

    # a placeholder to make it appear in the generated doc
    regParam = Param(Params._dummy(), "regParam", "regularization parameter (>= 0)")

    def __init__(self):
        super(HasRegParam, self).__init__()
        #: param for regularization parameter (>= 0)
        self.regParam = Param(self, "regParam", "regularization parameter (>= 0)")
        if None is not None:
            self._setDefault(regParam=None)

    def setRegParam(self, value):
        """
        Sets the value of :py:attr:`regParam`.
        """
        self._paramMap[self.regParam] = value
        return self

    def getRegParam(self):
        """
        Gets the value of regParam or its default value.
        """
        return self.getOrDefault(self.regParam)


class HasFeaturesCol(Params):
    """
    Mixin for param featuresCol: features column name.
    """

    # a placeholder to make it appear in the generated doc
    featuresCol = Param(Params._dummy(), "featuresCol", "features column name")

    def __init__(self):
        super(HasFeaturesCol, self).__init__()
        #: param for features column name
        self.featuresCol = Param(self, "featuresCol", "features column name")
        if 'features' is not None:
            self._setDefault(featuresCol='features')

    def setFeaturesCol(self, value):
        """
        Sets the value of :py:attr:`featuresCol`.
        """
        self._paramMap[self.featuresCol] = value
        return self

    def getFeaturesCol(self):
        """
        Gets the value of featuresCol or its default value.
        """
        return self.getOrDefault(self.featuresCol)


class HasLabelCol(Params):
    """
    Mixin for param labelCol: label column name.
    """

    # a placeholder to make it appear in the generated doc
    labelCol = Param(Params._dummy(), "labelCol", "label column name")

    def __init__(self):
        super(HasLabelCol, self).__init__()
        #: param for label column name
        self.labelCol = Param(self, "labelCol", "label column name")
        if 'label' is not None:
            self._setDefault(labelCol='label')

    def setLabelCol(self, value):
        """
        Sets the value of :py:attr:`labelCol`.
        """
        self._paramMap[self.labelCol] = value
        return self

    def getLabelCol(self):
        """
        Gets the value of labelCol or its default value.
        """
        return self.getOrDefault(self.labelCol)


class HasPredictionCol(Params):
    """
    Mixin for param predictionCol: prediction column name.
    """

    # a placeholder to make it appear in the generated doc
    predictionCol = Param(Params._dummy(), "predictionCol", "prediction column name")

    def __init__(self):
        super(HasPredictionCol, self).__init__()
        #: param for prediction column name
        self.predictionCol = Param(self, "predictionCol", "prediction column name")
        if 'prediction' is not None:
            self._setDefault(predictionCol='prediction')

    def setPredictionCol(self, value):
        """
        Sets the value of :py:attr:`predictionCol`.
        """
        self._paramMap[self.predictionCol] = value
        return self

    def getPredictionCol(self):
        """
        Gets the value of predictionCol or its default value.
        """
        return self.getOrDefault(self.predictionCol)


class HasProbabilityCol(Params):
    """
    Mixin for param probabilityCol: Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities..
    """

    # a placeholder to make it appear in the generated doc
    probabilityCol = Param(Params._dummy(), "probabilityCol", "Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities.")

    def __init__(self):
        super(HasProbabilityCol, self).__init__()
        #: param for Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities.
        self.probabilityCol = Param(self, "probabilityCol", "Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities.")
        if 'probability' is not None:
            self._setDefault(probabilityCol='probability')

    def setProbabilityCol(self, value):
        """
        Sets the value of :py:attr:`probabilityCol`.
        """
        self._paramMap[self.probabilityCol] = value
        return self

    def getProbabilityCol(self):
        """
        Gets the value of probabilityCol or its default value.
        """
        return self.getOrDefault(self.probabilityCol)


class HasRawPredictionCol(Params):
    """
    Mixin for param rawPredictionCol: raw prediction (a.k.a. confidence) column name.
    """

    # a placeholder to make it appear in the generated doc
    rawPredictionCol = Param(Params._dummy(), "rawPredictionCol", "raw prediction (a.k.a. confidence) column name")

    def __init__(self):
        super(HasRawPredictionCol, self).__init__()
        #: param for raw prediction (a.k.a. confidence) column name
        self.rawPredictionCol = Param(self, "rawPredictionCol", "raw prediction (a.k.a. confidence) column name")
        if 'rawPrediction' is not None:
            self._setDefault(rawPredictionCol='rawPrediction')

    def setRawPredictionCol(self, value):
        """
        Sets the value of :py:attr:`rawPredictionCol`.
        """
        self._paramMap[self.rawPredictionCol] = value
        return self

    def getRawPredictionCol(self):
        """
        Gets the value of rawPredictionCol or its default value.
        """
        return self.getOrDefault(self.rawPredictionCol)


class HasInputCol(Params):
    """
    Mixin for param inputCol: input column name.
    """

    # a placeholder to make it appear in the generated doc
    inputCol = Param(Params._dummy(), "inputCol", "input column name")

    def __init__(self):
        super(HasInputCol, self).__init__()
        #: param for input column name
        self.inputCol = Param(self, "inputCol", "input column name")
        if None is not None:
            self._setDefault(inputCol=None)

    def setInputCol(self, value):
        """
        Sets the value of :py:attr:`inputCol`.
        """
        self._paramMap[self.inputCol] = value
        return self

    def getInputCol(self):
        """
        Gets the value of inputCol or its default value.
        """
        return self.getOrDefault(self.inputCol)


class HasInputCols(Params):
    """
    Mixin for param inputCols: input column names.
    """

    # a placeholder to make it appear in the generated doc
    inputCols = Param(Params._dummy(), "inputCols", "input column names")

    def __init__(self):
        super(HasInputCols, self).__init__()
        #: param for input column names
        self.inputCols = Param(self, "inputCols", "input column names")
        if None is not None:
            self._setDefault(inputCols=None)

    def setInputCols(self, value):
        """
        Sets the value of :py:attr:`inputCols`.
        """
        self._paramMap[self.inputCols] = value
        return self

    def getInputCols(self):
        """
        Gets the value of inputCols or its default value.
        """
        return self.getOrDefault(self.inputCols)


class HasOutputCol(Params):
    """
    Mixin for param outputCol: output column name.
    """

    # a placeholder to make it appear in the generated doc
    outputCol = Param(Params._dummy(), "outputCol", "output column name")

    def __init__(self):
        super(HasOutputCol, self).__init__()
        #: param for output column name
        self.outputCol = Param(self, "outputCol", "output column name")
        if None is not None:
            self._setDefault(outputCol=None)

    def setOutputCol(self, value):
        """
        Sets the value of :py:attr:`outputCol`.
        """
        self._paramMap[self.outputCol] = value
        return self

    def getOutputCol(self):
        """
        Gets the value of outputCol or its default value.
        """
        return self.getOrDefault(self.outputCol)


class HasNumFeatures(Params):
    """
    Mixin for param numFeatures: number of features.
    """

    # a placeholder to make it appear in the generated doc
    numFeatures = Param(Params._dummy(), "numFeatures", "number of features")

    def __init__(self):
        super(HasNumFeatures, self).__init__()
        #: param for number of features
        self.numFeatures = Param(self, "numFeatures", "number of features")
        if None is not None:
            self._setDefault(numFeatures=None)

    def setNumFeatures(self, value):
        """
        Sets the value of :py:attr:`numFeatures`.
        """
        self._paramMap[self.numFeatures] = value
        return self

    def getNumFeatures(self):
        """
        Gets the value of numFeatures or its default value.
        """
        return self.getOrDefault(self.numFeatures)


class HasCheckpointInterval(Params):
    """
    Mixin for param checkpointInterval: checkpoint interval (>= 1).
    """

    # a placeholder to make it appear in the generated doc
    checkpointInterval = Param(Params._dummy(), "checkpointInterval", "checkpoint interval (>= 1)")

    def __init__(self):
        super(HasCheckpointInterval, self).__init__()
        #: param for checkpoint interval (>= 1)
        self.checkpointInterval = Param(self, "checkpointInterval", "checkpoint interval (>= 1)")
        if None is not None:
            self._setDefault(checkpointInterval=None)

    def setCheckpointInterval(self, value):
        """
        Sets the value of :py:attr:`checkpointInterval`.
        """
        self._paramMap[self.checkpointInterval] = value
        return self

    def getCheckpointInterval(self):
        """
        Gets the value of checkpointInterval or its default value.
        """
        return self.getOrDefault(self.checkpointInterval)


class HasSeed(Params):
    """
    Mixin for param seed: random seed.
    """

    # a placeholder to make it appear in the generated doc
    seed = Param(Params._dummy(), "seed", "random seed")

    def __init__(self):
        super(HasSeed, self).__init__()
        #: param for random seed
        self.seed = Param(self, "seed", "random seed")
        if None is not None:
            self._setDefault(seed=None)

    def setSeed(self, value):
        """
        Sets the value of :py:attr:`seed`.
        """
        self._paramMap[self.seed] = value
        return self

    def getSeed(self):
        """
        Gets the value of seed or its default value.
        """
        return self.getOrDefault(self.seed)


class HasTol(Params):
    """
    Mixin for param tol: the convergence tolerance for iterative algorithms.
    """

    # a placeholder to make it appear in the generated doc
    tol = Param(Params._dummy(), "tol", "the convergence tolerance for iterative algorithms")

    def __init__(self):
        super(HasTol, self).__init__()
        #: param for the convergence tolerance for iterative algorithms
        self.tol = Param(self, "tol", "the convergence tolerance for iterative algorithms")
        if None is not None:
            self._setDefault(tol=None)

    def setTol(self, value):
        """
        Sets the value of :py:attr:`tol`.
        """
        self._paramMap[self.tol] = value
        return self

    def getTol(self):
        """
        Gets the value of tol or its default value.
        """
        return self.getOrDefault(self.tol)


class HasStepSize(Params):
    """
    Mixin for param stepSize: Step size to be used for each iteration of optimization..
    """

    # a placeholder to make it appear in the generated doc
    stepSize = Param(Params._dummy(), "stepSize", "Step size to be used for each iteration of optimization.")

    def __init__(self):
        super(HasStepSize, self).__init__()
        #: param for Step size to be used for each iteration of optimization.
        self.stepSize = Param(self, "stepSize", "Step size to be used for each iteration of optimization.")
        if None is not None:
            self._setDefault(stepSize=None)

    def setStepSize(self, value):
        """
        Sets the value of :py:attr:`stepSize`.
        """
        self._paramMap[self.stepSize] = value
        return self

    def getStepSize(self):
        """
        Gets the value of stepSize or its default value.
        """
        return self.getOrDefault(self.stepSize)


class DecisionTreeParams(Params):
    """
    Mixin for Decision Tree parameters.
    """

    # a placeholder to make it appear in the generated doc
    maxDepth = Param(Params._dummy(), "maxDepth", "Maximum depth of the tree. (>= 0) E.g., depth 0 means 1 leaf node; depth 1 means 1 internal node + 2 leaf nodes.")
    maxBins = Param(Params._dummy(), "maxBins", "Max number of bins for discretizing continuous features.  Must be >=2 and >= number of categories for any categorical feature.")
    minInstancesPerNode = Param(Params._dummy(), "minInstancesPerNode", "Minimum number of instances each child must have after split. If a split causes the left or right child to have fewer than minInstancesPerNode, the split will be discarded as invalid. Should be >= 1.")
    minInfoGain = Param(Params._dummy(), "minInfoGain", "Minimum information gain for a split to be considered at a tree node.")
    maxMemoryInMB = Param(Params._dummy(), "maxMemoryInMB", "Maximum memory in MB allocated to histogram aggregation.")
    cacheNodeIds = Param(Params._dummy(), "cacheNodeIds", "If false, the algorithm will pass trees to executors to match instances with nodes. If true, the algorithm will cache node IDs for each instance. Caching can speed up training of deeper trees.")

    def __init__(self):
        super(DecisionTreeParams, self).__init__()
        #: param for Maximum depth of the tree. (>= 0) E.g., depth 0 means 1 leaf node; depth 1 means 1 internal node + 2 leaf nodes.
        self.maxDepth = Param(self, "maxDepth", "Maximum depth of the tree. (>= 0) E.g., depth 0 means 1 leaf node; depth 1 means 1 internal node + 2 leaf nodes.")
        #: param for Max number of bins for discretizing continuous features.  Must be >=2 and >= number of categories for any categorical feature.
        self.maxBins = Param(self, "maxBins", "Max number of bins for discretizing continuous features.  Must be >=2 and >= number of categories for any categorical feature.")
        #: param for Minimum number of instances each child must have after split. If a split causes the left or right child to have fewer than minInstancesPerNode, the split will be discarded as invalid. Should be >= 1.
        self.minInstancesPerNode = Param(self, "minInstancesPerNode", "Minimum number of instances each child must have after split. If a split causes the left or right child to have fewer than minInstancesPerNode, the split will be discarded as invalid. Should be >= 1.")
        #: param for Minimum information gain for a split to be considered at a tree node.
        self.minInfoGain = Param(self, "minInfoGain", "Minimum information gain for a split to be considered at a tree node.")
        #: param for Maximum memory in MB allocated to histogram aggregation.
        self.maxMemoryInMB = Param(self, "maxMemoryInMB", "Maximum memory in MB allocated to histogram aggregation.")
        #: param for If false, the algorithm will pass trees to executors to match instances with nodes. If true, the algorithm will cache node IDs for each instance. Caching can speed up training of deeper trees.
        self.cacheNodeIds = Param(self, "cacheNodeIds", "If false, the algorithm will pass trees to executors to match instances with nodes. If true, the algorithm will cache node IDs for each instance. Caching can speed up training of deeper trees.")

    def setMaxDepth(self, value):
        """
        Sets the value of :py:attr:`maxDepth`.
        """
        self._paramMap[self.maxDepth] = value
        return self

    def getMaxDepth(self):
        """
        Gets the value of maxDepth or its default value.
        """
        return self.getOrDefault(self.maxDepth)

    def setMaxBins(self, value):
        """
        Sets the value of :py:attr:`maxBins`.
        """
        self._paramMap[self.maxBins] = value
        return self

    def getMaxBins(self):
        """
        Gets the value of maxBins or its default value.
        """
        return self.getOrDefault(self.maxBins)

    def setMinInstancesPerNode(self, value):
        """
        Sets the value of :py:attr:`minInstancesPerNode`.
        """
        self._paramMap[self.minInstancesPerNode] = value
        return self

    def getMinInstancesPerNode(self):
        """
        Gets the value of minInstancesPerNode or its default value.
        """
        return self.getOrDefault(self.minInstancesPerNode)

    def setMinInfoGain(self, value):
        """
        Sets the value of :py:attr:`minInfoGain`.
        """
        self._paramMap[self.minInfoGain] = value
        return self

    def getMinInfoGain(self):
        """
        Gets the value of minInfoGain or its default value.
        """
        return self.getOrDefault(self.minInfoGain)

    def setMaxMemoryInMB(self, value):
        """
        Sets the value of :py:attr:`maxMemoryInMB`.
        """
        self._paramMap[self.maxMemoryInMB] = value
        return self

    def getMaxMemoryInMB(self):
        """
        Gets the value of maxMemoryInMB or its default value.
        """
        return self.getOrDefault(self.maxMemoryInMB)

    def setCacheNodeIds(self, value):
        """
        Sets the value of :py:attr:`cacheNodeIds`.
        """
        self._paramMap[self.cacheNodeIds] = value
        return self

    def getCacheNodeIds(self):
        """
        Gets the value of cacheNodeIds or its default value.
        """
        return self.getOrDefault(self.cacheNodeIds)

