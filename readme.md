# RosLibJS Ros2wasm example

## Installing pixi

This demo relies on pixi a package manage alternative to conda, the install instructions are available here (pixi_docs)[https://pixi.sh/latest/], here are the required commands:

On linux or mac-os
```
curl -fsSL https://pixi.sh/install.sh | sh
```

On windows
```
powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

## Running the demo

### ros2wasm launch
First to launch the ros2wasm jupyter-lite demo you just need to open the following website: https://ros2wasm.github.io/jupyter-lite and run the first to cells setting ROSLIBS_ENABLE to 1

### Launching native ros2 node
Thanks to pixi you just need to launch the following command on this directory

```
git clone 'this repo'
cd 'this repo'
pixi run demo
```

This will install ros2-humble in a isolated pixi enviroment thanks to (robostack)[https://robostack.github.io/index.html] and launch the rosbridge_websocket node required to comunicate to roslibjs

This also runs a minimal publisher example on the topic `\topic` that can be subscribed on the notebook

