import matplotlib.pyplot as plt
import numpy as np

def plot_shape(vertices, color, label):
    vertices = np.array(vertices)
    vertices = np.vstack((vertices, vertices[0])) 
    plt.plot(vertices[:, 0], vertices[:, 1], color=color, label=label)

def scale(vertices, scale_factor):
    return np.array(vertices) * scale_factor

def rotate(vertices, angle_degrees):
    angle_radians = np.radians(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians)],
                                [np.sin(angle_radians), np.cos(angle_radians)]])
    return np.dot(vertices, rotation_matrix)

def translate(vertices, tx, ty):
    return vertices + np.array([tx, ty])

def main():
    plt.figure(figsize=(8, 8))

    
    square_vertices = [[2, 0], [2, 2], [4, 2], [4, 0]]
    plot_shape(square_vertices, 'blue', 'Body of the House')

   
    triangle_vertices = [[2, 2], [3, 4], [4, 2]]
    plot_shape(triangle_vertices, 'green', 'Roof of the House')

    rectangle_vertices = [[1, 0], [5, 0], [5, 4], [1, 4]]
    plot_shape(rectangle_vertices, 'brown', 'Door of the House')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.title("House Design Using Geometric Shapes")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.axis('equal')

    plt.show()

   

    plt.figure(figsize=(8, 8))

  
    square_vertices_scaled = scale(square_vertices, 1.5)
    square_vertices_rotated = rotate(square_vertices_scaled, 45)
    square_vertices_translated = translate(square_vertices_rotated, 2, 1)
    plot_shape(square_vertices_translated, 'blue', 'Body of the House')

 
    triangle_vertices_scaled = scale(triangle_vertices, 1.5)
    triangle_vertices_rotated = rotate(triangle_vertices_scaled, 45)
    triangle_vertices_translated = translate(triangle_vertices_rotated, 2, 1)
    plot_shape(triangle_vertices_translated, 'green', 'Roof of the House')

 
    rectangle_vertices_scaled = scale(rectangle_vertices, 1.5)
    rectangle_vertices_rotated = rotate(rectangle_vertices_scaled, 45)
    rectangle_vertices_translated = translate(rectangle_vertices_rotated, 2, 1)
    plot_shape(rectangle_vertices_translated, 'brown', 'Door of the House')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.title("Transformed House Design Using Geometric Shapes")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.axis('equal')

    plt.show()

if __name__ == "__main__":
    main()
