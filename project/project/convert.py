import onnx2keras
from onnx2keras import onnx_to_keras
import keras
import onnx

onnx_model = onnx.load('model.onnx')

k_model = onnx_to_keras(onnx_model, [input])

