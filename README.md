## BMI Calculator using Python Tkinter

**BMI formula**:
- US units: BMI = (weight (lb) / height^2 (in)) * 703
- Metric units: BMI = weight (kg) / height^2 (m)

**Example 1**:

Weight 64 kg and height 1.9 meters tall

BMI = w / h^2

BMI = 64 / 1.9^2

BMI = 64 / 3.61

BMI = 17.1

**Example 2**:

Weight 184 lb and height 5.10 feet

BMI = (w / h^2) * 703

BMI (184 / 4900) * 703

BMI = 0.3755 * 703

BMI = 26.4

**BMI categories are as follows**:

- Severely underweight: less than 16.0
- Underweight: between 16.0 and 18.4
- Normal: between 18.5 and 24.9
- Overweight: between 25.0 and 29.9
- Moderately Obese: between 30.0 and 34.9
- Severely Obese: between 35.0 and 39.9
- Morbidly Obese: greater than 40.0

*Note*: Keep in mind that BMI is a ratio between height and total body weight and does not differentiate between weight from muscle or weight from fat, nor consider an individual's body frame type. It is only *one of the several tools* used to assess a person's weight and overall health.

The following program uses the two following functions:

- `calculateBMI()`
- `indexBMI()`

Within `calculateBMI()`, the following is executed:

- the user weight is converted to kg
- the user height is converted to centimeters
- BMI is calculated and rounded
- `indexBMI()` is called

Within `indexBMI()`, the following is executed:

- the final result is displayed depending on the BMI value

**If you are concerned about your weight, it is best to consult with a healthcare professional.**