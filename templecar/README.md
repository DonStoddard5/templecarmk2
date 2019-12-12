# templecarmk2

![car](readmeimages/car.jpg)

## Starting the program

## Controling the Car

The car uses modified WASD controls to move.

W/A moves the car forwards and back

A/S turn the wheels

Q/E turn the wheels and move the car forward simutaneously

## Data Collection

usbwriter.py records speed, steering, and an image every # seconds and stores it in:

```
/templecar/src/{filename}.csv
```

Each line represents a new dataset, and the data is saved in the following format:
```
{speed 1}, {steering 1}, {image 1}
{speed 2}, {steering 2}, {image 2}
…
{speed n}, {steering n}, {image n}
```

## System Architecture

words
