from manim import *

# manim -pql -s -o C:\\Users\\sweet\\masters_thesis\\img\\test.png python_scripts/manim_test.py ArrowsInCircles command for rendering class as image to custom file

class ArrowsInCircles(Scene):
    def construct(self):
        # Parameters for the scene
        arrow_length = 1  # Length of each arrow
        arrow_direction = UP  # Direction of arrows
        circle_radius = 0.5  # Radius of each circle
        circle_opacity = 0.3  # Transparency of circles
        grid_size = 3  # Number of rows and columns

        # Create a grid of arrows with circles
        for i in range(-grid_size, grid_size + 1):
            for j in range(-grid_size, grid_size + 1):
                # Position of the arrow and circle
                position = np.array([i, j, 0])

                # Create an arrow
                arrow = Arrow(
                    start=position - 0.5 * arrow_length * arrow_direction,
                    end=position + 0.5 * arrow_length * arrow_direction,
                    color=BLUE
                )

                # Create a semi-transparent circle around the arrow
                circle = Circle(
                    radius=circle_radius,
                    color=YELLOW,
                    fill_opacity=circle_opacity,
                    fill_color=YELLOW
                ).move_to(position)

                # Add the circle and arrow to the scene
                self.add(circle, arrow)

        # Play a simple animation
        self.wait(2)  # Hold the scene for 2 seconds