# Amador UAVS Software Application

My name is [Elijah Bantugan](https://elijahb.xyz), a 9th grade programmer. 

## Project Structure

**#1**: `center.py`

**#2**: geofence.py

**3**: `generator.py`, `train.py`, `val.py`, `vision.py`

## Something I wish I changed

If i had the time, I would deffinently rewrite the generator script- Because of the fact that the script would use random.choice to pick shape, and character, it would create a class imbalance and mean that there wouldn't be enough imgaes for each class. I would change how the generator script worked by:

1. Loop through each shape type
2. Loop through each character for that shape
3. Apply a variety of rotations, so that the model can detect when given different rotations

(I noticed that when going through generated images, whenever I would find a certain shape + character combination, the rotation differences between each of those would be very similar, causing the model to lack in detection abilities)