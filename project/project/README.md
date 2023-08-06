## Installation
Download the project
Download Node.js
Download Expo on mobile devices
Download yarn: https://www.codehub.com.vn/Huong-Dan-Cai-Dat-va-Su-Dung-Yarn-Package-Manager

```terminal
git clone https://github.com/ultralytics/yolov5
pip install -qr requirements.txt
```

## Usage
As our team are facing some bugs with integrating our computer vision model into Front End code, you can run these 2 parts separately following these steps:



Part 1: Running FE code
```terminal
cd project
cd api 
python main.py
cd ..
cd Recysion
yarn install
yarn add expo
npx expo start
yarn start
```

Part 2: Running Computer Vision Model
```new terminal
python detech.py --weights best.pt --img 640 --conf 0.25 --source 0
```
Scan the qr code



## Contributing

If you want to contribute to a project and make it better, your help is very welcome.


