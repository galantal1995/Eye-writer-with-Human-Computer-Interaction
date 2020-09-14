# Eye-writer-with-Human-Computer-Interaction

This is an eye tracking apparatus that allows people to communicate by tracking their pupil movement. 
- This system is based on a PS3 camera which is modified by placing an infrared filter behind its lens and infrared LED illuminators are built around the camera.
- The so-called red eye effect is exploited which is when the eye is illuminated by infrared light, the light reflects back from the pupil. This reflected light is captured by the camera and computer vision algorithms are used in python (OpenCV) to track the position of the eye. 
- A keyboard is implemented in the software and a mouse-like pointer that can be moved by the eye. Wherever the eye blinks on the keyboard (pointer disappears for more than 1s), that letter will be taken by the computer.
- At the end the text is converted to audio. 
