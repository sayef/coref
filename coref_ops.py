from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf
from tensorflow.python import pywrap_tensorflow

_dir = os.path.dirname(os.path.abspath(__file__))

coref_op_library = tf.load_op_library(os.path.join(_dir, "coref_kernels.so"))

extract_spans = coref_op_library.extract_spans
tf.NotDifferentiable("ExtractSpans")
