# Turtle Graphics - Drawing Polygons

This Python program uses the `turtle` module to draw polygons with sides ranging from 3 (triangle) to 10 (decagon). Each polygon is drawn with a randomly selected color, and the turtle automatically draws each shape in sequence.

## Features

- **Polygon Drawing**: The program draws shapes from triangles to decagons.
- **Random Colors**: Each shape is drawn in a randomly chosen color from a predefined color list.
- **Interactive Window**: The turtle window stays open until clicked, giving the user time to admire the drawn shapes.

## How it Works

1. **Draw Shapes**: The `draw_shape(sides)` function draws a polygon based on the number of sides provided. The turtle moves forward by a fixed amount for each side, and turns by the appropriate angle (calculated using the formula `360 / sides`).
2. **Random Colors**: Before drawing each shape, the turtle's color is set to a random choice from the color list.
3. **Loop from 3 to 10 Sides**: The program uses a loop to draw polygons with 3 to 10 sides.
