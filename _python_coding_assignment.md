Python Assignment 1:
-------------------------

Given a string sentence print the words in reverse order. Remove the words "the, and, on, and over" from the output. For example:

"The quick brown fox jumps over the lazy dog" -> "dog lazy jumps fox brown quick"

Python Assignment 2:
-------------------------

Write a python script that downloads the a wiki page for a university and scrape it for information about student population (total students, undergraduates, and postgraduates). For example:

    https://en.wikipedia.org/wiki/Michigan_State_University
    https://en.wikipedia.org/wiki/University_of_Virginia

return an object that contains:

    {
      "students":		50,543,
      "undergraduates":	39,143,
      "postgraduates":	11,400
    }

Python Assignment 3:
-------------------------

Write a script that takes in the following video

  http://download.openalpr.com/road.mp4

and:
 
  - Drops its frame rate to 5 FPS, and throws away all frames after the first minute.
  - Saves all frames to a certain directory.
  - Writes frame-specific information to a YAML file, including:
    - frame_number
    - file_path

**Bonus**:

Use an object detector of the framework of your choice (can be pre-trained) to add the following attributes to each frame:

  - Detected object classes existing in image and their counts (i.e. 3 vehicles, 4 pedestrians, 2 cyclists)
  - Bounding boxes for detected classes (list-like) 
  - Append this information to the yaml file for each image

Here is one possible object detector for reference: https://github.com/ibaiGorordo/ONNX-ImageNet-1K-Object-Detector

Python Assignment 4:
---------------------

 Aircraft sorting:
  
    - Create a program that can accept aircraft objects and assign them to a runway.
    - A sample template (Aircraft Queuing Template.py) is available.  Scroll to the bottom of this gist
    - There are more aircraft than there are runways.  Some planes must wait.
    - Runways are small, medium, and large.  Small runways can only handle planes with < 200,000 pounds, medium runways up to 500,000 pounds, and large can handle any size aircraft.
    - The planes with the most passengers are given highest priority for a particular runway.
    - The planes should be spread out optimally on each runway so that the planes go out as quickly as possible.
​
  Input:
  
    2 small runways, 3 medium runways, and 1 large runway
    Aircraft: 400,000 pounds, 212 passengers
    Aircraft: 100,000 pounds, 55 passengers
    Aircraft: 100,000 pounds, 25 passengers
    Aircraft: 100,000 pounds, 95 passengers
    Aircraft: 100,000 pounds, 115 passengers
    Aircraft: 250,000 pounds, 121 passengers
    Aircraft: 600,000 pounds, 15 passengers
    Aircraft: 300,000 pounds, 155 passengers
    Aircraft: 600,000 pounds, 225 passengers
    Aircraft: 100,000 pounds, 95 passengers
    Aircraft: 100,000 pounds, 116 passengers
    Aircraft: 250,000 pounds, 3 passengers
​
  Output (planes ordered by position in line):
  
    Runway R1 (small): Aircraft A1  (A1.pounds, A1.passengers), Aircraft A2  (A2.pounds, A2.passengers), Aircraft A3  (A3.pounds, A3.passengers), 
    Runway R2 (medium): Aircraft A4  (A4.pounds, A4.passengers), Aircraft A5  (A5.pounds, A5.passengers), Aircraft A6  (A6.pounds, A6.passengers), 
    ...
​
  Aircraft Queuing Template is provided in case it is useful to answer the question.