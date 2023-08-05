
import torch
import torchvision.transforms as transforms
from PIL import Image
import torch
import base64
from flask import jsonify
from flask import request
from flask import Flask
from io import BytesIO
from flask_cors import CORS


app = Flask(__name__)

cors = CORS(app)

model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path='best.pt', force_reload=True)

model.eval()

transform = transforms.Compose([
    transforms.Resize((640, 640)),  # Change image size to 640x640
    transforms.ToTensor(),  # Convert image to tensor
])

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get base64 data from request
        data = request.json['base64_data']
        base64_data = data.split(',')[1]

        binary_data = base64.b64decode(base64_data)

        image = Image.open(BytesIO(binary_data))
        image = image.convert("RGB")
        image_tensor = transform(image).unsqueeze(0)

        # Perform forward pass to get predictions from the model
        with torch.no_grad():
            predictions = model(image_tensor)

        bboxes = predictions[0][:, :4]
        labels = predictions[0][:, 5]  # Predicted labels for each bounding box
        confidences = predictions[0][:, 4]

        # Process the predictions
        prediction_list = []
        for (bbox, label, confidence) in zip(bboxes, labels, confidences):
            prediction_list.append({
                "bbox": bbox.tolist(),  # Convert tensors to lists
                "label": int(label),
                "confidence": float(confidence),
            })

        # Return the predictions
        return jsonify({"predictions": prediction_list}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)