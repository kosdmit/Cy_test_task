## Note
This project was developed for job test task

## What is this
This is an autotest application for testing web form. 
It includes 57 test items which combine different test methods and data for cover many test cases.
You can read about included tests here (*at this moment only russian lang*): https://github.com/kosdmit/Cy_test_task/blob/99d09a0e12c96315243673d99d96b5cb1d59c901/docs/check-list.md

### Features
- These are easily expandable test cases
- It uses `mimesis` package for generating test data
- It uses parametrization for make code shorter

## Getting Started

Below is instruction on setting up this project locally.
To get a local copy up and running follow these simple steps.

### Prerequisites
_Let's check if we are ready._

* This project uses Python 3.11. Check your python version:
  ```sh
  python --version
  ```
  *work on earlier versions is not guaranteed*

### Installation

_Let`s start._

1. Clone the repo
   ```sh
   git clone https://github.com/kosdmit/Cy_test_task.git
   ```
2. Create and activate a virtual environment
   ```sh
   cd yourrepository
   virtualenv venv
   source venv\Scripts\activate
   ```
   If you are on Unix or MacOS, run this for activate virtual environment:  
   ```sh
   source venv/bin/activate
   ```

3. Install required Python packages
   ```sh
   pip install -r requirements.txt
   ```
   
4. That`s it! Run main.py and test it!
   ```sh
   python main.py
   ```
   
### Thank you for attention!
