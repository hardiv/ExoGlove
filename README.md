# GripPi

Welcome to the home of the **GripPi** Codebase! This project is a glove exoskeleton powered by a Raspberry Pi, designed to assist stroke patients in gripping objects with the help of a predictive Computer Vision algorithm.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [License](#license)
- [Contact](#contact)

## Project Overview

GripPi is a cutting-edge assistive device aimed at improving the quality of life for stroke survivors. By leveraging the power of Raspberry Pi and advanced sensor technology, GripPi provides targeted rehabilitation to help users recover their grip strength more effectively and efficiently.

## Features

- **Image Recognition**: Utilises a lightweight model built using Tensorflow and Keras to help predict whether to grip objects or not.
- **Sensor Fusion**: Combines Image Recognition data with recordings from an IR sensor to gauge whether an object can be grabbed or not.

## Installation

Follow these steps to set up GripPi:

1. Clone the repository:
    ```sh
    git clone https://github.com/hardiv/GripPi.git
    ```
2. Navigate to the project directory:
    ```sh
    cd GripPi
    ```
3. Install the necessary dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the setup script:
    ```sh
    python setup.py
    ```

## Usage

To start using GripPi, follow these instructions:

1. Power up your Raspberry Pi and ensure it is connected to the necessary hardware (See [Hardware Requirements](#hardware-requirements))
2. Navigate to the project directory:
    ```sh
    cd GripPi
    ```
3. Run the main program:
    ```sh
    python main.py
    ```

For detailed usage instructions and tutorials, refer to the [Wiki](https://github.com/hardiv/GripPi/wiki).

## Hardware Requirements

- Raspberry Pi (Model 3B+ or newer recommended)
- IR sensor
- Raspberry Pi Camera Module
- Servo Motors
- Motor Controller
- Glove
- Ivy Grip Tape

For a detailed list of hardware components and assembly instructions, please visit the [Hardware Setup](https://github.com/hardiv/GripPi/wiki/Hardware-Setup) page.

## Software Requirements

- Python 3.7 or higher

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
