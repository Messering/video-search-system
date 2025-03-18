import matplotlib.pyplot as plt

def plot_similarity_matrix(similarity_matrix, title='Similarity Matrix'):
    plt.figure(figsize=(8, 6))
    plt.imshow(similarity_matrix, interpolation='nearest', cmap='hot')
    plt.title("Similarity Matrix")
    plt.xlabel('Query')
    plt.ylabel('Target')
    plt.colorbar()
    plt.show()
