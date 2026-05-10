import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    @staticmethod
    def plot_age_distribution(df, save_path):
        plt.figure(figsize=(10, 6))
        sns.histplot(df['age'], kde=True, color='skyblue')
        plt.title('Patient Age Distribution (Cleaned)')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.savefig(save_path)
        plt.close()

    @staticmethod
    def plot_cholesterol_trends(df, save_path):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df['cholesterol'], color='lightgreen')
        plt.title('Cholesterol Levels Distribution')
        plt.savefig(save_path)
        plt.close()
